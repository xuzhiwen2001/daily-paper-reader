---
title: "EMBER: Contextualized gene representations enable compositional prediction across cellular perturbations"
title_zh: EMBER：情境化基因表征支持跨细胞扰动的组合式预测
authors: "Ho, N., Xing, E. P., Ma, J."
date: 2026-11-01
pdf: "https://www.biorxiv.org/content/10.64898/2026.10.28.762655v2.full.pdf"
tags: ["query:virtual-cell"]
score: 9.0
evidence: 对单一与组合扰动效应的组合式预测
tldr: 预测单基因与组合扰动效应需要能整合功能关系与细胞状态、并可跨任务迁移的基因表示。EMBER以基因中心基础模型，结合交互引导对比学习与掩码表达重建，在多样且平衡采样的单细胞语料上预训练。它冻结编码器，用轻量探针组合上下文基因嵌入，统一支持单基因响应、双基因互作和多靶点药物响应预测。该方法提升跨情境预测与遗传互作排序，并优先识别mTOR抑制下的SCFD1候选依赖。
source: biorxiv
selection_source: fresh_fetch
motivation: 单基因与组合扰动效应预测缺乏能整合功能关系和细胞状态、且可跨任务迁移的基因表示。
method: EMBER在平衡采样的单细胞语料上，以交互引导对比学习和掩码表达重建预训练；冻结编码器，用轻量探针组合上下文嵌入完成多任务预测。
result: 在跨情境扰动响应预测和遗传互作排序上优于基线，并优先识别mTOR抑制下自噬体-溶酶体融合介导因子SCFD1为候选依赖。
conclusion: 上下文基因嵌入可作为可复用模块，支持遗传与药物扰动建模及情境特异性干预候选排序。
---

## 摘要
预测单一扰动和组合扰动的效应，对于识别情境特异性脆弱性和设计靶向干预至关重要。然而，学习能够整合功能关系与细胞状态、并可迁移至不同扰动任务的基因表征仍具挑战性。在此，我们提出 EMBER，一种以基因为中心的基础模型，可学习基因的情境依赖性功能表征。EMBER 在预训练中将相互作用引导的对比学习与掩码表达重建相结合；预训练所用单细胞语料经过精心构建，以兼顾多样性并在细胞类型和实验批次间实现平衡采样。EMBER 通过可组合嵌入框架将基因表征学习与任务特异性预测解耦：预训练编码器保持冻结，而轻量级探针组合情境化基因嵌入，以预测单一和组合扰动的效应。相同的预训练表征支持单基因扰动响应预测、双基因相互作用预测和多靶点药物响应预测。相对于所评估的基线方法，EMBER 提升了跨情境扰动响应预测和遗传相互作用排序性能。EMBER 还将自噬体-溶酶体融合的介导因子 SCFD1 优先列为 mTOR 抑制期间的候选依赖性基因。总之，这些结果确立了情境化基因嵌入作为建模遗传和药理学扰动的可复用构建模块，支持对遗传相互作用和情境特异性干预进行优先排序以供实验测试。

## Abstract
Predicting the effects of individual and combined perturbations is central to identifying context-specific vulnerabilities and designing targeted interventions. Yet learning gene representations that integrate functional relationships with cellular state and transfer across perturbation tasks remains challenging. Here, we present EMBER, a gene-centric foundation model that learns context-dependent functional representations of genes. EMBER combines interaction-guided contrastive learning with masked expression reconstruction during pretraining on a single-cell corpus curated for diversity and balanced sampling across cell types and experimental batches. EMBER decouples gene representation learning from task-specific prediction through a composable embedding framework: the pretrained encoder remains frozen, while lightweight probes combine contextualized gene embeddings to predict individual and combined perturbation effects. The same pretrained representations support single-gene perturbation-response prediction, digenic interaction prediction, and multi-target drug-response prediction. EMBER improves cross-context perturbation-response prediction and genetic-interaction ranking relative to evaluated baselines. EMBER also prioritized SCFD1, a mediator of autophagosome-lysosome fusion, as a candidate dependency during mTOR inhibition. Together, these results establish contextualized gene embeddings as reusable building blocks for modeling genetic and pharmacological perturbations, supporting the prioritization of genetic interactions and context-specific interventions for experimental testing.