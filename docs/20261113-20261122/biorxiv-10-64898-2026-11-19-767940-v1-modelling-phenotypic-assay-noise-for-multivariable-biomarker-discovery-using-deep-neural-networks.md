---
title: Modelling Phenotypic Assay Noise for Multivariable Biomarker Discovery using Deep Neural Networks
title_zh: 利用深度神经网络建模表型检测噪声以进行多变量生物标志物发现
authors: "Bannon, J. J., Scott, K. L. S. L., Delgado Sanchez, M., Khodakarami, F., Gruener, R. F., Huang, R. S., Haibe-Kains, B."
date: 2026-11-20
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.19.767940v1.full.pdf"
tags: ["query:virtual-cell"]
score: 6.0
evidence: 建模表型检测噪声的深度神经网络用于癌症药物反应预测
tldr: 癌症药物反应预测常受生物标志物不足与表型检测噪声影响，而现有模型多假设读数无误差。作者在四个细胞系药筛数据中确认噪声，并提出显式建模噪声的DeepCINET框架，以噪声感知排序提升泛化。结果显示其跨实验条件和未见样本表现优于基线，尤其善于优先识别最敏感细胞系。该工作将表型检测噪声确立为药物反应建模中被忽视的关键误差源，并提供噪声感知的多变量标志物发现框架。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有药敏预测模型常忽略细胞活性检测噪声，可能学习实验伪影而非真实生物学敏感性，限制标志物发现与泛化。
method: 作者在四个常用癌细胞系药筛数据中识别表型噪声，并提出DeepCINET，用噪声感知排序显式建模检测误差。
result: DeepCINET在多种设置下优于基线，跨实验条件和未见样本泛化更好，尤其提升最敏感细胞系的优先识别。
conclusion: 研究将表型检测噪声确立为药物反应建模中被忽视的关键误差源，并提供噪声感知的多变量生物标志物发现框架。
---

## 摘要
准确预测癌症药物反应仍是精准肿瘤学中的一项重大挑战。尽管一些疗法由临床批准的生物标志物指导，但这些标志物通常预测价值有限，并且对许多药物而言并不可用。在大型癌细胞系药物基因组学筛选数据上训练的人工智能与机器学习方法为更全面的反应预测提供了有前景的途径，但它们通常假设表型读数是在无误差情况下测量的。这一假设存在问题，因为基于活力的药物反应检测本质上具有噪声，可能使模型学到实验伪影，而非具有生物学意义的敏感性决定因素。在此，我们表明表型测量噪声存在于四个广泛使用的癌细胞系筛选数据集中，并引入深度一致性指数网络（Deep Concordance Index Networks, DeepCINET），这是一个显式考虑该噪声的深度学习框架。跨数据集而言，纳入这种噪声感知排序策略可改善在不同实验条件下以及对先前未见样本的泛化能力。DeepCINET在多种设置下优于基线模型，在优先识别最药物敏感细胞系方面尤其取得显著提升。总之，这些结果确立了表型检测噪声是药物反应建模中一个关键且此前被忽视的误差来源，并为噪声感知的多变量生物标志物发现提供了原则性框架。

## Abstract
Accurately predicting cancer drug response remains a major challenge in precision oncology. Although some therapies are guided by clinically-approved biomarkers, these markers often yield limited predictive value and are unavailable for many drugs. Artificial Intelligence and Machine Learning approaches trained on large-scale cancer cell line pharmacogenomic screens offer a promising route to more comprehensive response prediction, yet they generally assume that phenotypic readouts are measured without error. This assumption is problematic because viability-based drug response assays are inherently noisy, potentially causing models to learn experimental artefacts rather than biologically meaningful determinants of sensitivity. Here, we show that phenotypic measurement noise is present in four widely used cancer cell line screening datasets and introduce Deep Concordance Index Networks (DeepCINET), a deep learning framework that explicitly accounts for this noise. Across datasets, incorporating this noise-aware ranking strategy improves generalization across experimental conditions and to previously unseen samples. DeepCINET outperforms baseline models in multiple settings, with particularly notable gains in prioritizing the most drug-sensitive cell lines. Together, these results establish phenotypic assay noise as a critical and previously overlooked source of error in drug response modelling and provide a principled framework for noise-aware multivariable biomarker discovery.