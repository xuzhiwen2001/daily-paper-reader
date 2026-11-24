import importlib.util
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

import fitz
from PIL import Image


def _load_module(module_name: str, path: Path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


ARXIV_HTML = """
<html><body>
<figure class="ltx_figure" id="S1.F1">
  <img src="x1.png" alt="overview">
  <figcaption class="ltx_caption"><span class="ltx_tag ltx_tag_figure">Figure 1: </span>Overview of the  model.</figcaption>
</figure>
<figure class="ltx_figure" id="S2.F2">
  <figure class="ltx_subfigure"><img src="x2.png"></figure>
  <figure class="ltx_subfigure"><img src="x3.png"></figure>
  <figcaption class="ltx_caption"><span class="ltx_tag">Figure 2: </span>Results across datasets.</figcaption>
</figure>
<figure class="ltx_figure" id="S3.F3">
  <object type="image/svg+xml" data="2611.20575v1/fig3.svg" class="ltx_graphics"></object>
  <figcaption class="ltx_caption"><span class="ltx_tag">Figure 3: </span>Architecture diagram.</figcaption>
</figure>
<figure class="ltx_table"><table><tr><td>no img</td></tr></table></figure>
<img src="logo.png">
</body></html>
"""

BIORXIV_HTML = """
<html><body>
<div class="highwire-figure highwire-figure-caption-center" id="F1">
  <span class="hw-responsive-img"><img class="fragment-image lazyload" alt="Figurxe 1."
    src="data:image/gif;base64,R0lGODlhAQABAAAAACw=" data-src="https://www.biorxiv.org/content/biorxiv/early/2026/11/16/2026.09.24.754259/F1.medium.gif"></span>
  <noscript><img class="fragment-image" src="https://www.biorxiv.org/content/biorxiv/early/2026/11/16/2026.09.24.754259/F1.medium.gif"></noscript>
</div>
<div class="fig-caption"><span class="fig-label">Figurxe 1.</span> Overview of PerturbBridge pipeline.</div>
<div class="highwire-figure" id="F2">
  <img src="https://www.biorxiv.org/content/biorxiv/early/2026/11/16/2026.09.24.754259/F2.medium.gif">
</div>
<div class="fig-caption"><span class="fig-label">Figurxe 2.</span> Latent bridge dynamics.</div>
<span class="highwire-include-inline-graphic"><img src="https://www.biorxiv.org/sites/default/files/highwire/biorxiv/early/2026/11/16/2026.09.24.754259/embed/inline-graphic-1.gif"></span>
</body></html>
"""


class PaperFiguresOfficialTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = Path(__file__).resolve().parents[1]
        src_dir = root / "src"
        if str(src_dir) not in sys.path:
            sys.path.insert(0, str(src_dir))
        cls.mod = _load_module("paper_figures_official_mod", src_dir / "paper_figures.py")

    # ---- URL 推导 ----

    def test_arxiv_html_candidates(self):
        self.assertEqual(
            self.mod._arxiv_html_candidates("https://arxiv.org/pdf/2611.20575v1"),
            ["https://arxiv.org/html/2611.20575v1", "https://arxiv.org/html/2611.20575"],
        )
        self.assertEqual(
            self.mod._arxiv_html_candidates("http://arxiv.org/abs/2401.12345v2.pdf"),
            ["https://arxiv.org/html/2401.12345v2", "https://arxiv.org/html/2401.12345"],
        )
        self.assertEqual(self.mod._arxiv_html_candidates("https://www.biorxiv.org/content/x"), [])

    def test_biorxiv_full_candidates(self):
        self.assertEqual(
            self.mod._biorxiv_full_candidates("https://www.biorxiv.org/content/10.64898/2026.09.24.754259v2.full.pdf"),
            ["https://www.biorxiv.org/content/10.64898/2026.09.24.754259v2.full"],
        )
        self.assertEqual(
            self.mod._biorxiv_full_candidates("https://www.biorxiv.org/content/10.1101/2024.01.01.001v1"),
            ["https://www.biorxiv.org/content/10.1101/2024.01.01.001v1.full"],
        )
        self.assertEqual(self.mod._biorxiv_full_candidates("https://arxiv.org/pdf/2611.20575v1"), [])

    # ---- arXiv HTML 解析 ----

    def test_figures_from_arxiv_html(self):
        base = "https://arxiv.org/html/2611.20575v1"
        items = self.mod._figures_from_arxiv_html(ARXIV_HTML, base)
        # 裸文件名 src：正确候选（带尾斜杠 base）排第一，另一代写法作为回落
        self.assertEqual(items[0]["urls"][0], base + "/x1.png")
        self.assertEqual(items[0]["urls"][1], "https://arxiv.org/html/x1.png")
        self.assertTrue(all(item["kind"] == "raster" for item in items[:3]))
        self.assertEqual(items[0]["caption"], "Figure 1: Overview of the model.")
        self.assertEqual(items[2]["caption"], "Figure 2: Results across datasets.")
        # SVG object 形态（2024+ LaTeXML 常见）也要识别
        self.assertEqual(items[3]["kind"], "svg")
        self.assertEqual(items[3]["urls"][0], base + "/fig3.svg")
        self.assertEqual(items[3]["caption"], "Figure 3: Architecture diagram.")
        # 无图 figure（纯表格）与页面级 logo.png 不入选
        self.assertEqual(len(items), 4)
        self.assertFalse(any("logo" in u for item in items for u in item["urls"]))

    def test_figures_from_arxiv_html_skips_data_uris(self):
        html = '<figure><img src="data:image/png;base64,AAAA"><figcaption>cap</figcaption></figure>'
        self.assertEqual(self.mod._figures_from_arxiv_html(html, "https://arxiv.org/html/x"), [])

    # ---- bioRxiv HTML 解析 ----

    def test_figures_from_biorxiv_html(self):
        base = "https://www.biorxiv.org/content/10.64898/2026.09.24.754259v2.full"
        items = self.mod._figures_from_biorxiv_html(BIORXIV_HTML, base)
        self.assertEqual(len(items), 2)
        # 懒加载 data-src 也认；medium.gif 升级为 large.jpg，且保留原始 URL 作为回落候选
        self.assertEqual(
            items[0]["urls"],
            [
                "https://www.biorxiv.org/content/biorxiv/early/2026/11/16/2026.09.24.754259/F1.large.jpg",
                "https://www.biorxiv.org/content/biorxiv/early/2026/11/16/2026.09.24.754259/F1.medium.gif",
            ],
        )
        # 防爬变异的 "Figurxe 1." label 被剥除，拼回干净的 "Figure 1." 前缀
        self.assertEqual(items[0]["caption"], "Figure 1. Overview of PerturbBridge pipeline.")
        self.assertEqual(items[1]["urls"][0],
                         "https://www.biorxiv.org/content/biorxiv/early/2026/11/16/2026.09.24.754259/F2.large.jpg")
        self.assertEqual(items[1]["caption"], "Figure 2. Latent bridge dynamics.")
        # 行内公式图（inline-graphic）不入选
        self.assertFalse(any("inline-graphic" in item["urls"][0] for item in items))

    # ---- PDF 兜底：显示尺寸过滤 ----

    def _make_png_bytes(self, size, color):
        img = Image.new("RGB", size, color)
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        return buf.getvalue()

    def test_pdf_fallback_filters_by_display_size(self):
        """像素超大但排版极小的 logo（CEBSIT 案例特征）必须被显示占比过滤掉。"""
        with tempfile.TemporaryDirectory() as d:
            pdf_path = Path(d) / "sample.pdf"
            out_dir = Path(d) / "assets"

            # 2000x1500 的高分辨率图，摆在页面上却只有 80x60pt（约 0.9% 页面面积）
            logo_like = self._make_png_bytes((2000, 1500), (30, 60, 180))
            # 640x480 的普通图，占约 20% 页面面积
            real_fig = self._make_png_bytes((640, 480), (220, 80, 80))

            doc = fitz.open()
            page = doc.new_page()
            page.insert_image(fitz.Rect(40, 40, 400, 340), stream=real_fig)
            page.insert_image(fitz.Rect(420, 40, 500, 100), stream=logo_like)
            doc.save(pdf_path)
            doc.close()

            figures = self.mod.extract_figures_from_pdf(
                str(pdf_path), str(out_dir), "assets/figures/arxiv/test-paper"
            )

            self.assertEqual(len(figures), 1)
            self.assertEqual((figures[0]["width"], figures[0]["height"]), (640, 480))

    def test_display_fraction_env_override(self):
        with tempfile.TemporaryDirectory() as d:
            pdf_path = Path(d) / "sample.pdf"
            out_dir = Path(d) / "assets"
            # 正方形图摆进正方形 rect（110x110pt，约 2.4% 页面面积）
            img = self._make_png_bytes((400, 400), (10, 200, 10))
            doc = fitz.open()
            page = doc.new_page()
            page.insert_image(fitz.Rect(300, 300, 410, 410), stream=img)  # ~2.4% 页面面积
            doc.save(pdf_path)
            doc.close()

            original = self.mod.os.environ.get(self.mod.MIN_DISPLAY_FRACTION_ENV)
            try:
                self.mod.os.environ[self.mod.MIN_DISPLAY_FRACTION_ENV] = "0.02"
                figures = self.mod.extract_figures_from_pdf(
                    str(pdf_path), str(out_dir), "assets/figures/arxiv/env-paper"
                )
                self.assertEqual(len(figures), 1)
                self.mod.os.environ[self.mod.MIN_DISPLAY_FRACTION_ENV] = "0.05"
                figures_strict = self.mod.extract_figures_from_pdf(
                    str(pdf_path), str(out_dir) + "-strict", "assets/figures/arxiv/env-paper"
                )
                self.assertEqual(figures_strict, [])
            finally:
                if original is None:
                    self.mod.os.environ.pop(self.mod.MIN_DISPLAY_FRACTION_ENV, None)
                else:
                    self.mod.os.environ[self.mod.MIN_DISPLAY_FRACTION_ENV] = original

    # ---- ensure_paper_media 官方源优先 ----

    def test_ensure_paper_media_prefers_official_source(self):
        import contextlib

        with tempfile.TemporaryDirectory() as d:
            docs_dir = Path(d)
            calls = {"official": 0, "pdf": 0}

            fake_figures = [
                {"url": "assets/figures/arxiv/p1/fig-001.webp", "caption": "Figure 1: real",
                 "page": 0, "index": 1, "width": 800, "height": 600, "label": "Figure"}
            ]

            def fake_official(*, pdf_url, source_key, output_dir, relative_prefix):
                calls["official"] += 1
                return list(fake_figures), True

            def fail_pdf(*args, **kwargs):
                calls["pdf"] += 1
                raise AssertionError("官方源命中时不应下载 PDF")

            original_official = self.mod._extract_figures_official
            original_pdf = self.mod._download_pdf_bytes
            try:
                self.mod._extract_figures_official = fake_official
                self.mod._download_pdf_bytes = fail_pdf
                with contextlib.redirect_stdout(io.StringIO()):
                    figures, tables = self.mod.ensure_paper_media(
                        pdf_url="https://arxiv.org/pdf/2611.20575v1",
                        docs_dir=str(docs_dir),
                        source_key="arxiv",
                        asset_key="p1",
                    )
            finally:
                self.mod._extract_figures_official = original_official
                self.mod._download_pdf_bytes = original_pdf

            self.assertEqual(calls["pdf"], 0)
            self.assertEqual(len(figures), 1)
            self.assertEqual(figures[0]["caption"], "Figure 1: real")
            self.assertEqual(tables, [])

            figure_meta = json.loads((docs_dir / "assets/figures/arxiv/p1/meta.json").read_text(encoding="utf-8"))
            table_meta = json.loads((docs_dir / "assets/tables/arxiv/p1/meta.json").read_text(encoding="utf-8"))
            self.assertEqual(figure_meta["extractor"], "arxiv-html")
            self.assertEqual(len(figure_meta["figures"]), 1)
            self.assertEqual(table_meta["tables"], [])

            # 二次调用应命中缓存，不再触发官方提取
            def fail_official(*args, **kwargs):
                raise AssertionError("应命中缓存")

            self.mod._extract_figures_official = fail_official
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    figures_cached, _ = self.mod.ensure_paper_media(
                        pdf_url="https://arxiv.org/pdf/2611.20575v1",
                        docs_dir=str(docs_dir),
                        source_key="arxiv",
                        asset_key="p1",
                    )
            finally:
                self.mod._extract_figures_official = original_official
            self.assertEqual(len(figures_cached), 1)


    # ---- _extract_figures_official 定论语义 ----

    def test_extract_official_no_figures_is_definitive(self):
        import contextlib

        original_fetch = self.mod._fetch_page_text
        try:
            self.mod._fetch_page_text = lambda url: "<html><body><p>text only</p></body></html>"
            with contextlib.redirect_stdout(io.StringIO()):
                figures, definitive = self.mod._extract_figures_official(
                    pdf_url="https://arxiv.org/pdf/1234.5678v1",
                    source_key="arxiv",
                    output_dir=tempfile.mkdtemp(),
                    relative_prefix="assets/figures/arxiv/x",
                )
            self.assertEqual((figures, definitive), ([], True))
        finally:
            self.mod._fetch_page_text = original_fetch

    def test_extract_official_download_failure_is_not_definitive(self):
        import contextlib

        original_fetch = self.mod._fetch_page_text
        original_get = self.mod.requests.get
        try:
            self.mod._fetch_page_text = lambda url: (
                '<figure><img src="1234.5678v1/x1.png"><figcaption>cap</figcaption></figure>'
            )

            def _boom(*args, **kwargs):
                raise RuntimeError("network down")

            self.mod.requests.get = _boom
            with contextlib.redirect_stdout(io.StringIO()):
                figures, definitive = self.mod._extract_figures_official(
                    pdf_url="https://arxiv.org/pdf/1234.5678v1",
                    source_key="arxiv",
                    output_dir=tempfile.mkdtemp(),
                    relative_prefix="assets/figures/arxiv/x",
                )
            self.assertEqual((figures, definitive), ([], False))
        finally:
            self.mod._fetch_page_text = original_fetch
            self.mod.requests.get = original_get

    # ---- SVG 渲染 ----

    def test_render_svg_from_urls(self):
        import contextlib

        svg_bytes = (
            b'<svg xmlns="http://www.w3.org/2000/svg" width="200" height="100">'
            b'<rect width="200" height="100" fill="#3366cc"/></svg>'
        )

        class FakeResp:
            status_code = 200
            content = svg_bytes
            text = ""

        original_get = self.mod.requests.get
        try:
            self.mod.requests.get = lambda *a, **k: FakeResp()
            with tempfile.TemporaryDirectory() as d:
                dst = Path(d) / "fig-001.webp"
                with contextlib.redirect_stdout(io.StringIO()):
                    width, height = self.mod._render_svg_from_urls(["https://arxiv.org/html/x/fig.svg"], str(dst))
                self.assertTrue(dst.exists())
                self.assertEqual(height * 2, width)  # 200x100 viewBox 等比放大
                self.assertGreaterEqual(width, 200)  # 至少原始尺寸
        finally:
            self.mod.requests.get = original_get

    def test_extract_official_renders_svg_items(self):
        import contextlib

        svg_bytes = (
            b'<svg xmlns="http://www.w3.org/2000/svg" width="300" height="150">'
            b'<rect width="300" height="150" fill="#cc3366"/></svg>'
        )

        class FakeResp:
            status_code = 200
            content = svg_bytes
            text = ""

        original_fetch = self.mod._fetch_page_text
        original_get = self.mod.requests.get
        try:
            self.mod._fetch_page_text = lambda url: (
                '<figure class="ltx_figure"><object type="image/svg+xml" data="1234.5678v1/f1.svg"></object>'
                "<figcaption>Figure 1: svg path works</figcaption></figure>"
            )
            self.mod.requests.get = lambda *a, **k: FakeResp()
            with tempfile.TemporaryDirectory() as d:
                with contextlib.redirect_stdout(io.StringIO()):
                    figures, definitive = self.mod._extract_figures_official(
                        pdf_url="https://arxiv.org/pdf/1234.5678v1",
                        source_key="arxiv",
                        output_dir=d,
                        relative_prefix="assets/figures/arxiv/svgtest",
                    )
                self.assertEqual(definitive, True)
                self.assertEqual(len(figures), 1)
                self.assertEqual(figures[0]["caption"], "Figure 1: svg path works")
                self.assertTrue((Path(d) / "fig-001.webp").exists())
        finally:
            self.mod._fetch_page_text = original_fetch
            self.mod.requests.get = original_get


if __name__ == "__main__":
    unittest.main()
