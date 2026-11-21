---
title: Combinatorial perturbation structure enables graded inference of signaling activity by CIRCE
title_zh: 组合扰动结构使 CIRCE 能够分级推断信号传导活性
authors: "Hutchins, N. T., Maffa, S., Lu, C., Li, P."
date: 2026-11-20
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.19.767979v1.full.pdf"
tags: ["query:virtual-cell"]
score: 9.0
evidence: 扰动响应建模，可分级推断扰动身份与强度
tldr: 细胞需从外部输入推断信号活动的身份与强度，但现有扰动响应模型常把同一输入下的细胞视为离散类别，忽略响应幅度差异。CIRCE 将扰动组合编码到二值组合空间，并用随汉明距离衰减的 Boltzmann 分布替代 one-hot 监督，从而在无剂量标签下同时学习输入身份与强度。该方法保持分类准确率并改善校准，可在单细胞水平解析连续通路活性；中间分数主要反映响应状态模糊性，而非模型知识不足。在工程与天然组织中均恢复梯度活性，表明组合扰动筛选可作为自校准框架解码分级细胞响应。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 1210, \"height\": 937}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-002.webp\", \"caption\": \"\", \"page\": 4, \"index\": 2, \"width\": 2573, \"height\": 1460}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-003.webp\", \"caption\": \"\", \"page\": 5, \"index\": 3, \"width\": 1191, \"height\": 1057}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-004.webp\", \"caption\": \"\", \"page\": 7, \"index\": 4, \"width\": 1651, \"height\": 1436}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-005.webp\", \"caption\": \"\", \"page\": 14, \"index\": 5, \"width\": 2174, \"height\": 1409}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-006.webp\", \"caption\": \"\", \"page\": 15, \"index\": 6, \"width\": 1567, \"height\": 1243}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-007.webp\", \"caption\": \"\", \"page\": 16, \"index\": 7, \"width\": 1607, \"height\": 1247}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-008.webp\", \"caption\": \"\", \"page\": 17, \"index\": 8, \"width\": 1430, \"height\": 928}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-009.webp\", \"caption\": \"\", \"page\": 18, \"index\": 9, \"width\": 1430, \"height\": 1412}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-010.webp\", \"caption\": \"\", \"page\": 19, \"index\": 10, \"width\": 1035, \"height\": 967}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-011.webp\", \"caption\": \"\", \"page\": 20, \"index\": 11, \"width\": 1628, \"height\": 1264}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-012.webp\", \"caption\": \"\", \"page\": 21, \"index\": 12, \"width\": 1430, \"height\": 1294}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-013.webp\", \"caption\": \"\", \"page\": 22, \"index\": 13, \"width\": 1430, \"height\": 840}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-014.webp\", \"caption\": \"\", \"page\": 23, \"index\": 14, \"width\": 1430, \"height\": 1135}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-015.webp\", \"caption\": \"\", \"page\": 24, \"index\": 15, \"width\": 1722, \"height\": 1368}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-016.webp\", \"caption\": \"\", \"page\": 25, \"index\": 16, \"width\": 1430, \"height\": 898}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-017.webp\", \"caption\": \"\", \"page\": 26, \"index\": 17, \"width\": 1430, \"height\": 898}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-018.webp\", \"caption\": \"\", \"page\": 27, \"index\": 18, \"width\": 1430, \"height\": 898}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-11-19-767979-v1/fig-019.webp\", \"caption\": \"\", \"page\": 28, \"index\": 19, \"width\": 1795, \"height\": 1224}]"
motivation: 现有扰动响应模型将同一输入下的细胞视为离散类别，忽略响应幅度差异，难以同时推断输入身份与强度。
method: CIRCE 用二值组合空间表示扰动组合，以随汉明距离衰减的 Boltzmann 分布替代 one-hot 监督，无需剂量分辨标签。
result: 模型保持分类准确率并改善校准，可解析单细胞连续通路活性；中间分数主要反映细胞响应状态模糊性。
conclusion: 工程与天然组织中均恢复梯度活性，说明组合扰动筛选可作为自校准框架解码分级细胞响应。
---

## 摘要
细胞将外部输入解码为不同幅度的胞内活动，而推断输入的身份和强度对于细胞命运工程至关重要。然而，扰动-响应模型通常将暴露于给定输入的所有细胞视为一个离散类别，忽略了响应幅度上的细胞间差异。在此，我们提出一种结构化标签框架，可在无需剂量分辨训练标签的情况下，从组合扰动筛选中同时推断输入身份和强度。我们将每种扰动组合表示在二值组合空间中，并用随组合间汉明距离衰减的玻尔兹曼分布替代 one-hot 监督。该方法在保持分类准确性的同时改善了校准，并解析单个细胞中的连续通路活动。重要的是，中间分数主要反映细胞响应状态的不确定性，而非模型知识不足。应用于工程组织和天然组织时，校准后的模型成功恢复了分级活动。这些结果确立了组合扰动筛选作为解码分级细胞响应的自校准框架。

## Abstract
Cells decode external inputs into intracellular activities of varying magnitude, and inferring both input identity and strength is crucial for cell-fate engineering. However, perturbation-response models typically treat all cells exposed to a given input as a discrete class, ignoring cell-to-cell variation in response magnitude. Here, we introduce a structured-label framework that infers both input identity and strength from combinatorial perturbation screens without dose-resolved training labels. We represent each perturbation combination in a binary combinatorial space and replace one-hot supervision with a Boltzmann distribution that decays with the Hamming distance between combinations. This approach preserves classification accuracy while improving calibration and resolving continuous pathway activities across individual cells. Importantly, intermediate scores primarily reflect ambiguity in cellular response states rather than insufficient model knowledge. Applied to engineered and natural tissues, the calibrated model successfully recovered graded activities. These results establish combinatorial perturbation screens as a self-calibrating framework for decoding graded cellular responses.

---

## 论文详细总结（自动生成）

# 论文总结：Combinatorial perturbation structure enables graded inference of signaling activity by CIRCE

## 1. 核心问题与整体含义

- **研究背景**：细胞命运决定不仅取决于外部输入（配体）的身份，还取决于胞内响应的幅度。在胚胎发育、干细胞分化、免疫细胞分化等过程中，配体浓度梯度、细胞类型差异、通路间串扰以及细胞噪声都会导致同一输入下响应强度的显著异质性。
- **核心问题**：现有基于扰动数据的机器学习模型（如 scVI/scANVI 系谱）通常把扰动预测建模为二分类任务（扰动“存在/不存在”）或 64 类多分类任务，将所有暴露于同一输入的细胞视为一个离散类别，从而**掩盖了响应幅度的细胞间变异**，难以在目标细胞类型或中间响应状态下恢复真实的信号强度。
- **直接训练的困难**：若要显式学习扰动强度，需要覆盖多个精确测量剂量的训练标签，此类数据极为稀缺；且随着扰动通路数增加，组合与剂量的联合空间会迅速爆炸。
- **关键洞察**：组合扰动筛选本身隐含了响应幅度的信息——同一通路在不同共刺激组合中处于不同细胞环境，通路间串扰会产生一系列“有效响应强度”，即使名义标签仍是二值的。这种组合结构可以作为**内部校准尺度**。
- **整体含义**：论文提出 CIRCE（Calibrated Intracellular Response Continuum Estimation），试图把“组合扰动标签”从分类负担转变为校准来源，从而在无剂量分辨标签的条件下学习连续、分级的信号活性表示。

## 2. 方法论

### 2.1 核心思想

- 将 6 条发育信号通路（BMP、FGF、RA、SHH、TGF-β、WNT）的每种组合编码为 **6 位二值向量**，共 64 种组合。
- 用**汉明距离**（Hamming distance）度量两个组合在标签空间中的几何距离，并假设该距离与转录组响应相似性相关。
- 用随汉明距离衰减的 **Boltzmann 分布软标签**替代 one-hot 硬标签，使模型对“只错一个通路”的预测给予部分 credit，而非与完全错误的组合等同对待。

### 2.2 关键技术细节

- **软目标分布**：对观测组合 $y$，组合 $c_i$ 的目标权重为
  $$w_i = \frac{\exp(-\beta \cdot d_H(y, c_i))}{\sum_{j}\exp(-\beta \cdot d_H(y, c_j))}$$
  其中 $d_H$ 为汉明距离，$\beta$ 为逆温度参数，控制概率在观测组合周围的集中程度。
- **损失函数**：软目标与预测类别分布之间的交叉熵
  $$\mathcal{L}_{\text{Hamming}} = -\sum_i w_i \log p_i$$
- **β 设置**：可退火（从 3.0 指数退火到 10.0，先学全局几何再锐化个体组合），或固定为 3.0 / 4.0。实验显示 β=4.0 整体最优；β=3.0 因过度平滑导致准确率低、ECE 高；退火模型收敛到标准多分类损失，未受益于组合结构。
- **模型骨干**：共享的 scVI/scANVI 变分自编码器（VAE），负二项似然，批次协变量条件化解码器，ELBO 训练目标。分类器在 scVI 骨干上微调 scANVI。
- **通路得分读出**：对所有包含目标通路的组合类别概率求和（边际化），得到 0–1 之间的单通路活性分数。
- **不确定性估计**：MC dropout（推理时保留 dropout，每细胞 10 次前向）与独立初始化模型集成；用预测熵分解为**偶然不确定性**（aleatoric，单次前向平均熵）与**认知不确定性**（epistemic，总熵与偶然不确定性之差，即互信息），并用 BALD 主动学习框架验证。
- **校准评估**：期望校准误差（ECE），衡量预测概率与实际阳性频率的偏差；另用单调性（monotonicity）衡量分级分数与经典响应基因表达的一致性。

### 2.3 对比方法

- **Binary**：6 个独立二分类器，拼接输出组合预测。
- **Multiclass**：单一 64 类 softmax 分类器。
- **MultiTask**：共享潜在表示 + 6 个二分类交叉熵头。
- **Disentangled**：联合优化多分类与二分类目标。
- **CIRCE**：与多分类模型同架构，但使用 Hamming-Boltzmann 软标签目标。
- 另做了**通用标签平滑**消融（固定 ε、按汉明距离缩放 ε、按 MC dropout 熵自适应 ε），以检验增益是否仅来自一般性平滑。

## 3. 实验设计

### 3.1 数据集与场景

- **小鼠与人类胚胎干细胞组合信号筛选**（GSE289836、GSE327767；来自 Hutchins 2026 与 Yeo 2020）：6 条通路随机配体组合，固定单一浓度，scRNA-seq 覆盖 5–6 个分化批次（器官特异性间充质、内胚层、原条、早期中胚层等）。
- **小鼠原肠胚形成图谱**（GSE87038，约 13 万细胞）：作为独立外部测试集，用于评估中间分数比例。
- **微流控人内胚层前后轴（AP）图案化模型**（GSE285075）：BMP、WNT、FGF 从后侧形成连续浓度梯度，前侧由 BMP/TGF-β 抑制维持；模型在离散组合上训练，却在连续空间梯度上评估，属严格分布外测试。
- **小鼠神经管（E8.5）背腹轴（DV）**：BMP/WNT 指定背侧、SHH 指定腹侧，利用经典标志基因重建 DV 轴。
- **胚胎体节中胚层**：沿体轴变化的信号活性，作为额外验证场景。

### 3.2 Benchmark 与评估指标

- **分类性能**：精确匹配准确率（exact-match accuracy）、归一化汉明距离、通路级 accuracy / AUPRC / AUROC / F1。
- **校准**：组合级 ECE、边际化后的通路级 ECE。
- **分级性**：中间分数比例（0.1–0.9 之间的预测占比）。
- **生物学一致性**：与经典响应基因集（Table 1）表达的单调性相关，并经随机基因集零分布归一化。
- **空间梯度质量**：沿伪时间轴的梯度方向与形状、分箱内预测概率的离散度（tightness，按 Bhatia-Davis 不等式归一化的标准差）。
- **不确定性验证**：合成数据（40 基因响应块 + 200 非响应基因；标签翻转制造 aleatoric；120 基因未观测程序制造 epistemic）验证分解正确性；BALD vs 随机采样主动学习。

### 3.3 训练/测试划分

- 留一批次及其相关细胞类型作为测试集，其余批次训练，评估跨细胞类型泛化；同时报告 in-sample 随机划分结果。

## 4. 资源与算力

- **论文未明确报告 GPU 型号、数量或训练总时长**。
- 仅提供了训练超参数：VAE 骨干训练 40 个 epoch，Adam 优化器（学习率 $5\times10^{-4}$，权重衰减 $1\times10^{-5}$），batch size 64，线性 KL warm-up 3000 步，梯度裁剪 1.0；分类器微调 5 个 epoch，early stopping（patience=10），batch size 256。
- 由于使用已发表的公共数据集与相对轻量的 scVI/scANVI 骨干，算力需求推测不高，但文中未量化，无法评估其计算成本与可复现性。

## 5. 实验数量与充分性

- **实验规模**：覆盖 2 类组合筛选数据（小鼠 + 人类，多批次）、1 个独立图谱（原肠胚形成）、2 个空间梯度系统（微流控内胚层、神经管）、1 个额外体节中胚层场景；对比 5 类模型 + 3 种 β 设置 + 多种标签平滑变体；包含合成数据验证、主动学习实验、样本量饱和分析（每组合约 80 细胞后性能平台化）、邻域图分析等。
- **充分性**：整体较为充分。分类性能、校准、分级性、生物学一致性、空间梯度质量多维度评估；跨批次/跨细胞类型留出验证增强了泛化说服力；合成数据对不确定性分解的验证设计合理。
- **客观与公平性**：
  - 所有模型共享同一 scVI/scANVI 骨干与相同边际化读出，比较口径较统一；Binary 模型的架构经过交叉验证选择，多分类模型与 CIRCE 同架构，控制较好。
  - 但存在若干可讨论之处：CIRCE 的 β 为人工设定/退火，基线未获得等价的超参搜索预算；通用标签平滑消融显示部分校准增益可被简单平滑获得，说明 CIRCE 的优势幅度需谨慎解读；生物学验证主要依赖经典标志基因相关性，而非直接通路活性测量。
  - 主动学习实验显示 BALD 并不优于随机采样，作者将其解释为 aleatoric 主导的证据，但这也说明该框架在减少标注成本方面并无实际优势。

## 6. 主要结论与发现

- **组合标签具有几何结构**：组合间汉明距离与转录组距离（cosine、Euclidean、Wasserstein）显著正相关（Spearman ρ≈0.36–0.37，p<1e-60），且经共享最近邻连接性独立验证，说明组合结构编码了响应相似性信息。
- **CIRCE 改善校准且不牺牲分类性能**：在组合级与通路级 ECE 上整体最优（β=4.0），同时保持高 F1；其增益并非来自分类性能下降，而是概率质量分布更合理。
- **产生更多中间分数**：在扰动筛选与独立原肠胚图谱上，Binary 与 Multiclass 预测集中于 0 或 1，CIRCE 显著增加 0.1–0.9 区间的预测比例。
- **中间分数主要反映生物学异质性而非模型无知**：BALD 主动学习未优于随机采样；不确定性分解显示 aleatoric 占主导；中间分数伴随更高的 aleatoric 不确定性和与二值标签的偏离；中间分数与经典响应基因表达呈单调相关。
- **恢复工程化梯度**：在微流控内胚层 AP 轴上，CIRCE 从转录状态单独重建了 BMP、WNT、FGF 向后侧递增的连续梯度，方向正确，尽管训练标签中不含激动剂浓度。
- **恢复天然组织梯度**：在神经管 DV 轴上恢复 WNT/BMP 与 SHH 的反向梯度；在体节中胚层恢复沿体轴的连续信号剖面；CIRCE 在空间分箱内的预测离散度显著更小（校准更好）。
- **实验设计启示**：性能在每组合约 80 细胞后饱和，扩大组合覆盖比在已有条件中增加细胞数更有价值。

## 7. 优点

- **方法论新颖且优雅**：用汉明距离几何 + Boltzmann 软标签把“组合结构”转化为校准信号，无需剂量分辨标签，概念简洁、实现代价低，可嵌入现有 scVI/scANVI 生态。
- **问题定位准确**：明确指出二分类/多分类框架对响应幅度的掩盖，并给出可操作的替代目标函数。
- **多维度验证**：分类、校准、分级性、不确定性来源、基因

表达一致性、空间梯度重建、主动学习等，覆盖了从统计性质到生物学解释的多个层次；尤其是用合成数据验证 aleatoric/epistemic 分解、用 BALD 排除"中间分数=模型无知"这一竞争性解释，体现了较强的论证自觉。
- **生物学落地性强**：不仅在 benchmark 指标上比较，还在微流控 AP 轴、神经管 DV 轴、体节中胚层三个具有明确空间梯度的系统中检验，使"分级推断"从抽象分数变成可对照解剖学的连续图谱。
- **消融设计有针对性**：专门的通用标签平滑消融直接回应了"增益是否只是平滑"的质疑，虽未完全消除该疑问，但至少把讨论推进到可检验层面。
- **对实验社区有直接指导价值**：样本量饱和分析（每组合约 80 细胞）与"扩大组合覆盖优于增加单条件细胞数"的结论，对组合筛选的预算分配具有可操作意义。

## 8. 局限与不足

- **核心假设的强度未被充分压力测试**：汉明距离—转录组相似性的相关性虽显著，但 Spearman ρ 仅约 0.36–0.37，属中等偏弱；这意味着"组合几何"只能解释响应变异的一部分，其余部分（细胞类型、批次、噪声）可能主导。论文未系统检验当该相关性更弱（如通路高度冗余或强拮抗）时 CIRCE 是否仍稳健。
- **β 的选取缺乏原则性**：β=4.0 为经验最优，退火策略反而退化到标准多分类，说明"软标签"的有效区间较窄且依赖数据；基线模型未获得同等超参搜索预算，公平性存在折扣。
- **增益幅度有限且部分可被简单平滑复现**：通用标签平滑消融显示部分校准改善可由固定 ε 平滑获得，说明 CIRCE 的独特贡献需要更精细的分解（几何结构 vs. 一般正则化）。
- **"分级"的验证依赖相关而非因果**：单调性检验使用经典标志基因表达作为参照，而非直接的蛋白磷酸化、通路报告基因或剂量响应测量；因此"恢复了信号强度"更准确的表述是"恢复了与经典响应程序一致的连续变异"。
- **空间梯度验证为定性/半定量**：AP 轴、DV 轴的方向正确性与离散度指标有说服力，但缺少与真实配体浓度分布的定量比对（如免疫染色或 FRET 报告），梯度形状的正确性未被外部标定。
- **不确定性框架的实用价值未兑现**：BALD 不优于随机采样，作者归因于 aleatoric 主导，但这同时意味着该方法在主动学习/降低标注成本场景下没有实际收益，相关讨论略显防御性。
- **算力与可复现性信息缺失**：未报告 GPU 资源、训练时长、随机种子数量与超参搜索范围，限制了独立复现与成本评估。
- **仅覆盖 6 条通路的固定浓度筛选**：结论向其他通路、其他浓度区间、扰动（CRISPR/药物）模态的外推性未知；64 类组合在多通路扩展时会面临类别数指数增长的问题，论文未讨论该扩展路径。

## 9. 启发与展望

- **"把标签结构当监督信号"的范式可迁移**：任何具有组合/层级/序数结构的扰动标签（如多基因敲除、药物联用、剂量阶梯）都可能存在类似的几何先验，可用距离核软标签替代 one-hot，这一思路不限于发育信号通路。
- **软标签的核函数选择值得系统研究**：本文用汉明距离 + Boltzmann 核，未来可考虑学习得到的嵌入距离、通路间先验相似性（如通路串扰网络）或数据驱动的邻域图，从而突破"标签几何 = 响应几何"这一较强假设。
- **分级读出可作为空间转录组与谱系追踪的分析工具**：若能恢复连续通路活性，可用于重建发育轨迹上的信号梯度、识别响应阈值与细胞命运分叉点。
- **与机制模型耦合**：将 CIRCE 的连续通路分数作为输入，拟合剂量—响应或通路串扰的动力学模型，可能弥补纯数据驱动方法缺乏机制解释的短板。
- **不确定性分解的应用方向**：尽管 BALD 未奏效，aleatoric 主导的结论本身有生物学含义——中间分数可能反映真实的细胞状态异质性，可作为识别"亚群混合"或"响应过渡态"的无监督指标。

## 10. 总体评价

本文针对组合扰动筛选中"标签二值化掩盖响应幅度"这一被普遍忽视的问题，提出了一个概念简洁、实现成本低的解决方案：利用组合标签的汉明几何构造 Boltzmann 软目标，使分类器在无剂量标签条件下输出连续、经校准的通路活性分数。其贡献主要在于**问题重构**（把组合结构从分类负担转为校准尺度）与**多系统验证**（合成数据、组合筛选、独立图谱、工程化与天然空间梯度），而非单纯的性能提升——事实上分类性能与基线相当，校准与分级性的改善幅度中等且部分可被简单平滑复现。

论文最有力的证据是空间梯度重建：模型仅在离散组合上训练，却能在微流控 AP 轴与神经管 DV 轴上输出方向正确的连续梯度，且分箱内离散度更小，这为"分级推断具有生物学真实性"提供了较强的旁证。相对薄弱的环节是核心几何假设的中等相关性、β 的经验性、以及"分级=信号强度"缺乏直接生化标定。

总体而言，这是一篇方法论上有巧思、验证上较扎实、但优势幅度需谨慎解读的工作。它更适合被定位为"为组合扰动数据提供一个更合理的概率读出层"，而非"解决了信号强度推断问题"；其真正价值可能在于启发社区重新审视扰动标签中未被利用的结构信息。

（完）
