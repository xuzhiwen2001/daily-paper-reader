---
title: Mapping whole-tissue spatial multi-omics at single-cell resolution with STEP
title_zh: 利用STEP在单细胞分辨率下绘制全组织空间多组学图谱
authors: "Hu, Z., Zhu, Z., Cai, L., Zhan, Y., Yan, X., Wang, Z., Chen, J., Sun, B., Jiang, S., Du, S., Wang, H., Li, X., Wang, F., Wang, G., Zou, Q., Du, Y., Yuan, Z., Zhang, Y."
date: 2026-11-20
pdf: "https://www.biorxiv.org/content/10.1101/2024.11.22.624797v2.full.pdf"
tags: ["query:spatial-gene"]
score: 8.0
evidence: 整合组织学图像与空间转录组、单细胞数据进行全切片分子图谱映射
tldr: 空间多组学常聚焦实测区域的聚类或域识别，尚缺单细胞分辨率下整张切片（含未测区域）跨组学映射的通用框架。STEP将概率推断与深度学习结合，灵活整合组织学、空间转录组、单细胞和多组学数据。它支持Xenium、CITE-seq与成像质谱流式三模态整合，并用六张低分辨率切片重建3D多组学脑细胞图谱。该框架为低成本探索空间生物学提供了互补模态整合工具。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-1101-2024-11-22-624797-v2/fig-001.webp\", \"caption\": \"\", \"page\": 39, \"index\": 1, \"width\": 1219, \"height\": 1453}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-1101-2024-11-22-624797-v2/fig-002.webp\", \"caption\": \"\", \"page\": 40, \"index\": 2, \"width\": 1123, \"height\": 1536}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-1101-2024-11-22-624797-v2/fig-003.webp\", \"caption\": \"\", \"page\": 41, \"index\": 3, \"width\": 1123, \"height\": 1536}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-1101-2024-11-22-624797-v2/fig-004.webp\", \"caption\": \"\", \"page\": 42, \"index\": 4, \"width\": 1123, \"height\": 1536}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-1101-2024-11-22-624797-v2/fig-005.webp\", \"caption\": \"\", \"page\": 43, \"index\": 5, \"width\": 1123, \"height\": 1536}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-1101-2024-11-22-624797-v2/fig-006.webp\", \"caption\": \"\", \"page\": 44, \"index\": 6, \"width\": 1148, \"height\": 1586}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-1101-2024-11-22-624797-v2/fig-007.webp\", \"caption\": \"\", \"page\": 45, \"index\": 7, \"width\": 1123, \"height\": 1536}]"
motivation: 现有空间多组学方法偏重实测区域的聚类或域识别，缺少单细胞分辨率下整张切片跨组学层映射的通用框架。
method: STEP融合概率推断与深度学习，灵活整合组织学、空间转录组、单细胞及多组学数据，实现实测与未测区域的单细胞分辨率映射。
result: STEP完成Xenium、CITE-seq和成像质谱流式三模态整合，并由六张低分辨率空间转录组切片重建3D多组学脑细胞图谱。
conclusion: STEP提供低成本、通用的空间多模态整合工具，可借助互补组学数据在整张组织切片上探索空间生物学。
---

## 摘要
空间组学技术彻底改变了我们在组织背景下绘制转录组、蛋白质组或代谢组图谱的能力。然而，现有的空间多组学方法侧重于从实测图谱中进行聚类或区域识别，仍缺乏一个能够在单细胞分辨率下跨额外组学层面对实测和未实测区域进行全切片绘制的通用框架。在此，我们提出STEP，一个将概率推断与深度学习相结合的计算框架，可灵活整合组织学、空间分辨转录组学（SRT）、单细胞和/或多组学数据。我们在多种应用中验证了STEP的优势。此外，STEP能够实现Xenium、CITE-seq和成像质谱流式的三模态整合，从而基于一个小基因面板绘制全转录组范围的基因表达和蛋白质图谱。通过SRT、组织学、单核RNA测序和inCITE-seq的四模态整合，STEP从六张低分辨率SRT切片重建了一个3D多组学脑细胞图谱。总体而言，STEP通过整合多种互补模态，为探索空间生物学提供了一种经济有效的工具。

## Abstract
Spatial omics technologies have revolutionized our ability to map transcriptomic, proteomic, or metabolomic profiles within tissue contexts. However, existing spatial multi-omics approaches emphasize clustering or domain identification from measured profiles, while a general framework for whole-slice mapping in measured and unmeasured areas at single-cell resolution across additional omics layers remains lacking. Here we introduce STEP, a computational framework that integrates probabilistic inference with deep learning for flexible integration of histology, spatially resolved transcriptomics (SRT), single-cell, and/or multi-omics data. We validated STEP's advantages across diverse applications. Furthermore, STEP enables tri-modal integration of Xenium, CITE-seq, and imaging mass cytometry to map transcriptome-wide gene expression and protein profiles from a small gene panel. Through quadra-modal integration of SRT, histology, single-nucleus RNA sequencing, and inCITE-seq, STEP reconstructs a 3D multi-omics brain cell atlas from six low-resolution SRT sections. Collectively, STEP provides a cost-effective tool for exploring spatial biology by integrating diverse, complementary modalities.

---

## 论文详细总结（自动生成）

# STEP 论文结构化总结

## 1. 核心问题与整体含义

- **背景**：空间组学（Spatial Omics）可在组织原位绘制转录组、蛋白质组或代谢组图谱，是理解细胞组织方式、功能与相互作用的关键手段。理想目标是"在单细胞分辨率下、跨多张切片、高效构建全组织多组学图谱"。
- **现有技术瓶颈**：
  - 测序类 SRT（如 10x Visium）覆盖全转录组，但每个 spot 含多个细胞，缺乏单细胞分辨率；部分高分辨率平台存在分子横向扩散或无法覆盖整张切片的问题。
  - 成像类 SRT（如 MERFISH、osmFISH）具备单细胞分辨率，但受限于预设基因面板，且循环成像耗时长。
  - scRNA-seq 提供完整单细胞转录组，但丢失空间信息。
  - 真正的空间多组学实验成本高、技术复杂，难以大规模推广。
- **现有计算方法局限**：
  - 多数方法只做**两两模态整合**（基因填补、反卷积、超分辨、组织学预测表达等），未充分利用跨模态互补信息。
  - 空间域识别方法只做 niche 发现，不推断缺失模态，也不生成全切片单细胞图谱。
  - 已有三模态工作常忽略组织学图像；OmiCLIP 仅做 patch 级双模态对齐，无单细胞分辨率与多组学融合。
- **论文定位**：提出 **STEP**，一个平台无关、可灵活组合的"超模态（hyper-modal）"计算框架，目标是在单细胞分辨率下，对**实测区与未测区**同时完成跨组学层的全切片映射。

---

## 2. 方法论

### 2.1 核心思想
将**概率推断**与**深度学习**混合：先用概率模型在已测区域内把 SRT 信号"分配"到分割出的单细胞，再用图注意力网络把信息扩散到未测区域，最后借助单细胞/多组学参考做全转录组或多组学增强。框架按输入模态动态启用模块，支持双模态、三模态、四模态配置。

### 2.2 流程与关键技术

**（1）数据预处理**
- 用 QuPath + StarDist（MoNuSeg 预训练权重）做 H&E 细胞核分割，并扩展为细胞掩膜，提取形态学特征（形状、颜色光学密度等）；大图分块（2000×2000，含 100 像素重叠边距）处理以避免细胞被切断。
- 基于 DEG 筛选信息基因。
- 用**条件变分自编码器（CVAE）**做生成式域适应，消除 SRT 与单细胞参考之间的平台效应；通过从单细胞参考生成"伪 spot"、混合真实 spot 来对齐两种条件的细胞类型组成分布。

**（2）Cell Identification（细胞识别）**
- 建立**泊松分布推断模型**：spot 的 UMI 计数服从 Poisson，其相对表达由各细胞按面积占比贡献叠加，并加入 spot 特异效应与随机噪声。
- 不同于 RCTD/SpatialScope 假设同类型细胞表达完全相同，STEP 用**逐细胞相对表达**替代平均签名矩阵，并引入形态学特征回归项（`log(λ) = Σ one-hot·S + Σ 形态特征·β`）。
- 对形态-基因关联系数 β 施加 **spike-and-slab 先验**（伯努利变量控制是否激活 + 正态 slab），实现稀疏化，缓解多重共线性与过拟合。
- 引入 **Potts 空间先验**：相邻且形态相似的细胞更可能同类型，用形态相似度加权邻居标签一致性。

**（3）Spatial Diffusion（空间扩散）**
- 以细胞空间坐标为节点、K 近邻为边构图，节点特征为形态学特征。
- 用**多头图注意力网络（GAT）**做半监督学习，以已识别细胞类型为标签，将标签"扩散"到未测区域细胞；由于 GAT 可适应动态图拓扑，训练好的模型可迁移到同组织的其他切片甚至不同患者切片。

**（4）Omics Enhancement（组学增强）**
- 对每个空间细胞，在单细胞参考中取 K 近邻（余弦距离），仅保留余弦相似度为正的邻居，按归一化权重加权平均得到全基因表达（公式 10–11）。
- 再做**空间校正**：用相邻 spot 的高斯核（尺度 σ 固定为 0.1）计算局部表达，作为缩放因子修正单细胞表达，保证空间连续性。
- 多组学场景下该策略可直接推广到其他组学对：一个模态定义细胞相似性，另一模态据此映射。

---

## 3. 实验设计

### 3.1 数据集与场景
| 场景 | 数据 |
|---|---|
| 胰腺导管腺癌（PDAC-A/B） | Spatial Transcriptomics（spot 级、全转录组、H&E）+ InDrop scRNA-seq |
| 乳腺癌 BRCA-A/B1/B2 | 10x Visium + 多套 scRNA-seq 参考（10x Chromium ×2、InDrop）；另用 Xenium 数据构造 Visium 式伪 spot 做补充基准 |
| 结直肠癌 | Xenium 伪 spot 基准（含非配对 scRNA-seq 参考）、Visium HD（12.4 万→42.7 万细胞） |
| 小鼠皮层 | 10x Visium 连续切片 + scRNA-seq；MERFISH（MOp、Moffit）、osmFISH（AllenSSp、Zeisel） |
| 三模态整合 | 人乳腺癌 Xenium + CITE-seq + 成像质谱流式（IMC） |
| 四模态 3D 图谱 | 小鼠脑 35 张冠状切片（Spatial Transcriptomics）+ snRNA-seq + inCITE-seq，仅用 6 张切片训练 |
| 大规模可扩展性 | Visium HD、MERSCOPE（71.3 万细胞） |

### 3.2 Benchmark 与对比方法
- **spot 级反卷积**：SpaDecon、CellDART、CARD、Cell2location。
- **单细胞级识别**：STIE（1.0×/2.5×）、SpatialScope。
- **超分辨基因预测**：BayesSpace、SpatialScope、iStar、XFuse。
- **基因填补**：gimVI、Seurat、SpaGE。
- **评价指标**：ARI、ACC、NMI、F1、MSE、PCC、SPCC、Spearman 相关、sACC、Moran's I / Geary's C、Cohen's d、重叠系数等。
- **验证策略**：spot masking（掩蔽率至 0.7）、跨切片/跨患者迁移、留一基因（leave-one-gene-out）填补、与 Allen Brain Atlas ISH 图像比对、UMAP/热图/空间可视化定性比较。
- **统计检验**：Mann–Whitney U、单侧 Wilcoxon 秩和检验、FDR 校正（FDR < 0.05）、Fisher 合并 p 值。

---

## 4. 资源与算力

- 文中明确说明：实验在 **Ubuntu 服务器**上完成，配置为 **2 块 AMD EPYC 7763 64 核处理器、503 GiB 内存、单张 NVIDIA GeForce RTX 4090（24 GB）GPU**。
- **未报告**具体训练时长、各模块的 GPU 小时数或能耗；也未给出不同数据集上的推理耗时对比。
- 软件环境：Python 3.10.14、QuPath 0.5.1、StarDist 扩展 0.5.0，其余依赖版本列于补充表 6。

---

## 5. 实验数量与充分性

### 5.1 实验规模（粗略统计）
- **主基准**：PDAC（细胞识别 + 基因预测）、BRCA-A（细胞识别 + 基因预测）、Xenium 伪 spot（乳腺癌 + 结直肠癌）——约 4 组独立基准。
- **鲁棒性消融**（BRCA-A 为主）：
  - 3 套不同 scRNA-seq 参考（10x Chromium ×2、InDrop）；
  - 随机丢弃 30% 基因（保留 >92% 性能）；
  - 参考细胞类型的合并/删除/细分/不平衡扰动；
  - 模拟不同 spot 尺寸与稀疏度的 SRT；
  - 不同组织学风格与特征表示（含虚拟冷冻切片）。
- **未测区域重建**：不同 mask 率、相邻切片迁移、跨患者迁移——约 3–4 组。
- **跨平台应用**：Visium 小鼠皮层（含仅 H&E 的相邻切片迁移）、MERFISH（2 数据集）、osmFISH（2 数据集）留一基因填补——共 4 组填补基准。
- **大规模可扩展性**：Visium HD、MERSCOPE——2 组。
- **多模态整合**：三模态（Xenium+CITE-seq+IMC）1 组、四模态 3D 图谱 1 组（含 6/35 切片训练对比）。
- 另有大量补充图（Supplementary Figs. 1–93）支撑。

### 5.2 充分性与公平性评估
- **充分性较高**：覆盖多种平台（测序类/成像类）、多种组织（胰腺、乳腺、结直肠、脑）、多物种（人/鼠）、多分辨率与多组学层，且专门设计了参考扰动、基因缺失、分辨率变化等敏感性分析，鲁棒性论证较扎实。
- **客观性措施**：使用公开数据集与官方注释；统计检验含 FDR 校正；重复运行 5 次；伪 spot 基准以原始 Xenium 注释为 ground truth。
- **潜在公平性问题**：
  - PDAC/BRCA 缺乏真实单细胞级注释，评价依赖**区域级 H&E 标注**（参照 CARD 做法将细胞标签粗化到区域），这对单细胞级方法（STEP、STIE、SpatialScope）与 spot 级反卷积方法的比较口径不完全对等。
  - 部分对比方法"因算法限制或缺少功能设计"无法在大规模数据上运行，导致这些场景下缺少完整横向比较。
  - 三模态/四模态整合缺乏同组织、同切片的真实多组学 ground truth，主要以与相邻切片 Visium、IF 图像、Allen Atlas 的一致性做间接验证。

---

## 6. 主要结论与发现

1. **细胞识别更优**：在 PDAC 与 BRCA 上，STEP 在多项指标上优于 spot 级反卷积与单细胞级推断方法；能刻画精细边界（如胰腺腺泡细胞）、捕获稀有细胞（ductal high-hypoxic 仅占 1.21%，沿癌区外周分布）、区分 cancer clone A/B 亚区，并对染色伪影稳健。
2. **形态学一致性**：STEP 识别的癌细胞形态特征显著区别于其他类型（嗜酸性光密度 Cohen's d=0.699，核质面积比 d=0.512，p<0.0001）；稀有缺氧细胞与癌细胞形态分布高度重叠（核面积重叠系数 92.3%，核苏木精光密度 93.9%），符合生物学预期。
3. **基因预测更精细**：相比 BayesSpace（仅细分 spot）、SpatialScope（仅 spot 内单细胞）、iStar/XFuse（patch 级回归导致模糊），STEP 给出全切片单细胞级基因表达，标记基因空间富集与细胞类型对应良好。
4. **鲁棒性强**：跨 3 套参考、跨平台（10x Chromium/InDrop）、丢 30% 基因仍保留 >92% 性能、对参考组成扰动与组织学风格变化均稳定。
5. **可重建未测区域**：mask 率 0.7 下仍保持识别与表达预测；可跨相邻切片与跨患者迁移，并据此解析乳腺癌分子亚型（BRCA-A 以 Luminal B/HER2 富集为主，BRCA-B1/B2 含侵袭性 TNBC 区域）及 IDC 与 DCIS/LCIS 的边界微环境差异。
6. **跨平台通用**：Visium 上可用 6 张切片训练后推广到仅 H&E 的切片；MERFISH/osmFISH 上留一基因填补的 Spearman 相关显著优于 gimVI、Seurat、SpaGE（多数比较 FDR<0.05，仅 STEP vs gimVI 在 AllenSSp 上 FDR=0.165）；填补结果与 Allen ISH 图像一致。
7. **可扩展**：Visium HD 上把 124,399 细胞扩展至 426,954 细胞；MERSCOPE 71.3 万细胞完成全基因组未测基因填补。
8. **三模态整合有效**：Xenium+CITE-seq+IMC 实现单细胞分辨率转录组+蛋白图谱；CK5 富集于肌上皮细胞（4.70 倍）、CD15 富集于所有肿瘤类别（2.65 倍），与文献一致；CD20 预测与 IF 图像共定位良好。但基因-蛋白一致性有限（34.88% 的配对 Pearson r>0.1，37.21% 为负相关），反映转录后/翻译后调控。
9. **四模态 3D 图谱经济可行**：仅用 6/35 张切片训练即可达到最高 87.7% 空间准确率，精确重建海马 CA/DG 等精细层状结构，并推断 NeuN、c-Fos 等蛋白的 3D 分布。

---

## 7. 优点

- **框架通用性强**：平台无关，同时支持测序类与成像类 SRT，模块可按模态组合动态启用，覆盖双/三/四模态，扩展性好。
- **真正实现"全切片 + 单细胞 + 跨组学"**：同时解决"未测区域"（空间外推）与"未测基因/蛋白"（组学外推）两类缺失问题，这是相比现有方法的核心增量。
- **概率模型设计细致**：泊松似然 + 逐细胞表达（而非平均签名）+ spike-and-slab 稀疏先验 + Potts 空间先验，兼顾统计可解释性与生物学合理性；形态学特征被显式建模并与基因关联。
- **工程落地性好**：提供开源代码、Zenodo 存档与免安装网页应用；GAT 支持跨切片迁移，显著降低重复建模成本。
- **验证体系较完整**：多平台、多组织、多物种；含掩蔽实验、留一基因、跨切片/跨患者迁移、参考扰动、分辨率与组织学风格敏感性分析；统计检验规范（FDR 校正、效应量、空间自相关检验）。
- **成本效益突出**：用 6 张低分辨率切片 + 29 张 H&E 图像重建 3D 多组学图谱，为大规模计划（Human Cell Atlas、BRAIN Initiative）提供降本思路。

---

## 8. 不足与局限

- **建模假设限制**：Omics Enhancement 依赖"局部一致性与平滑性"的距离假设，可能削弱组织异质性的刻画；高斯核尺度固定为 0.1，缺乏自适应机制。
- **计算效率**：作者自述需发展更高效的生成模型以支撑大规模应用；文中未报告训练/推理耗时，实际可扩展性的时间成本不明。
- **基因-蛋白推断的生物学上限**：转录本到蛋白的推断只捕捉部分调控层级（忽略翻译控制、翻译后修饰、蛋白稳态、RNA 速率等），约 37% 的蛋白-基因对呈负相关，说明蛋白推断存在不确定性。
- **参考数据依赖**：三模态结果中 DCIS 亚克隆因 IMC 参考不含对应亚型而出现 UMAP 混叠，说明参考组织的生理相似性直接决定亚型分辨能力；跨平台/跨参考的偏差风险仍存在。
- **评价口径的局限**：主要基准缺乏真实单细胞级注释，依赖区域级标注

- **评价口径的局限（续）**：主要基准缺乏真实单细胞级注释，依赖区域级标注，使"单细胞级方法"的优势难以被严格量化；将细胞标签粗化到区域虽便于与 spot 级方法同口径比较，但会掩盖 spot 内部异质性，也可能对能输出单细胞结果的方法产生标签噪声惩罚或评价偏差。
- **缺乏真实多组学 ground truth**：三模态（Xenium+CITE-seq+IMC）与四模态 3D 图谱的验证主要依赖与相邻切片、IF 图像、Allen Atlas 的间接一致性，缺少同组织、同切片、同细胞的配对多组学测量，因而无法排除平台/切片间差异对结论的贡献。
- **基线覆盖不完整**：部分对比方法因算法限制、缺少相应功能或无法扩展至大规模数据而未能在所有场景运行，导致这些场景下缺少完整横向比较，削弱了"全面优于现有方法"这一结论的强度。
- **缺失场景为人工模拟**：mask spot、跨切片/跨患者迁移、留一基因等实验均为对"未测区域/未测基因"的模拟，与真实场景中的组织撕裂、切片缺失、取样偏差、批次效应仍有差距，外推性能在真实缺失数据上的表现尚待验证。
- **形态学特征与分割的平台依赖性**：细胞识别与空间扩散高度依赖 StarDist 分割质量与 H&E 染色风格；不同扫描仪、染色批次、组织类型下的分割误差会通过形态-基因回归项与 GAT 标签传播放大，跨中心应用可能需要重新校准。
- **超参数敏感性披露不足**：K 近邻数、高斯核尺度（固定 σ=0.1）、spike-and-slab 先验超参数、Potts 权重等对结果的影响主要置于补充材料，正文缺少系统的敏感性分析与默认值选取依据。
- **资源报告不完整**：虽给出硬件配置，但未报告各数据集的运行时间、内存峰值与 GPU 小时数；考虑到全切片分块处理与 503 GiB 内存配置，Visium HD、MERSCOPE 级别数据的实际时间成本与可及性仍不明确。
- **生物学解释需谨慎**：稀有缺氧细胞与癌细胞在形态分布上高度重叠（重叠系数 >92%），既可能反映真实生物学，也可能提示仅凭形态学特征区分某些亚群的能力有限，需更多分子标记独立验证。
- **统计优势并非普遍显著**：个别比较未达显著（如 AllenSSp 上 STEP 与 gimVI 的 FDR=0.165），说明相对优势存在数据集依赖性，结论应表述为"多数场景更优"而非"一致更优"。
- **可复现门槛**：尽管提供开源代码、Zenodo 存档与网页应用，完整复现仍需多套单细胞参考、组织学图像与较长预处理流程（QuPath/StarDist 分割、CVAE 域适应），对计算与数据整理能力有一定要求。

---

## 9. 总体评价与定位

- **方法学贡献**：STEP 的核心增量在于把"空间外推"（未测区域）与"组学外推"（未测基因/蛋白）统一进一个可组合框架，并以"泊松分配 + 稀疏形态-基因关联 + Potts 空间先验 + GAT 标签扩散 + 参考近邻映射"的分层设计兼顾统计可解释性与工程可扩展性，区别于仅做两两模态整合或仅做 niche 发现的现有方法。
- **实证强度**：实验覆盖测序类与成像类平台、多种组织与物种、多分辨率与多组学层，并配有参考扰动、基因缺失、分辨率变化、跨切片/跨患者迁移等敏感性分析，论证较为扎实；但受限于真实单细胞级与配对多组学 ground truth 的缺失，其绝对精度与跨中心泛化能力仍需独立复现与前瞻性验证。
- **适用场景**：适合预算受限、已有 H&E 与少量 SRT 切片、希望构建全切片单细胞或多组学图谱的研究场景，尤其在大规模图谱计划（如 Human Cell Atlas、BRAIN Initiative）的降本增效方面具有现实意义。
- **后续方向**：自适应核尺度与图结构、端到端多模态生成模型以提升效率、跨中心染色标准化、与真实配对多组学实验的联合验证，以及更系统的超参数与不确定性量化。

（完）
