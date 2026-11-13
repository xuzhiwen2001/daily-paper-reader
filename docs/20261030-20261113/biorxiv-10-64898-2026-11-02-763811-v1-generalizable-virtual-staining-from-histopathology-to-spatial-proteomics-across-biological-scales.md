---
title: Generalizable virtual staining from histopathology to spatial proteomics across biological scales
title_zh: 跨生物尺度从组织病理学到空间蛋白质组学的可泛化虚拟染色
authors: "Liu, Y., Falik, O., Zhong, Z., Yu, L., Luo, R., Jin, C., Chen, H., Mayer, A. T., Trevino, A. E., Chou, P., Dai, Y., Wu, Z."
date: 2026-11-04
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.02.763811v1.full.pdf"
tags: ["query:spatial-gene"]
score: 8.0
evidence: "从H&E组织学预测空间蛋白的多模态模型"
tldr: "常规H&E组织切片缺乏直接空间蛋白测量，但蕴含分子状态相关形态信息。作者提出QUEST，将蛋白标志物表示为语义查询，从配对H&E与MIF图像中学习可泛化的多重免疫荧光预测。模型在逾万个组织区域训练，跨组织类型和队列重建蛋白表达，并支持细胞表型、邻域分析、组织空间结构与患者分层。该工作把虚拟染色从图像生成拓展为连接常规病理与空间蛋白组学的灵活接口。"
source: biorxiv
selection_source: fresh_fetch
motivation: "常规H&E存档缺少直接空间蛋白测量，限制分子与形态信息联合利用。"
method: "提出QUEST框架，以蛋白标志物为语义查询，在逾万配对H&E-MIF组织区域上训练多路预测。"
result: 跨组织类型和队列重建蛋白强度，保留细胞与组织尺度信息，支持表型、邻域、空间组织及患者分层。
conclusion: "虚拟染色成为连接常规组织学与空间蛋白组学的灵活接口，提升H&E档案分析价值。"
---

## 摘要
大型组织学档案记录了分子组织状态的形态学相关特征，但缺乏直接的空间蛋白质测量。在本研究中，我们表明常规苏木精-伊红（H&E）组织学可提供一种可查询的、基于形态的空间蛋白表达表征，其信息价值从像素层面一直延伸到患者层面。为此，我们开发了QUEST，一种将蛋白标志物表示为语义查询的模型框架，用于灵活的多重免疫荧光（MIF）预测。QUEST在包含超过10,000个组织区域的配对H&E与MIF图像异质性图谱上训练，捕获了与蛋白标志物相关的形态学模式，并在多种组织类型和队列中重建了其表达强度。其效用超越了图像重建，并在多个尺度上保留了具有生物学意义的信息：虚拟染色在细胞和组织尺度上保留了蛋白标志物表达，支持细胞表型分析、细胞邻域分析以及空间组织构成的表征，保留了用于患者分层的临床相关信号，并使基于H&E的查询能够检索具有相似分子谱的MIF参考。这些发现使虚拟染色不再仅仅是图像生成，而成为常规组织学与空间蛋白质组学之间的灵活接口，从而拓展了现有H&E档案的分析价值。

## Abstract
Large histology archives capture morphological correlates of molecular tissue states but lack direct spatial protein measurements. In this study, we show that routine hematoxylin and eosin (H&E) histology can provide a queryable, morphology-based representation of spatial protein expression that remains informative from pixels to patients. To achieve this, we developed QUEST, a model framework that represents protein markers as semantic queries for flexible multiplex immunofluorescence (MIF) prediction. Trained on a heterogeneous atlas of paired H&E and MIF images comprising over 10,000 tissue regions, QUEST captured morphological patterns associated with protein markers and reconstructed their expression intensities across diverse tissue types and cohorts. Its utility extended beyond image reconstruction and preserved biologically meaningful information across multiple scales: virtual staining preserved protein marker expression at the cellular and tissue scales, supported cell phenotyping, cellular neighborhood analysis, and characterization of spatial tissue organization, retained clinically relevant signals for patient stratification, and enabled H&E-based queries to retrieve MIF references with similar molecular profiles. These findings position virtual staining not simply as image generation but as a flexible interface between routine histology and spatial proteomics, expanding the analytical value of existing H&E archives.