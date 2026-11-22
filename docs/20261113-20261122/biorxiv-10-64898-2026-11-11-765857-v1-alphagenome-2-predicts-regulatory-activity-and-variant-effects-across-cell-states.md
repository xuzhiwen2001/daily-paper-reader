---
title: AlphaGenome 2 predicts regulatory activity and variant effects across cell states
title_zh: AlphaGenome 2 预测跨细胞状态的调控活性与变异效应
authors: "Gayoso, A., Mottram, A., Karollus, A., Novati, G., Drotar, P., Reid, J., Meng-Papaxanthos, L., Kosiorek, A., Arvaniti, E., Dutordoir, V., De, S., Ward, T., Hong Wong, L., Perino, M., Taylor, K., Cheng, J., Latysheva, N., Pan, J., Hariharan, D., Bycroft, C., Nicolaisen, L., Hassabis, D., Kohli, P., Avsec, Z."
date: 2026-11-17
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.11.765857v1.full.pdf"
tags: ["query:virtual-cell"]
score: 6.0
evidence: 深度学习预测不同细胞状态下变异对基因表达的影响
tldr: "非编码变异通过特定细胞状态调控基因，但单细胞图谱供体不足难以直接关联变异与表达。AG2以1Mb序列加组织/细胞类型/状态条件为输入，跨人和小鼠单细胞图谱训练，可推断未测表观轨道并预测多模态变异效应。它在单细胞eQTL因果召回上于90%精度下翻倍，增强子-基因连接达SOTA，并构建了覆盖数百细胞类型、700万常见变异的图谱。"
source: biorxiv
selection_source: fresh_fetch
motivation: 非编码变异效应依赖细胞状态，现有深度学习模型难以区分相近细胞状态且需微调，单细胞图谱又缺乏足够供体做变异关联。
method: AG2以1Mb DNA序列和指定组织、细胞类型或状态为条件输入，基于跨物种单细胞图谱与bulk功能基因组数据训练，并从基因表达推断条件以泛化到新数据。
result: "AG2超越微调后的AlphaGenome 1及专用模型，90%精度下因果单细胞eQTL召回翻倍，增强子-基因连接达SOTA，可定位复杂性状位点因果变异。"
conclusion: AG2提供将观测性单细胞图谱转化为变异效应图的范式，并发布覆盖数百人类细胞类型、700万常见变异的增强子-基因连接与评分图谱。
---

## 摘要
大多数与人类性状和疾病相关的遗传变异位于非编码 DNA 中，它们可在特定细胞类型和状态下改变基因调控。单细胞图谱绘制了跨组织和发育过程的这些状态，但很少对足够多的供体进行检测，因而难以直接将变异与表达关联起来。深度学习模型有望通过从 DNA 序列预测变异效应来弥合这一差距，但它们难以区分相关细胞状态，并且需要针对新数据集进行微调。在此，我们提出 AlphaGenome 2（AG2），它在针对基因表达和染色质可及性的调控活性及变异效应的细胞类型特异性预测方面取得了显著进展。AG2 基于覆盖全生物体的人和小鼠单细胞图谱及 bulk 功能基因组学数据训练，输入为 1 Mb 的 DNA 序列以及指定目标组织、细胞类型或细胞状态的条件。条件输入使 AG2 能够插补未测量的表观基因组轨道，并预测跨细胞类型的多模态变异效应。直接从基因表达推断该条件，可使 AG2 无需微调即可扩展到未见过的数据集和细胞状态。AG2 优于经过微调的 AlphaGenome 1 以及在目标数据集上训练的专用模型，在 90% 精确率下使因果单细胞 eQTL 的召回率翻倍。AG2 还实现了最先进的增强子-基因连接，并能在复杂性状位点精确定位因果变异。在数百种人类细胞类型中，我们生成了一个包含增强子-基因连接以及 700 万个常见变异评分的图谱。随着单细胞分析在发育、组织和疾病队列中的不断扩展，AG2 为将观察性图谱转化为变异效应图谱提供了蓝图。

## Abstract
Most genetic variants associated with human traits and diseases lie in non-coding DNA, where they can alter gene regulation in specific cell types and states. Single-cell atlases chart these states across tissues and development, but rarely profile enough donors to associate variants with expression directly. Deep learning models could bridge this gap by predicting variant effects from DNA sequence, yet they poorly distinguish related cell states and require fine-tuning for new datasets. Here we present AlphaGenome 2 (AG2), which substantially advances cell-type-specific prediction of regulatory activity and variant effects for gene expression and chromatin accessibility. Trained on organism-wide human and mouse single-cell atlases and bulk functional genomics data, AG2 takes as input a 1-Mb DNA sequence and a condition specifying a target tissue, cell type, or cell state. Conditioning enables AG2 to impute unmeasured epigenomic tracks and predict multimodal variant effects across cell types. Inferring this condition directly from gene expression extends AG2 to unseen datasets and cell states without fine-tuning. AG2 outperforms fine-tuned AlphaGenome 1 and specialized models trained on target datasets, doubling recall of causal single-cell eQTLs at 90% precision. AG2 also achieves state-of-the-art enhancer-gene linking and can pinpoint causal variants at complex trait loci. Across hundreds of human cell types, we generated an atlas of enhancer-gene links and scores for 7 million common variants. As single-cell profiling expands across development, tissues, and disease cohorts, AG2 provides a blueprint for turning observational atlases into variant effect maps.