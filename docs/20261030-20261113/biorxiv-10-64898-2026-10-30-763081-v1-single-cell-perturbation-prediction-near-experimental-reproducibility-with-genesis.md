---
title: Single-cell perturbation prediction near experimental reproducibility with GENESIS
title_zh: 利用 GENESIS 实现接近实验可重复性的单细胞扰动预测
authors: "Conci, R., D'Ascenzo, D., Cultrera di Montesano, S., Raghavan, S., Winter, P. S., Van Allen, E. M., Crawford, L., Lotter, W."
date: 2026-11-01
pdf: "https://www.biorxiv.org/content/10.64898/2026.10.30.763081v1.full.pdf"
tags: ["query:virtual-cell"]
score: 10.0
evidence: 预测单细胞扰动响应分布的生成式框架，并采用实验校准评测
tldr: 单细胞扰动图谱难以穷举所有生物背景、扰动与剂量组合，亟需预测未测条件下的细胞响应分布。GENESIS以实验条件协变量为输入，用轻量神经网络和能量评分训练生成模型。在Tahoe-100M与PBMC细胞因子图谱中，它显著优于现有生成模型和统计基线，并在独立重复条件上接近实验可重复性。该工作还提出以实验可重复性校准误差的评估框架，并显示更广但较浅的测量有助于扩大覆盖和补全稀疏样本。
source: biorxiv
selection_source: fresh_fetch
motivation: 单细胞扰动实验组合空间巨大，穷举测量不可行；需要准确预测未测条件，并以实验可重复性衡量预测是否实用。
method: 提出GENESIS生成框架，以定义实验条件的协变量直接预测单细胞响应分布，并用轻量神经网络和严格proper scoring rule能量评分训练。
result: 在Tahoe-100M与PBMC图谱中显著优于现有生成模型和统计基线，独立重复条件接近实验可重复性；少条件/少细胞训练仍准确，并可恢复上下文依赖转录程序。
conclusion: 更广而较浅的扰动测量可扩大实验覆盖，GENESIS可补全稀疏采样群体并预测未测条件，为扰动研究提供互补策略。
---

## 摘要
单细胞扰动图谱如今可在数百万个细胞上测量细胞响应，但生物学背景、扰动、剂量及其他实验变量可能组合的数量使穷尽式测量不可行。在此，我们提出 GENESIS（Generative ENErgy-based Single-cell Intervention Simulator，基于能量的生成式单细胞干预模拟器），一种可直接从定义实验条件的协变量预测单细胞响应分布的生成式框架。GENESIS 使用轻量级神经网络，并以能量得分（energy score）——一种针对分布的严格适当评分规则——进行训练。我们引入一种实验校准的评估框架，其中预测误差是相对于同一条件下重复测量的可重复性来解读的。在 Tahoe-100M 小分子图谱和一个大型 PBMC 细胞因子图谱上，GENESIS 显著优于现有生成模型和统计基线，并在独立重复条件下接近实验可重复性。重要的是，仅使用可用实验条件或细胞的一小部分进行训练时，GENESIS 仍保持准确，且生成的图谱可恢复实验观察到的情境依赖性转录程序。在相当训练细胞预算下，当测量覆盖更多实验条件而非对更少条件进行更深入分析时，GENESIS 获得更准确的预测。总之，这些发现提示了一种扰动研究的互补策略：更广泛、较低深度的测量可扩展实验覆盖范围，而 GENESIS 可增强稀疏采样的群体并预测未测量条件下的响应。

## Abstract
Single-cell perturbation atlases now measure cellular responses across millions of cells, but the number of possible combinations of biological contexts, perturbations, doses and other experimental variables make exhaustive measurements infeasible. Here, we present GENESIS (Generative ENErgy-based Single-cell Intervention Simulator), a generative framework that predicts single-cell response distributions directly from the covariates defining an experimental condition. GENESIS uses a lightweight neural network trained with the energy score, a strictly proper scoring rule for distributions. We introduce an experiment-calibrated evaluation framework in which prediction error is interpreted relative to the reproducibility of repeated measurements of the same condition. Across the Tahoe-100M small-molecule atlas and a large PBMC cytokine atlas, GENESIS significantly outperforms existing generative models and statistical baselines and approaches experimental reproducibility on independently repeated conditions. Importantly, GENESIS remains accurate when trained on only a fraction of the available experimental conditions or cells, and generated profiles recover experimentally observed context-dependent transcriptional programs. At comparable training-cell budgets, GENESIS achieves more accurate predictions when measurements span more experimental conditions rather than profiling fewer conditions more deeply. Together, these findings suggest a complementary strategy for perturbation studies: broader, lower-depth measurements can expand experimental coverage, while GENESIS augments sparsely sampled populations and predicts responses in unmeasured conditions.