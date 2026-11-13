---
title: "RELAY: Relational In-Context Learning for Cellular Perturbation Prediction"
title_zh: RELAY：用于细胞扰动预测的关系型上下文学习
authors: "Sun, Y., Feng, J., Wang, Y., Xie, W., Zhang, Y., Zhang, X."
date: 2026-11-03
pdf: "https://www.biorxiv.org/content/10.64898/2026.10.31.763027v1.full.pdf"
tags: ["query:virtual-cell"]
score: 9.0
evidence: 用关系式上下文学习预测细胞扰动响应
tldr: 细胞扰动响应受扰动身份、细胞类型、供体与剂量等多变量影响，构成多维条件空间，未测条件预测困难。RELAY将相关条件下已测的对照—扰动响应对作为上下文示例，仅利用共享变量关系而非变量具体取值来推断目标响应。在化学、遗传和细胞因子扰动数据上，它在未见过变量取值时优于现有上下文方法，在未见过组合时优于监督扰动预测方法。该工作表明关系型上下文学习可绕开显式变量表示，提升跨条件泛化。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法依赖变量取值的显式表示，泛化到未见过取值受表示可用性与质量限制。
method: RELAY以与目标共享部分实验变量的已测对照—扰动对为上下文示例，只输入共享关系、不输入变量值，预测目标响应。
result: 在化学、遗传、细胞因子扰动数据上，RELAY在未见过变量取值场景优于现有上下文方法，在未见过组合场景优于监督预测方法。
conclusion: 关系型上下文学习可避免显式变量表示依赖，提升细胞扰动跨条件预测泛化，资源将开源。
---

## 摘要
细胞对扰动的响应会随多个实验变量而变化，例如扰动身份、细胞类型、供体和剂量，从而定义了一个多维条件空间，其中每个被测量的细胞群体占据一个坐标。现有方法利用这些变量值的显式表示来预测未测量的条件，因此对未见值的泛化依赖于此类表示的可用性和质量。我们提出 RELAY，一种关系型上下文模型，它根据相关坐标处的已测响应来预测未测量的坐标。对于每个目标，RELAY 使用与目标共享一个或多个实验变量的条件中已测的对照—扰动配对，例如另一种细胞类型中的相同扰动。该模型仅接收共享了哪些变量，而不接收其具体取值，并利用这些示例来预测目标响应。我们在化学、遗传和细胞因子扰动数据集上，在两种设置下评估 RELAY：未见组合，即测试值在训练期间被单独观察到，但未以其目标组合形式出现；以及未见变量值，即测试值仅在推理时通过上下文引入。在未见变量值设置下，RELAY 优于现有的上下文学习方法；在未见组合设置下，RELAY 优于有监督的扰动预测方法。所有资源将开源，包括代码和数据。

## Abstract
Cellular responses to perturbations vary across multiple experimental variables, such as perturbation identity, cell type, donor, and dose, defining a multidimensional condition space in which each measured population occupies one coordinate. Existing methods predict unmeasured conditions using explicit representations of these variable values, generalizing unseen values therefore depends on the availability and quality of such representations. We present RELAY, a relational in-context model that predicts unmeasured coordinates from measured responses at related coordinates. For each target, RELAY uses measured control--perturbed pairs from conditions that share one or more experimental variables with the target, such as the same perturbation in another cell type. The model receives only which variables are shared, not their values, and uses these demonstrations to predict the target response. We evaluate RELAY on chemical, genetic, and cytokine perturbation datasets under two settings: unseen combinations, where test values are individually observed during training but not in their target combinations, and unseen variable values, where test values are introduced only through context at inference. RELAY outperforms existing in-context methods on unseen variable values and supervised perturbation-prediction methods on unseen combinations. All resources will be open sourced, including code and data.