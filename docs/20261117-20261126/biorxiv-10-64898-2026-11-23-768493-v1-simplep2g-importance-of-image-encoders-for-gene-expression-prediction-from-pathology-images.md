---
title: "SimpleP2G: Importance of Image Encoders for Gene Expression Prediction from Pathology Images"
title_zh: SimpleP2G：图像编码器在病理图像基因表达预测中的重要性
authors: "Wang, J., Zhang, J., Hsieh, C.-Y., Gu, C., Heng, P.-A."
date: 2026-11-25
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.23.768493v1.full.pdf"
tags: ["query:spatial-gene"]
score: 9.0
evidence: 利用冻结图像编码器从病理图像直接预测基因表达
tldr: 病理图像到基因表达预测（P2G）中，图像编码器、预测头和空间上下文常被同时改动，导致性能差异难以归因。作者在5个HEST-1K数据集、两个200基因面板和每数据集3张留出切片上做配对输入控制，并把图像输入统一替换为Virchow2。提出直接对冻结嵌入做基因查询解码的SimpleP2G，以及加入空间位置邻域嵌入的SimpleP2G-cross。结果显示Virchow2在39/40组方法-数据集-面板比较中提升PCC-200，SimpleP2G在共享特征下单patch平均PCC-200于5个数据集均最高，说明应先改进图像表示，再增加预测头复杂度。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有P2G研究常同时改动预测头、图像编码器和空间上下文，导致性能提升来源难以归因。
method: 在5个HEST-1K数据集和两个200基因面板上做配对图像输入控制，提出基于冻结嵌入的直接基因查询解码器SimpleP2G及其空间邻域版本。
result: 替换为Virchow2在40组方法-数据集-面板比较中39组提升；共享特征下SimpleP2G单patch平均PCC-200在5个数据集均最高。
conclusion: 应先改进图像表示再增加预测头复杂度；冻结病理嵌入上的直接解码器已是强基线，并提供可复现控制。
---

## 摘要
病理图像到基因表达（P2G）研究常常同时改变预测头、图像编码器和空间上下文，导致性能差异难以归因。我们通过配对图像输入对照和明确的输入设置来考察这些因素。我们的主要比较覆盖五个 HEST-1K 数据集、两个 200 基因面板，以及每个数据集三个选定的留出切片，并使用经验证集选择的检查点。在所有五个数据集上，用 Virchow2 替换传统图像输入后，在 40 个方法—数据集—面板比较中有 39 个提高了平均 PCC-200，而有一个比较下降。我们提出 SimpleP2G，一种在冻结嵌入上直接进行基因查询的解码器，以及 SimpleP2G-cross，它加入具有空间位置的邻域嵌入。在共享 Virchow2 特征的情况下，SimpleP2G 在两个面板下于所有五个数据集上均具有最高的单图块平均 PCC-200；跨图块变体在每个面板下于五个数据集中的四个上领先。解码器和上下文消融表明，更大的深度和更广的上下文并不能一致地改善预测。总体而言，这些结果提示应在增加预测头复杂度之前先改进图像表示：在冻结的病理嵌入上使用直接解码器已经提供了强基线。我们希望我们重新实现的图像编码器升级基线以及 SimpleP2G 模型能够为未来 P2G 研究提供透明、可复现且强有力的对照。

## Abstract
Pathology-image-to-gene-expression (P2G) studies often change the prediction head, image encoder, and spatial context together, making performance differences difficult to attribute. We examine these factors through paired image-input controls and explicit input regimes. Our main comparison covers five HEST-1K datasets, two 200-gene panels, and three selected held-out slides per dataset, using validation-selected checkpoints. Across all five datasets, replacing conventional image inputs with Virchow2 improves mean PCC-200 in 39 of 40 method--dataset--panel comparisons, while one comparison decreases. We introduce SimpleP2G, a direct gene-query decoder over frozen embeddings, and SimpleP2G-cross, which adds spatially positioned neighboring embeddings. With shared Virchow2 features, SimpleP2G has the highest single-patch mean PCC-200 on all five datasets under both panels; the cross-patch variant leads on four of five datasets under each panel. Decoder and context ablations show that greater depth and broader context do not consistently improve prediction. Together, these results suggest improving image representations before adding prediction-head complexity: a direct decoder over frozen pathology embeddings already provides a strong baseline. We hope our reimplemented image-encoder-upgraded baselines and SimpleP2G models serve as transparent, reproducible, and strong controls for future P2G research.

---

## 论文详细总结（自动生成）

# SimpleP2G 论文结构化总结

## 1. 核心问题与研究背景

- **领域背景**：H&E 病理切片易得，而空间转录组（ST）测量昂贵、通量低。病理图像→基因表达预测（P2G）旨在用形态学信息推断空间分辨的基因表达，连接两者。
- **核心痛点**：近年 P2G 系统大量投入"预测头"设计（对比检索、扩散/流生成、基因排序目标、空间图/Transformer），但新方法往往**同时**更换了更强的病理基础模型特征、引入了邻域或全切片上下文、并改变了训练日程。这种"复合改动"使得性能提升**无法归因**于头设计本身。
- **研究问题**：在保持下游预测方法（头、目标、划分、训练日程）不变的前提下，仅改进视觉表示能带来多少收益？在强表示之上，还需要多复杂的头与上下文？
- **整体含义**：作者主张"**先改进图像表示，再增加预测头复杂度**"，并提供一个透明、可复现的强基线作为社区对照。

## 2. 方法论

### 2.1 配对图像输入对照（归因框架）

- 固定下游头、损失、数据划分与训练日程，仅把参考图像输入替换为 Virchow2 特征（必要时重算检索邻居与特征图结构），报告**配对**的 PCC 变化 Δ。
- 参考输入分别为：BLEEP 用 ImageNet ResNet50、HisToGene 用原始 patch、MERGE 用其发布的 TCGA-ResNet18 特征、M2TGLGO 用 ImageNet ResNet50。
- 区分两类问题：**编码器升级**（下游计算固定）与**头比较**（编码器固定，但显式说明各方法可用的上下文，不强求输入完全对齐）。

### 2.2 问题形式化

- 切片含 M 个 ST spot，spot *i* 有图像块 *v_i*、坐标 *r_i*、表达 *x_i*（C 个基因）；训练目标为 log2(count+1)，测试时不可见表达。
- **单图块设置**：`x̂_i = f_θ(v_i)`
- **跨图块设置**：`x̂_i = f_θ(v_i, C_i)`，其中 `C_i = {(v_j, r_j − r_i) : j ∈ N_i} ∪ G`，N_i 为空间邻域，G 为可选的切片级图像信息；**邻域的表达值从不作为输入**。

### 2.3 SimpleP2G（单图块）

- 冻结编码器 φ（Virchow2，CLS token 拼接 patch token 均值，D=2560）→ 2 层 MLP + SiLU → T=4 个条件 token `Z^tar_i ∈ R^{T×D}`（固定解码器接口，适配任意编码器维度）。
- **基因查询解码器**：可学习查询表 `Q ∈ R^{C×D}`（每基因一个查询），经 L=12 层 pre-norm Transformer 解码层（基因间自注意力 + 对条件 token 的交叉注意力 + 门控 FFN，残差与 RMSNorm，D=384，6 头）。
- 每个查询输出均值 `μ̂` 与对数方差 `log σ̂²`；softplus 保证变换后表达空间中的均值非负。
- **损失**：高斯负对数似然 `L = 1/(2BC) Σ[(x−μ̂)²/σ̂² + log σ̂²]`，`log σ̂²` 截断于 [−10, 10]。
- **优化**：AdamW（β=0.9/0.999）、梯度裁剪 1.0、线性 warmup + 余弦衰减、EMA；推理仅需一次确定性前向（无检索库、无迭代采样）。

### 2.4 SimpleP2G-cross（跨图块）

- 邻居集合 N_i 为除自身外 **K=24** 个最近测量 spot；同一冻结编码器产生目标与邻居嵌入。
- 每个邻居投影为一个 token 并加**相对坐标位置编码**（按切片中位最近邻间距 a_S 归一化）：`z^nbr_ij = h_nbr(e_j) + h_pos((r_j − r_i)/a_S)`；缺失邻居填充并掩码。
- 可选**切片 token**：`z_slide = h_slide(mean_m e_m)`。
- 解码器条件序列 `Z_i = [Z^tar_i ; {z^nbr_ij} ; z_slide]`——"仅目标/仅邻居/目标+邻居/目标+邻居+切片"仅在条件序列上不同，解码器与损失不变。

## 3. 实验设计

### 3.1 数据与场景

- **5 个 HEST-1K 数据集**：Brain、PRAD、HER2ST、Lung、ccRCC；覆盖 5 个器官、人与小鼠组织、3 种测序平台（Visium、ST v1、Xenium），共 **117 张切片、226,656 个 spot**。
- **划分**：每数据集 3 个"留一测试切片"折（leave-one-slide-out），每折另留 1 张验证切片，划分在训练前固定并由所有方法共享；属**切片级**而非患者级留出。
- **基因面板**：过滤线粒体/核糖体基因后构建两个 200 基因面板——HMHVG-200（高均值+高方差）与 HVG-200（跨切片批次感知高变基因），仅用各折训练表达选取。
- **指标**：PCC-200 为主指标（面板内逐基因相关均值），PCC-50（前 50 高相关基因）为补充，另报 MSE、MAE；常数预测对可变目标记零相关；三切片均值 ± 样本 SD，seed 42。

### 3.2 对比方法与 benchmark

- **单图块（4 个）**：BLEEP（对比检索）、Stem（条件扩散）、STRank†（相对排序）、SimpleP2G。
- **跨图块（6 个）**：Gene-DML（目标/邻居/全局三通路）、HisToGene、STFlow（全切片流匹配）、MERGE（层次图）、M2TGLGO†（拓扑+基因关系）、SimpleP2G-cross。
- 所有方法共享冻结 Virchow2 特征、同一测试折、同一面板与验证选点规则；† 表示作者自行适配并在附录 B 详述。
- **消融**：6 种编码器（Virchow2、UNI、CONCH、DINOv2-S/L、SAM-B）；解码器/损失（Linear-MSE、MLP-MSE、2 层-MSE、12 层-MSE、12 层-Gaussian NLL）；条件序列（仅邻居 K=24、target+K=8/24/48、target+K24+slide）。
- **定性分析**：HER2ST fold 0（SPA148）上 ResNet50 vs Virchow2 的配对比较，展示 IGKC、LYZ、TFF3 三基因的空间图与逐基因 PCC/RMSE；附录 D 用 Reactome 通路做探索性富集检验。

## 4. 资源与算力

- 明确给出：使用 **PyTorch 2.10.0**，实验总计约 **1,700 A100 GPU 小时**。
- **未明确说明**：GPU 的具体数量、单次训练时长、各方法/消融的算力拆分。
- 精度细节有交代：多数运行用 FP16 混合精度，STRank 用 FP32，Stem 在若干折切换 BF16，BLEEP 参考输入的验证/推理部分用 FP32。

## 5. 实验数量与充分性

### 规模

- **配对编码器实验**：4 方法 × 5 数据集 × 2 面板 = **40 组方法–数据集–面板比较**，对应 **120 个配对折**，全部报告。
- **主实验**：10 个模型 × 5 数据集 × 2 面板 × 3 折。
- **三组消融**：编码器 6 × 10 组合；解码器/损失 5 × 10 组合；条件序列 5 × 10 组合（均用 fold 0、seed 42）。
- 另有定性/逐基因分析、通路探索（395 次 Fisher 检验）。

### 充分性与公平性

- **公平性较好**：编码器、划分、基因面板、检查点选择规则、评估 spot 全部共享；配对比较在同方法内进行，避免"非配对排行榜"的混淆。
- **透明性**：自行适配的基线（STRank†、M2TGLGO†）与接口改动在附录 B 逐条说明；跨图块方法若原生使用全切片上下文，则保留其信息优势而非强行对齐。
- **局限**：仅 3 张测试切片、单一 seed，作者自述"提供描述性变异而非统计显著性证据"；无显著性检验、无置信区间；部分基线为再实现，可能未达原方法最优调参状态。

## 6. 主要结论与发现

- **编码器影响占主导**：Virchow2 替换参考输入后，**39/40** 组比较的平均 PCC-200 提升，绝对变化范围 −0.0118 ~ +0.3113；120 个配对切片中 **115 个**提升，40 组中 **35 组**三张切片全部提升；MSE 在 98/120、MAE 在 96/120 下降。典型例：HisToGene 在 HER2ST HMHVG 从 0.1209 → 0.4321。
- **唯一反例**：BLEEP 在 Brain HMHVG 从 0.3376 降至 0.3258，源于第三张切片 −0.1242 的大幅下降，说明特征依赖型头（检索）对嵌入几何变化敏感。
- **SimpleP2G 单图块最强**：两面板下 5 个数据集的平均 PCC-200 均最高，五数据集均值 HMHVG **0.5336**、HVG **0.2485**。
- **SimpleP2G-cross 具竞争力**：每个面板下 4/5 数据集领先；五数据集均值 0.5789/0.2722，优于 M2TGLGO（0.5685/0.2588）与 Gene-DML（0.5538/0.2596）；PRAD HMHVG 与 ccRCC HVG 上 M2TGLGO 更强。
- **编码器排序依组织与面板而变**：Virchow2 在 7/10 组合最佳；UNI 在 Brain HMHVG（0.3859 vs 0.3803）与 ccRCC HMHVG（0.3381 vs 0.2704）领先；DINOv2-L 在 Brain HVG 领先（0.1712 vs 0.1690）——通用视觉编码器可在个别比较中胜过病理专用编码器。
- **复杂度非一致有益**：12 层注意力在 7/10 组合优于 2 层但参数 45.971M vs 16.468M；MLP 在 Brain HMHVG 最佳；Gaussian NLL 在 8/10 组合优于 12 层 MSE，但在 ccRCC HMHVG 从 0.3842 掉到 0.2704；邻域从 8→24→48 非单调；slide token 仅在 7/10 组合提升（HER2ST HVG 升、其 HMHVG 与 PRAD HMHVG 降）。
- **总体建议**：冻结病理嵌入上的直接解码器已是强基线，应先升级图像表示，再讨论头的复杂度。

## 7. 优点

- **归因设计严谨**：配对图像输入对照 + 显式输入制度（单图块/跨图块）分离了"编码器"与"头/上下文"两类因素，方法论上比非配对排行榜更有说服力。
- **基线简洁且强**：SimpleP2G 无训练图像骨干、无检索库、无迭代采样，单次前向推理，却全面领先，具备实用参考价值。
- **透明可复现**：代码开源；所有基线适配、超参、精度切换、折构造、检查点规则均写入附录；逐折结果以 CSV 提供。
- **覆盖面广**：5 个器官、人/鼠、3 种测序平台、两个基因面板，且 120 个配对折全部报告，不挑结果。
- **如实报告负结果**：BLEEP 反例、ccRCC 上

- **如实报告负结果**：BLEEP 反例、ccRCC 上 Gaussian NLL 由 0.3842 掉至 0.2704、slide token 在 HER2ST HMHVG 与 PRAD HMHVG 的下降、邻域规模 8→24→48 的非单调性等，均被明确列出而非选择性汇报，增强了结论可信度。
- **对照条件交代清楚**：明确区分"编码器升级"与"头比较"两类实验，并在跨图块比较中保留各方法原生的全切片上下文优势，避免以"对齐输入"为名削弱基线。
- **工程可复用性**：固定解码器接口（T 个条件 token）使任意维度编码器可直接接入；单次确定性前向、无检索库与迭代采样，推理成本低，便于作为后续工作的默认对照。

## 8. 局限与不足

- **统计效力偏弱**：每数据集仅 3 张留出测试切片、单一 seed（42），作者自述仅提供"描述性变异而非统计显著性证据"；全文无显著性检验、无置信区间、无多 seed 方差，因此"39/40 提升"这类计数结论虽直观，但对切片间波动的稳健性未被量化。
- **划分粒度**：采用切片级留出而非患者级留出，同一患者的其他切片可能进入训练集，存在乐观偏差风险；对 HER2ST 等多切片同源数据集尤需注意。
- **基线强度存疑**：STRank†、M2TGLGO† 为作者自行适配，BLEEP、Stem、STFlow、MERGE 等虽尽量沿用官方配置，但未做逐方法的超参搜索，无法排除"基线未调至最优"导致的相对高估；论文亦未报告各基线在其原论文设定下的复现差距。
- **编码器空间有限**：仅比较 6 种冻结编码器，且全部为通用/病理自监督模型，未涉及编码器微调、多编码器融合、或更强的多模态病理基础模型（如基于图文对齐的更大模型），"表示决定上限"的结论外推需谨慎。
- **基因面板受限**：主结论建立在两个 200 基因面板上，未评估全转录组、不同面板规模或面板选择策略（如仅 HVG、仅 marker 基因）对方法排序的影响；PCC-200 与 PCC-50 的差异也提示指标选择会改变结论细节。
- **跨图块设置的前提**：SimpleP2G-cross 的邻域取自"已测量 spot"，在真实部署中仍需先对测试切片做部分 ST 测量，因而并非纯图像推断；论文未讨论在邻域稀疏或测量预算受限时的退化行为。
- **算力报告不完整**：仅给出约 1,700 A100 GPU 小时的总量与 PyTorch 2.10.0、混合精度设置，缺少 GPU 数量、单次训练/推理时长、各方法与消融的算力拆分，复现成本难以预估。
- **生物学解释较浅**：Reactome 通路富集为探索性分析，395 次 Fisher 检验未见多重比较校正说明，通路层面的结论应视为假设生成而非确证。
- **定性分析覆盖窄**：逐基因空间图仅展示 HER2ST 单折的 3 个基因（IGKC、LYZ、TFF3），不足以代表跨器官、跨平台的形态–表达对应关系。

## 9. 启示与展望

- **方法学启示**：P2G 领域的性能比较应默认采用"同方法内配对 Δ"的归因范式，并显式声明输入制度（单图块 / 跨图块 / 是否含切片级信息），否则排行榜上的提升难以区分"表示红利"与"头设计红利"。
- **实践建议**：在资源有限时，优先投资更强的病理基础模型特征与更干净的评估协议，而非复杂生成头；冻结嵌入 + 轻量解码器即可作为强基线，复杂头应在此之上证明增量价值。
- **可延伸方向**：患者级划分与多 seed 统计检验、编码器轻量微调或 LoRA 适配、全转录组与可变面板规模、邻域测量预算受限下的主动选择策略、以及将不确定性（Gaussian NLL 的方差输出）用于下游空间域识别与差异表达的可信度加权。
- **社区价值**：论文公开代码、逐折 CSV 与全部基线适配细节，配合其"先表示、后头"的主张，可作为后续 P2G 工作的事实对照基准与复现起点。

（完）
