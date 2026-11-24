---
title: Model evaluation metrics of Virtual Cell Challenge 2026
title_zh: Virtual Cell Challenge 2026 的模型评估指标
authors: "Dobin, A., Adduri, A., Sullivan, J., Lyda, J., Mehta, R., Leto, D. E., Datlinger, P., VanHorn, S., Chizari, S., Ranadive, N., Nagesh, S., Tung, P.-Y., Li, N., Caputo, J., Plosky, B. S., Ricci-Tam, C., Senturia, R., Feng, K., Chu, T., Tsui, M., Eraslan, B., Bevilacqua, B., Carpenter, C., Verma, R., Yan, Z., Min, J., Torun, F. M., Averbukh, I., Sandmann, T., Chen, T. J., Dicks, S., Mosafi, O., Rvachov, T., Shin, H., Sundaram, L., Voss, D., Zhang, Y., Zynda, G., van Overbeek, M., Muzaffar, U., Woodrow, A., Burke, D. P., Hsu, P. D., Konermann, S., Arc Virtual Cell Team,, Goodarzi, H."
date: 2026-11-23
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.17.767214v1.full.pdf"
tags: ["query:virtual-cell"]
score: 9.0
evidence: 面向虚拟细胞模型扰动响应预测的评估指标
tldr: 虚拟细胞模型旨在用计算方法预测基因、环境与化学扰动的影响，减少昂贵实验依赖。2026年虚拟细胞挑战赛要求模型零样本预测六种人类细胞系中CRISPRi敲低后的转录响应。作者围绕三项原则设计六项评估指标：反映实验提取的生物学信息、在实验重复上校准、抵御不预测响应却提高分数的捷径。结果表明，六项指标均将实验重复评分置于均值基线之上，且2025年指标遗留的捷径方案不再能提升分数。
source: biorxiv
selection_source: fresh_fetch
motivation: 虚拟细胞模型评估需要可信指标，既能体现扰动实验的生物学信息，又要在实验重复上校准，并防止无预测能力的捷径刷分。
method: 围绕上述三原则设计六项指标，两项比较预测与实测细胞的伪批量表达谱，四项评估各扰动的响应基因，并实现于开源Python包cell-eval2。
result: 在挑战赛数据上，六项指标对实验重复的评分均高于均值基线；2025年指标中可利用的捷径方案在新指标下无法再提高分数。
conclusion: 新指标比上一届更稳健，能更忠实衡量零样本扰动响应预测，为虚拟细胞挑战赛2026提供可靠评估基础。
---

## 摘要
虚拟细胞模型旨在通过计算机模拟预测遗传、环境、化学及其他扰动的影响，从而减少对复杂且昂贵实验的依赖。Virtual Cell Challenge 2026 推动该领域朝这一目标迈进，要求模型零样本预测六种人类细胞系中 CRISPRi 敲低引起的转录响应。模型与实验的忠实程度通过将其预测与真实数据进行比较的指标来评估，而设计此类指标并非易事。我们围绕三项原则制定了 2026 年挑战赛的指标：指标应 (i) 反映从实验中提取的生物学信息，(ii) 在实验重复上得到校准，(iii) 抵抗那些在不预测响应的情况下提高分数的捷径方案。本文介绍最终得到的六项指标、每项指标背后的理由及其在挑战赛数据上的评估。其中两项指标比较预测细胞与实测细胞的伪批量表达谱，另外四项评估对每种扰动产生响应的基因，这是 Perturb-seq 实验的核心读数。这些指标在开源 Python 包 cell-eval2 中实现。在挑战赛数据上，六项指标对实验重复的评分均高于平均基线，并且 2025 年挑战赛指标未能排除的捷径方案不再能够提高分数。因此，新指标比之前的指标更稳健。

## Abstract
Virtual cell models aim to predict the effects of genetic, environmental, chemical and other perturbations in silico, reducing the dependency on complex and costly experiments. The Virtual Cell Challenge 2026 motivates the field toward this goal, tasking models with zero-shot prediction of the transcriptional responses to CRISPRi knockdowns in six human cell lines. The faithfulness of a model to the experiment is assessed by metrics that compare its predictions with the real data, and designing such metrics is not trivial. We developed the metrics of the 2026 Challenge around three principles: a metric should (i) reflect the biological information extracted from experiments, (ii) be calibrated on a repeat of the experiment, and (iii) resist shortcut solutions that raise the score without predicting the response. Here we present the six resulting metrics, the reasoning behind each of them, and their evaluations on the Challenge data. Two of the metrics compare the pseudobulk expression profiles of predicted and measured cells, while four assess the genes that respond to each perturbation, the central readout of a Perturb-seq experiment. The metrics are implemented in cell-eval2, an open-source Python package. On the Challenge data, all six metrics score a repeat of the experiment above the mean baseline, and the shortcut solutions that the metrics of the 2025 Challenge left open can no longer raise the score. The new metrics are therefore more robust than the previous ones.

---

## 论文详细总结（自动生成）

# 《Virtual Cell Challenge 2026 的模型评估指标》论文结构化总结

## 1. 核心问题与研究动机

- **背景**：虚拟细胞模型试图在计算机中预测遗传、环境、化学等扰动对细胞的影响，以减少对昂贵、复杂实验的依赖。Perturb-seq 将 pooled CRISPR 扰动与单细胞 RNA 测序结合，可在一次实验中测量上千种扰动的转录响应，为模型提供训练数据与真值。
- **挑战赛设定**：Virtual Cell Challenge 2026 要求参赛模型对六种人类细胞系中的 CRISPRi 敲低效应做**零样本预测**（训练数据可来自任何公开或自有数据，但没有挑战赛专属训练集），并提供 400 个预测单细胞 × 18,533 个基因的原始计数矩阵。
- **核心问题：指标设计**。单细胞测量噪声很大，连实验重复都无法完全复现测量谱。因此：
  - 忽略噪声的指标可能把“无变化预测”（直接用对照细胞）排在“实验重复”之上；
  - 指标可能对与生物学无关的属性（如预测值的尺度）敏感；
  - 竞赛参与者会主动优化分数，任何“不预测响应也能提分”的空间都会诱发**捷径方案**（shortcut solutions）。
- **2025 年指标的缺陷**：L1 距离对效应尺度敏感；未校正的 MAE 使实验重复劣于无变化预测；目标基因、提交的对照细胞、任意尺度/对数归一化输入等均被捷径利用。
- **论文定位**：提出围绕三项原则（反映生物学信息、在实验重复上校准、抵抗捷径）重新设计的**六项评估指标**，并给出其在挑战赛数据上的表现。

## 2. 方法论

### 2.1 总体设计原则与评分锚定

- **六项指标**：两项比较伪批量表达谱（扰动判别、表达误差），四项评估差异表达基因（倍数变化误差、显著集一致性、方向保真产出、方向覆盖度）。
- **统一锚定公式**：将原始指标值 $u$ 线性变换为
  $$s = \frac{u - b}{r - b}$$
  其中 $b$ 为**均值基线**（该细胞系所有构建体平均响应的等权平均，视为无扰动特异性信息的预测），$r$ 为**实验重复**（将每种扰动与对照的细胞随机对半切分、互相预测，重复 5 次取平均）。
  - 0 分 = 均值基线，1 分 = 实验重复；不设上限，允许超过 1（因半切分重复噪声更大）。
  - 仅两个误差类指标例外：倍数变化误差下限 −6；表达误差截断在 [0,1]。
- **靶基因剔除**：每个扰动的靶基因从全部六项指标中剔除（因为敲低自身靶基因无需模型），扰动判别中还剔除全部 300 个面板靶基因，防止利用靶基因列表作弊。

### 2.2 伪批量表达谱的定义

- 对一组细胞，按基因求和计数、归一化到固定总量 $T_S = 5\times10^4$ 后取 $\log(1+\cdot)$；扰动效应 = 扰动谱 − 实测对照谱。相比 2025 年对 log-normalized 表达取均值（受 Jensen 不等式影响、依赖细胞间方差），新定义更稳定。

### 2.3 两项表达指标

- **扰动判别（PDS）**：
  - 用**余弦距离**（仅依赖方向，与效应尺度无关）比较预测效应与 300 个实测效应；
  - 按自身实测效应在候选中的归一化排名计分，$PDS_p = 1 - k_p/(n-1)$，并列取平均秩；
  - 无信息预测期望得 0.5。相比 2025 年改用余弦距离（消除尺度依赖）并剔除全部靶基因（防止“抬高其他 299 个靶基因”的捷径）。
- **表达误差**：
  - 核心是**校正采样噪声的平方误差**：$\|\hat x_p - x_p\|^2$ 的期望包含两项采样方差，用 delete-one jackknife 估计并减去；
  - 分子 $N_p$ 含两项防作弊设计：$\min(\hat C_p, C_p)$ 限制预测可获得的噪声信用不超过实测谱；因子 $\rho \le 1$ 按预测谱跨扰动的变异程度封顶总校正量；
  - 分母 $D_p$ 为实测谱与对照谱之间校正后的平方距离，表达误差 $E = \sum_p N_p / \sum_p D_p$（取比值和而非逐扰动比值的平均，避免弱效应扰动分母不稳）。
  - 关键发现：未校正时，实验重复的误差在 78–94% 的扰动上大于无变化预测，全系综层面也更大（1.08–1.46 vs 1），故校正是必要的。

### 2.4 四项差异表达指标

- **DE 判定流程**：对每个扰动 vs 实测对照做双侧 Wilcoxon 秩和检验（正态近似 + 结与连续性校正），BH 校正（**按扰动内部**而非全局校正），FDR < 0.05；倍数变化用算术均值（归一化到 10⁶ CPM）的 $\log_2$ 比；低表达基因过滤**仅基于对照细胞**（避免泄漏响应信息），保留约 9,537–10,124 个基因。
- **倍数变化误差**：在实测显著基因集 $S_p$ 上计算预测与实测 log2FC 的归一化 MAE，仅评估 $|S_p| \ge 10$ 的扰动；无变化预测恰为 1。
- **显著集一致性**：预测与实测显著基因集的 **Jaccard 指数**（假阳性与漏检同等惩罚）。
- **方向保真产出**：$F_p = k / \max(n_{pred}, n_{real})$，即正确方向比例乘以覆盖项，防止“只报最有把握的少数基因”刷高准确率。
- **方向覆盖度**：按提交自身的显著性排序实测 DE 基因，找纯度 ≥ 90% 的最深前缀 $k^*$，$Reach_p = k^*/n_{real}$；不要求 FDR 校准，只要求排序正确。

## 3. 实验设计

- **数据/场景**：
  - 六种人类细胞系（不同组织来源），同一 CRISPRi guide 文库、10x Genomics Flex 平台；
  - 统一基因轴 18,533 个；每个细胞系 300 个扰动（验证系 A/B/C 共用一套面板，测试系 D/E/F 共用另一套，重叠 129 个基因）；
  - 排除 Replogle et al. (2022) 与 Nadig et al. (2025) 四个必需基因筛选中出现过的靶基因，防止从公开数据“搬运”响应；
  - 每个构建体精确下采样 400 个细胞，对照池 46 个非靶向构建体 × 400 细胞 = 18,400 个对照细胞；按二项稀疏化统一测序深度至中位约 20,000 UMIs。
- **Benchmark 与对照基线**：
  - **均值基线** $b$：该系所有构建体的平均响应；
  - **实验重复** $r$：细胞对半切分、5 次随机切分的重复；
  - **无变化预测**（仅用于分析，如表达误差对比）；
  - **2025 年挑战赛的三项指标**（L1 距离扰动判别、MAE、DE 重叠）作为对照，并在相同数据上复算以暴露其缺陷。
- **捷径测试**：对预测效应施加不同缩放因子检验 L1 距离的尺度依赖（补充图 S2）；检查目标基因剔除前后的排名作弊；分析最终验证排行榜前十名提交的计数方差（Fano 因子）以识别残余捷径。

## 4. 资源与算力

- 论文**不涉及模型训练**，是评估方法学论文；算力信息主要在补充说明中：
  - `cell-eval2` 为 GPU 加速实现，DE 检验通过 `gpudge` 在 GPU 上运行；
  - 在 300 个扰动的单个 Perturb-seq 屏上，**1 块 NVIDIA H100 GPU 耗时 117 秒**计算两包共有的 26 项指标（采用 cell-eval 0.6.6 约定），而 `cell-eval 0.8.1` 在 **16 个 CPU 线程上耗时 58 分钟**；采用自身约定（测试基因更少）时仅需 34 秒。
- 未报告训练算力、GPU 数量或总机时（因无模型训练），这一点论文亦未明确说明。

## 5. 实验数量与充分性

- **规模**：6 个细胞系 × 6 项指标，每项指标均报告均值基线与实验重复（5 次随机切分）的逐系综、逐扰动分布（图 4.1、4.2、5.1），并覆盖验证与测试两个阶段。
- **消融/对比性分析**：
  - 有无采样噪声校正的对比（图 4.2）；
  - 余弦距离 vs L1 距离的尺度敏感性分析（补充图 S2）；
  - 2025 年指标在相同数据上的复算对比；
  - 前十名提交的 Fano 因子与噪声信用分析；
  - 细胞系间上下文特异性的初步量化（前十名仅复现 2–12% 的系特异性响应）。
- **充分性与客观性**：
  - 优点：所有指标均用“实验重复应优于平凡基线”这一可证伪标准检验，且六个系、六项指标全部通过；锚定值（$b$、$r$）未向参赛者公开，减少针对性过拟合。
  - 局限：缺乏对指标本身统计不确定性（如 bootstrap 置信区间）的系统报告；未做指标间相关性/冗余度分析；上下文特异性只做了描述性分析，未设计专门指标。

## 6. 主要结论与发现

- 六项指标在全部六个细胞系上均使**实验重复得分高于均值基线**（PDS 重复 0.923–0.984；表达误差校正后重复 0.025–0.069 而基线 1.01–1.03；倍数变化误差重复 0.36–0.45；Jaccard 重复 0.35–0.43；方向保真产出重复 0.74–0.83；覆盖度重复 0.95–0.98）。
- **未校正的误差指标会把实验重复排在无变化预测之下**，这直接说明 2025 年 MAE 的设计缺陷；噪声占实测扰动–对照平方距离的 38–60%。
- **L1 距离使分数依赖效应尺度**：效应缩小 64 倍时 PDS 降至约 0.5（无信息水平），放大 1.4–2 倍时略高于重复本身；余弦距离对此完全不变。
- 2025 年指标遗留的捷径（尺度操纵、目标基因泄漏、使用提交自身对照、任意对数归一化）在新指标下**不再能提分**。
- **残余问题**：最终验证榜前十名中八名提交的细胞计数在基因维度上方差低于采样允许（Fano 因子 < 0.5 的基因占 26–50%，缺失至少 23–41% 的泊松噪声），却仍获得 91–100% 的噪声校正信用——说明 $\min$ 与 $\rho$ 只能封顶、无法验证噪声真实性。
- **显著集本身低可重复**（Jaccard 仅约 0.4）是检验功效有限所致，而非实验失败；方向信息则高度可重复（93–95%）。
- 前十名提交仅复现了约一半系间差异响应中的 2–12%，**上下文特异性预测仍是短板**。

## 7. 优点

- **原则驱动、可证伪的指标设计**：以“实验重复必须优于平凡基线”作为硬性验收标准，方法论上严谨且可迁移到其他基准。
- **对捷径的系统性防御**：靶基因剔除、仅基于对照的基因过滤、原始计数与尺度上限、实测对照、噪声校正封顶、方向保真产出对“少报基因”的惩罚等，形成多层防护。
- **统计上更正确的表达误差**：基于高维两样本检验（Bai–Saranadasa、Chen–Qin）的无偏平方距离估计与 jackknife 方差估计，解决了噪声主导误差的问题。
- **指标贴合实验读数**：四项 DE 指标对应实验者真正报告的“哪些基因变、变多少、往哪变”，而非便利的汇总统计量。
- **工程贡献**：开源 `cell-eval2`（MIT 许可，GPU 加速，较 CPU 版提速约 30 倍），并提供 `vcc2026` preset 与指标规范文档，便于复现与社区使用。
- **诚实的自我批判**：论文明确承认仍存在的捷径、指标不对称性及上下文特异性缺口，并给出改进方向。

## 8. 不足与局限

- **残余捷径未被完全封堵**：表达误差的噪声校正无法验证预测谱是否真的携带所申报的噪声，实证显示前十名中八名存在“噪声不足却拿满校正”的现象；$\rho$ 因子同样可被策略性利用。
- **方向保真产出的不对称性**：对少报基因的惩罚远重于多报，作者承认这是为封堵捷径而接受的妥协，但可能系统性偏袒“多报 + 方向随机”的策略（随机全报期望 0.5）。
- **显著集一致性指标区分度低**：即便实验重复的 Jaccard 也仅 0.35–0.43，指标本身接近噪声下限，对模型优劣的判别力有限。
- **无跨细胞系上下文指标**：六项指标均在系内比较，未衡量扰动响应如何随细胞背景变化；作者自己指出这是重要缺口，且初步分析显示领先模型几乎未复现系特异性响应。
- **评估覆盖有限**：每个系仅 300 个扰动、每扰动 400 个细胞，统计功效受限；基因过滤阈值（对照 CPM > 5）会漏掉约 1% 的“对照低表达、扰动高表达”基因对。
- **缺乏指标不确定性量化**：未报告置信区间、指标间相关性或敏感性分析（如切分次数、细胞数变化对锚定的影响）。
- **基线定义的依赖**：均值基线依赖“至少 300 个细胞且通过敲低过滤”的构建体集合，不同数据规模下可比性需进一步验证。
- **应用限制**：指标针对 Perturb-seq 转录组读数设计，不覆盖蛋白组、表观组等其他层次；对非 CRISPRi 扰动（如过表达、药物）的适用性未讨论。

（完）
