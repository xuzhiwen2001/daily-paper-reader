---
title: LingoCell interprets gene perturbations through natural language and tissue niches
title_zh: LingoCell 通过自然语言和组织生态位解读基因扰动
authors: "Yang, Y., Xu, W., Zhang, Z., Cui, Y., Yu, X., Gu, W., Wang, J., Nakai, K."
date: 2026-11-10
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.08.765157v1.full.pdf"
tags: ["query:virtual-cell"]
score: 8.0
evidence: 单细胞基础模型开展单基因与组合的原位扰动模拟
tldr: 单细胞基础模型难以用生物语言解释表达量变化、迁移到稀疏空间数据并解释细胞微环境。LingoCell将单细胞与空间转录组表征同语言对齐，同时保持基因表达可编辑，支持注释、整合、描述生成和扰动读出。在肺腺癌中，它揭示弱化肺泡分化与强化恶性程序的协同疾病响应；在结直肠癌中，它发现同一成纤维细胞状态向T细胞、巨噬细胞和肿瘤细胞传递不同程序。该框架为靶点组合与基质干预优先级提供统一工具。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有单细胞基础模型难以用自然语言解释表达量变化、迁移至稀疏空间数据并刻画细胞微环境。
method: LingoCell对齐细胞表征与语言并保持基因表达可编辑，扩展至空间组织，实现无参考注释、生态位嵌入和空间扰动。
result: 肺腺癌中揭示肺泡分化减弱与恶性程序增强的协同响应；结直肠癌中同一成纤维细胞状态向多种细胞传递不同程序。
conclusion: 该模型统一单细胞与空间扰动解释，为优先筛选靶点组合和基质干预方案提供框架。
---

## 摘要
单细胞基础模型是解析细胞身份和疾病状态的通用工具，但难以用生物学语言解释表达量变化、迁移至稀疏空间测量数据，以及解释细胞生态位。我们提出 LingoCell，一种连接单细胞与空间转录组学的基础模型。它将细胞表征与语言对齐，同时保持基因表达可编辑，支持细胞注释、跨批次整合、描述生成，以及单基因和组合式计算机模拟扰动的疾病语言读出。扩展到组织层面，它无需单细胞参考即可注释细胞，学习以身份为条件的生态位嵌入，并通过替换和编辑邻近细胞表达进行空间计算机模拟扰动。在肺腺癌中，LingoCell 揭示了同时削弱肺泡分化程序和增强恶性程序所产生的协同疾病反应。在结直肠癌中，它揭示了同一成纤维细胞状态向 T 细胞、巨噬细胞和肿瘤细胞传递的不同程序。LingoCell 提供了一个统一框架，用于优先确定靶点组合和基质干预方案。

## Abstract
Single-cell foundation models are general tools for resolving cell identities and disease states, but struggle to interpret changes in expression magnitude in biological language, to transfer to sparse spatial measurements, and to explain cellular niches. We introduce LingoCell, a foundation model connecting single-cell and spatial transcriptomics. It aligns cell representations with language while keeping gene expression editable, supporting cell annotation, cross-batch integration, description generation, and disease-language readouts of single-gene and combinatorial in silico perturbations. Extended to tissues, it annotates cells without single-cell references, learns identity-conditioned niche embeddings, and performs spatial in silico perturbation by replacing and editing neighbor expression. In lung adenocarcinoma, LingoCell revealed synergistic disease responses to jointly weakening alveolar differentiation programs and strengthening malignant programs. In colorectal cancer, it revealed different programs conveyed by the same fibroblast state to T cells, macrophages, and tumor cells. LingoCell provides a unified framework for prioritizing target combinations and stromal intervention programs.