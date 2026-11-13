---
title: Digital twins forecast individual immune trajectories
title_zh: 数字孪生预测个体免疫轨迹
authors: "Hu, C., Yu, C., Chen, C. Y.-C."
date: 2026-10-30
pdf: "https://www.biorxiv.org/content/10.64898/2026.10.23.761347v1.full.pdf"
tags: ["query:virtual-cell"]
score: 9.0
evidence: 将共享虚拟细胞模型个性化构建为个体数字孪生
tldr: "人体免疫状态高度个体化，现有预测多依赖单次挑战前测量和人群汇总模式，难以刻画个人变化。ImmuneTwins用个体单细胞观测个性化共享虚拟细胞模型，随新数据更新数字孪生。它在两个外部队列将免疫年龄误差降低32%和42%，重复流感疫苗接种中变化方向预测准确率提高35%，误差随观测累积下降27%。该工作确立了可预测个体免疫轨迹并识别特征免疫标志的虚拟细胞数字孪生。"
source: biorxiv
selection_source: fresh_fetch
motivation: 免疫系统个体差异显著，但现有免疫响应预测器通常只用单次挑战前测量，并依赖跨人群汇总模式，难以跟踪个人动态。
method: ImmuneTwins以共享虚拟细胞模型为基础，用每个个体的单细胞观测进行个性化，并在每次新观测后更新数字孪生。
result: "在两个外部队列，免疫年龄误差较最佳方法降低32%和42%；重复流感疫苗接种中，细胞变化方向预测准确率提高35%，误差随观测积累下降27%。"
conclusion: 研究证明虚拟细胞数字孪生可预测个体免疫变化，并定位长寿者B细胞重塑及骨髓瘤治疗中的患者特异性免疫轨迹。
---

## 摘要
人类免疫系统在个体间差异显著，并会随感染、疫苗接种和治疗而发生变化。目前正在构建AI虚拟细胞以模拟细胞对扰动的响应。然而，这些模型与大多数免疫应答预测器一样，仅用一次挑战前测量来描述每个人，并基于跨个体汇总的模式预测变化。数字孪生可随着对个体的每一次新观测进行更新，从而预测该个体免疫状态如何变化。在此我们提出ImmuneTwins，它通过用每个个体的观测对共享虚拟细胞模型进行个性化，从单细胞图谱构建这些数字孪生。在两个外部人群中，ImmuneTwins相较现有最佳方法将免疫年龄误差分别降低了32%和42%。在重复流感疫苗接种过程中，其数字孪生预测免疫细胞变化方向的准确率比已发表最佳方法高35%，且随着观测累积，误差下降了27%。这些数字孪生揭示，免疫细胞和血浆蛋白在90天内约恢复其偏离持续个人参考值的一半，而应答幅度在不同挑战间存在差异。它们进一步定位了极端长寿中的B细胞重塑，并预测了骨髓瘤治疗期间患者特异性的免疫轨迹。这些结果确立了用于预测个体免疫变化和识别每个人特征性免疫特征的虚拟细胞数字孪生。

## Abstract
The human immune system differs markedly between individuals and changes in response to infection, vaccination and treatment. AI virtual cells are being built to simulate cellular responses to perturbation. Yet these models, like most immune-response predictors, describe each person by a single pre-challenge measurement and forecast change from patterns pooled across people. Digital twins, updated with every new observation of an individual, could forecast how that person's immune state changes. Here we present ImmuneTwins, which builds these twins from single-cell profiles by personalizing a shared virtual-cell model with each individual's observations. In two external populations, ImmuneTwins reduced immune-age error by 32% and 42% relative to the best existing method. During repeated influenza vaccination, its twins predicted the direction of immune-cell change 35% more accurately than the best published method, and their error fell by 27% as observations accumulated. The twins revealed that immune cells and plasma proteins recover about half their deviation from a persistent personal reference within 90 days, whereas response size varies between challenges. They further localized B-cell remodelling in exceptional longevity and anticipated patient-specific immune trajectories during myeloma treatment. These results establish virtual-cell digital twins for forecasting individual immune change and identifying each person's characteristic immune features.