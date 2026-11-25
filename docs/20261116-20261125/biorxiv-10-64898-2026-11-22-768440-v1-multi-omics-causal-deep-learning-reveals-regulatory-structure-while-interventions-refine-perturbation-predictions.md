---
title: Multi-omics causal deep learning reveals regulatory structure while interventions refine perturbation predictions
title_zh: 多组学因果深度学习揭示调控结构，而干预可改进扰动预测
authors: "Goudarzi, S., Nandi, V., Liu, N., Goodarzi, H."
date: 2026-11-24
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.22.768440v1.full.pdf"
tags: ["query:virtual-cell"]
score: 8.0
evidence: 结合CRISPR干预的因果深度学习改进扰动预测
tldr: 单细胞观测数据难以区分相关与因果，且多模态扰动数据获取受限，制约基因调控网络推断。CMC-VAE在潜空间学习基因-基因、蛋白-蛋白及基因-蛋白连接，并映射回测量特征，以约81万CITE-seq图谱训练。模型恢复共表达、转录因子调控子和免疫信号，跨模态图富集同源转录-蛋白对，在三个CRISPR筛选中排序优于相关性与潜变量基线。观测数据不能确定调控方向，但微调潜网络可利用干预改善扰动响应预测，显示因果结构与干预数据互补。
source: biorxiv
selection_source: fresh_fetch
motivation: 观测单细胞数据无法区分相关与因果，多模态扰动数据又有限，亟需可解释且能泛化的调控推断方法。
method: 提出CMC-VAE，在潜空间构建基因-蛋白连接网络并映射回测量特征，用观测CITE-seq训练，再以CRISPR扰动微调。
result: 模型恢复共表达、转录因子调控子和免疫信号，跨模态图富集同源转录-蛋白对；在三个CRISPR筛选中排序优于基线，但观测训练不能确定调控方向。
conclusion: 干预微调主要学习跨敲除共享响应，在较大Perturb-seq中可学基因特异效应并迁移，模拟中还恢复边方向，表明因果结构与干预互补。
---

## 摘要
从单细胞数据推断基因调控很困难，因为观察性测量无法区分相关性与因果性，而且扰动数据（尤其是多模态扰动数据）仍然难以获取。为此，我们提出跨模态因果变分自编码器（CMC-VAE），其在潜空间中学习一个连接基因与蛋白的网络（基因-基因、蛋白-蛋白和基因-蛋白），并将每个连接映射回测量特征。CMC-VAE 在 809,130 个观察性 CITE-seq 图谱上训练，能够恢复共表达、转录因子调控子和免疫信号程序，并学习到一个富集转录本-蛋白同源配对的稀疏跨模态图谱。在开发过程中使用的三个 CRISPR 筛选上，它对敲除响应基因的排序优于相关性和潜变量 VAE 基线。将模型拟合到某一筛选的未扰动对照细胞且不使用扰动标签时，该模型将测得的敲除 RNA 响应转化为蛋白响应，效果优于相关性图谱和同源转录本。然而，基因间调控的方向无法从观察性数据中恢复。在 CITE-seq 筛选上，仅微调潜网络即可提高留出响应相关性，主要通过学到一种跨敲除共享的响应。在更大规模的 Perturb-seq 筛选上（约 1,000 个训练扰动），微调潜网络可学到能够迁移到留出基因的基因特异性效应，其效果优于在相同细胞上微调的基因级因果模型；在模拟中，此类干预还恢复了观察性训练未能解决的边方向。

## Abstract
Inferring gene regulation from single-cell data is difficult because observational measurements cannot distinguish correlation from causation and access to perturbational data, especially with multiple modalities, remains limited. Here we present the Cross-Modal Causal Variational Autoencoder (CMC-VAE), which learns a network linking genes and proteins (gene-gene, protein-protein and gene-protein) in the latent space and maps each connection back onto measured features. Trained on 809,130 observational CITE-seq profiles, CMC-VAE recovers co-expression, transcription factor regulons and immune signalling programs, and learns a sparse cross-modal map enriched for transcript-protein cognate pairs. On three CRISPR screens used during development, it ranks knockout-responsive genes better than correlation and latent-VAE baselines. Fitted to a screen's unperturbed control cells, without perturbation labels, the model translates measured knockout RNA responses into protein responses better than a correlation map and cognate transcripts. The direction of gene-to-gene regulation, however, is not recovered from observational data. On the CITE-seq screens, fine-tuning only the latent network improves held-out response correlation, mainly by learning a response shared across knockouts. On larger Perturb-seq screens, with about 1,000 training perturbations, fine-tuning the latent network learns gene-specific effects that transfer to held-out genes, more so than a gene-level causal model fine-tuned on the same cells, and in simulation, such interventions also restore edge orientations that observational training leaves unresolved.

---

## 论文详细总结（自动生成）

# 论文结构化总结：CMC-VAE 多组学因果深度学习

## 1. 核心问题与整体含义（研究动机与背景）

- **核心问题**：单细胞多组学（如 CITE-seq 同时测量 RNA 与表面蛋白）数据本质上是**观察性**的，无法区分相关与因果；而扰动数据（尤其同时测量 RNA 与蛋白的多模态扰动数据）稀缺、覆盖基因有限。因此需要回答一个实际问题：**从丰富的观察性数据中能学到多少有用结构？又需要多少干预数据才能改进扰动预测？**
- **背景**：RNA 与蛋白水平共同变化可能源于一方调控另一方、共同响应上游信号、或仅标记同一细胞类型；配对测量只能揭示关联，不能确定谁在上游。经典因果可识别性理论（Markov 等价类、LiNGAM 等）表明，方向性在特定假设下才可从观察数据恢复，而这些假设在单细胞数据中是否成立尚不清楚。
- **现有方法定位**：totalVI、MOFA+、MultiVI 等侧重模态对齐、去噪与插补；sVAE、NODAGS-Flow 利用扰动数据学习因果表征；PIE 等借助先验知识提升跨情境预测。本文则试图**在潜空间中显式构建可编辑的基因-蛋白图网络**，并检验观察数据与干预数据各自能贡献什么。
- **整体含义**：论文主张一种"分工"设计原则——**观察数据提供稳定的表征、候选交互结构与跨模态映射；定向扰动则用于学习扰动特异性效应与边方向**，从而为多模态虚拟细胞模型提供"可干预的因果图"这一潜在修正层。

## 2. 方法论：CMC-VAE 的核心思想与技术细节

- **整体架构**：跨模态因果变分自编码器（Cross-Modal Causal VAE）。对每个细胞：
  - 独立残差编码器分别将 2,692 个 RNA 特征和 144 个蛋白特征映射为对角高斯后验：**128 维 RNA 潜变量 + 64 维蛋白潜变量 = 192 维外生潜变量 ε**，并向标准正态先验正则化。
  - 潜空间采用**线性结构方程模型（SCM）**：`z = Aᵀz + ε`，整理得 `z = (I − Aᵀ)⁻¹ε`。
  - 线性解码器分别重建 RNA 与蛋白：`x̂ = Dz + b`。
- **潜邻接矩阵 A（192×192）分四块**：
  - `Arr`（RNA→RNA，假设为 GRN）、`App`（蛋白→蛋白，假设为 PPI）、`Wrp`（RNA→蛋白，翻译）、`Wpr`（蛋白→RNA，反馈）。
  - 采用 source-by-target 约定；每个元素 = **Gumbel-sigmoid 可微二值门 × 实值权重**；对角线掩码去除自环；**允许环与反馈回路**。
- **投影到测量特征空间**：`G = DADᵀ`，四块分别给出基因-基因、基因-蛋白、蛋白-基因、蛋白-蛋白的打分，用于与生物学参考网络比较（但作者明确声明这不是独立识别的直接效应）。
- **训练目标（公式 3）**：重建 MSE + free-bits KL + 谱稳定性惩罚（ρ(A) 超过 0.9 时惩罚）+ 门 L1 稀疏 + 解码器列正交惩罚 + **解码器 group-lasso（16 组）**。最终模型不含无环性惩罚；实测谱半径 ≈ 0.89。
- **解码器引导的扰动预测（公式 4）**：
  - 用目标基因 g 的 RNA 解码器载荷绝对值归一化得到 `s_j`，对相关潜连接做缩放 `A_mut = A ⊙ (1 − s)`；
  - 求解修改后的线性系统 `z_mut = (I − A_mutᵀ)⁻¹(ε + Δε)`，其中 ε 取最多 4,000 个对照细胞的后验均值，Δε 为把被敲除基因外生输入拉向零的偏移（实测仅贡献约 0.01% 响应范数）；
  - 输出 `Δx = D(z_mut − z)`。由于使用绝对载荷，该操作**只排序响应幅度、不固定符号**（故仅用于零样本排序；Perturb-seq 微调改用带符号的敲低偏移）。
- **干预微调**：冻结编码器与解码器，**仅更新潜邻接**（4 个门 logit 块 + 4 个权重块），损失为负 Pearson + 平方误差 + 蛋白响应项 + 谱半径守卫（公式 5），留出整基因评估。可加 InfoNCE 对比项提升检索。
- **对照细胞适配**：在新情境仅用该情境**未扰动对照细胞**（无扰动标签）微调编码器、解码器与潜图，加入跨模态重建项。

## 3. 实验设计：数据集、基准与对比方法

- **观察训练语料**：Hao 健康 PBMC 参考（161,764 细胞，8 供者）+ Stephenson COVID-19 图谱（647,366 细胞，130 供者），共 **809,130 个配对 CITE-seq 图谱**；基因词表 2,692，蛋白面板 144。
- **扰动数据集（4 个 CITE-seq 筛选 + 2 个 Perturb-seq）**：
  - 开发用：Frangieh Perturb-CITE-seq（174 单元，7 蛋白）、Chen Perturb-icCITE-seq（122 单元，78 蛋白）、Arce CRISPRi Perturb-CITE-seq（23 单元，84 蛋白）。
  - **完全留出**：Papalexi ECCITE-seq（THP-1，13 个可评估敲除），用于最终测试，预设主终点为均值中心化 pearDE 与检索。
  - 大规模：K562 与 Jurkat 必需基因 CRISPRi Perturb-seq（约 1,000 训练扰动；428/399 留出基因；3 个独立模型/细胞系）。
- **基准与参考**：共表达、STRING、DoRothEA、CollecTRI、9 个 curated 免疫程序、74 个同源转录-蛋白对、36 个表面复合物连接（15 cis + 21 trans）。
- **对比方法**：totalVI、GRNBoost2、DeepSEM（含谱稳定版及**参数量匹配的微调版**）、相关性基线、岭回归、kNN、GEARS、Ahlmann-Eltze 线性模型、scGPT 嵌入 + 岭回归、DirectLiNGAM（合成实验）。
- **评估指标**：AUROC（排序 DE 基因）、signed pearDE、**均值中心化 pearDE**、留出基因检索（chance 0.5）、同源富集倍数、Gini 系数、边方向准确率（模拟）。
- **关键消融/控制**：打乱 `Arr`、置零 `Arr`、转置 `Arr`；27 种模型配置；非高斯先验、独立性惩罚、辅助变量条件；标签打乱、screen-mean 目标、符号翻转、均值中心化目标；仅对照细胞预训练。

## 4. 资源与算力

- **论文正文、方法、数据与代码可用性、致谢等部分均未报告 GPU 型号、数量、训练时长或总算力开销**。
- 仅可间接推断的规模信息：809,130 细胞、192 维潜空间、约 1,000 个训练扰动的 Perturb-seq、每细胞系 3 个独立种子模型、27 种配置比较、模拟 15 次重复；微调设为 150 步、每步 3,000 细胞、学习率 5×10⁻⁴。
- 结论：**算力披露不足**，无法据此评估可复现的计算成本或能效。

## 5. 实验数量与充分性

- **实验组数概览**：
  - 4 个 CITE-seq 扰动筛选（3 开发 + 1 完全留出）+ 2 个大规模 Perturb-seq 细胞系 + 1 个合成模拟研究；
  - 参考网络比较（4 类参考 + 9 个免疫程序 + 74 同源对 + 36 复合物对）；
  - 图消融 3 种（打乱/置零/转置）× 3 个筛选；
  - 27 种训练配置（补充表 4）+ 多种先验/正则变体；
  - 微调的 4 类控制目标 + 2 种目标函数（标准/InfoNCE）× 2 细胞系；
  - 对照细胞适配 + 与岭回归、相关图谱、同源转录本对比；
  - 留出基因划分（401 基因中 280 训练 / 121 评估）、留一队列实验（补充注 14）。
- **充分性评价**：
  - **优点**：覆盖面广，包含留出筛选、多种阴性对照（标签打乱、均值目标）和参数量匹配的 DeepSEM 比较，统计检验使用 bootstrap + BH 校正，报告效应量与置信区间。
  - **需注意的公平性问题**：
    - 三个开发筛选**参与了模型选择**，因此其性能并非严格独立验证；作者以 Papalexi 留出筛选弥补，但该筛选仅 13 个可评估敲除、主终点为 null。
    - 基线多以**默认设置**运行，可能未充分调优。
    - 蛋白层面验证在各队列间**不均衡**（Frangieh 仅 7 个重叠蛋白，Arce 留出仅个位数扰动）。
    - 微调超参在开发阶段以留出基因性能选定，作者声明因控制组使用相同权重故不影响对照比较，但仍存在选择偏差的潜在空间。

## 6. 主要结论与发现

- **观察数据能学到什么**：
  - 恢复共表达（AUROC 0.98）、STRING（0.76）、DoRothEA（0.68）、CollecTRI（0.63）；但相关性基线在定向调控子参考上几乎持平，说明**与"定向"数据库的一致性主要来自共表达**。
  - 9 个免疫程序高于随机，MHC I 类抗原呈递最高（AUROC 0.92）；健康 vs COVID 训练会改变程序构成。
  - **跨模态翻译图最特异**：74 个同源对的 RNA→蛋白权重中位数是非同源对的 **8.2 倍**（totalVI 3.0 倍），Gini 0.74 vs 0.54；同源边强度与"蛋白可被自身转录本预测程度"高度相关（Spearman ρ = 0.90）。
  - 蛋白-蛋白图对表面复合物 AUROC 0.62，与共表达（0.61）相当，**证据有限且跨模型不一致**。
- **观察数据不能学到什么**：
  - **基因间调控方向无法恢复**：投影 GRN 近乎对称（中位正/反向权重差 <0.5%，互反性 ≈0.99），转置 `Arr` 对 AUROC 影响 ≤0.02；signed pearDE 小且符号不一致（0.10、−0.13、0.01）。27 种配置、非高斯先验、无环约束等均未改善方向预测。
  - 敲除响应排序**部分依赖学习到的图**（打乱/置零 `Arr` 会降低 AUROC），但排序很大程度上反映"哪些基因普遍易响应"，且用对照细胞表达变异度排序甚至更高。
- **扰动预测表现**：开发筛选 RNA AUROC = 0.61/0.66/0.76，优于相关性与 totalVI；留出 Papalexi 达 0.70（totalVI 0.58），与相关性（0.69）、DeepSEM（0.67）持平；**但预设主终点（中心化 pearDE、检索）对所有方法均为 null**。
- **跨模态翻译**：PBMC 模型直接迁移到筛选对照细胞时蛋白插补很差（中位 r = 0.05/0.02/0.03），用**无标签对照细胞适配**后升至 0.23/0.08/0.31；敲除 RNA→蛋白响应翻译的中心化 pearDE 从 0.05 升至 **0.49**，检索从 0.57 升至 **0.83**，优于语料相关图谱与同源转录本，但**仍不及同细胞拟合的岭回归（0.70 / 0.91）**。
- **干预微调**：
  - CITE-seq 筛选上，留出 RNA pearDE
