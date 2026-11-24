from __future__ import annotations

import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urljoin

import fitz
import requests
from PIL import Image

try:
    from bs4 import BeautifulSoup
except ImportError:  # pragma: no cover - bs4 缺失时官方源通道静默关闭，走 PDF 兜底
    BeautifulSoup = None


MIN_FIGURE_WIDTH = 240
MIN_FIGURE_HEIGHT = 180
MIN_FIGURE_AREA = 120_000
WEBP_QUALITY = 82
FIGURE_META_VERSION = 3
OFFICIAL_HTML_TIMEOUT = 60
OFFICIAL_UA = "Mozilla/5.0 (compatible; daily-paper-reader/1.0)"
MIN_DISPLAY_FRACTION_DEFAULT = 0.04
MIN_DISPLAY_FRACTION_ENV = "DPR_FIGURE_MIN_DISPLAY_FRACTION"
PAPERCROPPER_SCRIPT_ENV = "PAPERCROPPER_SCRIPT"
PAPERCROPPER_DIR_ENV = "PAPERCROPPER_DIR"
PAPERCROPPER_MODEL_ENV = "PAPERCROPPER_MODEL"
PAPERCROPPER_PYTHON_ENV = "PAPERCROPPER_PYTHON"
PAPERCROPPER_DISABLE_ENV = "PAPERCROPPER_DISABLE"
PAPERCROPPER_MODEL_FILENAME = "doclayout_yolo_docstructbench_imgsz1280_2501.pt"
PAPERCROPPER_LOG_LIMIT = 1200


def _safe_asset_key(value: str) -> str:
    text = str(value or "").strip()
    if not text:
        return "paper"
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", text)
    text = text.strip("-._")
    return text or "paper"


def _relative_prefix(source_key: str, asset_key: str) -> str:
    return "/".join(["assets", "figures", source_key, _safe_asset_key(asset_key)])


def _absolute_dir(docs_dir: str, source_key: str, asset_key: str) -> str:
    return os.path.join(docs_dir, "assets", "figures", source_key, _safe_asset_key(asset_key))


def _relative_tables_prefix(source_key: str, asset_key: str) -> str:
    return "/".join(["assets", "tables", source_key, _safe_asset_key(asset_key)])


def _absolute_tables_dir(docs_dir: str, source_key: str, asset_key: str) -> str:
    return os.path.join(docs_dir, "assets", "tables", source_key, _safe_asset_key(asset_key))


def _load_cached_media(meta_path: str, key: str) -> List[Dict[str, Any]]:
    if not os.path.exists(meta_path):
        return []
    try:
        with open(meta_path, "r", encoding="utf-8") as f:
            payload = json.load(f) or {}
    except Exception:
        return []
    if int(payload.get("version") or 0) != FIGURE_META_VERSION:
        return []
    items = payload.get(key)
    if not isinstance(items, list):
        return []
    out: List[Dict[str, Any]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        url = str(item.get("url") or "").strip()
        if not url:
            continue
        out.append(
            {
                "url": url,
                "caption": str(item.get("caption") or "").strip(),
                "page": int(item.get("page") or 0),
                "index": int(item.get("index") or 0),
                "width": int(item.get("width") or 0),
                "height": int(item.get("height") or 0),
            }
        )
    return out


def _load_cached_figures(meta_path: str) -> List[Dict[str, Any]]:
    return _load_cached_media(meta_path, "figures")


def _load_cached_tables(meta_path: str) -> List[Dict[str, Any]]:
    return _load_cached_media(meta_path, "tables")


def _save_media_meta(meta_path: str, items: List[Dict[str, Any]], *, extractor: str, key: str) -> None:
    os.makedirs(os.path.dirname(meta_path), exist_ok=True)
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "version": FIGURE_META_VERSION,
                "extractor": extractor,
                key: items,
            },
            f,
            ensure_ascii=False,
            indent=2,
        )


def _save_figures_meta(meta_path: str, figures: List[Dict[str, Any]], *, extractor: str) -> None:
    _save_media_meta(meta_path, figures, extractor=extractor, key="figures")


def _save_tables_meta(meta_path: str, tables: List[Dict[str, Any]], *, extractor: str) -> None:
    _save_media_meta(meta_path, tables, extractor=extractor, key="tables")


def _warn_papercropper(message: str) -> None:
    print(f"[WARN] PaperCropper 表格/图表提取降级：{message}", flush=True)


def _tail_log_text(text: str, limit: int = PAPERCROPPER_LOG_LIMIT) -> str:
    compact = re.sub(r"\s+", " ", str(text or "")).strip()
    if len(compact) <= limit:
        return compact
    return "..." + compact[-limit:]


def _papercropper_was_configured() -> bool:
    return any(
        str(os.getenv(name) or "").strip()
        for name in [PAPERCROPPER_SCRIPT_ENV, PAPERCROPPER_DIR_ENV, PAPERCROPPER_MODEL_ENV, PAPERCROPPER_PYTHON_ENV]
    )


def _download_pdf_bytes(pdf_url: str, timeout: int = 90) -> bytes:
    resp = requests.get(
        str(pdf_url or "").strip(),
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=max(int(timeout or 1), 1),
    )
    resp.raise_for_status()
    return resp.content


def _truthy_env(name: str) -> bool:
    return str(os.getenv(name) or "").strip().lower() in {"1", "true", "yes", "on"}


def _env_float(name: str, default: float) -> float:
    raw = str(os.getenv(name) or "").strip()
    try:
        value = float(raw)
        return value if value >= 0 else default
    except ValueError:
        return default


def _fetch_page_text(url: str) -> Optional[str]:
    try:
        resp = requests.get(url, headers={"User-Agent": OFFICIAL_UA}, timeout=OFFICIAL_HTML_TIMEOUT)
    except Exception:
        return None
    if resp.status_code != 200 or not resp.text:
        return None
    return resp.text


def _clean_caption(text: Any) -> str:
    compact = re.sub(r"\s+", " ", str(text or "")).strip()
    return compact[:600]


# ---------------------------------------------------------------------------
# 官方源提取（优先通道）：arXiv HTML / bioRxiv 全文页直接提供真图 + caption
# ---------------------------------------------------------------------------

_ARXIV_PDF_URL_RE = re.compile(r"arxiv\.org/(?:pdf|abs|html)/([A-Za-z0-9.\-_/]+?)(?:\.pdf)?(?:[?#].*)?$")


def _arxiv_html_candidates(pdf_url: str) -> List[str]:
    """https://arxiv.org/pdf/2611.20575v1 → https://arxiv.org/html/2611.20575v1（外加不带版本号的候选）。"""
    match = _ARXIV_PDF_URL_RE.search(str(pdf_url or "").strip())
    if not match:
        return []
    arxiv_id = match.group(1).strip("/")
    if not arxiv_id or "." not in arxiv_id:
        return []
    candidates = ["https://arxiv.org/html/" + arxiv_id]
    versionless = re.sub(r"v\d+$", "", arxiv_id)
    if versionless and versionless != arxiv_id:
        candidates.append("https://arxiv.org/html/" + versionless)
    return candidates


def _biorxiv_full_candidates(pdf_url: str) -> List[str]:
    """https://www.biorxiv.org/content/<DOI>v2.full.pdf → https://www.biorxiv.org/content/<DOI>v2.full。"""
    text = str(pdf_url or "").strip().split("#", 1)[0].split("?", 1)[0]
    if "biorxiv.org" not in text:
        return []
    url = text
    for suffix in (".full.pdf", ".full", ".pdf"):
        if url.endswith(suffix):
            url = url[: -len(suffix)]
            break
    if "/content/" not in url:
        return []
    return [url + ".full"]


def _figures_from_arxiv_html(html_text: str, base_url: str) -> List[Dict[str, Any]]:
    """解析 LaTeXML 渲染的 arXiv HTML。

    图片有两种形态：<img src>（光栅）与 <object type="image/svg+xml" data>（矢量，
    2024 起的常见形态）。相对路径存在两代写法（"2611.20575v1/x1.png" 与 "x1.png"），
    各自对应不同的 base 解析，这里同时生成候选 URL，由下载环节按序尝试。
    """
    if not html_text or BeautifulSoup is None:
        return []
    try:
        soup = BeautifulSoup(html_text, "html.parser")
    except Exception:
        return []
    base_slash = base_url if base_url.endswith("/") else base_url + "/"
    items: List[Dict[str, Any]] = []
    seen_urls: set = set()

    def _candidate_urls(src: str) -> List[str]:
        # 老版 LaTeXML 用裸文件名（"x1.png"，相对 base 目录）；新版带 id 段
        # （"2611.20575v1/x1.png"，相对页面 URL）。按写法把正确候选排前面。
        if "/" in src:
            candidate_bases = (base_url, base_slash)
        else:
            candidate_bases = (base_slash, base_url)
        urls: List[str] = []
        for candidate_base in candidate_bases:
            url = urljoin(candidate_base, src)
            if url.startswith("http") and url not in urls:
                urls.append(url)
        return urls

    def _add(urls: List[str], kind: str, caption: str) -> None:
        key = urls[0]
        if key in seen_urls:
            return
        seen_urls.add(key)
        items.append({"urls": urls, "kind": kind, "caption": caption, "page": 0, "label": "Figure"})

    for fig in soup.find_all("figure"):
        imgs = fig.find_all("img")
        objects = fig.find_all("object", attrs={"type": re.compile(r"image/svg", re.I)})
        if not imgs and not objects:
            continue
        captions = fig.find_all("figcaption")
        caption = _clean_caption(captions[-1].get_text(" ", strip=True)) if captions else ""
        for img in imgs:
            src = str(img.get("src") or "").strip()
            if not src or src.startswith("data:"):
                continue
            urls = _candidate_urls(src)
            if urls:
                _add(urls, "raster", caption)
        for obj in objects:
            data = str(obj.get("data") or "").strip()
            if not data or data.startswith("data:"):
                continue
            urls = _candidate_urls(data)
            if urls:
                _add(urls, "svg", caption)
    return items


_BIORXIV_FIG_SRC_RE = re.compile(r"/F(\d+)\.(?:large\.jpg|large\.png|medium\.gif)$")


def _figures_from_biorxiv_html(html_text: str, base_url: str) -> List[Dict[str, Any]]:
    """解析 bioRxiv 全文页。

    实际标记（Highwire）：图片懒加载（data-src，noscript 回退），官方图为
    F<N>.medium.gif / F<N>.large.jpg；caption 是图片容器的兄弟 div.fig-caption
    （不是 <figcaption>），且 fig-label 的文字会被站点防爬变异（如 "Figurxe"），
    因此按 F<N> 编号做图注配对，label 剥除后统一拼回干净的 "Figure N." 前缀。
    """
    if not html_text or BeautifulSoup is None:
        return []
    try:
        soup = BeautifulSoup(html_text, "html.parser")
    except Exception:
        return []

    figs: Dict[int, List[str]] = {}
    for img in soup.find_all("img"):
        src = str(img.get("data-src") or img.get("src") or "").strip()
        if not src or src.startswith("data:"):
            continue
        url = urljoin(base_url, src)
        match = _BIORXIV_FIG_SRC_RE.search(url)
        if not match:
            continue
        no = int(match.group(1))
        if no in figs:
            continue
        urls = [url]
        if url.endswith(".medium.gif"):  # 优先高清 large.jpg，失败回落 medium.gif
            urls.insert(0, url[: -len(".medium.gif")] + ".large.jpg")
        figs[no] = urls

    captions: Dict[int, str] = {}
    for cap in soup.find_all(class_="fig-caption"):
        full_text = _clean_caption(cap.get_text(" ", strip=True))
        label_node = cap.find(class_="fig-label")
        label_text = _clean_caption(label_node.get_text(" ", strip=True)) if label_node else ""
        body = full_text
        if label_text and body.startswith(label_text):
            body = body[len(label_text):].strip()
        num_match = re.search(r"(\d+)", label_text or full_text)
        if num_match:
            captions[int(num_match.group(1))] = body or full_text

    items: List[Dict[str, Any]] = []
    for no in sorted(figs):
        items.append(
            {
                "urls": figs[no],
                "kind": "raster",
                "caption": f"Figure {no}. {captions[no]}" if captions.get(no) else "",
                "page": 0,
                "label": "Figure",
            }
        )
    return items


def _official_source_plan(source_key: str, pdf_url: str) -> Tuple[List[str], Any, str]:
    key = str(source_key or "").strip().lower()
    if key == "arxiv":
        return _arxiv_html_candidates(pdf_url), _figures_from_arxiv_html, "arxiv-html"
    if key == "biorxiv":
        return _biorxiv_full_candidates(pdf_url), _figures_from_biorxiv_html, "biorxiv-full"
    return [], None, ""


def _save_webp_from_bytes(image_bytes: bytes, dst_path: str) -> Tuple[int, int]:
    with Image.open(io.BytesIO(image_bytes)) as img:
        img.load()
        width, height = img.size
        if img.mode == "RGBA":
            bg = Image.new("RGB", img.size, (255, 255, 255))
            bg.paste(img, mask=img.split()[-1])
            export_img = bg
        elif img.mode != "RGB":
            export_img = img.convert("RGB")
        else:
            export_img = img.copy()
    export_img.save(dst_path, format="WEBP", quality=WEBP_QUALITY, method=6)
    return width, height


def _download_first_image(urls: List[str], dst_path: str) -> Tuple[int, int]:
    last_err: Optional[Exception] = None
    for url in urls:
        try:
            resp = requests.get(url, headers={"User-Agent": OFFICIAL_UA}, timeout=OFFICIAL_HTML_TIMEOUT)
            if resp.status_code != 200 or not resp.content:
                last_err = RuntimeError(f"HTTP {resp.status_code} for {url}")
                continue
            return _save_webp_from_bytes(resp.content, dst_path)
        except Exception as exc:  # noqa: BLE001 - 逐候选降级
            last_err = exc
            continue
    raise last_err or RuntimeError("no image urls")


SVG_RENDER_TARGET_WIDTH = 1400.0


def _render_svg_from_urls(urls: List[str], dst_path: str) -> Tuple[int, int]:
    """下载 SVG（arXiv LaTeXML 的矢量图形态），用 PyMuPDF 渲染成位图后转 webp。"""
    last_err: Optional[Exception] = None
    for url in urls:
        try:
            resp = requests.get(url, headers={"User-Agent": OFFICIAL_UA}, timeout=OFFICIAL_HTML_TIMEOUT)
            if resp.status_code != 200 or not resp.content:
                last_err = RuntimeError(f"HTTP {resp.status_code} for {url}")
                continue
            with fitz.open("svg", stream=resp.content) as sdoc:
                page = sdoc[0]
                page_width = float(page.rect.width) or 1.0
                scale = max(1.0, min(6.0, SVG_RENDER_TARGET_WIDTH / page_width))
                pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
                png_bytes = pix.tobytes("png")
            return _save_webp_from_bytes(png_bytes, dst_path)
        except Exception as exc:  # noqa: BLE001 - 逐候选降级
            last_err = exc
            continue
    raise last_err or RuntimeError("no svg urls")


def _extract_figures_official(
    *,
    pdf_url: str,
    source_key: str,
    output_dir: str,
    relative_prefix: str,
) -> Tuple[List[Dict[str, Any]], bool]:
    """官方源提取。返回 (figures, definitive)：
    - definitive=True 表示官方页面成功获取且结果可信（有图或确认无图）；
    - definitive=False 表示页面拿不到或候选图全部下载失败，调用方应继续走 PDF 兜底。
    """
    candidates, parser, extractor_name = _official_source_plan(source_key, pdf_url)
    if not candidates or parser is None:
        return [], False
    os.makedirs(output_dir, exist_ok=True)
    saved: List[Dict[str, Any]] = []
    for page_url in candidates[:3]:
        html_text = _fetch_page_text(page_url)
        if html_text is None:
            continue
        found = parser(html_text, page_url)
        if not found:
            return [], True  # 页面存在但确实没有 figure
        for item in found:
            if len(saved) >= 12:  # 单篇上限保护
                break
            index = len(saved) + 1
            file_name = f"fig-{index:03d}.webp"
            abs_path = os.path.join(output_dir, file_name)
            item_urls = list(item.get("urls") or [])
            try:
                if str(item.get("kind") or "raster") == "svg":
                    width, height = _render_svg_from_urls(item_urls, abs_path)
                else:
                    width, height = _download_first_image(item_urls, abs_path)
            except Exception:
                continue
            saved.append(
                {
                    "url": "/".join([relative_prefix.strip("/"), file_name]),
                    "caption": str(item.get("caption") or ""),
                    "page": int(item.get("page") or 0),
                    "index": index,
                    "width": width,
                    "height": height,
                    "label": str(item.get("label") or "Figure"),
                }
            )
        if saved:
            return saved, True
        return [], False  # 有候选图但全部下载/渲染失败 → 交给 PDF 兜底
    return [], False


def _first_existing(candidates: List[str]) -> str:
    for candidate in candidates:
        path = str(candidate or "").strip()
        if path and os.path.exists(path):
            return path
    return ""


def _resolve_papercropper() -> Tuple[str, str, str]:
    if _truthy_env(PAPERCROPPER_DISABLE_ENV):
        return "", "", ""

    configured_dir = str(os.getenv(PAPERCROPPER_DIR_ENV) or "").strip()
    cache_root = os.path.expanduser("~/.cache/dpr-tools/papercropper")
    script_path = _first_existing(
        [
            str(os.getenv(PAPERCROPPER_SCRIPT_ENV) or "").strip(),
            os.path.join(configured_dir, "extract.py") if configured_dir else "",
            os.path.join(cache_root, "PaperCropper", "extract.py"),
            os.path.expanduser("~/.cache/dpr-tools/PaperCropper/extract.py"),
            "/tmp/PaperCropper/extract.py",
        ]
    )
    model_path = _first_existing(
        [
            str(os.getenv(PAPERCROPPER_MODEL_ENV) or "").strip(),
            os.path.join(configured_dir, "models", PAPERCROPPER_MODEL_FILENAME) if configured_dir else "",
            os.path.join(cache_root, "models", PAPERCROPPER_MODEL_FILENAME),
            os.path.expanduser(f"~/.cache/dpr-tools/papercropper/models/{PAPERCROPPER_MODEL_FILENAME}"),
            f"/tmp/papercropper-run/models/{PAPERCROPPER_MODEL_FILENAME}",
        ]
    )
    python_path = _first_existing(
        [
            str(os.getenv(PAPERCROPPER_PYTHON_ENV) or "").strip(),
            os.path.join(cache_root, "venv", "bin", "python"),
            "/tmp/papercropper-venv/bin/python",
            sys.executable,
        ]
    )
    if not script_path or not model_path or not python_path:
        return "", "", ""
    return python_path, script_path, model_path


def _load_image_size(path: str) -> tuple[int, int]:
    with Image.open(path) as img:
        img.load()
        return img.size


def _save_webp_from_path(src_path: str, dst_path: str) -> tuple[int, int]:
    with Image.open(src_path) as img:
        img.load()
        width, height = img.size
        if img.mode == "RGBA":
            bg = Image.new("RGB", img.size, (255, 255, 255))
            bg.paste(img, mask=img.split()[-1])
            export_img = bg
        elif img.mode != "RGB":
            export_img = img.convert("RGB")
        else:
            export_img = img.copy()
        export_img.save(dst_path, format="WEBP", quality=WEBP_QUALITY, method=6)
        return width, height


def _natural_sort_key(path: str) -> List[Any]:
    name = os.path.basename(path)
    parts = re.split(r"(\d+)", name)
    return [int(part) if part.isdigit() else part.lower() for part in parts]


def _collect_papercropper_pngs(
    src_dir: str,
    output_dir: str,
    relative_prefix: str,
    *,
    file_prefix: str,
    label: str,
) -> List[Dict[str, Any]]:
    if not os.path.isdir(src_dir):
        return []

    os.makedirs(output_dir, exist_ok=True)
    items: List[Dict[str, Any]] = []
    seen_hash: set[str] = set()
    paths = [
        os.path.join(src_dir, name)
        for name in os.listdir(src_dir)
        if name.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
    ]
    for index, src_path in enumerate(sorted(paths, key=_natural_sort_key), start=1):
        try:
            with open(src_path, "rb") as f:
                sha = hashlib.sha256(f.read()).hexdigest()
        except Exception:
            continue
        if sha in seen_hash:
            continue
        seen_hash.add(sha)
        file_name = f"{file_prefix}-{len(items) + 1:03d}.webp"
        abs_path = os.path.join(output_dir, file_name)
        try:
            width, height = _save_webp_from_path(src_path, abs_path)
        except Exception:
            continue
        items.append(
            {
                "url": "/".join([relative_prefix.strip("/"), file_name]),
                "caption": "",
                "page": 0,
                "index": len(items) + 1,
                "width": width,
                "height": height,
                "label": label,
            }
        )
    return items


def _extract_media_with_papercropper(
    pdf_path: str,
    figure_output_dir: str,
    figure_relative_prefix: str,
    table_output_dir: str,
    table_relative_prefix: str,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    python_path, script_path, model_path = _resolve_papercropper()
    if not python_path or not script_path or not model_path:
        if not _truthy_env(PAPERCROPPER_DISABLE_ENV) and _papercropper_was_configured():
            _warn_papercropper("未找到可用的 PaperCropper 脚本或模型，改用备用图片提取器。")
        return [], []

    timeout = int(os.getenv("PAPERCROPPER_TIMEOUT_SECONDS") or "360")
    conf = str(os.getenv("PAPERCROPPER_CONF") or "0.4")
    imgsz = str(os.getenv("PAPERCROPPER_IMGSZ") or "1024")
    dpi = str(os.getenv("PAPERCROPPER_DPI") or "200")
    png_dpi = str(os.getenv("PAPERCROPPER_PNG_DPI") or "260")
    batch_size = str(os.getenv("PAPERCROPPER_BATCH_SIZE") or "4")
    padding = str(os.getenv("PAPERCROPPER_PADDING") or "2.0")

    with tempfile.TemporaryDirectory(prefix="papercropper_") as tmp_root:
        cmd = [
            python_path,
            script_path,
            "--pdf",
            pdf_path,
            "--model",
            model_path,
            "--output",
            tmp_root,
            "--formats",
            "png",
            "--targets",
            "figure,table",
            "--conf",
            conf,
            "--imgsz",
            imgsz,
            "--dpi",
            dpi,
            "--png-dpi",
            png_dpi,
            "--batch-size",
            batch_size,
            "--padding",
            padding,
        ]
        try:
            proc = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=max(timeout, 30),
                check=False,
            )
        except subprocess.TimeoutExpired:
            _warn_papercropper(f"执行超时（>{max(timeout, 30)}s），改用备用图片提取器。")
            return [], []
        if proc.returncode != 0:
            detail = _tail_log_text("\n".join([proc.stdout or "", proc.stderr or ""]))
            suffix = f"；输出：{detail}" if detail else ""
            _warn_papercropper(f"执行失败 returncode={proc.returncode}{suffix}")
            return [], []

        doc_output = os.path.join(tmp_root, os.path.splitext(os.path.basename(pdf_path))[0])
        figures = _collect_papercropper_pngs(
            os.path.join(doc_output, "Figures_png"),
            figure_output_dir,
            figure_relative_prefix,
            file_prefix="fig",
            label="Figure",
        )
        tables = _collect_papercropper_pngs(
            os.path.join(doc_output, "Tables_png"),
            table_output_dir,
            table_relative_prefix,
            file_prefix="table",
            label="Table",
        )
        if figures:
            _save_figures_meta(os.path.join(figure_output_dir, "meta.json"), figures, extractor="papercropper")
        if tables:
            _save_tables_meta(os.path.join(table_output_dir, "meta.json"), tables, extractor="papercropper")
        if not figures and not tables:
            detail = _tail_log_text("\n".join([proc.stdout or "", proc.stderr or ""]))
            suffix = f"；输出：{detail}" if detail else ""
            _warn_papercropper(f"执行完成但未产出 figure/table{suffix}")
        else:
            print(f"[INFO] PaperCropper 提取完成：figures={len(figures)} tables={len(tables)}", flush=True)
        return figures, tables


def extract_figures_from_pdf(
    pdf_path: str,
    output_dir: str,
    relative_prefix: str,
    *,
    min_width: int = MIN_FIGURE_WIDTH,
    min_height: int = MIN_FIGURE_HEIGHT,
    min_area: int = MIN_FIGURE_AREA,
    min_display_fraction: Optional[float] = None,
) -> List[Dict[str, Any]]:
    """兜底提取：抽取 PDF 内嵌光栅图。

    过滤两条线：一是图片自身像素数（min_width/min_height/min_area）；
    二是图片在页面上的显示面积占比（min_display_fraction，默认 0.04，
    可用 DPR_FIGURE_MIN_DISPLAY_FRACTION 覆盖）——机构 logo/徽标常是
    超高分辨率光栅但在页面上只占小角落，靠像素阈值挡不住，必须看
    实际排版尺寸。找不到摆放矩形的图（嵌在 Form XObject 里）保守保留。
    """
    if min_display_fraction is None:
        min_display_fraction = _env_float(MIN_DISPLAY_FRACTION_ENV, MIN_DISPLAY_FRACTION_DEFAULT)
    os.makedirs(output_dir, exist_ok=True)
    figures: List[Dict[str, Any]] = []
    seen_xref: set[int] = set()
    seen_sha: set[str] = set()
    fig_index = 1

    with fitz.open(pdf_path) as doc:
        for page_idx in range(len(doc)):
            page = doc[page_idx]
            try:
                page_area = float(page.rect.get_area())
            except Exception:
                page_area = 0.0
            for image_info in page.get_images(full=True):
                xref = int(image_info[0] or 0)
                if xref <= 0 or xref in seen_xref:
                    continue
                seen_xref.add(xref)

                if page_area > 0 and min_display_fraction > 0:
                    try:
                        rects = [r for r in page.get_image_rects(xref) if r is not None and not r.is_empty]
                    except Exception:
                        rects = []
                    if rects:
                        best_area = max(float(r.get_area()) for r in rects)
                        if best_area / page_area < min_display_fraction:
                            continue

                try:
                    raw = doc.extract_image(xref)
                except Exception:
                    continue
                image_bytes = raw.get("image") if isinstance(raw, dict) else None
                if not image_bytes:
                    continue
                sha = hashlib.sha256(image_bytes).hexdigest()
                if sha in seen_sha:
                    continue
                seen_sha.add(sha)

                try:
                    with Image.open(io.BytesIO(image_bytes)) as img:
                        img.load()
                        width, height = img.size
                        if width < min_width or height < min_height or width * height < min_area:
                            continue
                        if img.mode == "RGBA":
                            bg = Image.new("RGB", img.size, (255, 255, 255))
                            bg.paste(img, mask=img.split()[-1])
                            export_img = bg
                        elif img.mode != "RGB":
                            export_img = img.convert("RGB")
                        else:
                            export_img = img.copy()
                except Exception:
                    continue

                file_name = f"fig-{fig_index:03d}.webp"
                abs_path = os.path.join(output_dir, file_name)
                export_img.save(abs_path, format="WEBP", quality=WEBP_QUALITY, method=6)

                figures.append(
                    {
                        "url": "/".join([relative_prefix.strip("/"), file_name]),
                        "caption": "",
                        "page": page_idx + 1,
                        "index": fig_index,
                        "width": width,
                        "height": height,
                    }
                )
                fig_index += 1

    _save_figures_meta(os.path.join(output_dir, "meta.json"), figures, extractor="pymupdf-images")
    return figures


def ensure_paper_figures(
    *,
    pdf_url: str,
    docs_dir: str,
    source_key: str,
    asset_key: str,
    force: bool = False,
) -> List[Dict[str, Any]]:
    figures, _tables = ensure_paper_media(
        pdf_url=pdf_url,
        docs_dir=docs_dir,
        source_key=source_key,
        asset_key=asset_key,
        force=force,
    )
    return figures


def ensure_paper_media(
    *,
    pdf_url: str,
    docs_dir: str,
    source_key: str,
    asset_key: str,
    force: bool = False,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    if not str(pdf_url or "").strip():
        return [], []

    figure_dir = _absolute_dir(docs_dir, source_key, asset_key)
    table_dir = _absolute_tables_dir(docs_dir, source_key, asset_key)
    figure_relative_prefix = _relative_prefix(source_key, asset_key)
    table_relative_prefix = _relative_tables_prefix(source_key, asset_key)
    figure_meta_path = os.path.join(figure_dir, "meta.json")
    table_meta_path = os.path.join(table_dir, "meta.json")
    if not force:
        cached_figures = _load_cached_figures(figure_meta_path)
        cached_tables = _load_cached_tables(table_meta_path)
        if cached_figures and cached_tables:
            return cached_figures, cached_tables
        if (cached_figures or os.path.exists(figure_meta_path)) and os.path.exists(table_meta_path):
            return cached_figures, cached_tables

    # 优先官方源：arXiv HTML / bioRxiv 全文页直接给真图 + caption，矢量图也能覆盖
    official_figures, official_definitive = _extract_figures_official(
        pdf_url=pdf_url,
        source_key=source_key,
        output_dir=figure_dir,
        relative_prefix=figure_relative_prefix,
    )
    if official_figures:
        extractor_name = _official_source_plan(source_key, pdf_url)[2] or "official-html"
        _save_figures_meta(figure_meta_path, official_figures, extractor=extractor_name)
        _save_tables_meta(table_meta_path, [], extractor="none")
        return official_figures, []
    if official_definitive:
        # 官方页面成功获取但确实没有 figure：缓存空结果，避免每次运行重复抓取
        _save_figures_meta(figure_meta_path, [], extractor="official-empty")
        _save_tables_meta(table_meta_path, [], extractor="none")
        return [], []

    pdf_bytes = _download_pdf_bytes(pdf_url)
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=True) as tmp_pdf:
        tmp_pdf.write(pdf_bytes)
        tmp_pdf.flush()

        figures, tables = _extract_media_with_papercropper(
            tmp_pdf.name,
            figure_dir,
            figure_relative_prefix,
            table_dir,
            table_relative_prefix,
        )
        if figures or tables:
            # 补齐另一侧空 meta，保证 meta.json 缓存命中判断成立
            if figures and not os.path.exists(table_meta_path):
                _save_tables_meta(table_meta_path, [], extractor="none")
            if tables and not os.path.exists(figure_meta_path):
                _save_figures_meta(figure_meta_path, [], extractor="none")
            return figures, tables

        fallback_figures = extract_figures_from_pdf(tmp_pdf.name, figure_dir, figure_relative_prefix)
        _save_tables_meta(table_meta_path, [], extractor="none")
        return fallback_figures, []
