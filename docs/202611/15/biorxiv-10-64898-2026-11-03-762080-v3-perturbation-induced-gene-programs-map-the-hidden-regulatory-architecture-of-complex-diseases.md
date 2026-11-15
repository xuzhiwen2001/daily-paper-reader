---
title: Perturbation-induced gene programs map the hidden regulatory architecture of complex diseases
title_zh: 扰动诱导的基因程序揭示复杂疾病的隐藏调控架构
authors: "Turhan, B., Lee, H., Liu, D., Le, A., Ghosh, A., Nandi, D., Mazumder, R., Engreitz, J. M., Jin, X., Huangfu, D., Dey, K. K."
date: 2026-11-11
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.03.762080v3.full.pdf"
tags: ["query:virtual-cell"]
score: 7.0
evidence: 在CRISPR Perturb-seq中为单个扰动学习多尺度基因程序
tldr: 稳态分子图谱难以捕捉扰动后才显现的疾病调控程序。作者提出Perturbscape，用线性与非线性对比学习从CRISPR Perturb-seq中学习单扰动多尺度基因程序，并与人类遗传学整合。跨7个系统、53个性状的分析显示，扰动诱导程序的可遗传性信息量最高提升4.3倍，且在控制稳态优先级后仍显著。该框架还揭示了K562、HepG2及胰岛分化、神经元亚类中的疾病相关通路。
source: biorxiv
selection_source: fresh_fetch
motivation: 稳态分子图谱难以完整反映遗传变异影响复杂疾病的调控程序，尤其缺少仅在细胞受扰动后出现的程序。
method: 提出Perturbscape，用线性和非线性对比学习及互补程序学习，从CRISPR Perturb-seq学习单扰动多尺度基因程序，并整合人类遗传学。
result: 在7个系统、53个性状中，扰动诱导程序可遗传性信息量最高提升4.3倍，控制稳态后仍显著，并获K562、HepG2等正交证据支持。
conclusion: 扰动诱导基因程序是疾病相关调控信息的互补层，可揭示稳态图谱未充分代表的遗传信息通路与情境特异调控关系。
---

## 摘要
稳态分子谱不能完整捕捉遗传变异影响复杂疾病的调控程序，尤其是仅在细胞受到扰动时才出现的程序。在此，我们提出 Perturbscape，一个计算框架，它利用线性和非线性对比方法以及互补的程序学习方法，在 CRISPR Perturb-seq 筛选中为单个扰动学习多尺度基因程序，并将其与人类遗传学整合，以优先排序疾病相关基因、扰动和下游调控通路。在来自 7 个 Perturb-seq 系统和 53 种复杂疾病与性状（GWAS 平均 N=291K）的 15,859 个扰动×背景谱中，扰动诱导程序显示出比类似稳态多组织基因优先排序高达 4.3 倍的遗传力信息量，并且在考虑稳态优先排序后，在所有 34 个匹配的细胞系统-性状比较中保留了显著的条件遗传力信息量。保留扰动特异性程序进一步使性状相关性评分比来自对照细胞、合并扰动或差异表达汇总的程序高 2.5-5.3 倍。在 K562 中，Perturbscape 优先排序的基因对罕见变异负荷基因表现出比稳态优先排序更强的富集，并得到正交增强子 CRISPRi 筛选的支持。在 HepG2 中，LDL 胆固醇相关的扰动诱导程序特异性地揭示了他汀响应通路，而稳态 PoPS 优先排序未显著富集这些通路，药理学转录反应和人群血浆蛋白质组学支持这一点。Perturbscape 还恢复了血液相关性状条件下的反式调控关系，这些关系在 IFN-γ 刺激的单核细胞中特异性地得到群体 trans-eQTL 的支持（OR = 1.30，P=1.6e-05）。Perturbscape 进一步揭示了胰腺胰岛分化过程中单基因糖尿病调控因子与多基因 T2D 风险之间的发育阶段特异性汇聚，以及体内神经元亚类特异性的自闭症相关调控程序。总之，这些发现确立了扰动诱导的基因程序作为疾病相关调控信息的补充层，揭示了稳态分子图谱未能完整呈现的具有遗传信息价值的通路和情境特异性调控关系。

## Abstract
Steady-state molecular profiles incompletely capture the regulatory programs through which genetic variation influences complex disease, particularly programs that emerge only when cells are perturbed. Here, we introduce Perturbscape, a computational framework that learns multiscale gene programs for individual perturbations in a CRISPR Perturb-seq screen using linear and nonlinear contrastive approaches alongside complementary program-learning methods, and integrates them with human genetics to prioritize disease-relevant genes, perturbations and downstream regulatory pathways. Across 15,859 perturbation-by-context profiles from 7 Perturb-seq systems and 53 complex diseases and traits (mean GWAS N=291K), perturbation-induced programs showed up to 4.3-fold higher heritability informativeness than analogous steady-state multi-tissue gene prioritization, and retained significant conditional heritability informativeness across all 34 matched cell system-trait comparisons after accounting for steady-state prioritization. Preserving perturbation-specific programs further yielded 2.5-5.3-fold higher trait relevance scores than programs derived from control cells, pooled perturbations or differential-expression summaries. In K562, Perturbscape-prioritized genes showed stronger enrichment for rare-variant burden genes than steady-state prioritization and were supported by orthogonal enhancer CRISPRi screens. In HepG2, LDL cholesterol-associated perturbation-induced programs specifically revealed statin-responsive pathways not significantly enriched by steady-state PoPS prioritization, supported by pharmacological transcriptional responses and population plasma proteomics. Perturbscape also recovered blood-related trait-conditioned trans-regulatory relationships that were specifically supported by population trans-eQTLs in IFN-gamma-stimulated monocytes (OR = 1.30, P=1.6e-05). Perturbscape further revealed developmental-stage-specific convergence between monogenic diabetes regulators and polygenic T2D risk during pancreatic islet differentiation, and neuronal-subclass-specific autism-associated regulatory programs in vivo. Together, these findings establish perturbation-induced gene programs as a complementary layer of disease-relevant regulatory information, revealing genetically informative pathways and context-specific regulatory relationships incompletely represented by steady-state molecular atlases.