-- ============================================================
-- 在 Supabase project 中创建阅读状态云同步表（user_read_state）
-- ============================================================
-- 说明：
--   - app/read-state-sync.js 以 (github_username, paper_id) 为联合主键
--     做 PostgREST upsert（on_conflict=github_username,paper_id）；
--   - 前端持有 publishable/anon key 调用，因此需要放开 anon 角色的
--     读写权限（按设计：按 GitHub 用户名公开隔离的阅读状态）。

create table if not exists public.user_read_state (
  github_username text not null,
  paper_id text not null,
  status text not null default 'read',
  read_at timestamptz,
  updated_at timestamptz not null default now(),
  primary key (github_username, paper_id)
);

alter table public.user_read_state enable row level security;

drop policy if exists "public read user_read_state" on public.user_read_state;
create policy "public read user_read_state"
  on public.user_read_state
  for select
  to anon, authenticated
  using (true);

drop policy if exists "public insert user_read_state" on public.user_read_state;
create policy "public insert user_read_state"
  on public.user_read_state
  for insert
  to anon, authenticated
  with check (true);

drop policy if exists "public update user_read_state" on public.user_read_state;
create policy "public update user_read_state"
  on public.user_read_state
  for update
  to anon, authenticated
  using (true)
  with check (true);

drop policy if exists "public delete user_read_state" on public.user_read_state;
create policy "public delete user_read_state"
  on public.user_read_state
  for delete
  to anon, authenticated
  using (true);

grant select, insert, update, delete on table public.user_read_state to anon, authenticated;
