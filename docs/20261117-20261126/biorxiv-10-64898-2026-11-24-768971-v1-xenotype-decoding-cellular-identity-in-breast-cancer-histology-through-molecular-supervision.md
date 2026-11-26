---
title: "XenoType: Decoding cellular identity in breast cancer histology through molecular supervision"
title_zh: XenoType：通过分子监督解码乳腺癌组织学中的细胞身份
authors: "Forjaz, D. F., Vieira, D. F., Queiroga, V., Willig, M. L., Joshi, S., Kiemen, A. L., Forjaz, A., Wirtz, D., Wu, P.-H."
date: 2026-11-25
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.24.768971v1.full.pdf"
tags: ["query:spatial-gene"]
score: 7.0
evidence: 利用空间分子测量监督组织学图像的细胞分类
tldr: "从H&E图像解析肿瘤微环境细胞组成意义重大，但现有分类器依赖人工标注且类别粗略。XenoType以同切片Xenium空间转录组作分子监督，并融合四个单细胞RNA参考确定七类细胞注释，推理时仅需H&E图像。在八个留出乳腺切片上，其七分类macro-F1为0.571，高于重训CellViT++的0.403，肌上皮与内皮细胞提升显著。该工作降低逐样本分子检测依赖，推动常规组织学的可扩展细胞分型。"
source: biorxiv
selection_source: fresh_fetch
motivation: "现有H&E细胞分类多受限于人工标注和粗形态类别，空间分子监督又常需另切片或主观聚类，限制可扩展性。"
method: "XenoType用同切片Xenium空间转录组监督H&E细胞分类，融合四个scRNA-seq参考调和七类注释，训练后仅用H&E推理。"
result: 八个留出乳腺切片上，七分类macro-F1为0.571，优于重训CellViT++的0.403；肌上皮F1升至0.572，内皮达0.682。
conclusion: 该方法实现无需逐样本分子检测的常规组织学细胞分型，并展示跨空间转录组平台的泛化潜力。
---

## 摘要
从组织学图像中表征肿瘤微环境的细胞组成，是理解癌症生物学并为治疗决策提供依据的基础。深度学习已实现基于苏木精-伊红（H&E）图像的自动化细胞核检测与分类，然而由于依赖人工标注，细胞分类器在很大程度上仍局限于宽泛的形态学类别。近期研究利用空间分子测量来监督组织学分类，但这些方法通常需要单独的组织切片，或会导致H&E染色发生改变，且所得细胞类型注释依赖于标志物选择和聚类参数等主观选择。在此，我们开发了XenoType，一个可直接从常规组织学图像将细胞分类为七种分子信息指导类别的框架，并使用配对的同一切片Xenium空间转录组数据进行训练。细胞类型注释由四个单细胞RNA测序参考数据集整合协调得到，从而减少对标志物选择的依赖。在八个留出的乳腺组织切片上，XenoType在四分类（macro-F1：0.703 vs. 0.569）和七分类（macro-F1：0.571 vs. 0.403）体系下均优于使用相同分子注释重新训练的常用CellViT++，其中肌上皮细胞（F1：0.175至0.572）和内皮细胞（F1：0.395至0.682）的提升最大。分子测量仅在训练阶段需要；在推理阶段，XenoType仅使用H&E图像。模型与参考之间的一致性随注释置信度提高而持续增加，且XenoType可泛化到来自不同空间转录组平台、独立进行分子谱分析的乳腺组织切片，支持无需对每个样本进行分子谱分析即可从常规组织学实现可扩展的细胞类型映射。

## Abstract
Characterizing the cellular composition of the tumor microenvironment from histological images is fundamental to understanding cancer biology and informing treatment decisions. Deep learning has enabled automated nuclear detection and classification from hematoxylin and eosin (H&E) images, yet cell classifiers remain largely confined to broad morphological categories owing to a reliance on manual annotations. Recent efforts have used spatial molecular measurements to supervise histological classification, but these approaches often require separate tissue sections or produce altered H&E staining, and the resulting cell-type annotations depend on subjective choices such as marker selection and clustering parameters. Here we develop XenoType, a framework that classifies cells into seven molecularly informed categories directly from routine histology, trained using paired same-section Xenium spatial transcriptomics. Cell-type annotations are reconciled from four single-cell RNA-sequencing references, reducing dependence on marker choices. Across eight held-out breast tissue sections, XenoType outperformed commonly used CellViT++ retrained on the same molecular annotations under both four-class (macro-F1: 0.703 vs. 0.569) and seven-class (macro-F1: 0.571 vs. 0.403) taxonomies, with the largest gains for myoepithelial (F1: 0.175 to 0.572) and endothelial cells (F1: 0.395 to 0.682). Molecular measurements are required only during training; at inference, XenoType uses the H&E image alone. Model-reference agreement increased consistently with annotation confidence, and XenoType generalized to an independently profiled breast tissue section from a different spatial transcriptomics platform, supporting scalable cell-type mapping from routine histology without per-specimen molecular profiling.