---
title: "MorphoANOVA: Dissecting Histology-Gene Expression Relationships in Spatial Transcriptomics"
title_zh: MorphoANOVA：解析空间转录组学中的组织学-基因表达关系
authors: "Chen, P.-W., Yan, G., Yu, S., Li, J. J."
date: 2026-11-09
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.05.764699v1.full.pdf"
tags: ["query:spatial-gene"]
score: 8.0
evidence: 基因层面统计框架，解析组织学形态与空间基因表达的关系
tldr: 空间转录组同时提供基因表达与组织形态，但系统判断哪些基因与形态相关、关联是否随空间变化仍困难。MorphoANOVA用嵌套空间变系数模型和序贯ANOVA，分解全切片形态关联、位置特异变化及形态外空间变异。模拟验证其可区分各成分并恢复空间模式。人脑皮层与乳腺癌分析识别出不同形态-表达模式及相关通路，为基因优先级和空间解释提供框架。
source: biorxiv
selection_source: fresh_fetch
motivation: 空间转录组中基因表达与组织形态的关系广泛存在，但缺乏基因层面、可空间分解的系统统计框架。
method: 提出MorphoANOVA，用嵌套空间变系数模型与序贯ANOVA，检验全切片形态关联、位置特异变化及形态外空间变异。
result: 模拟显示可区分模型成分并恢复空间模式；人脑皮层和乳腺癌中识别出不同形态-表达程序，HER2阳性患者侵袭标志基因位置特异关联更一致。
conclusion: 该框架支持基因优先级排序、通路富集和空间成分可视化，帮助系统解释组织形态相关的空间表达模式。
---

## 摘要
空间转录组学（ST）可在组织架构内测量数百至数千个基因的表达，通常伴随组织学图像。然而，系统刻画哪些基因与组织形态相关、这些关联是否具有空间变化，以及哪些基因在形态所捕获的模式之外表现出额外的空间表达模式，仍具挑战性。在此，我们提出 MorphoANOVA，一种逐基因统计框架，用于刻画 ST 所测基因中的形态-表达关系。MorphoANOVA 使用嵌套空间变系数模型和序贯方差分析，评估与 H&E 衍生形态特征的全切片关联、这些关联的位置特异性变化，以及在考虑所选特征后的额外空间变异。所得统计量支持基因优先级排序和通路富集分析，而空间成分图有助于解释单个基因。模拟表明，MorphoANOVA 能够区分建模成分并恢复其空间模式。将其应用于人皮层和乳腺癌，可识别与不同形态-表达模式相关的生物学程序，并揭示与细胞组成的独特关系。在三名 HER2 阳性乳腺癌患者中，浸润性癌标志基因一致表现出更强的位置特异性形态关联证据。因此，MorphoANOVA 提供了一个系统解释与组织形态相关的空间基因表达模式的框架。

## Abstract
Spatial transcriptomics (ST) measures the expression of hundreds to thousands of genes within tissue architecture, often accompanied by histology images. However, it remains challenging to systematically characterize which genes exhibit associations with tissue morphology, whether these associations vary spatially, and which genes show additional spatial expression patterns beyond those captured by morphology. Here we introduce MorphoANOVA, a gene-wise statistical framework for characterizing morphology--expression relationships across genes measured by ST. Using nested spatially varying coefficient models and sequential ANOVA, MorphoANOVA assesses slide-wide associations with an H\&E-derived morphology feature, location-specific changes in these associations, and additional spatial variation after accounting for the selected feature. The resulting statistics enable gene prioritization and pathway enrichment analysis, while spatial component maps support the interpretation of individual genes. Simulations demonstrate MorphoANOVA's ability to distinguish the modeled components and recover their spatial patterns. Applications to human cortex and breast cancer identify biological programs associated with different morphology--expression patterns and reveal distinct relationships with cell composition. Across three HER2-positive breast cancer patients, invasive-cancer marker genes consistently exhibit stronger evidence of location-specific morphology associations. MorphoANOVA thus provides a framework for systematically interpreting spatial gene-expression patterns in relation to tissue morphology.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究背景**：空间转录组（ST）同时提供空间位置上的基因表达与 H&E 组织学图像。组织形态与基因表达相关，但这种关系可能因基因、组织区域和细胞状态而异：某些基因在全切片层面与形态相关，某些基因的形态关联具有位置特异性，还有些基因在形态特征之外仍有额外空间表达模式。
- **核心问题**：现有方法多聚焦于“从组织学预测表达”或“多模态整合/空间域识别”，缺乏一个**逐基因、可分解、可统计检验**的统一框架，分别回答：
  1. 基因表达是否与所选 H&E 形态特征在全切片层面相关；
  2. 这种关联是否随空间位置变化；
  3. 在考虑该形态特征后，是否仍有额外空间表达变异。
- **整体含义**：MorphoANOVA 旨在把“形态–表达关系”拆成可解释的统计成分，支持基因优先级排序、通路富集、空间成分可视化以及与细胞组成的关联分析，从而系统解释 ST 中的空间基因表达模式。论文为 bioRxiv 预印本，尚未经同行评审。

## 2. 方法论

### 核心思想

- 对每个基因拟合四个**嵌套空间变系数模型（SVCM）**，通过**序贯 ANOVA** 比较相邻模型，检验不同来源的空间结构。
- 使用 H&E 衍生标量形态特征 \(h_i\)，并在切片内中心化。形态特征可以是图像强度摘要、学习到的组织学嵌入等。

### 模型与检验流程

四个嵌套模型为：

- \(M_1: y_i=\beta_0+\varepsilon_i\)：仅截距。
- \(M_2: y_i=\beta_0+\beta_1 h_i+\varepsilon_i\)：加入全切片 H&E 效应。
- \(M_3: y_i=\beta_0+\beta_1 h_i+\beta_1(z_i)h_i+\varepsilon_i\)：加入位置特异 H&E 效应，其中 \(\beta_1(z_i)\) 为空间平滑函数并约束均值为 0。
- \(M_4: y_i=\beta_0(z_i)+\beta_1 h_i+\beta_1(z_i)h_i+\varepsilon_i\)：用空间变化截距 \(\beta_0(z_i)\) 捕捉考虑 H&E 后的额外空间变异。

拟合方式：高斯广义可加模型（GAM，identity link），空间项用惩罚薄板回归样条，平滑参数用 REML 估计。

序贯检验：

- \(F_{21}\)：\(M_2\) vs. \(M_1\)，检验全切片 H&E 效应 \(H_0:\beta_1=0\)。
- \(F_{32}\)：\(M_3\) vs. \(M_2\)，检验位置特异 H&E 效应 \(H_0:\beta_1(z)\equiv 0\)。
- \(F_{43}\)：\(M_4\) vs. \(M_3\)，检验 H&E 之外的额外空间变异 \(H_0:\beta_0(z)\equiv\beta_0\)。

F 型统计量基于残差平方和与有效自由度：
\[
F=\frac{(RSS_r-RSS_f)/(edf_f-edf_r)}{RSS_f/(n-edf_f)}.
\]
由于空间项为惩罚平滑，使用有效自由度而非名义自由度，得到近似 F 检验，并通过模拟评估校准。

拟合优度用序贯调整 \(R^2\) 增量表示：
- \(\Delta R^2_{21}=R^2(M_2)\)：全切片 H&E 效应；
- \(\Delta R^2_{32}=R^2(M_3)-R^2(M_2)\)：位置特异 H&E 效应；
- \(\Delta R^2_{43}=R^2(M_4)-R^2(M_3)\)：H&E 外额外空间变异。

### 下游分析

- **基因优先级**：保留 \(\Delta R^2_{32}\ge 0.03\) 的基因按 \(F_{32}\) 排序；保留 \(\Delta R^2_{43}\ge 0.03\) 的基因按 \(F_{43}\) 排序；取 top N 做 GO Biological Process 与 KEGG 富集，BH 校正。
- **单基因空间解释**：总 H&E 效应定义为 \([\hat\beta_1+\hat\beta_1(z_i)]h_i\)；额外空间变异为居中的 \(\hat\beta_0(z_i)\)。用逐点估计/标准误计算 z 统计量，并在空间位置上做 BH 校正，识别 adjusted \(p\le0.05\) 的区域。
- **细胞组成关联**：计算拟合成分与细胞类型比例之间的 Spearman 相关；单细胞分辨率数据先
