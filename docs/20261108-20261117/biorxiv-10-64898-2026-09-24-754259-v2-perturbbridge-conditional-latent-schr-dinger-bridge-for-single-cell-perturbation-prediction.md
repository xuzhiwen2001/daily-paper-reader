---
title: "PerturbBridge: Conditional Latent Schr dinger Bridge for Single-Cell Perturbation Prediction"
title_zh: PerturbBridge：用于单细胞扰动预测的条件潜空间薛定谔桥
authors: "Liu, Z., Jiang, C., Yang, C., Wang, X., Liu, X."
date: 2026-11-16
pdf: "https://www.biorxiv.org/content/10.64898/2026.09.24.754259v2.full.pdf"
tags: ["query:virtual-cell"]
score: 10.0
evidence: 用条件潜空间薛定谔桥进行单细胞扰动响应预测
tldr: 单细胞扰动预测需从非配对对照与扰动群体推断未见干预的转录响应，而高维稀疏表达使直接学习桥动态困难。PerturbBridge 用响应锚定自编码器构建保留主扰动响应方向的潜空间，并以可处理的薛定谔桥近似建模条件随机传输。其扰动诱导桥 Transformer 通过扰动与时间槽引导潜坐标交互来估计漂移。在 Norman、Sci-Plex3 与 Replogle RPE1 上，差异表达方向恢复和扰动效应相关性领先，基因表达预测具竞争力。
source: biorxiv
selection_source: fresh_fetch
motivation: 从非配对单细胞群体预测未见扰动的转录响应，直接在高维稀疏基因表达上学习薛定谔桥动态仍很困难。
method: 响应锚定自编码器构建保留主响应方向的潜空间，PerturbBridge 以可处理近似建模条件薛定谔桥，并用扰动诱导桥 Transformer 估计漂移。
result: 在 Norman、Sci-Plex3 和 Replogle RPE1 上，差异表达方向恢复与扰动效应相关性领先，基因表达预测准确度具竞争力。
conclusion: PerturbBridge 将响应锚定潜表示与条件薛定谔桥结合，为单细胞扰动响应预测提供了有效的潜空间随机传输框架。
---

## 摘要
\textbf{动机：}单细胞扰动预测旨在从非配对的对照与扰动群体中恢复对未见干预的转录响应。薛定谔桥为将这些转变建模为随机传输提供了原则性框架，但直接从高维、稀疏的基因表达谱中学习桥动力学仍然具有挑战性。\textbf{结果：}我们提出 PerturbBridge，一种用于单细胞扰动响应预测的条件潜空间薛定谔桥框架。一个以响应为锚的自编码器构建紧凑的细胞表示，该表示保留从训练扰动中识别出的主要转录响应方向，同时编码补充性的细胞变异。在该潜空间中，PerturbBridge 通过薛定谔桥的可处理近似来建模条件随机传输。我们引入扰动诱导桥 Transformer（Perturbation-Induced Bridge Transformer），其在漂移估计过程中利用扰动和时间相关槽位来引导潜坐标之间的交互。在 Norman、Sci-Plex3 和 Replogle RPE1 上的评估表明，该方法在差异表达方向恢复和扰动效应相关性方面表现领先，同时具有有竞争力的基因表达预测精度。\textbf{可用性：}源代码见 \url{https://github.com/echQoQ/PerturbBridge}，存档版本见 \url{https://doi.org/10.5281/zenodo.24272128}。

## Abstract
\textbf{Motivation:}Single-cell perturbation prediction seeks to recover transcriptional responses to unseen interventions from unpaired control and perturbed populations. The Schr\"odinger Bridge provides a principled framework for modeling these transitions as stochastic transport, but learning bridge dynamics directly from high-dimensional, sparse gene-expression profiles remains challenging. \textbf{Results:} We present PerturbBridge, a conditional latent Schr\"odinger Bridge framework for single-cell perturbation response prediction. A response-anchored autoencoder constructs a compact cellular representation that preserves dominant transcriptional response directions identified from training perturbations while encoding complementary cellular variation. In this latent space, PerturbBridge models conditional stochastic transport through a tractable approximation to the Schr\"odinger Bridge. We introduce the Perturbation-Induced Bridge Transformer, which uses perturbation and time-dependent slots to guide interactions among latent coordinates during drift estimation. Evaluations on Norman, Sci-Plex3, and Replogle RPE1 demonstrate leading performance in differential-expression direction recovery and perturbation-effect correlation, alongside competitive gene-expression prediction accuracy. \textbf{Availability:} The source code is available at \url{https://github.com/echQoQ/PerturbBridge}, with an archived version at \url{https://doi.org/10.5281/zenodo.24272128}.

---

## 论文详细总结（自动生成）

# PerturbBridge 论文结构化总结

## 一、核心问题与研究背景

- **任务定义**：单细胞扰动预测旨在从**非配对**的对照群体与扰动群体中，推断细胞在**未见干预**（新基因扰动、新药物/剂量、新细胞背景）下的转录组响应。
- **根本困难**：
  - 单细胞测序是破坏性的，无法观测同一细胞扰动前后的状态，因此只能获得两个边缘分布，缺乏细胞级对应关系。
  - 可能的干预、剂量与细胞背景组合空间巨大，穷举实验不可行（虚拟细胞的核心瓶颈）。
  - 基因表达数据**高维且稀疏**，直接在此空间学习随机动力学非常困难。
- **理论工具**：薛定谔桥（Schrödinger Bridge, SB）以相对熵最小化在给定端点边缘分布间构造随机传输过程，天然不要求配对样本，理论上适配该问题；但一般端点分布下 SB 无闭式解，数值求解昂贵。
- **已有工作与空白**：
  - GEARS（基因关系图）、scGPT（预训练表示）、chemCPA/PRnet（化学扰动条件生成）、PerturbNet（条件可逆流）。
  - CellFlow（flow matching 条件传输）、scLDM（条件潜扩散）。
  - Departures 同样基于 SB，但需在**基因表达空间**同时学习连续表达与离散激活状态两条桥，并依赖 minibatch 最优传输构造端点耦合。
- **本文定位**：把 SB 从高维基因空间搬到**紧凑潜空间**，并解决"潜空间是否保留扰动诱导的转录变化"这一关键矛盾。

---

## 二、方法论

### 2.1 总体框架（两阶段训练）

1. **第一阶段**：训练响应锚定自编码器（RA-AE），仅做基因表达重建，随后**冻结**编码器与解码器。
2. **第二阶段**：在冻结潜空间中，用非配对对照/扰动细胞的潜表示训练条件桥模型（PIBT 参数化漂移场）。
3. **推理**：对照细胞 → 编码 → 在目标扰动条件下按学习到的随机动力学传输 → 解码为预测扰动细胞群体。

### 2.2 响应锚定自编码器（RA-AE）

- **构建共享响应子空间**：
  - 对每个（细胞背景 τ，扰动条件 c）计算群体平均响应差 Δ_{τ,c} = 扰动组均值 − 对照组均值。
  - 将各 Δ 作为列堆叠为 Δ ∈ R^{G×M}，做 SVD，取前 r 个左奇异向量构成正交基 U ∈ R^{G×r}（UᵀU = I_r），张成"主导转录响应方向"。
- **正交分解**：对中心化后的表达 x − μ，
  - 响应对齐坐标 a = Uᵀ(x − μ) ∈ R^r（**直接保留，不经压缩**）；
  - 正交残差 q = P⊥(x − μ)，P⊥ = I_G − UUᵀ。
- **残差非线性编码**：h = E_φ(q) ∈ R^{d−r}，潜变量 z̃ = [a; h] ∈ R^d。
- **解码**：x̃ = μ + Ua + P⊥D_ψ(h)；损失为逐基因 MSE（L_rec = E[‖x − x̃‖²₂/G]）。
- **潜空间归一化**：用全局均值 m 与尺度 s（各维方差均值的平方根）标准化，得到完整编码器 e_φ 与解码器 d_ψ。
- **关键性质**：由 UᵀP⊥ = 0 可证 Uᵀ(d_ψ(e_φ(x)) − x) = 0，即**响应对齐坐标在重建中被精确保留**，重建误差只落在正交补空间。

### 2.3 条件潜空间薛定谔桥

- 固定编码器诱导潜分布 ρ^τ_0 = (e_φ)#π^τ_0，ρ^{τ,c}_1 = (e_φ)#π^{τ,c}_1。
- 条件 SB：P* = argmin_P D_KL(P‖R^τ)，约束端点边缘为 ρ^τ_0、ρ^{τ,c}_1；解可写成"参考路径条件分布的混合"，权重由最优端点耦合 γ* 给出。
- **可处理近似（核心简化）**：
  - 参考过程取常系数各向同性布朗运动 dZ_t = σ_B dW_t；
  - **放弃最优耦合求解**，直接独立采样端点，即 γ = ρ^τ_0 ⊗ ρ^{τ,c}_1（保留边缘分布，但不保证熵最优）。
  - 借用 I²SB 的解析条件桥：q(z_t|z_0,z_1) = N((1−t)z_0 + t z_1, σ_B² t(1−t) I_d)，可直接采样 z_t = (1−t)z_0 + t z_1 + σ_B√(t(1−t))·ε。
  - 对应参考漂移 b_ref = (z_1 − z_t)/(1 − t)。
- **桥匹配目标**：L_SB = E[(1/d)‖v_θ(z_t, t, ĉ) − b_ref‖²]，其中 ĉ = κ_ω(τ, c) 编码扰动身份、协变量与细胞背景。
- **理论保证**：该目标的总体系最优解是参考漂移的条件期望；经 Markovian projection，以 v* 为漂移、σ_B 为扩散系数的扩散过程具有与桥混合相同的时边缘分布（Fokker–Planck 方程给出），从 ρ^τ_0 出发可在连续时间极限下恢复规定端点分布。

### 2.4 扰动诱导桥 Transformer（PIBT）

- **动机**：扰动响应涉及潜坐标间的协同变化，仅用特征调制式条件注入（如 DiT 的 adaLN）不足以刻画"条件依赖的坐标交互"。
- **特征级 token 化**：每个潜坐标作为一个 token，F^(0)_j = z_{t,j}·w_j + b_j ∈ R^H。
- **条件诱导槽（slots）**：S^(0) = reshape_{K×H}(MLP([e_t; e_c])) + I_slot，e_t 为时间嵌入，e_c = W_c ĉ + b_c 为条件嵌入，I_slot 为可学习槽身份嵌入。
- **共享亲和力的"读–处理–写"机制**（借鉴 BiXT）：
  - 亲和矩阵 M^ℓ = Q^ℓ(K_s^ℓ)ᵀ/√A，其中 Q 来自坐标 token，K_s 来自**固定的初始槽** S^(0)，故亲和力同时依赖当前细胞状态与扰动/时间条件；
  - 同一 M^ℓ 双向归一化：R^ℓ = softmax_coord(M^ℓ)（坐标→槽聚合权重），W^ℓ = softmax_slot(M^ℓ)（槽→坐标分发权重）；
  - 读：S'^ℓ = S^(0) + (R^ℓ)ᵀV^ℓ，S''^ℓ = S'^ℓ + FFN(LN(S'^ℓ))；
  - 写：F^{ℓ+1} = F^ℓ + (W^ℓ S''^ℓ) W_O。
- **效率设计**：坐标之间不做直接自注意力，仅通过 K 个紧凑槽间接交互；各 block 复用同一 S^(0)，但亲和力逐层重算以适配演化中的细胞状态。
- **输出头**：共享线性头将每个坐标表示映射为对应漂移分量 v_{θ,j}。

### 2.5 随机推断

- 求解 SDE：dz_t = v_θ(z_t, t, ĉ)dt + √(2γ(t))dW_t，取 γ(t) = σ_B²/2 与训练参考扩散一致。
- 用 Euler–Maruyama 离散，N = 100 步；末端潜状态经 RA-AE 解码得预测表达。
- 对每个对照细胞独立采样多条轨迹，得到预测扰动细胞群体（可产生分布级多样性）。

### 2.6 关键超参数与实现

- RA-AE：编码器隐层 512/256，对称解码器，GELU。
- 潜维/响应维 (d, r)：
