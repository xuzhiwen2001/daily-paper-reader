---
title: Disentangled generative modeling of single-cell perturbation responses across dynamic cellular states
title_zh: 跨动态细胞状态的单细胞扰动响应的解耦生成建模
authors: "Wang, Y., Zhao, Y., Li, S., Yang, D."
date: 2026-11-10
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.07.765083v1.full.pdf"
tags: ["query:virtual-cell"]
score: 9.0
evidence: 解耦式深度生成模型建模单细胞扰动响应
tldr: 单细胞扰动研究常被细胞周期、状态、供体差异和应激掩盖处理效应。PertVI用解耦变分推断将基线、状态、批次与处理诱导位移分开，并把异常响应隔离到正交空间。模拟与T细胞筛选中，它能区分毒性表型、解析调控子动力学和双相反弹，并发现表型移动与广泛转录扰动解耦。该工作为动态细胞系统的机制化扰动建模提供结构化框架。
source: biorxiv
selection_source: fresh_fetch
motivation: 标准模型将单细胞压缩为统一表示，处理效应易被分裂、谱系、供体和应激混淆。
method: PertVI是深度生成模型，解耦基线分裂相、细胞状态、批次与处理位移，并用正交异常空间隔离离群响应。
result: 模拟基准中准确解耦耦合生物轴并恢复弱扰动信号；T细胞筛选中区分记忆前体佐剂与毒性表型，解析动力学轨迹和双相反弹。
conclusion: 表明表型移动受状态特异性脉冲调控而非广泛转录响应，为结构引导的方差解耦提供原理验证。
---

## 摘要
单细胞扰动研究越来越多地在复杂的多条件生物系统中开展，为理解干预如何重塑细胞状态和分子程序提供了强有力的视角。然而，标准计算模型将单细胞表达谱压缩为统一表征，其中处理效应被细胞分裂、谱系进展、供体差异和细胞应激所掩盖。在此，我们提出用于扰动响应的解耦变分推断（Disentangled Variational Inference for Perturbation Response, PertVI），一种深度生成模型，它将基线有丝分裂期、细胞状态和批次效应与处理诱导的偏移分离开来，同时在正交异常空间中将异常的离流形响应隔离开来。这种结构化设计解决两个相互交织的任务：(1) 量化处理诱导的细胞状态组成变化；(2) 推断响应处理的状态门控转录变化。在模拟基准测试中，PertVI 能够准确解耦耦合的生物学轴并恢复微弱的处理特征。在原代人 CD8+ 和 CD4+ T 细胞的条件性化学和遗传筛选中，PertVI 将记忆前体佐剂与毒性拟表型区分开，将共聚类的调控因子解析为具有方向性的动力学轨迹以及被标准工作流掩盖的双相反弹模式，并揭示处理诱导的表型转变与广泛的转录扰动响应解耦，而是由状态特异性脉冲驱动。总而言之，PertVI 为单细胞扰动响应建模带来了独特的机制粒度，为动态细胞系统中生物学信息驱动、结构引导的方差解耦提供了原理验证。

## Abstract
Single-cell perturbation studies are increasingly conducted across complex, multi-condition biolog-ical systems, offering a powerful lens into how interventions reshape cell states and molecular pro-grams. However, standard computational models compress single-cell profiles into unified repre-sentations where treatment effects are obscured by cell division, lineage progression, donor varia-tion, and cellular stress. Here, we present Disentangled Variational Inference for Perturbation Re-sponse (PertVI), a deep generative model that separates baseline mitotic phase, cellular state, and batch effects from treatment-induced shifts while isolating aberrant off-manifold responses in or-thogonal anomaly space. This structured design tackles two intertwined tasks: (1) quantifying treatment-induced changes in cell-state composition, and (2) inferring state-gated transcriptional changes in response to treatment. Across simulated benchmarks, PertVI accurately disentangles coupled biological axes and recovers weak treatment signatures. In conditional chemical and genet-ic screens of primary human CD8+ and CD4+ T cells, PertVI separates memory-precursor adju-vants from toxic phenocopies, resolves co-clustered regulators into directional kinetic trajectories and biphasic rebounders obscured by standard workflows, and reveals that treatment-induced phe-notypic shifting is decoupled from broad transcriptional perturbation responses and instead gov-erned by state-specific impulses. Altogether, PertVI brings unique mechanistic granularity to sin-gle-cell perturbation response modeling, serving as a proof of principle for biology-informed, struc-ture-guided variance disentanglement in dynamic cellular systems.