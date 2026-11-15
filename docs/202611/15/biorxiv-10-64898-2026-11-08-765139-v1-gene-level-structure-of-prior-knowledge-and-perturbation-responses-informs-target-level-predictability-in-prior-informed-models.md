---
title: Gene-level structure of prior knowledge and perturbation responses informs target-level predictability in prior-informed models
title_zh: 先验知识与扰动响应的基因水平结构可为先验信息模型中的靶标水平可预测性提供信息
authors: "Park, J., Sim, H., Hwang, B."
date: 2026-11-10
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.08.765139v1.full.pdf"
tags: ["query:virtual-cell"]
score: 9.0
evidence: 预测未见遗传扰动的转录响应模型
tldr: 转录响应预测模型日益引入生物先验知识，但先验知识能否反映各靶点的扰动响应关系仍不清楚。作者构建基因相似性框架，系统比较八类先验知识与六套Perturb-seq数据衍生的共功能、共调控关系。研究发现先验一致性及先验衍生的训练-测试相似度可追踪靶点级预测性能的相对差异。该框架揭示先验与扰动响应对齐的基因和情境异质性，为在测量响应前评估可预测性提供依据。
source: biorxiv
selection_source: fresh_fetch
motivation: 先验知识常被用于扰动响应预测，但其与靶点扰动关系的匹配程度及对预测性能的指示作用尚不明确。
method: 构建基因相似性框架，量化八类生物先验知识之间及与六套Perturb-seq衍生的共功能、共调控关系的一致性，并关联三种先验模型预测性能。
result: "先验一致性解释共功能一致变异的30-47%、共调控的35-43%；必需基因更高，转录因子和信号基因更低，且随表达特征和细胞情境变化。"
conclusion: 先验一致性和训练-测试相似度可在未测响应时提供靶点可预测性的相对判断，但关联强度受模型、数据和先验来源影响。
---

## 摘要
背景：针对未见遗传扰动的转录响应的预测模型日益纳入生物学先验知识。然而，先验知识在多大程度上反映每个靶标的扰动-响应关系，以及先验衍生的度量与靶标水平预测性能的吻合程度，仍不清楚。在此，我们开发了一个基因相似性框架，用于量化八种生物学先验知识来源之间的一致性，以及先验知识与来自六个 Perturb-seq 数据集的共功能或共调控关系之间的一致性。结果：在全基因组和必需基因筛选中，先验一致性解释了共功能一致性变异的30-47%和共调控一致性变异的35-43%。与 Perturb-seq 响应的一致性在必需基因中较高，在转录因子和信号基因中较低，并随基因表达特征和细胞背景而变化。我们比较了先验一致性和先验衍生的训练-测试相似性与基于观测测试响应的度量在追踪靶标水平预测性能方面的表现。在三个先验信息模型中，对于观测到的扰动-响应关系与先验知识更匹配且与训练扰动更相似的靶标，预测更准确。值得注意的是，在不使用测试响应的情况下计算的先验一致性和先验衍生训练-测试相似性，能够追踪靶标水平预测性能的相对差异。这些关联的强度因模型和数据集而异；对于训练-测试相似性，还因先验来源而异。结论：我们的框架揭示了生物学知识与扰动响应对齐方式的基因水平和背景水平异质性，并为在测量扰动响应之前评估相对扰动可预测性提供了先验基础。

## Abstract
Background: Predictive models of transcriptional responses to unseen genetic perturbations increasingly incorporate biological prior knowledge. However, it remains unclear how well prior knowledge reflects each target's perturbation-response relationships and how closely prior-derived measures track target-level predictive performance. Here, we develop a gene-similarity framework to quantify agreement among eight sources of biological prior knowledge and between prior knowledge and co-function or co-regulation relationships derived from six Perturb-seq datasets. Results: In genome-wide and essential-gene screens, prior agreement accounted for 30-47% of the variance in co-function agreement and 35-43% in co-regulation agreement. Agreement with Perturb-seq responses was higher for essential genes, lower for transcription factor and signaling genes, and varied with gene expression characteristics and cellular context. We compared prior agreement and prior-derived train-test similarity with measures based on the observed test response in tracking target-level predictive performance. Across three prior-informed models, predictions were more accurate for targets whose observed perturbation-response relationships better matched prior knowledge and that were more similar to training perturbations. Notably, prior agreement and prior-derived train-test similarity, calculated without the test response, tracked relative differences in target-level predictive performance. The strength of these associations varied across models and datasets and, for train-test similarity, across prior sources. Conclusion: Our framework reveals gene- and context-level heterogeneity in how biological knowledge aligns with perturbation responses, and provides an a priori basis for assessing relative perturbation predictability before perturbation responses are measured.

---

## 论文详细总结（自动生成）

## 一、核心问题与整体含义

- **研究背景**：Perturb-seq 将遗传扰动与单细胞转录组读出结合，使得"对未见扰动进行转录响应预测"成为可能。近年 GEARS、PRESAGE、TxPert 等先验信息模型（prior-informed models）大量引入共表达、GO 图、通路注释、预训练基因嵌入等生物先验以提升泛化能力。
- **核心矛盾**：先验知识来源于异质组织、检测手段与注释体系，而 Perturb-seq 响应是在特定细胞类型与实验条件下测得的。一个基因在数据库中"被研究得很充分"，并不代表其在该情境下的扰动响应能被先验准确刻画。聚合层面的 benchmark 分数会掩盖单个靶标之间的巨大差异。
- **已有工作的空白**：
  - GEARS 考察了知识图谱连通性与模型不确定性；TxPert 关联了靶标知识与图度数；PRESCRIBE 用靶标-训练相似性估计置信度；PRESAGE 用聚合先验嵌入的邻域密度。
  - 但"先验之间的一致性"虽可在不测响应的情况下计算，却**不能直接说明先验在多大程度上捕捉了该靶标的扰动-响应关系**；先验衍生度量与基于观测测试响应的度量在追踪靶标级性能上的相对表现也未被系统比较。
- **整体含义**：作者希望建立一个**基因水平的统一框架**，把"先验间一致性—先验与观测响应的一致性—靶标级预测性能"三者串联起来，从而在**测量响应之前**就能给出靶标可预测性的相对判断，用于实验优先级排序与主动学习。

## 二、方法论

### 核心思想
将所有异质的先验来源与 Perturb-seq 数据统一转换为**基因相似性谱（gene similarity profile）**：每个基因表示为一个"它与所有其他基因相似度"的向量，从而可在同一表示空间内做局部与全局比较。

### 关键概念
- **共功能（co-function）**：Perturb-seq 中扰动效应谱之间的相似性。
- **共调控（co-regulation）**：被测量 mRNA 在不同扰动下响应谱之间的相似性。
- **相似性矩阵构建**：
  - PRESAGE 衍生的嵌入（GenePT、STRINGdb、MSigDB、DepMap）与 scGPT 嵌入：使用余弦相似度。
  - PERISCOPE、Marbach 调控网络、UnTANGLeD：先转为基因-特征矩阵，再用 Spearman 相关。
  - Perturb-seq：对扰动效应矩阵按扰动均值中心化后计算余弦相似度（以去除跨扰动共享的系统性响应成分）。

### 基因水平一致性度量
- **局部一致性**：两个相似性谱各自 top-K 最近邻基因集合的 **IoU（交并比）**，取 K=100。
- **全局一致性**：两个完整相似性谱之间的 **Spearman 相关**。
- **零分布标准化**：随机配对基因重复 1,000 次，将观测值转为局部/全局 Z 分数。
- **基因一致性分数（GAS）**：局部与全局 Z 分数的平均；任一 Z > 2.5 视为显著。
- **先验一致性（prior agreement）**：对 28 个先验对（8 个来源两两组合）的 GAS 取平均。
- **共功能/共调控一致性**：对 8 个先验分别与 Perturb-seq 共功能/共调控矩阵比较得到的 GAS 取平均。

### 回归与方差分解
- 以共功能或共调控一致性为因变量，先验一致性为核心自变量，加入协变量：必需基因、信号通路基因、转录因子（TF）、控制细胞中的平均表达与表达方差。
- 报告协变量调整后的系数，以及 ΔR² = R²_full − R²_reduced 来量化额外解释方差；FDR 用 Benjamini–Hochberg 校正。

### 可预测性（forecastability）框架
- **定义**：对每个留出靶标计算一个预定义的可预测性度量，再计算该度量与观测预测性能（加权 R²(Δpert)）在靶标间的 Pearson 相关。
- **2×2 度量体系**：
  - 一致性类（A）：A_prior（先验间）vs A_cofunc（先验与观测共功能）。
  - 训练-测试相似性类（S）：S_cofunc（基于观测共功能矩阵）vs S_prior（对功能共识组 5 个先验的 S 取平均）。
- **S 的定义**：每个测试扰动与 K 个最近训练扰动的平均相似度，K=5（对 K=5/10/20 做了稳定性检验）。
- **情境稳定/特异分类**：在 4 个必需基因筛选中，对共功能一致性的均值与标准差设阈值，分别做 GSEA 识别情境稳定与情境特异通路。

## 三、实验设计

### 先验知识来源（8 个）
- 图衍生：**MSigDB**、**STRINGdb**
- 模型衍生嵌入：**GenePT**、**scGPT**（blood 预训练模型）
- CRISPR 衍生：**DepMap**、**PERISCOPE**（A549）
- 观测数据：**Marbach et al.** 调控网络（CML）、**UnTANGLeD** 基因-性状关联
- 为保证可比性，取 8 个来源共有的 **10,875 个基因**作为参考基因集。

### Perturb-seq 数据集（6 个）
- Replogle et al. 2022：K562 全基因组、K562 必需基因、RPE1 必需基因、HepG2 必需基因、Jurkat 必需基因
- Nadig et al. 2025：RPE1 TF-wide
- Huang et al. 2025（X-Atlas/Orion）：HEK293、HCT116 全基因组
- 覆盖 69–83% 的扰动靶标与 77–81% 的被测 mRNA。

### Benchmark 与对比方法
- **预测模型**：GEARS、scLAMBDA、PRESAGE（三种先验信息模型）。
- **基准框架**：扩展 Miller et al. 的 CellSimBench 流程，五折扰动级留出交叉验证，评估指标为加权 R²(Δpert)，并与**均值预测器基线**对比。
- **对照度量**：A_prior vs A_cofunc；S_cofunc vs S_prior vs 各单一先验的 S。
- **额外分析**：跨情境扩展（9 种细胞系 × 靶标集组合）、必需基因限制评估（匹配训练/测试扰动数量）、回顾性训练集选择分析（K562 全基因组，5 个随机 100 扰动测试集）。

### 验证性分析
- 相似性谱 vs 原始谱的跨数据集区分度（K562 全基因组 vs 必需基因，用能量距离、Pearson/Spearman/余弦）。
- 中心化 vs 未中心化的相似性分布对比。
- GSEA 富集（GO BP、CORUM、GWAS Catalog），识别 12 个先验通路簇（PC）、6 个共功能簇（FC）、6 个共调控簇（RC）。

## 四、资源与算力

- **论文正文与 Methods 中均未明确说明**所使用的 GPU 型号、数量、训练时长或总计算量。
- 仅提及模型训练"使用其原始流程或对应的 CellSimBench 适配器"，以及使用 gseapy 做富集分析、在公开数据与 Zenodo 预处理矩阵上运行。
- 因此无法从文本评估其算力规模，这是该预印本在可复现性描述上的一个缺口。

## 五、实验数量与充分性

- **规模**：8 个先验 × 28 个先验对；8 个先验 × 6 个 Perturb-seq 数据集的先验–响应比较；3 个预测模型 × 5–9 个数据集/情境组合；9 种细胞情境 × 靶标集组合的 forecastability 分析；5 次重复的训练集选择实验。
- **消融/稳健性检验**：
  - K 值（5/10/20）对 S 度量的稳定性；
  - 中心化 vs 未中心化对相似性分布的影响；
  - 相似性谱 vs 原始谱的跨数据集可比性；
  - 匹配训练/测试扰动数量以排除样本量混杂；
  - 匹配 A_prior 分布以隔离相似性效应。
- **充分性评价**：整体实验设计较为系统，覆盖了"先验–先验""先验–响应""度量–预测性能"三个层次，并做了情境与靶标集的交叉验证。但：
  - 预测模型仅 3 个，且以 PRESAGE 为主做跨情境扩展，模型层面的泛化证据有限；
  - 数据集虽多，但部分结论（如 HEK293/HCT116 的低 forecastability）无法完全归因于细胞情境，因靶标组成与实验流程也不同；
  - 属于观察性关联分析，未做前瞻性干预验证。
- **公平性**：使用了统一的参考基因集、统一的评估指标与五折交叉验证，并与均值基线对比，方法学上较为客观；但先验间存在信息复用，可能使一致性度量被高估（作者亦在局限中承认）。

## 六、主要结论与发现

1. **先验一致性可解释相当比例的响应一致性变异**：在全基因组筛选中解释共功能一致性的 47%、共调控一致性的 43%；在 4 个必需基因筛选中分别为 30–42% 与 35–40%。加入基因注释与表达特征后 ΔR² 进一步增加（共功能 0.011–0.064，共调控 0.115–0.194）。
2. **先验来源存在"功能共识组"**：scGPT、GenePT、MSigDB、STRINGdb、DepMap 相互一致性高（STRINGdb–GenePT 局部一致性显著基因占 67%）；PERISCOPE、UnTANGLeD、Marbach 一致性较低。
3. **共功能与共调控的先验偏好不同**：scGPT 与共调控一致性最高（与其单细胞表达预训练一致）；GenePT、MSigDB、STRINGdb、DepMap 与共功能更匹配。
4. **通路层面的共享与特异**：翻译/rRNA 成熟、OXPHOS/线粒体代谢在共功能与共调控中均富集；转录起始/中介体复合物为共功能特异；细胞周期/染色体分离为共调控特异。
5. **基因类别与表达特征的影响**：
