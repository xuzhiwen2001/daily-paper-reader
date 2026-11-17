---
title: "MELD: Mutation Effect Learning through Differential embeddings"
title_zh: MELD：通过差分嵌入学习突变效应
authors: "Alajji, A., Jashil, R., Mall, R., Elshrif, M."
date: 2026-11-09
pdf: "https://www.biorxiv.org/content/10.64898/2026.10.29.762727v1.full.pdf"
tags: ["query:virtual-cell"]
score: 6.0
evidence: 通过野生型与突变型差分预测单核苷酸变异的功能后果
tldr: 单核苷酸变异效应预测对临床基因组学重要，但现有序列到功能模型依赖绝对基因组轨迹，变异评分多在训练后通过计算机诱变完成。MELD将野生型与突变体logit差Δz直接放入监督目标，结合共享CNN-Transformer编码器、突变掩码增强、多尺度突变中心池化和自适应放大因子。在ClinVar上仅1.9M参数即达AUROC 0.986，显著优于同数据同骨干的ISM基线0.800，并在共享基准上超过更大规模基础模型。结果表明直接差分监督是一种紧凑、数据高效的事后ISM替代方案。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有Enformer、Borzoi、AlphaGenome等模型用绝对轨迹训练，变异效应靠事后ISM打分，野生型-突变体差异未进入损失函数，且大模型成本高。
method: MELD用共享CNN-Transformer编码器分别编码WT与突变体，加入突变掩码增强、多尺度突变中心池化及可学习自适应放大因子，直接监督Δz=zmut-zwt。
result: ClinVar上AUROC 0.986，同骨干ISM仅0.800；共享基准0.967，高于AlphaGenome 0.924；仅5万训练变异即超ISM全量训练。
conclusion: 直接差分监督能以1.9M参数实现紧凑、数据高效且更强的变异效应预测，是事后ISM评分的有力替代。
---

## 摘要
我们提出 MELD（Mutation Effect Learning through Differential Embeddings，通过差分嵌入学习突变效应），这是一种紧凑模型，通过直接基于野生型（WT）与突变型之间的差分进行训练，来预测单核苷酸变异（SNV）的功能后果。解释 SNV 是临床基因组学的核心，但实验表征无法扩展到数百万个已观察到的变异。领先的序列到功能模型（Enformer、Borzoi、AlphaGenome）在绝对基因组轨迹上训练，并通过计算机模拟诱变（ISM）事后对变异打分，因此 WT 与突变型之间的差异从未进入训练损失。MELD 则将 logit 差值 Δz = z_mut - z_wt 置于监督目标中。它结合了共享的 CNN-Transformer 编码器、突变型特异性突变掩码增强、多尺度以突变位点为中心的池化，以及一个可学习的自适应放大因子。在 ClinVar（157 万个变异）上，MELD（190 万参数）达到 AUROC 0.986，而使用相同数据、相同骨干网络的 ISM 基线为 0.800，消融实验证实了各组成部分的贡献。在共享基准上，它优于参数量多 3–1,300 倍的冻结基础模型（AUROC 0.967，而 AlphaGenome 为 0.924，Nucleotide Transformer 为 0.936）。仅使用 50,000 个训练变异，它就超过了在全部 148 万个变异上训练的 ISM 基线（AUROC 0.903 对 0.796）。在 BRCA1 饱和基因组编辑上，冻结的 MELD 达到 Spearman ρ 0.42，高于 Borzoi（0.40），而 ClinVar 迁移将其提升至 0.45。这些结果表明，直接差分监督是一种紧凑、数据高效的方法，可替代使用规模大得多的预训练模型进行事后 ISM 打分。

## Abstract
We introduce MELD (Mutation Effect Learning through Differential Embeddings), a compact model for predicting the functional consequences of single nucleotide variants (SNVs) by training directly on the wild-type (WT) versus mutant differential. Interpreting SNVs is central to clinical genomics, yet experimental characterization cannot scale to millions of observed variants. Leading sequence-to-function models (Enformer, Borzoi, AlphaGenome) are trained on absolute genomic tracks and score variants post hoc through in-silico mutagenesis (ISM), so the WT-mutant difference never enters the training loss. MELD instead places the logit difference {Delta}z = zmut - zwt inside the supervised objective. It combines a shared CNN-Transformer encoder, a mutant-specific mutation-mask boost, multiscale mutation-centered pooling, and a learned adaptive amplification factor . On ClinVar (1.57M variants), MELD (1.9M parameters) reached an AUROC of 0.986 versus 0.800 for a same-data, same-backbone ISM baseline, with ablations confirming the contribution of each component. On a shared benchmark, it outperformed frozen foundation models with 3-1,300x more parameters (AUROC 0.967 vs. 0.924 for AlphaGenome and 0.936 for Nucleotide Transformer). With only 50, 000 training variants, it exceeded the ISM baseline trained on all 1.48M (AUROC 0.903 vs. 0.796) variants. On BRCA1 saturation genome editing, frozen MELD achieved a Spearman {rho} of 0.42, above Borzoi (0.40), and ClinVar transfer raised it to 0.45. These results demonstrate that direct differential supervision is a compact, data-efficient alternative to post-hoc ISM scoring with substantially larger pretrained models.