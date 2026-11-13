---
title: "Where single-cell foundation models help: a benchmark of annotation, perturbation and regulatory inference against simple baselines"
title_zh: 单细胞基础模型在何处发挥作用：注释、扰动与调控推断相较简单基线的基准评测
authors: "Cupaioli, F. A., Merelli, I."
date: 2026-11-10
pdf: "https://www.biorxiv.org/content/10.64898/2026.11.03.763968v2.full.pdf"
tags: ["query:virtual-cell"]
score: 8.0
evidence: 系统评测单细胞基础模型在计算扰动预测中的表现
tldr: 单细胞基础模型被寄望统一完成注释、扰动和调控推断，但其相对简单基线的增益缺少同数据评测。本文在K562 Perturb-seq、原代细胞、脑类器官和肺癌活检上统一比较五种基础模型、CellOracle、STATE及任务匹配基线。跨物种标签迁移优势最大，小鼠肺注释最高0.98，种内注释仅与主成分相当；零样本扰动方向可部分复现，类器官敲除效应多由靶基因表达位置解释。作者发布fmaudit基准与等基因参考任务，明确适用边界和验证需求。
source: biorxiv
selection_source: fresh_fetch
motivation: 单细胞基础模型被提出为注释、扰动和调控推断的通用工具，但其相对简单基线的实际增益尚不清楚。
method: 在K562 Perturb-seq、原代细胞、脑类器官和肺癌活检上，统一评测五种基础模型、CellOracle、STATE及任务匹配基线。
result: 跨物种迁移优势最明显，小鼠肺注释最高0.98；种内注释仅与主成分相当，零样本扰动可部分捕捉方向，类器官敲除效应多由靶表达解释。
conclusion: 基础模型价值集中在跨物种标签迁移等特定任务；作者发布fmaudit基准与等基因参考任务，强调克隆与供体差异需重复验证。
---

## 摘要
单细胞基础模型（FM）被提出作为细胞类型注释、in silico扰动和基因调控网络（GRN）推断的通用工具。为识别其增值所在，我们在相同数据上对五个FM（scGPT、Geneformer V1和V2、Nicheformer、scFoundation）、CellOracle、包括STATE在内的有监督扰动模型，以及任务匹配的简单基线进行了基准评测；数据涵盖K562 Perturb-seq筛选与原代细胞，到健康供体与同基因型脑白质营养不良脑类器官、一个公开类器官CRISPR筛选以及肺癌活检。当标签需要跨物种迁移时，FM最为有用：从人到小鼠肺，Nicheformer达到0.98的准确率，Geneformer V2和scFoundation约为0.90，而最佳基线为0.68。零样本in silico扰动捕获了K562中真实应答的方向，最多75%的扰动朝预期方向偏移（scFoundation，p < 1e-8）；Geneformer V2网络比共表达网络更好地恢复患者水平的肿瘤差异表达（富集倍数2.9对2.0）。在同一物种内，FM嵌入的细胞注释准确率与主成分相当。在类器官中，预测的敲除效应在很大程度上可由靶基因的表达位置解释，而表达匹配的对照测试分离出基因特异性部分，占效应的12%至35%。同基因型Canavan和Krabbe类器官以及4H患者类器官（每个细胞系和时间点仅一个文库）尚不能将方法差异与克隆和供体间差异区分开，这界定了未来验证所需的重复实验。微调改变了分类准确率，但未改变敲除排名。我们以fmaudit软件包形式发布该基准、基线、流程检查以及同基因型参考任务，以便在FM已能发挥作用的那些任务上评估新模型。

## Abstract
Single-cell foundation models (FMs) are proposed as general tools for cell-type annotation, in silico perturbation and gene-regulatory-network (GRN) inference. To identify where they add value, we benchmarked five FMs (scGPT, Geneformer V1 and V2, Nicheformer, scFoundation), CellOracle, supervised perturbation models including STATE, and task-matched simple baselines on the same data, from K562 Perturb-seq screens and primary cells to healthy-donor and isogenic leukodystrophy brain organoids, a public organoid CRISPR screen and lung cancer biopsies. FMs were most useful when labels had to be transferred across species: from human to mouse lung, Nicheformer reached 0.98 accuracy and Geneformer V2 and scFoundation about 0.90, against 0.68 for the best baseline. Zero-shot in silico perturbations captured the direction of real responses in K562, with up to 75% of perturbations shifted in the expected direction (scFoundation, p < 1e-8), and Geneformer V2 networks recovered patient-level tumour differential expression better than co-expression (fold enrichment 2.9 versus 2.0). Within a species, FM embeddings annotated cells as accurately as principal components. In organoids, predicted knockout effects were largely explained by where the target is expressed, and an expression-matched control test isolated the gene-specific part, 12 to 35% of the effects. Isogenic Canavan and Krabbe organoids and 4H patient organoids, with one library per line and time point, did not yet separate methods from differences between clones and donors, which defines the replication needed for future validation. Fine-tuning changed classification accuracy but not knockout rankings. We release the benchmark, baselines, pipeline checks and the isogenic reference task as the fmaudit package, so that new models can be evaluated on the tasks where FMs already help.