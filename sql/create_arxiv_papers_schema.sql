-- ============================================================
-- 在 Supabase project 中创建 arXiv 论文表（arxiv_papers）
-- ============================================================
-- 说明：
--   - 列集合与 src/maintain/sync.py normalize_paper + 向量编码的写入字段对齐；
--   - search_tsv 为生成列（english tsvector），match_arxiv_papers_bm25 依赖它
--     做长窗口 GIN 预过滤，见 sql/match_arxiv_papers.sql 头部说明；
--   - 使用方式：在 Supabase SQL Editor 中整体执行本文件，
--     然后执行 match_arxiv_papers.sql 与 enable_preprint_anon_read_policies.sql。

create extension if not exists vector;

create table if not exists public.arxiv_papers (
  id text primary key,
  source text not null default 'arxiv',
  source_paper_id text,
  doi text,
  version text,
  title text not null,
  abstract text,
  authors jsonb not null default '[]'::jsonb,
  primary_category text,
  categories jsonb not null default '[]'::jsonb,
  published timestamptz,
  link text,
  pdf_url text,
  embedding vector(384),
  embedding_model text,
  embedding_dim int,
  embedding_updated_at timestamptz,
  search_tsv tsvector generated always as (
    to_tsvector('english', coalesce(title, '') || ' ' || coalesce(abstract, ''))
  ) stored,
  updated_at timestamptz not null default now()
);

-- BM25 长窗口预过滤依赖的 GIN 索引（命名与 match_arxiv_papers.sql 头部约定一致）
create index if not exists idx_arxiv_papers_search_tsv
  on public.arxiv_papers using gin (search_tsv);

-- 时间窗过滤依赖的 B-tree 索引
create index if not exists arxiv_papers_published_idx
  on public.arxiv_papers (published desc);

create index if not exists arxiv_papers_source_published_idx
  on public.arxiv_papers (source, published desc);
