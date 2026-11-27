---
title: "Where single-cell foundation models help: a public-data benchmark of annotation, in silico perturbation and gene regulatory inference"
title_zh: 单细胞基础模型在何处有帮助：一项关于注释、计算机模拟扰动和基因调控推断的公共数据基准测试
authors: "Cupaioli, F. A., Merelli, I."
date: 2026-11-26
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.03.763968v4.full.pdf"
tags: ["query:virtual-cell"]
score: 9.0
evidence: 在计算机扰动任务上基准测试单细胞基础模型与监督扰动模型
tldr: 单细胞基础模型被寄望用于注释、计算机扰动与基因调控推断，但适用边界不明。作者用公共数据和预设方案评测五款基础模型、四款新模型、CellOracle、监督扰动模型及简单基线。关键结果是：跨物种迁移中Nicheformer人→鼠肺达0.98，Geneformer V2鼠→人宏F1为0.88；种内嵌入未超主成分；81项删除测试均未达预设标准，而7/8模型的基因向量可提升敲低效应预测。基准与检查以fmaudit发布。
source: biorxiv
selection_source: fresh_fetch
motivation: 单细胞基础模型号称通用，但注释、扰动和调控推断的真实增益缺乏统一、可复现的公共数据评测。
method: 按预设方案在Perturb-seq、脑类器官、小鼠皮层和肺癌活检等公共数据上，对比基础模型、CellOracle、监督扰动模型与简单基线。
result: 跨物种注释增益最大；种内嵌入不敌主成分；零样本扰动仅部分有效，删除测试0/81达标；基因向量提升敲低效应预测。
conclusion: 基础模型的价值集中在跨物种迁移和基因向量特征，而非通用替代；作者发布fmaudit基准及检查以促进可复现评测。
---

## 摘要
单细胞基础模型（FM）被提出作为细胞类型注释、计算机模拟扰动和基因调控网络推断的通用工具。我们在新结果产生之前即固定的分析方案下，基于公共数据对五个FM（scGPT、Geneformer V1和V2、Nicheformer、scFoundation）、四个更新的FM、CellOracle、监督扰动模型以及任务匹配的简单基线进行了基准测试；数据涵盖细胞系和原代T细胞的Perturb-seq筛选、脑类器官筛选、发育中的小鼠皮层以及肺癌活检。FM在跨物种迁移标签时帮助最大：Nicheformer从人到小鼠肺达到0.98准确率，高于所有基线（最高0.94）；微调后的Geneformer V2从小鼠到人达到宏F1 0.88，而基线最高为0.74。在K562中，零样本扰动捕获了真实反应的方向（高达76%的扰动），Geneformer V2通过其过表达方案追踪CRISPRa效应大小（rho = 0.30），其网络比共表达更好地恢复了肿瘤差异表达。在同一物种内，FM嵌入未超过主成分。计算机模拟缺失跟随靶标表达，并且在七个具有重复水平真实值的筛选中，81项测试均未达到预设标准，尽管在K562和RPE1中测得效应在文库间可重复。相比之下，八个FM中七个（包括三个更新模型）的基因向量加到表达特征上后，在独立的全基因组K562筛选中预测了哪些敲低具有大效应（rho在0.34至0.44之间，而仅用表达为0.26）。我们以fmaudit包的形式发布该基准及其检查。

## Abstract
Single-cell foundation models (FMs) are proposed as general tools for cell-type annotation, in silico perturbation and gene-regulatory-network inference. We benchmarked five FMs (scGPT, Geneformer V1 and V2, Nicheformer, scFoundation), four newer FMs, CellOracle, supervised perturbation models and task-matched simple baselines on public data, from Perturb-seq screens of cell lines and primary T cells to a brain organoid screen, the developing mouse cortex and lung cancer biopsies, under an analysis plan fixed before the new results. FMs helped most when labels were transferred across species: Nicheformer reached 0.98 accuracy from human to mouse lung, above every baseline (at most 0.94), and fine-tuned Geneformer V2 reached macro-F1 0.88 from mouse to human, against at most 0.74. In K562, zero-shot perturbations captured the direction of real responses (up to 76% of perturbations), Geneformer V2 tracked CRISPRa effect sizes with its overexpression protocol (rho = 0.30), and its networks recovered tumour differential expression better than co-expression. Within a species, FM embeddings did not exceed principal components. In silico deletions followed target expression and, across seven screens with replicate-level ground truth, met the predefined criterion in none of 81 tests, although in K562 and RPE1 the measured effects replicated between libraries. In contrast, the gene vectors of seven of eight FMs, including three newer models, added to expression features, predicted which knockdowns have large effects in an independent genome-wide K562 screen (rho between 0.34 and 0.44, against 0.26 with expression alone). We release the benchmark and its checks as the fmaudit package.

---

## 论文详细总结（自动生成）

# 论文中文详细总结

## 1. 核心问题与整体含义（研究动机与背景）

- **背景**：以 scGPT、Geneformer、Nicheformer、scFoundation 为代表的单细胞基础模型（FM）被宣称为通用工具，可零样本或微调用于细胞类型注释、计算机模拟扰动（in silico perturbation）和基因调控网络（GRN）推断；若可靠，将能在类器官、组织等难以进行基因改造的系统中开展"干实验"。
- **已有反证**：此前的独立评测已削弱上述预期，例如零样本 FM 嵌入在聚类/数据整合上不优于高变基因或主成分，深度学习扰动预测模型不优于线性或均值基线，零样本嵌入与表达预测方法也未见改进。
- **关键空白**：这些研究多只评估细胞系中的单一任务，不清楚其结论能否外推到类组织系统和疾病模型，也不清楚一个任务上表现好的模型能否在另一个任务上被信任。
- **本文目标**：在**新结果产生之前即固定分析方案**的前提下，用纯公共数据，在三个任务（注释、扰动、GRN）× 三个生物复杂度层级（细胞系与原代细胞、神经组织、人体组织）上系统评测 FM，并回答"FM 到底在何处有帮助"。

## 2. 方法论：核心思想与关键技术细节

- **核心思想**：构建"任务 × 系统"的评测网格，每一行（同一任务、同一数据）内所有方法使用**相同的细胞、数据划分、基因全集和指标**，并强制与任务匹配的非 FM 简单基线、朴素预测器和置换零假设比较。
- **注释流程**：用零样本细胞嵌入做 kNN 标签迁移（数据集内 k=30、余弦距离；跨数据集 k=20、欧氏距离并带置信度覆盖）；跨物种使用一对一直系同源基因和粗略类别映射；基线为 2000 个高变基因上的 PCA + 同一分类器、z-score 高变基因、CellTypist。
- **计算机模拟扰动**：采用"嵌入—删除—再嵌入"（embed–delete–re-embed）协议，靶基因从每个细胞的输入中删除，效应定义为原始与扰动嵌入的余弦距离并按细胞类型平均；对 scGPT 固定采样基因与打破平局的方式，保证两次输入只差目标基因；删除前做**靶基因检出检查**；Geneformer 另用其原生过表达协议（把目标移到输入第一位）模拟 CRISPRa。
- **真实效应的度量**：组织数据以文库 + 细胞类型的伪批量计数、edgeR 准似然计算，避免把同一文库细胞当作独立重复；组织筛选的真实值为 FDR<0.05 的 DEG 数与组成变化的 CMH log odds ratio；小鼠皮层采用配对设计（同类别同文库的 GFP 对照，≥3 细胞/组、≥20 扰动细胞、≥2 文库）。
- **预设判定规则**：预测为"阳性"须同时满足：Spearman ρ>0 且族内 BH q<0.05；比最佳朴素预测器高至少 0.10 且 bootstrap 差值区间>0；超过在表达十分位或细胞类型内置换基因的零假设（1000 次置换）。
- **朴素预测器**：靶基因平均表达、检出率、扰动/对照细胞数、文库大小、每细胞类型检出基因数。
- **复制上限（replication ceiling）**：以文库两半之间（或供体之间）测得效应的一致性作为真实值噪声上限。
- **表达匹配特异性检验**：将删除目标基因的嵌入位移，与在同一细胞中逐一删除 20 个表达匹配对照基因的位移比较，定义特异效应 S = 观测 − 对照均值，z = S / sd(对照)，z>2 视为存在特异超额位移。
- **基因表征分析**：取各 FM 的上下文无关基因向量（不含位置嵌入），作为岭回归特征预测每个靶标的 log DEG 数，单独或叠加到表达特征（平均 log 表达、检出率、扰动细胞数）或 STRING v12 度上；用 5 折/10 折靶标交叉验证的合并折外 Spearman ρ 评分，并以 Freedman–Lane 残差置换（200 个零真实值）检验增益。
- **GRN 推断**：从上下文基因嵌入相似度和跨层跨头平均注意力构建基因—基因网络，用 FE@50（top-50 邻居的表达式匹配富集倍数，1 为随机）对 K562 敲低靶标、ChIP-Atlas ChIP-seq 靶标、肺癌 EGFR 抑制响应基因打分。
- **微调**：每个 FM 作为细胞类型分类器微调（线性探针、部分解冻、LoRA，scGPT 另含教程全量微调），4000 训练 / 1000 验证细胞，验证集选配置后只测一次；并用张量级权重检查确认参数确实改变。

## 3. 实验设计：数据集、Benchmark 与方法对比

- **Level 1（细胞系与原代细胞）**：Immune Human atlas（33,506 细胞、16 类）；Tabula Muris Senis 小鼠肺；Norman CRISPRa K562（91,205 细胞）；Adamson CRISPRi K562（68,603 细胞、87 条件）；K562 与 RPE1 必需基因 CRISPRi Perturb-seq；原代 CD4 T 细胞全基因组 CRISPRi 筛选（4 供体，静息及刺激 8h/48h）。
- **Level 2（神经组织）**：CHOOSE 脑类器官嵌合 CRISPR 筛选（28,344 细胞、36 基因、991 非靶向对照、16 细胞类型，HNOCA 作参考）；iPSC 来源神经元的 CRISPRi 与 CRISPRa 筛选；小鼠皮层体内 Perturb-seq（35 个孤独症/神经发育风险基因，E12.5 子宫内递送、P7 取样，17,889 分析细胞、17 文库、5 类别、374 GFP 对照）。
- **Level 3（人体组织）**：EGFR 突变非小细胞肺癌活检（23,261 Smart-seq2 细胞），HLCA core 作人肺参考。
- **确认性独立筛选**：K562 全基因组 CRISPRi Perturb-seq（7,568 靶标、267 文库；其中 7,509/7,557 靶标在本研究其他部分从未使用）。
- **对比方法**：五个 FM（scGPT、Geneformer V1-10M 与 V2-316M、Nicheformer、scFoundation）；四个更新 FM（UCE、SCimilarity、CellPLM、TranscriptFormer，按纳入基准数事先排序）；Cell
