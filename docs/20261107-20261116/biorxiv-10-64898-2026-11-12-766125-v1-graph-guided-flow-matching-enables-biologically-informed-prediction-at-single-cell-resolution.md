---
title: Graph-guided flow matching enables biologically informed prediction at single-cell resolution
title_zh: 图引导的流匹配能够在单细胞分辨率下实现具有生物学依据的预测
authors: "Liou, H.-Y., Sprang, M., Selby, D. A., Grossmann, G., Vollmer, S., Riesgo-Ferreiro, P., Gerbracht, J. V., Schroers, B., Strilic, B., Kim, J."
date: 2026-11-13
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.12.766125v1.full.pdf"
tags: ["query:virtual-cell"]
score: 10.0
evidence: 用图引导流匹配预测扰动后的单细胞转录组
tldr: Perturb-seq虽能并行解析基因扰动，但穷尽扰动空间仍不现实。GFM将生物知识图谱与潜在流匹配结合，直接预测扰动后的单细胞转录组。在多个大规模数据集上，它优于线性基线和现有深度学习模型，训练最高快30倍，并在双基因扰动及有限数据下保持稳健。该框架还在HSP90AA1失活和慢性髓性白血病靶点识别中验证，为治疗靶点优先排序提供生物信息引导的生成方案。
source: biorxiv
selection_source: fresh_fetch
motivation: Perturb-seq实验可大规模并行扰动，但无法穷尽全部基因组合，亟需准确预测未见扰动后的单细胞响应。
method: GFM整合生物知识图谱与潜在流匹配，构建生成式框架预测扰动后单细胞转录组。
result: 在多个Perturb-seq数据集上，GFM优于线性基线和现有深度学习模型，训练最高快30倍，双基因未见扰动预测具竞争力。
conclusion: GFM是生物信息引导的生成框架，可预测单细胞扰动响应并优先治疗靶点，并在HSP90AA1和CML中验证。
---

## 摘要
Perturb-seq 能够在单细胞分辨率下系统性地探究大规模并行遗传扰动，然而对完整扰动空间进行穷尽式表征仍不切实际。在此，我们提出图引导流匹配（Graph-guided Flow Matching，GFM），一种将生物知识图谱与潜在流匹配相结合的生成式框架，用于预测扰动后的单细胞转录组。在多个大规模 Perturb-seq 数据集上，GFM 在预测未见过的单基因扰动方面优于强线性基线和当前深度学习模型，同时训练速度最高可提升 30 倍，并在训练数据有限时仍保持稳健。当训练期间两个扰动基因均未被观察到时，GFM 在双基因扰动预测任务中也表现出具有竞争力的性能。消融实验表明，将流匹配与知识图谱相结合能够准确预测扰动响应。最后，GFM 能够准确计算 HSP90AA1 失活所引发的转录后果，并在慢性髓性白血病中识别出模型未曾见过的候选靶点。我们的研究确立了 GFM 作为一种具有生物学依据的生成式框架，可预测单细胞扰动响应，从而用于治疗靶点的优先级排序。

## Abstract
Perturb-seq enables systematic interrogation of massively parallel genetic perturbations at single-cell resolution, yet exhaustive characterization of the full perturbation space remains impractical. Here, we present Graph-guided Flow Matching (GFM), a generative framework that integrates biological knowledge graphs with latent flow matching to predict post-perturbation single-cell transcriptomes. Across multiple large-scale Perturb-seq datasets, GFM outperforms a strong linear baseline and current deep-learning models in predicting unseen single-gene perturbations, while training up to 30x faster and remaining robust with limited training data. GFM also demonstrates competitive performance in the two-gene perturbation prediction task when neither perturbed gene is observed during training. Ablation experiments show that combining flow matching with knowledge graphs enables accurate prediction of perturbation responses. Finally, GFM accurately calculates transcriptional consequences of HSP90AA1 inactivation and identifies target candidates unseen by the model in chronic myeloid leukemia. Our study establishes GFM as a biologically informed generative framework that predicts single-cell perturbation responses for prioritization of therapeutic targets.

---

## 论文详细总结（自动生成）

# 论文结构化总结：Graph-guided Flow Matching (GFM)

## 1. 核心问题与整体含义

- **背景**：Perturb-seq 将 CRISPR 激活/抑制与单细胞 RNA 测序结合，可在单细胞分辨率下并行解析数十万级遗传扰动，是研究基因调控网络、基因互作与药物靶点的重要工具。
- **核心矛盾**：扰动空间（尤其是多基因组合）的增长速度远超实验可扩展性，穷尽式实验表征不可行，因此亟需能从已有 Perturb-seq 数据学习并**泛化到未见扰动**的计算方法。
- **现有方法的不足**：
  - 基于预训练基础模型的方法（scGPT、CellFlow）依赖大规模预训练数据学习基因/扰动关系，**未显式建模扰动特异的基因-基因相互作用**；
  - 基于 GNN 的方法（GEARS、TxPert）引入了 GO、PPI 等生物先验，但生物先验对预测性能的贡献**缺乏系统剖析**，也未被有效整合进生成式框架；
  - 流匹配方法面临根本困难：单细胞测序是破坏性的，**扰动前后同一细胞的配对轨迹不可观测**；Meta Flow Matching、MixFlow 等主要改进源分布的初始化，而非建模扰动在系统中的传播过程。
- **整体含义**：论文提出将**生物知识图谱**与**潜在流匹配**结合，使生成模型具备生物学归纳偏置，从而在数据有限时仍能对未见扰动做出准确、可解释的单细胞转录组预测，并服务于治疗靶点优先级排序。

## 2. 方法论

### 2.1 核心思想
GFM 在 VAE 潜空间中，以知识图谱导出的扰动嵌入为条件，用神经 ODE 学习一个速度场，将高斯噪声沿最优传输（OT）路径输运到扰动后的细胞状态，再解码回基因表达空间。整体类比“文生图”的 prompt 引导生成，但 prompt 是图神经网络编码的扰动表示。

### 2.2 三大模块
- **VAE（潜空间编码）**
  - 编码器参数化高斯后验 \(q_\phi(z|x)=\mathcal{N}(\mu_\phi(x),\mathrm{diag}(\sigma_\phi^2(x)))\)，重参数化采样；
  - 解码器 \(f_\theta\) 重建表达谱，损失为重构误差 + KL 散度（ELBO）；
  - 仅用训练集细胞预训练；训练后直接取后验均值 \(\mu_\phi(x)\) 作为确定性潜编码供下游使用。
- **知识图谱约束的 GAT（扰动表示）**
  - 构建三张基因节点图并拼接为联合图 \(G_P\)：
    1. **GO 图**：沿用 GEARS，基于 GO 术语集的 Jaccard 相似度，每个目标基因保留 top-20 邻居；
    2. **PPI 图**：来自 STRING v12.0（人类），按 combined score 保留 top-10 邻居；
    3. **扰动相似图**：用 Replogle K562 全基因组 CRISPRi 数据，计算各扰动相对对照的平均表达变化向量 \(D_i=\bar{x}_i-\bar{x}_{ctrl}\)，以余弦相似度连边，保留 top-20。
  - 每个节点初始化可学习嵌入，经 2 层 GAT 做 2-hop 消息传递；
  - 多基因扰动的条件向量为各节点嵌入**求和**；对照条件用零向量。
- **OT 条件流匹配（生成）**
  - 训练前对**每个扰动条件独立**预计算精确 OT 耦合，得到配对 \((z_0,z_1)\sim\pi(y)\)，避免训练中反复做昂贵的 minibatch OT；
  - 采用仿射插值路径 \(z_t=(1-t)z_0+t z_1\)，目标速度 \(v_t=z_1-z_0\)；
  - 条件流匹配损失：\(\mathcal{L}_{CFM}=\mathbb{E}[\|v_\psi(t,z_t,y)-v_t\|_2^2]\)；
  - 时间用正弦嵌入，与潜状态、扰动嵌入拼接后经 MLP 输出速度；GNN 与 ODE 模块**联合训练**。
- **推理**
  - 使用 classifier-free guidance：\(v_{guided}=(1-\gamma)v_\psi(t,z_t,\varnothing)+\gamma v_\psi(t,z_t,y)\)，\(\gamma=1.5\)；
  - 用 dopri5 ODE 求解器从 \(t=0\) 积分到 \(t=1\)，最后由预训练 VAE 解码为表达谱。

### 2.3 关键设计取舍
- 不依赖“扰动前-后细胞”的显式配对（不可观测），而是用噪声到扰动状态的 OT 耦合替代，规避了不可观测轨迹带来的误差；
- 用预计算的条件特异 OT 替代训练中的在线 OT，提升效率并鼓励更直的流轨迹。

## 3. 实验设计

- **数据集**
  - 单基因 CRISPRi Perturb-seq：Replogle 的 **K562、RPE1、K562 全基因组筛选**，以及 Nadig 的 **HepG2、Jurkat**（共 4 个用于主基准）；
  - 双基因 CRISPRa：**Norman 数据集**（131 个双基因 + 152 个单基因扰动，K562）；
  - 下游应用：K562 全基因组 CRISPRi 数据用于 CML 靶点识别。
- **数据划分**
  - 单基因：train/val/test = 75%/10%/15%，**3 个独立随机 split**；
  - 双基因：50%/10%/40%（沿用 GEARS 的 simulation split），测试集按“两基因是否在训练中出现”分为 **seen-2 / seen-1 / seen-0** 三个难度子组。
- **Benchmark 与对比方法**
  - 深度学习基线：**CellFlow、GEARS、scGPT**；
  - 强线性基线：PCA 基因嵌入 + 线性映射扰动效应；
  - 参照上下界：**Perturb train**（随机采样训练集扰动细胞，近似下界）、**Technical duplicate**（真实数据对半划分，近似上界）；
  - 双基因 seen-2 额外加入 **additive 模型**（两单基因效应相加）。
- **评价指标**：MSE、Pearson、**Pearson delta**（相对 perturb-train 的差异信号相关性）、**2-Wasserstein 距离**、**Energy distance**；主评估限定在**每个扰动的 top-20 DEG**（并做 top-10 至 top-100 的敏感性分析）。除 Pearson delta 外均用 perturb-train 归一化。
- **消融与机制分析**
  - 模块消融：去掉 OT 流匹配目标（改为 MLP 直接回归潜终点）、随机置换图拓扑、两者同时消融；
  - 图类型消融：分别及两两随机置换 GO / PPI / 扰动相似图；
  - 图连接性分析：测试扰动的训练邻居数、训练邻居比例、与训练邻居扰动效应的最大/中位余弦相似度，与性能做 Spearman 相关。
- **下游验证**：预测 HSP90AA1 敲低的转录后果、GO 富集、按下调基因 Jaccard 相似度排序相似扰动、CML 候选靶点优先排序。

## 4. 资源与算力

- 文中明确给出：实验运行在 **4× NVIDIA H200 NVL GPU** 提供的 **单卡切片（18 GB 显存）** 上（驱动 610.43.02，CUDA 13.3）。
- 训练配置：VAE 最多 500 epochs（验证损失 100 轮不降则早停）；流匹配最多 500 epochs，每 50 epochs 用验证集 2-WD 评估（连续 4 次不降则早停）。
- 效率结论：训练比现有深度模型**快 1.5–30×**；推理时间与 GEARS 相当，比 CellFlow/scGPT **快约 100×**。
- **未明确说明**：总 GPU 小时数、单次训练的具体墙钟时长、各基线方法的调参与搜索成本。算力披露相对简略。

## 5. 实验数量与充分性

- **规模**：4 个单基因数据集 × 3 个独立 split；6 档训练数据比例（0.75→0.025）的鲁棒性曲线；双基因 3 个子组；4 个数据集上的多条件消融（模块消融 + 7 种图消融组合）；图连接性的多指标相关分析；1 个 CML 案例研究。整体实验量较充分。
- **客观性/公平性方面的优点**：
  - 使用三个独立随机 split 并汇总结果；
  - 引入 Dup（上界）与 Perturb train（下界）作为参照，并对指标做归一化，缓解了“模型只是复现通用扰动效应”的质疑；
  - 明确复现了领域内已知现象——线性基线优于多种深度模型，并在此基础上仍报告 GFM 的增益，态度较诚实；
  - 统一预测细胞数（每扰动 100 个），并说明去掉了 GEARS/scGPT 的最终平均步骤以获得单细胞输出。
- **潜在不足**：
  - 对比方法多按官方教程默认配置运行，**未做同等强度的超参搜索**，可能低估基线；
  - 双基因任务仅一个数据集（Norman），且该数据以加性效应为主，非加性互作的预测能力验证有限；
  - 主评估集中于 top-20 DEG，全转录组层面的表现证据不足；
  - E-distance 上所有模型均未优于随机采样，说明群体离散度维度未被任何方法很好解决，GFM 的优势主要体现在均值与 2-WD。

## 6. 主要结论与发现

- **单基因预测**：GFM 在 4 个数据集上对未见单基因扰动的 top-20 DEG 预测**全面优于** CellFlow、scGPT、GEARS 及强线性基线（均值指标与 2-WD），UMAP 与单基因表达分布也更贴近真实；但在 E-distance 上无优势。
- **鲁棒性**：训练数据从 75% 降至 2.5% 时所有模型性能下降，GFM 始终领先，且训练更快。
- **双基因预测**：seen-2、seen-1 子组与其他模型相当；**seen-0（两基因均未见过）子组优于现有深度模型**；seen-2 中加性模型最佳，印证该数据集中双基因效应高度可加（与文献中 >95% 可加的结论一致）。
- **消融结论**：
  - 去掉 OT 流匹配或随机化图拓扑都会显著降低性能，两者

- 消融结论（续）：
  - 去掉 OT 流匹配目标、改为 MLP 直接回归潜终点后，性能明显下降；随机置换图拓扑同样带来显著退化；**两者同时消融时退化幅度最大**，说明“图结构提供的生物学先验”与“OT 流匹配提供的生成式输运”是两个**互补且不可互相替代**的增益来源，而非同一效应的重复表述。
  - 图类型消融显示：单独随机置换 **扰动相似图** 造成的性能损失最大，PPI 次之，GO 相对最小；两两组合置换的退化大于单图置换，提示三类图编码了部分冗余但并非完全重叠的邻域信息。这一结果为“哪类生物先验真正有用”提供了此前文献中较少见的定量证据，也部分回应了论文开篇对 GEARS/TxPert 先验贡献缺乏系统剖析的批评。
  - **图连接性分析**：测试扰动在训练集中邻居的数量、邻居占比，以及其与最近训练邻居扰动效应的余弦相似度，均与预测性能呈正相关（Spearman）。这既是对“GFM 增益来自图外推”这一机制假设的直接支持，也暴露了一个内在依赖——对图中高度孤立、缺少相似训练邻居的扰动，GFM 的优势会收窄。
- **下游应用验证**：
  - 预测 HSP90AA1 敲低的转录后果，其下调基因集合的 GO 富集结果与已知 HSP90 生物学（伴侣蛋白、应激响应等）一致；
  - 以“下调基因 Jaccard 相似度”检索相似扰动，能够召回功能上相关的扰动，说明预测谱保留了可用的功能相似性结构，而不仅是数值拟合；
  - 在 K562 全基因组 CRISPRi 数据上对 CML 相关候选靶点做优先级排序，预测结果与已有治疗靶点/文献证据具有一致性，展示了从“预测表达谱”走向“靶点优先级”这一应用链条的可行性。不过该案例属于定性/半定量的概念验证，样本量与统计检验力度有限，尚不足以作为药物发现的独立证据。

## 7. 局限与批判性审视

除前文已列出的对比公平性与评测覆盖问题外，还有若干值得注意的点：

- **条件表示的加性偏置**：多基因扰动的条件向量由各基因节点嵌入**求和**得到，这一设计在结构上偏向可加效应，难以表达基因间的协同或拮抗。结合 Norman 数据本身以加性效应为主、且 seen-2 子组中简单加性模型即取得最佳表现，GFM 在**真正非加性互作**上的能力实际上尚未被严格检验。
- **图先验的跨细胞系迁移问题**：扰动相似图由 Replogle **K562** CRISPRi 数据构建，却被用于 RPE1、HepG2、Jurkat 等细胞系。不同细胞系的调控网络与扰动效应差异明显，这种跨语境复用可能同时带来信息增益与系统性偏差，论文未对此做针对性分析（例如按细胞系重建图并比较）。
- **对外部资源的依赖**：性能依赖 GO 注释质量、STRING 版本与 top-k 邻居阈值（20/10/20），这些超参的敏感性仅在附录或未充分展开；图构建的预处理成本也未计入“训练更快”的效率论述。
- **OT 预计算的统计噪声**：OT 耦合按每个扰动条件独立计算，对于训练集中细胞数较少的扰动，其耦合估计方差较大，可能影响该条件下的流场学习质量；论文未报告按扰动细胞数分层的性能。
- **潜空间确定性编码**：推理时仅取 VAE 后验均值，丢弃了后验方差，因此模型无法表达“同一扰动的细胞间异质性来自潜变量不确定性”这一层，与 E-distance 上无优势的结果相互呼应——GFM 优化的是条件均值分布的形状（2-WD、相关性），而非群体离散度。
- **指标设计的潜在偏倚**：主评估限定在由**真实数据**定义的 top-20 DEG 上，这一选择虽提升了信号信噪比，但也可能对某些基线（尤其是直接回归均值的方法）不完全公平，全转录组层面的结论仍显薄弱。
- **可解释性停留在间接层面**：论文通过图消融与连接性相关分析间接论证图先验的作用，但未深入展示 GAT 学到的边权重/注意力是否对应已知通路，因而“可解释”更多是框架层面的主张，而非逐案例的机制证据。

## 8. 总体评价与启示

- **方法层面的贡献**是清晰的：将“知识图谱编码的扰动条件”与“潜空间 OT 条件流匹配”组合为一个统一框架，并用预计算的条件特异 OT 耦合解决了单细胞破坏性测序导致的前后配对不可观测问题。这一“以分布级 OT 配对替代不可观测的单细胞轨迹”的思路，具有较强的可迁移性，可推广到其他缺乏配对观测的扰动/干预建模场景。
- **实证层面的贡献**同样值得肯定：三个独立 split、上下界参照、指标归一化、对“线性基线强于深度模型”这一不利事实的如实报告，以及把“生物先验到底有没有用”转化为可消融的实验问题，都提升了结论的可信度。
- **主要保留意见**集中在泛化边界的刻画不足：GFM 的优势在“测试扰动于图中拥有相似训练邻居”时最明显，而对非加性组合扰动、跨细胞系迁移、群体异质性（E-distance）三类情形，证据仍不充分。未来工作若能围绕“图构建的细胞系特异性”“条件组合的非加性建模（如双线性/交互项）”“潜变量不确定性传播”三个方向推进，将更完整地回答“能否泛化到真正未见的多基因扰动”这一核心问题。

（完）
