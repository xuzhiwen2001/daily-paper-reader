<div class="dpr-home-notice-card dpr-home-panel">
  <div class="dpr-home-notice-header dpr-home-panel-header">
    <h3 class="dpr-home-notice-title">公告与更新</h3>
    <a class="dpr-home-notice-tutorial" href="#/tutorial/README">使用教程 <span aria-hidden="true">›</span></a>
  </div>
  <div class="dpr-home-notice-entry">
    <time class="dpr-home-notice-date" datetime="2026-11-12">11.12</time>
    <div>
      <strong class="dpr-home-notice-entry-title">设置向导支持多厂商 LLM API</strong>
      <span class="dpr-home-notice-entry-summary">配置页不再写死 DeepSeek：可从 DeepSeek、GLM Coding 套餐、智谱开放平台、Kimi For Coding、Kimi 开放平台、硅基流动等预设中选择，或填任意 OpenAI 兼容端点；切换厂商自动联动端点与模型建议，已有配置自动识别。CI 字段名不变，工作流零改动。</span>
    </div>
  </div>
  <div class="dpr-home-notice-entry">
    <time class="dpr-home-notice-date" datetime="2026-10-05">10.05</time>
    <div>
      <strong class="dpr-home-notice-entry-title">medRxiv 自动更新已恢复</strong>
      <span class="dpr-home-notice-entry-summary">修复超长摘要导致的向量生成失败，维护任务现会限制单条 embedding 文本长度并分片写入。受影响范围已重新同步，公开读取、关键词检索与语义检索均已验证。</span>
    </div>
  </div>
  <div class="dpr-home-notice-entry">
    <time class="dpr-home-notice-date" datetime="2026-09-16">09.16</time>
    <div>
      <strong class="dpr-home-notice-entry-title">日报跨日重复推荐已修复</strong>
      <span class="dpr-home-notice-entry-summary">历史推荐现按原始召回标签与 arXiv 论文标识去重，暂停词条不再参与评分；同一专题次日不会重复推荐相同论文。已有历史页面保留，不自动删除。</span>
    </div>
  </div>
  <div class="dpr-home-site-stats" data-dpr-site-stats hidden aria-live="polite">
    <span>今天有 <strong class="dpr-home-site-stat-value" data-dpr-daily-readers>--</strong> 人在看论文</span>
    <span class="dpr-home-site-stat-separator" aria-hidden="true">·</span>
    <span>昨天有 <strong class="dpr-home-site-stat-value" data-dpr-yesterday-readers>--</strong> 人在看论文</span>
    <span class="dpr-home-site-stat-separator" aria-hidden="true">·</span>
    <span>已有 <strong class="dpr-home-site-stat-value" data-dpr-fork-count>--</strong> 人加入 Daily Paper Reader</span>
    <span class="dpr-home-history">
      <button type="button" class="dpr-home-history-trigger" data-dpr-history-trigger aria-label="查看最近 14 天阅读趋势"><span aria-hidden="true">🔍</span></button>
      <span class="dpr-home-history-popover" data-dpr-history-popover role="tooltip">
        <span class="dpr-home-history-header">近 14 天阅读趋势</span>
        <span class="dpr-home-history-meta">
          <span data-dpr-history-range>--</span>
          <span>峰值 <strong data-dpr-history-peak>--</strong></span>
        </span>
        <span class="dpr-home-history-chart" data-dpr-history-chart></span>
      </span>
    </span>
  </div>
</div>

<div class="dpr-home-dashboard-grid">
<section class="dpr-home-dashboard-card dpr-home-report-card">
  <div class="dpr-home-dashboard-header">
    <div>
      <span class="dpr-home-dashboard-kicker">2026-11-16 ~ 2026-11-25</span>
      <h3 class="dpr-home-dashboard-title">今日汇总</h3>
    </div>
    <strong class="dpr-home-dashboard-count">共 6 篇</strong>
  </div>
  <dl class="dpr-home-dashboard-stats">
    <div class="dpr-home-dashboard-stat"><dt>累计更新</dt><dd>1 次</dd></div>
    <div class="dpr-home-dashboard-stat"><dt>精读</dt><dd>3</dd></div>
    <div class="dpr-home-dashboard-stat"><dt>速读</dt><dd>3</dd></div>
  </dl>
  <p class="dpr-home-dashboard-body">最近更新：2026-11-25 18:46:10 UTC<br>状态：成功</p>
</section>
<section class="dpr-home-dashboard-card dpr-home-brief-card">
  <div class="dpr-home-dashboard-header">
    <div>
      <span class="dpr-home-dashboard-kicker">合并后生成</span>
      <h3 class="dpr-home-dashboard-title">今日简报</h3>
    </div>
    <strong class="dpr-home-dashboard-count">AI</strong>
  </div>
  <div class="dpr-home-dashboard-body">
<p>2026年11月16日至25日共筛选6篇论文，其中精读3篇、速读3篇，重点关注单细胞扰动建模与单细胞基础模型的评测。</p>
<p>最值得看的是《How Far Can Linear Go?》（9.0分），它用BiPert统一框架探讨线性方法的边界；《Hypothesis Generation and Semantic Attribution in Inverse Perturbation Modeling》（8.0分）则指向逆向扰动建模中的假设生成与语义归因。</p>
<p>普通读者可以先看9分那篇，了解线性方法能走多远，再用7分的CellBench对照基础模型的任务依赖与泛化限制。</p>
  </div>
</section>
<section class="dpr-home-dashboard-card dpr-home-deep-card">
  <div class="dpr-home-dashboard-header">
    <div>
      <span class="dpr-home-dashboard-kicker">今日累计</span>
      <h3 class="dpr-home-dashboard-title">精读推荐</h3>
    </div>
    <strong class="dpr-home-dashboard-count">3 篇</strong>
  </div>
  <div class="dpr-home-dashboard-body">
<ul class="dpr-home-dashboard-paper-list"><li><span class="dpr-home-dashboard-paper-title" title="How Far Can Linear Go? BiPert, a Unified Framework for Single-Cell Perturbation Modelling">How Far Can Linear Go? BiPert, a Unified Framework for Single-Cell Perturbation Modelling</span></li><li><span class="dpr-home-dashboard-paper-title" title="Hypothesis Generation and Semantic Attribution in Inverse Perturbation Modeling">Hypothesis Generation and Semantic Attribution in Inverse Perturbation Modeling</span></li><li><span class="dpr-home-dashboard-paper-title" title="Multi-omics causal deep learning reveals regulatory structure while interventions refine perturbation predictions">Multi-omics causal deep learning reveals regulatory structure while interventions refine perturbation predictions</span></li></ul>
  </div>
  <div class="dpr-home-dashboard-tags"><span class="dpr-home-dashboard-tag">virtual-cell <strong>3</strong></span></div>
</section>
<section class="dpr-home-dashboard-card dpr-home-skim-card">
  <div class="dpr-home-dashboard-header">
    <div>
      <span class="dpr-home-dashboard-kicker">今日累计</span>
      <h3 class="dpr-home-dashboard-title">速读推荐</h3>
    </div>
    <strong class="dpr-home-dashboard-count">3 篇</strong>
  </div>
  <div class="dpr-home-dashboard-body">
<ul class="dpr-home-dashboard-paper-list"><li><span class="dpr-home-dashboard-paper-title" title="CellBench: task-dependent performance and generalization limits of single-cell foundation models">CellBench: task-dependent performance and generalization limits of single-cell foundation models</span></li><li><span class="dpr-home-dashboard-paper-title" title="Learning Multimodal Representations from Partially Paired, Small-Scale Data">Learning Multimodal Representations from Partially Paired, Small-Scale Data</span></li><li><span class="dpr-home-dashboard-paper-title" title="A multimodal foundation model for tissue proteomics and morphology in cancer">A multimodal foundation model for tissue proteomics and morphology in cancer</span></li></ul>
  </div>
  <div class="dpr-home-dashboard-tags"><span class="dpr-home-dashboard-tag">spatial-gene <strong>2</strong></span><span class="dpr-home-dashboard-tag">virtual-cell <strong>1</strong></span></div>
</section>
</div>

<div class="dpr-home-promo-card dpr-home-panel">
  <div class="dpr-home-panel-header">
    <h3 class="dpr-home-promo-title">社区与支持</h3>
  </div>
  <p class="dpr-home-promo-copy">欢迎通过 Star、Fork、Issue 或 PR 一起完善 Daily Paper Reader。</p>
  <div class="dpr-home-promo-meta">
    <span>QQ群 <strong>583867967</strong></span>
    <span class="dpr-home-promo-separator" aria-hidden="true">·</span>
    <span>已有 <strong>1,491</strong> 人参与交流</span>
  </div>
</div>
