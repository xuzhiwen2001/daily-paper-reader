---
title: ExPert infers causal perturbations from cell states across biological and clinical contexts
title_zh: ExPert 从细胞状态推断跨生物学与临床情境的因果扰动
authors: "Schwartz, L., Schlamowitz, J. L., Kuznets-Speck, B., Johnson, C. W., Das, D., Grody, E. I., Bai, T., Sun, H., Senthilkumar, I., Primavera, G., Jung, J., Kuusik, B., Grant, R. A., Rojas, E., Abdrabou, A. M., Peiffer, B., Sun, Z., Diehl, A. M., Marr, C., Chandel, N. S., Mithal, D. S., Weinberg, S. E., Adli, M., Kalsotra, A., Prashnani, E., Goyal, Y."
date: 2026-11-03
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.02.762549v1.full.pdf"
tags: ["query:virtual-cell"]
score: 8.0
evidence: 从观测细胞状态反推因果扰动
tldr: 单细胞CRISPR筛选多用于预测扰动后的细胞状态，本文则反向提问：给定观察到的细胞状态，推断其可能的扰动来源。作者提出ExPert，在12种细胞情境共享的潜空间中为每个扰动学习原型，覆盖8964个扰动、1950万细胞。该方法在留出情境上的召回率超过现有最佳方法一倍以上，算力降低1000倍，并可零样本迁移到药物、蛋白降解与组合扰动。在酒精性肝病和原发性线粒体病中，它分别提示mRNA出核异常与受累复合物，并经实验或再分析验证。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有扰动响应模型多从扰动预测细胞状态，缺少从状态反推扰动来源的工具，而这类反向推断对解释疾病与药物机制很有价值。
method: 构建ExPert，在跨12种细胞情境共享的潜空间中为每个扰动学习一个原型，用8964个扰动、1950万细胞训练，查询时对19895个候选基因排序。
result: 留出情境召回率超过最佳基线一倍以上且算力少1000倍；无需重训即可迁移至药物、蛋白降解和组合扰动，过半候选基因未见于训练。
conclusion: 扰动图谱可被反向查询，从细胞状态推断可能驱动因素；在酒精性肝病与线粒体病中给出可验证的新机制线索。
---

## 摘要
汇集式单细胞 CRISPR 筛选推动了大量旨在预测对扰动响应的模型研究。我们提出了反向问题：哪种扰动产生了观察到的细胞状态？在此，我们开发了 ExPert（Extracting Perturbations），其在由 12 种细胞情境共享的潜在空间中为每种扰动学习一个原型，基于 8,964 种扰动和 1,950 万个细胞训练，并针对每个查询对 19,895 个候选基因进行排序，其中超过一半未参与训练。ExPert 在计算量减少 1,000 倍的情况下，将留出情境的召回率相比现有最佳方法提高了一倍以上，并在无需重新训练的情况下迁移至药物、蛋白质降解和组合扰动。在酒精相关性肝病中，它提示 mRNA 出核参与，尽管其表达未发生变化，我们通过实验证实了核内 poly(A) 滞留和异构体转换。在原发性线粒体病中，它从血液中识别出受影响的复合体，将信号定位至单核细胞，并标记出一个被误诊的对照样本。因此，扰动图谱可被反向查询，从状态推断可能的驱动因素。

## Abstract
Pooled single-cell CRISPR screens have driven substantial effort toward models predicting the response to a perturbation. We posed the inverse question: which perturbation produced an observed cell state? Here we developed ExPert (Extracting Perturbations), which learns one prototype per perturbation in a latent space shared by 12 cellular contexts, trained on 8,964 perturbations and 19.5 million cells, and ranks 19,895 candidate genes per query, over half absent from training. ExPert more than doubled held-out-context recall over the best existing method with 1,000-fold less compute, and transferred without retraining to drugs, protein degradation and combinations. In alcohol-associated liver disease it implicated mRNA export, unchanged in expression, and we experimentally confirmed nuclear poly(A) retention and isoform switching. In primary mitochondrial disease it recovered the affected complex from blood, localized the signal to monocytes, and flagged a misdiagnosed control. Perturbation atlases can thus be queried in reverse, from state to likely driver.