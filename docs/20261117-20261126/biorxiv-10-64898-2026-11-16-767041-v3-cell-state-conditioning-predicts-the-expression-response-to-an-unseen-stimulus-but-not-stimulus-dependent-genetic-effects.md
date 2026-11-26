---
title: Cell-state conditioning predicts the expression response to an unseen stimulus but not stimulus-dependent genetic effects
title_zh: 细胞状态条件化可预测对未见刺激的表达响应，但不能预测刺激依赖的遗传效应
authors: "He, H., Sun, J., Xu, J., Abudureyimu, M., Yang, Y., Huang, Y., Wang, Z., Xia, Q., Wang, S."
date: 2026-11-25
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.16.767041v3.full.pdf"
tags: ["query:virtual-cell"]
score: 9.0
evidence: 通过细胞状态条件化预测未见刺激的表达响应
tldr: 二代序列模型可将单细胞快照作为细胞状态条件输入，但该条件能否携带真实实验扰动尚未被检验。作者以干扰素-β刺激与未刺激的单核细胞为条件，检验预测表达响应是否与实测一致，并考察能否识别刺激特异eQTL。预测与实测响应在119个基因上Spearman ρ=0.616，删除全部靶基因后仍有0.607；但刺激特异的遗传效应缺乏可靠证据。结论是条件传递的是细胞状态而非扰动机制，表达层面可迁移、变异效应层面不可迁移。
source: biorxiv
selection_source: fresh_fetch
motivation: 检验以单细胞快照为条件的序列模型能否携带真实实验扰动，而非仅反映细胞状态标签。
method: 用已发表实验中干扰素-β刺激与未刺激的单核细胞（与测量细胞不重叠）作条件，比较预测与实测表达响应，并做刺激特异eQTL分析。
result: 119个基因上ρ=0.616，删除靶基因后0.607；15种条件的响应随真实生物学重叠度缩放（斜率0.73）；刺激特异遗传效应无证据，p由0.0019升至0.443。
conclusion: 条件传递细胞状态而非扰动机制：状态间在表达层面可迁移，在变异效应层面不支持，需建立分离两者的评估框架。
---

## 摘要
背景：第二代序列模型可以以单细胞快照提供的细胞状态为条件，而非从固定目录中选择，但这种条件化是否携带实验施加的扰动尚未被检验。结果：我们以已发表实验中的干扰素-β刺激和未刺激单核细胞对此类模型进行条件化，所用细胞与提供测量的细胞不重叠，并考察预测表达响应是否与实测响应一致，以及同一条件化是否识别出刺激状态特异的表达QTL。在119个基因上，预测响应与实测响应一致，Spearman ρ = 0.616（95% CI 0.486至0.716）；从条件化输入中删除全部119个目标基因后为0.607。在15种条件下，模型响应随每种条件生物学与目标响应的真实重叠程度而缩放（斜率0.73，Pearson 0.92），一个近邻单核细胞亚群得到0.295，而实测重叠为0.336。对于刺激特异性遗传效应，我们未发现可靠证据：一旦要求两种条件都必须具有可测量的预测效应，预先设定的主要分析臂的p值从0.0019变为0.443，且分离定位于静息条件基线。两代模型的目录均不含受扰动样本——4,430条轨迹中0条、2,799种条件中0种——尽管两者都带有激活状态标签，因此缺口在于实验扰动而非细胞状态。两项附带发现适用于本模型之外：可信集成员资格错误标记了超过一半的推定条件特异位点；以比值统计量中较大项作为门控会制造信号。结论：因此，条件化传递的是状态而非机制：状态间迁移在表达水平上得到支持，在变异效应水平上未得到支持；在声称二者任一之前，需要一种将两者分开的评估。

## Abstract
Background: Second-generation sequence models can be conditioned on a cell state supplied as a single-cell snapshot rather than selected from a fixed catalogue, but whether that conditioning carries an experimentally applied perturbation has not been tested. Results: We conditioned such a model on interferon-{beta}-stimulated and unstimulated monocytes from a published experiment, using cells disjoint from those providing the measurement, and asked whether the predicted expression response tracks the measured one and whether the same conditioning identifies expression QTL specific to the stimulated state. Predicted and measured responses agree at Spearman {rho} = 0.616 across 119 genes (95% CI 0.486 to 0.716), and at 0.607 after all 119 target genes are deleted from the conditioning input; across fifteen conditions the model's response scales with how much each condition's biology genuinely overlaps the target response (slope 0.73, Pearson 0.92), and a near-neighbour monocyte subset receives 0.295 against a measured overlap of 0.336. For stimulation-specific genetic effects we find no reliable evidence: the pre-specified primary arm moves from p = 0.0019 to 0.443 once both conditions must carry a measurable predicted effect, and the separation localises to the resting-condition baseline. Neither model generation's catalogue contains a perturbed sample, 0 of 4,430 tracks and 0 of 2,799 conditions, although both carry activation-state labels, so the gap is experimental perturbation rather than cell state. Two incidental findings apply beyond this model: credible-set membership mislabels over half of putatively condition-specific loci, and gating a ratio statistic on its larger term manufactures signal. Conclusions: Conditioning therefore conveys the state but not the mechanism: transfer between states is supported at the level of expression and unsupported at the level of variant effect, and an evaluation that separates the two is needed before either is claimed.

---

## 论文详细总结（自动生成）

# 论文结构化总结

## 1. 核心问题与整体含义

- **背景**：序列到功能模型（如 AlphaGenome）可直接从 DNA 序列预测调控活性（染色质可及性、基因表达）。第一代模型只能预测训练数据中固定的细胞类型与检测；2026 年底发布的第二代模型（AlphaGenome 2 等）允许用户以**单细胞表达谱**作为细胞状态条件输入，从而对训练目录之外的细胞状态进行预测。
- **核心问题**：这种"细胞状态条件化"能否携带**实验施加的扰动**——即 (a) 能否复现对未见刺激（干扰素-β）的表达响应；(b) 同一条件化能否识别**刺激状态特异的遗传效应**（response eQTL）。
- **研究动机**：大量免疫学问题关注扰动状态（细胞因子、病原体、药物响应）以及仅在刺激后显现的调控变异；response eQTL 研究已表明相当比例的遗传效应受刺激修饰，而参考目录主要来自未扰动组织。
- **关键概念区分**：条件是从表达谱学到的表示，描述"状态平均看起来如何"，而非"状态如何改变个体变异的后果"。因此**表达层面的状态迁移**与**变异效应层面的状态迁移**必须分开检验。

## 2. 方法论

### 核心思想
- 用单细胞快照构建"刺激态/静息态"条件，输入 AlphaGenome 2，比较预测的 log2 倍数变化与实测响应；再用同一对条件预测 eQTL 变异的效应，检验能否区分刺激特异与静息特异位点。

### 关键技术细节
- **条件构建**：每个条件取 256 个细胞（编码器上限），每库用 `default_rng(7)` 无放回抽取一次；少于 256 的群体（巨核细胞 122/134、树突状细胞 203/228）全部使用。
- **预测**：使用去噪单细胞基因表达头，200 kb 平均掩码；预测 log2FC = log2((刺激态活性+1)/(静息态活性+1))，实测响应 = log2((刺激 CPM+1)/(对照 CPM+1))。
- **输入区间**：取前 1,500 个表达基因中基因数最多的 40 个 1,048,576-bp bin，以 bin 中点为中心（因计数矩阵按染色体长度排序，全部落在 1–7 号染色体和 X）。
- **活性过滤**：两状态中较大预测活性 > 1，得到 119 个分析基因（分布于 35 个区间）。
- **基因 held-out**：将 119 个分析基因作为列从单细胞矩阵删除（35,635→35,516），重建条件并重新打分。
- **校准分析**：15 个条件（7 个未刺激、7 个刺激后、1 个匹配态），每点计算"该状态相对未刺激 CD14+ 的 log 比值"与"实测 IFN-β 响应"的 Spearman 相关，对模型值做 OLS 拟合；用分半法估计测量轴可靠性（0.967→Spearman–Brown 全样本 0.983），做误差校正（disattenuated slope）。
- **不确定性**：窗口聚类 bootstrap（2,000 次，seed 0，35 个 1 Mb 窗口）；split-half null（50 次）；深度匹配二项稀疏化（20 次）。
- **eQTL 分析**：从 eQTL Catalogue release 8 取 SuSiE fine-mapped eQTL；严格标签 = 仅进入某一条件 credible set，且另一条件全 summary statistics 中 |z| < 2，方向一致；检验统计量为 log2(刺激态绝对预测效应/静息态绝对预测效应)；可见性门控 max(A,B) > 0.1；双侧 Mann–Whitney；有界指数 (A−B)/(A+B) 报告效应量。
- **分析计划**：版本化文件 + 本地 SHA-256 哈希链（无外部注册），版本 1（11 月 13 日）指定 Fairfax IFN-γ 为主分析，版本 2（11 月 14 日）改为秩和检验、严格标签、0.1 可见性阈值并加入 4 个 Quach 复制臂；后续补充 A–D，所有偏离均记录。

## 3. 实验设计

### 数据集与场景
- **表达数据**：GSE96583 batch 2（Kang et al. 2018），8 名系统性红斑狼疮患者的 PBMC，未刺激与 IFN-β 刺激 6 小时；仅用 singlet，按细胞类型与文库合并计数。
- **条件细胞与测量细胞完全不重叠**：测量响应用 2,529 个未刺激 + 2,334 个刺激 CD14+ 单核细胞（已剔除 256 个条件细胞），文库深度 5.63M / 5.76M counts。
- **eQTL 数据**：两个单核细胞刺激研究——Fairfax 2014（IFN-γ、LPS 24h、LPS 2h）与 Quach 2016（流感、LPS、R848、Pam3CSK4），共 7 个刺激臂。

### Benchmark 与对照
- **split-half null**：将对照细胞对半分为两个"条件"，50 次抽样均值 ρ = +0.027（SD 0.229），无一达到观测值。
- **深度匹配对照**：将不相交计数二项稀疏化到早期共享细胞分析的深度（557,000 counts），20 次得 ρ = 0.434 ± 0.053，用于分解"共享细胞"与"测序深度"的贡献。
- **第一代模型对照**：在无刺激态 track 的 CD14+ 单核细胞 RNA track 与 DNase track 上重复位点比较。
- **错配条件对照**：改用 CD4 T 或 B 细胞作条件。
- **placebo splits、leave-one-out、移除两研究共享位点、更严格标签阈值**。
- **目录关键词搜索**：4,430 条第一代 track、2,799 个第二代条件，窄/宽两套关键词。
- **未直接对比的基线**：作者指出未与 scGen 等扰动响应模型或简单线性基线做直接比较。

## 4. 资源与算力

- **文中未提及任何 GPU 型号、数量或训练时长**。模型预测通过公共 API（AlphaGenome Python SDK v2.0.0）于 2026 年 11 月 13–16 日获取，属于**推理调用**而非本地训练，因此无训练算力信息。
- 分析代码与派生表格已公开（GitHub + Zenodo v1.1.0），可供复算而无需访问模型。

## 5. 实验数量与充分性

### 实验规模
- **表达层面**：主比较（119 基因）、去除 10 个最大响应基因、全基因 held-out、深度匹配稀疏化（20 次）、split-half null（50 次）、15 条件校准、分半可靠性估计（20 次）。
- **位点层面**：7 个刺激臂 × 4 种可见性门控（流感臂详列于表 2，全部臂见附表 S4），外加 leave-one-out、placebo split、共享位点移除、严格阈值等稳健性检验。
- **标签验证**：Fairfax 1,506 行、Quach 3,627 行逐一在另一条件 summary statistics 中核查。

### 充分性与公平性评价
- **表达层面较充分**：多重 null 与对照设计合理，held-out 实验巧妙；但仅一个细胞类型、一个刺激、一个数据集、119 个基因、仅 1–7 号染色体和 X。
- **校准分析**：15 个条件来自同一数据集、相关于同一实测响应，**不是独立重复**，且为事后探索性分析。
- **位点层面明显欠功效**：严格标签后每臂仅几十个可见位点，部分组仅 6–7 个，最小项门控下仅 2 个/组。
- **公平性问题**：错配细胞类型对照因预测崩溃而无信息；未做 donor-disjoint split；eQTL 臂均非 IFN-β，条件不匹配。
- **透明度较高**：分析计划版本化、偏离逐条记录、独立重算、72 个数值自动核对无差异；但部分阈值（如 z 分数验证标准）是在看到结果后修改的。

## 6. 主要结论与发现

- **表达响应可迁移**：119 基因上预测与实测 log2FC 的 Spearman ρ = 0.615（95% CI 0.486–0.716）；去除最大响应基因后 ρ = 0.563；删除全部靶基因后 ρ = 0.607，且与原预测相关 0.989——预测**不依赖靶基因自身的表达值**。
- **响应随状态相似度缩放**：15 个条件上模型值对实测重叠的回归斜率 0.728（误差校正后 0.741），Pearson 0.923，截距与零无异；平均恢复约 3/4 的秩结构。近邻的 FCGR3A+ 单核细胞得 0.295（实测重叠 0.336）。
- **系统性偏差**：刺激的 T/NK 三态是仅有的三个负残差（置换 p = 0.029），提示对这类状态会**低估**响应；刺激巨核细胞残差最大（+0.152，仅 134 个细胞）。
- **刺激特异遗传效应无可靠证据**：预设主分析（Fairfax IFN-γ）不确定（p = 0.096）；4 个复制臂中仅流感显著（p = 0.0019，四臂校正后 0.0076），但该差异来自**静息条件基线**（两组静息态预测 p = 0.00373，刺激态 p = 0.144），要求两条件均有可测量效应后 p = 0.443。
- **两个通用方法学陷阱**：
  - 以 credible-set 成员定义条件特异：71.5%（Fairfax）和 75.9%（Quach）的"条件特异"位点在另一条件 |z| ≥ 2；
  - 对**比值统计量按较大项门控**会放任分母接近检测下限，把基线差异伪装成条件依赖（经典比值变量问题）。
- **目录缺口**：两

- **目录缺口**：两代模型的目录覆盖均偏窄。第一代 4,430 条 track 中，窄关键词仅命中少量干扰素/刺激相关 track；第二代 2,799 个条件中，以“IFN”“stimulat”“cytokine”等检索，窄口径几乎为空，宽口径也仅覆盖少数组织与刺激组合。换言之，**刺激态条件在现有目录中基本缺席**，用户必须自备单细胞谱才能提出此类查询——这既是条件化接口的价值所在，也是其可用性的现实瓶颈。
- **总体判断**：表达层面的状态迁移**得到支持**（中等强度、可重复、不依赖靶基因表达），但**变异效应层面的状态迁移未获可靠证据**；唯一看似显著的复制臂在拆解后归于静息基线差异，而非刺激特异效应。

## 7. 局限、偏差与启示

### 作者承认的局限
- 单一数据集、单一细胞类型（CD14+ 单核细胞）、单一扰动（IFN-β 6 小时），外部效度有限。
- 分析基因仅 119 个，且因计数矩阵排序而集中于 1–7 号染色体与 X，存在**染色体覆盖偏倚**。
- eQTL 复制臂中无 IFN-β 臂，条件与标签来源不匹配，只能作为"跨刺激可迁移性"的弱检验。
- 校准分析为事后探索，15 个条件非独立重复。
- 未与 scGen、线性基线等扰动预测方法直接比较，无法定位该方法在现有工具谱系中的相对位置。

### 审稿视角的额外问题
- **统计功效与多重性**：位点层面每组仅数十个可见位点，Mann–Whitney 在小样本下对效应量估计极不稳定；四臂校正虽已做，但主分析 p = 0.096 被表述为"不确定"而非阴性，结论措辞需更谨慎。
- **标签定义的循环性风险**：用 credible set 成员与另一条件 |z| < 2 共同定义"条件特异"，而后者恰是待检验的对比维度之一，虽方向一致要求有所缓解，但仍可能引入选择偏倚；71.5%/75.9% 的"伪条件特异"比例说明该标签在真实数据中噪声很大。
- **比值统计量的固有缺陷**：log2(刺激态/静息态) 在分母趋零时方差爆炸，可见性门控 max(A,B) > 0.1 并不能消除该问题，反而系统性富集"一高一低"的位点，这正是作者自己指出的陷阱——但论文的补救（要求两条件均有可测量效应）使样本量骤降，功效随之崩塌。
- **"预测不依赖靶基因表达"的解读**：held-out 后预测相关 0.989 是有力证据，但也可能反映模型主要依赖**局部染色质/序列特征**而非细胞状态表示，从而削弱"条件化真正起作用"的论断；论文未做消融来区分"状态条件贡献"与"序列先验贡献"。
- **条件构建的稳健性未检验**：每库固定 256 细胞、单次 `default_rng(7)` 抽样，未报告不同抽样种子或不同细胞数下的方差，条件表示的稳定性缺乏量化。

### 对领域的启示
- **必须区分两类"状态迁移"**：表达谱层面的响应预测与变异效应层面的响应预测是不同难度的任务，前者可迁移不代表后者可迁移；评估条件化模型时应分别设立 benchmark。
- **条件表示是"状态指纹"而非"扰动算子"**：从静息/刺激快照学到的差异，编码的是状态间的平均差异，缺少"干预如何改变系统"的因果结构，因此难以外推到遗传效应的修饰。
- **eQTL 条件特异性的标注需要更严格的标准**：仅凭 credible set 成员判定会高估条件特异位点比例，建议结合两条件的完整 summary statistics、方向一致性与效应量阈值联合定义。
- **比值型检验统计量应慎用**：在低表达/低可及性位点上，比值会放大基线差异；更稳健的做法是在两条件下分别建模效应并检验交互项（如条件 × 基因型），或使用有界效应量并报告完整分布。
- **数据基础设施是瓶颈**：现有模型目录对刺激态覆盖极低，若要让条件化接口真正服务于免疫学与药物基因组学问题，需要在训练/目录层面系统性纳入扰动图谱（如 CITE-seq 刺激面板、 Perturb-seq 类数据）。

## 8. 一句话总结

该论文以 Kang IFN-β 单细胞数据构建刺激/静息条件输入 AlphaGenome 2，证明**表达层面的扰动响应可以中等强度地跨状态迁移（ρ ≈ 0.6，约恢复 3/4 的秩结构）**，但**未能证明同一条件化能识别刺激特异的遗传效应**——唯一显著信号经拆解归于静息基线差异，并由此提炼出 credible-set 标签高估与比值统计量门控两个通用方法学陷阱。

（完）
