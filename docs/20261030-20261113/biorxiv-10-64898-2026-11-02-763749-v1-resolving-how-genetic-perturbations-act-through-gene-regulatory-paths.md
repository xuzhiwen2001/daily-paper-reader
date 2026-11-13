---
title: Resolving how genetic perturbations act through gene regulatory paths
title_zh: 解析遗传扰动如何通过基因调控路径发挥作用
authors: "Ren, L., Duren, Z."
date: 2026-11-03
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.02.763749v1.full.pdf"
tags: ["query:virtual-cell"]
score: 8.0
evidence: 从Perturb-seq解析遗传扰动经调控路径的作用机制
tldr: Perturb-seq可测大量遗传扰动的转录响应，但单一基因响应混合多条调控路径，仅靠表达量难以解析扰动机制。REGA-perturb用参考表观基因组构建TF—调控元件—基因路径骨架，并借共享潜在程序汇聚扰动响应，推断各路径使用方式且只需RNA数据。在三套CRISPRi筛选共240万细胞中，其TF—靶标推断显著优于现有方法，可区分直接/间接靶标并预测留出TF靶标。该工作还揭示TF活性变化与表达层抵消的调控重连，为扰动机制解析提供可解释路径框架。
source: biorxiv
selection_source: fresh_fetch
motivation: Perturb-seq的基因表达响应混合多条调控路径，仅靠表达谱无法分辨扰动如何通过具体TF—调控元件—基因路径起作用。
method: REGA-perturb以参考表观基因组定义TF—调控元件—基因路径骨架，并通过共享潜在程序汇聚扰动响应，仅用RNA数据推断路径使用方式。
result: 三套CRISPRi筛选共240万细胞中，TF—靶标推断与ChIP-seq一致，随机增益超最佳方法4倍，并区分直接/间接靶标、预测留出TF靶标。
conclusion: 该工作把表观基因组路径骨架与扰动响应结合，揭示TF活性变化及表达层抵消的调控重连，为解析扰动机制提供可解释框架。
---

## 摘要
Perturb-seq可测量数千种遗传扰动的转录响应，但每个基因的响应混合了许多调控路径的贡献，因此无论模型多大，仅凭表达无法解析扰动如何起作用。我们提出REGA-perturb，它提供这种缺失信息而非增加模型复杂度：参考表观基因组定义了可能的转录因子（TF）-调控元件-基因路径支架，扰动响应通过共享潜在程序进行汇聚，确定每条路径的使用方式，且仅需RNA测量数据。在总计240万个细胞的三个CRISPR干扰筛选中，REGA-perturb推断的TF-靶标关系与ChIP-seq结合一致，其相对于随机基线的提升是最佳现有方法的四倍以上，区分了候选直接与间接靶标，并预测了训练中未包含的TF的靶标。它还推断了未反映在TF转录水平中的扰动诱导的TF活性变化，并解析了扰动特异性调控重连，其中相反的调控变化在表达水平上相互抵消。

## Abstract
Perturb-seq measures transcriptional responses to thousands of genetic perturbations, but each gene's response mixes the contributions of many regulatory paths, so how a perturbation acts cannot be resolved from expression alone, however large the model. Here we present REGA-perturb, which supplies this missing information rather than adding model complexity: reference epigenomes define a scaffold of possible transcription factor (TF)-regulatory element-gene paths, and perturbation responses, pooled through shared latent programs, determine how each path is used, requiring only RNA measurements. Across three CRISPR interference screens totaling 2.4 million cells, REGA-perturb inferred TF-target relationships that agreed with ChIP-seq binding with a gain over random more than four times that of the best existing method, separated candidate direct from indirect targets, and predicted targets of TFs withheld from training. It also inferred perturbation-induced changes in TF activity not reflected in TF transcript levels, and resolved perturbation-specific regulatory rewiring in which opposing regulatory changes cancel at the expression level.