---
title: Modelling Phenotypic Assay Noise for Multivariable Biomarker Discovery using Deep Neural Networks
title_zh: 利用深度神经网络建模表型检测噪声以发现多变量生物标志物
authors: "Bannon, J. J., Scott, K. L., Delgado Sanchez, M., Khodakarami, F., Gruener, R. F., Huang, R. S., Haibe-Kains, B."
date: 2026-11-20
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.19.767940v2.full.pdf"
tags: ["query:virtual-cell"]
score: 6.0
evidence: 建模表型噪声的深度神经网络药物响应预测
tldr: 癌症药物反应预测是精准肿瘤学难点，现有药基因组筛选模型通常忽略表型读数的测量误差。作者在四个常用细胞系数据集中证实 viability 药物反应测定存在噪声，并提出显式建模噪声的 DeepCINET 排序框架。该方法提升了跨实验条件和未见样本的泛化能力，在优先识别最敏感细胞系上增益明显。研究将表型测定噪声确立为药物反应建模中被忽视的关键误差源，并提供噪声感知的多变量生物标志物发现框架。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有AI药敏预测多假设表型读数无误差，但细胞活力测定本身有噪声，可能让模型学习实验伪影而非生物学信号。
method: 作者先量化四个常用细胞系筛选数据集的表型噪声，再提出DeepCINET，用噪声感知排序策略显式建模测量不确定性。
result: 在多个数据集中，DeepCINET跨实验条件和未见样本的泛化优于基线，尤其在优先识别最药物敏感细胞系时提升显著。
conclusion: 表型测定噪声是药敏建模中被忽视的重要误差源；该工作为噪声感知的多变量生物标志物发现提供了原则性框架。
---

## 摘要
准确预测癌症药物反应仍是精准肿瘤学中的一项重大挑战。尽管部分治疗由临床批准的生物标志物指导，但这些标志物通常预测价值有限，且在许多药物中并不可用。基于大规模癌细胞系药物基因组学筛选训练的人工智能与机器学习方法，为更全面的反应预测提供了一条有前景的途径，但这些方法通常假设表型读出值是在无误差情况下测得的。该假设存在问题，因为基于活力的药物反应检测本身具有噪声，可能使模型学到实验伪差，而非具有生物学意义的敏感性决定因素。在本研究中，我们表明表型测量噪声存在于四个广泛使用的癌细胞系筛选数据集中，并引入深度一致性指数网络（DeepCINET），这是一个显式考虑该噪声的深度学习框架。在各数据集中，纳入这种噪声感知排序策略可改善跨实验条件以及对先前未见样本的泛化能力。DeepCINET在多种设置下优于基线模型，在优先识别最药物敏感细胞系方面提升尤为显著。总之，这些结果确立了表型检测噪声是药物反应建模中一个关键且此前被忽视的误差来源，并为噪声感知的多变量生物标志物发现提供了一个基于原理的框架。

## Abstract
Accurately predicting cancer drug response remains a major challenge in precision oncology. Although some therapies are guided by clinically-approved biomarkers, these markers often yield limited predictive value and are unavailable for many drugs. Artificial Intelligence and Machine Learning approaches trained on large-scale cancer cell line pharmacogenomic screens offer a promising route to more comprehensive response prediction, yet they generally assume that phenotypic readouts are measured without error. This assumption is problematic because viability-based drug response assays are inherently noisy, potentially causing models to learn experimental artefacts rather than biologically meaningful determinants of sensitivity. Here, we show that phenotypic measurement noise is present in four widely used cancer cell line screening datasets and introduce Deep Concordance Index Networks (DeepCINET), a deep learning framework that explicitly accounts for this noise. Across datasets, incorporating this noise-aware ranking strategy improves generalization across experimental conditions and to previously unseen samples. DeepCINET outperforms baseline models in multiple settings, with particularly notable gains in prioritizing the most drug-sensitive cell lines. Together, these results establish phenotypic assay noise as a critical and previously overlooked source of error in drug response modelling and provide a principled framework for noise-aware multivariable biomarker discovery.