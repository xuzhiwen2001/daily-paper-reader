---
title: Predicting Transcriptional Responses to Unseen Compounds through Context Modeling and Multi-View Transfer
title_zh: 通过上下文建模与多视图迁移预测对未见化合物的转录响应
authors: "Lei, Y., Liang, H., Peng, K., Wen, J."
date: 2026-11-06
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.05.764505v1.full.pdf"
tags: ["query:virtual-cell"]
score: 9.0
evidence: 通过多视图迁移预测未见化合物的药物诱导转录响应
tldr: 药物诱导转录响应预测对虚拟筛选很重要，但现有模型几乎不利用化合物信息，在drug-blind基准上去掉药物输入后性能变化极小。UnDetect将细胞与实验背景变异同化合物效应分离，融合化学结构、靶点、作用机制和Cell Painting形态，构建可容忍信息缺失的多视图核并跨细胞系迁移残差响应。在drug-blind基准上它每折均优于忽略化合物的网络，板内得分0.117超过最强已发表模型的0.092，DeepCE基准Pearson达0.602。该工作说明分离背景与化合物效应并整合互补信息能提升未见化合物的转录响应预测。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有转录响应预测模型主要捕捉细胞和实验共性变异，对化合物输入依赖弱，难以区分药物特异效应。
method: UnDetect分离背景变异与化合物效应，用化学结构、靶点、机制和Cell Painting构建归一化多视图核，并跨细胞系迁移残差响应。
result: 在drug-blind基准每折均优于忽略化合物的网络，板内得分0.117对0.092；DeepCE基准Pearson为0.602对0.491，跨细胞系迁移多数评估提升。
conclusion: 结果表明，分离上下文与化合物效应并整合互补化合物信息，可提升未见化合物转录预测并扩展扰动图谱用于虚拟筛选。
---

## 摘要
预测药物诱导的转录响应可为新化合物的计算机筛选提供支持，但现有模型几乎未利用化合物信息：在一个药物盲的L1000基准上，从七个已发表模型中移除药物输入，准确率变化至多为0.012的Pearson相关系数。这些模型捕捉共有的细胞与实验变异，却忽略了区分药物效应的化合物特异性信号。我们提出UnDetect框架，将上下文变异与化合物效应分离，以预测对未进行转录谱分析的化合物的响应。UnDetect将化学结构、标注靶点、作用机制和Cell Painting形态整合到一个归一化多视图核中，该核可容纳不完整的化合物信息，并在已分析细胞系内部及跨细胞系迁移残差响应，从而使药理学和表型关系在化学相似性之外为预测提供信息。在一个药物盲基准上（其中配对对照揭示检测板），UnDetect是唯一在每个折中都优于忽略化合物的网络的模型；在一个对任何化合物盲预测均为零的板内评分上，它达到0.117，而最强已发表模型为0.092。在DeepCE的基准上，它达到0.602的Pearson相关系数，而报告值为0.491。跨细胞系迁移在28项LINCS L1000评估中全部28项得到改善，并在两个较高剂量下，在50项Tahoe-100M细胞系评估中分别改善47项和49项。这些结果表明，将上下文与化合物效应分离并整合互补的化合物信息可改善转录预测，并拓展扰动图谱在虚拟筛选中的效用。

## Abstract
Predicting drug-induced transcriptional responses could support in silico screening of new compounds, yet existing models barely use the compound: on a drug-blind L1000 benchmark, removing the drug input from seven published models changes accuracy by at most 0.012 Pearson correlation. They capture shared cellular and experimental variation while overlooking the compound-specific signals that distinguish drug effects. We present UnDetect, a framework that separates contextual variation from compound effects to predict responses to transcriptionally unprofiled compounds. UnDetect integrates chemical structure, annotated targets, mechanisms of action and Cell Painting morphology into a normalized multi-view kernel that accommodates incomplete compound information, and transfers residual responses within and across profiled cell lines, so that pharmacological and phenotypic relationships inform predictions beyond chemical similarity. On a drug-blind benchmark, where the paired control reveals the assay plate, UnDetect is the only model to beat a network that ignores the compound, in every fold; on a within-plate score that is zero for any compound-blind prediction, it reaches 0.117 against 0.092 for the strongest published model. On DeepCE's benchmark it reaches 0.602 Pearson correlation against the reported 0.491. Transfer across cell lines improves 28 of 28 LINCS L1000 and, at the two higher doses, 47 and 49 of 50 Tahoe-100M cell-line evaluations. These results show that separating context from compound effects and integrating complementary compound information improves transcriptional prediction and extends the utility of perturbation atlases for virtual screening.