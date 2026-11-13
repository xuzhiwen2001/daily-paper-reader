---
title: "RAPTORGraph: graph-based pathway modeling for causal discovery in single-cell perturbations"
title_zh: RAPTORGraph：基于图的通路建模用于单细胞扰动中的因果发现
authors: "Adhisantoso, Y. G., Schröder, S. K., Gress, M., Hernaez, M., Voges, J."
date: 2026-11-04
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.03.763980v1.full.pdf"
tags: ["query:virtual-cell"]
score: 9.0
evidence: 单细胞扰动中的因果发现与新扰动预测
tldr: 单细胞扰动实验对机制理解与药物发现至关重要，但现有因果表示学习方法在已知干预目标的Perturb-seq场景中难以处理干预溢出，且直接引入通路会带来确认偏误并忽略新信号。RAPTORGraph采用β变分自编码器与GraphPathway编码器显式建模学习通路中的基因互作，并通过预条件隔离扰动基因影响，形成单节点潜在干预。模型还结合最优传输对齐预处理稳定表示。实验显示其在下游未见扰动与非加性互作分析上优于或媲美现有方法。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法依赖稠密编码器，难以在已知干预目标的封闭世界中消除干预溢出；直接嵌入生物学通路又易产生确认偏误并遗漏新信号。
method: 提出RAPTORGraph：β变分自编码器搭配GraphPathway编码器建模学习通路内基因互作，预条件隔离扰动基因，并结合最优传输对齐预处理。
result: 在下游未见扰动分析中提升非加性互作等任务的最先进性能，同时在MSE和MMD等客观指标上保持竞争力。
conclusion: 表明图结构通路建模与单节点潜在干预可支持可识别因果发现，并减少溢出与确认偏误，为单细胞扰动因果学习提供新框架。
---

## 摘要
涉及单细胞扰动的实验对于理解细胞机制至关重要，并可加速药物发现。因果表示学习使我们能够揭示调控生物系统的潜在因素，并预测新扰动的影响。然而，现有方法由于依赖稠密编码器，无法在干预目标先验已知的封闭世界设定（如 Perturb-seq 实验）中处理干预溢出问题。此外，将整理好的生物通路纳入模型会引入确证偏差，迫使模型通过既有通路解释数据，减少模型可探索的假设集合，同时丢弃标注通路之外的新信号。在本工作中，我们提出 RAPTORGraph，一种带有 GraphPathway 编码器的 β-变分自编码器，可在学习到的通路内显式建模复杂的基因间相互作用。此外，我们模型的预条件处理隔离了扰动基因的影响，产生可识别因果发现所需的干净单节点潜在干预，并消除溢出。最后，我们在经最优传输对齐预处理的数据上训练模型，这保证了对照样本与扰动样本之间具有良定义的映射，并进一步稳定学习到的潜在表示。我们证明，RAPTORGraph 在未见扰动的下游分析（如非加性相互作用）上提升了最先进性能，同时在均方误差和最大均值差异等客观指标上具有竞争力。源代码见 https://github.com/sXperfect/RAPTORGraph。

## Abstract
Experiments involving the perturbation of individual cells are central to understanding cellular mechanisms and can accelerate drug discovery. Causal representation learning allows us to uncover the latent factors that regulate biological systems and predict the impact of novel perturbations. Unfortunately, existing methods fail to address intervention spillover in a closed-world setting where intervention targets are known a priori, such as in Perturb-seq experiments, due to their reliance on dense encoders. Furthermore, incorporating curated biological pathways into the model imposes a confirmatory bias, forcing it to explain the data through preexisting pathways and reducing the set of hypotheses the model can explore, while discarding novel signals that lie outside the annotated pathways. In this work, we introduce RAPTORGraph, a {beta}-variational autoencoder with a GraphPathway encoder that explicitly models complex gene-to-gene interactions within learned pathways. Moreover, our model's preconditioning isolates the influence of perturbed genes, yielding clean, single-node latent interventions required for identifiable causal discovery and eliminating spillover. Finally, we train the model on data preprocessed with optimal-transport alignment, which guarantees a well-defined mapping between control and perturbed samples and further stabilizes the learned latent representations. We demonstrate that RAPTORGraph improves state-of-the-art performance on downstream analyses of unseen perturbations, such as non-additive interactions, while performing competitively on objective metrics, such as mean squared error and maximum mean discrepancy. The source code is available at https://github.com/sXperfect/RAPTORGraph.