---
title: "CellBench: task-dependent performance and generalization limits of single-cell foundation models"
title_zh: CellBench：单细胞基础模型的任务依赖性能与泛化局限
authors: "Xu, Y., Li, Y., Yuan, Y., Xia, Q., Tao, H., Hu, F., Zang, Z."
date: 2026-11-23
pdf: "https://www.biorxiv.org/content/10.64898/2026.04.01.714123v3.full.pdf"
tags: ["query:virtual-cell"]
score: 7.0
evidence: 在遗传扰动筛选与响应预测上评测单细胞基础模型
tldr: 单细胞基础模型（scFMs）广泛用于转录组分析，但其嵌入保留何种生物信息、何时优于数据集拟合方法仍不清楚。作者提出CellBench，在跨组织、物种和遗传扰动筛选中统一评测冻结表征。结果显示不同模型捕获不同生物学侧面，经典基线仍具竞争力；预训练表征可迁移至小鼠监督分析，但在共享解码器下对未见扰动靶点的全基因组绝对误差未能优于“预测无变化”，且模型规模和预训练数据量不能可靠预测性能。该工作表明scFM价值取决于具体生物学任务与证据强度。
source: biorxiv
selection_source: fresh_fetch
motivation: scFMs嵌入是否保留关键生物信息、何时真正优于经典基线尚缺系统证据，亟需统一评测。
method: 构建CellBench，对冻结scFM表征进行跨组织、跨物种及遗传扰动筛选的统一基准测试，并比较经典基线。
result: 不同模型捕获不同生物学侧面，经典基线仍有竞争力；预训练表征可迁移至小鼠，但对未见扰动靶点绝对误差未改善，规模与数据量不能可靠预测性能。
conclusion: scFM表征的价值取决于具体生物学任务及支持其性能的证据强度，不能仅凭规模或数据量推断优势。
---

## 摘要
单细胞基础模型（scFMs）越来越多地用于转录组分析，但其嵌入保留了哪些生物学信息、以及在何时优于数据集拟合方法仍不清楚。在此，我们提出 CellBench，一个统一的基准，用于评估跨组织、物种和遗传扰动筛选的冻结 scFM 表征。我们发现不同模型捕获细胞生物学的不同方面，而经典基线在各任务中仍具竞争力。人类预训练表征可迁移至有监督的小鼠分析，但在共享解码器下，对于未见扰动靶标，它们未能相比“预测无变化”改善全基因组绝对误差。模型规模和所报告的预训练数据量均不能可靠预测性能。排除与预训练记录存在样本或供体标识符匹配的队列，会显著降低注释优势，而模型排名基本不变。总之，这些发现表明 scFM 表征的价值取决于生物学任务以及支持其性能的证据强度。

## Abstract
Single-cell foundation models (scFMs) are increasingly used for transcriptomic analysis, yet it remains unclear what biological information their embeddings preserve and when they outperform dataset-fitted methods. Here, we present CellBench, a unified benchmark of frozen scFM representations across tissues, species, and genetic perturbation screens. We find that different models capture distinct aspects of cellular biology, while classical baselines remain competitive across tasks. Human-pretrained representations transfer to supervised mouse analyses, but under a shared decoder they fail to improve genome-wide absolute error over predicting no change for unseen perturbation targets. Neither model size nor reported pretraining data volume reliably predicts performance. Excluding cohorts with sample or donor identifier matches to pretraining records substantially reduces annotation advantages without changing model rankings appreciably. Together, these findings show that the value of scFM representations depends on the biological task and the strength of the evidence supporting their performance.