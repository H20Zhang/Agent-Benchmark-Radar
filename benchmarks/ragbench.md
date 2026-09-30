# RAGBench：训练和检验检索增强回答的评分器

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2024-07<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2407.11005)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](ragbench.en.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已阅读下述主论文全文的方法、实验设置、结果与局限；未独立复现实验。

全文第1–8节及附录9.1–9.7，包括提示、后处理、训练和域外评测。

[arXiv v1；PDF 页眉为 2024-06-25，不据此推断首发时间](https://arxiv.org/pdf/2407.11005v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## 与相邻评测相比改变了什么

以下为基于所读协议的编辑比较，不表示论文宣称直接继承。

相较只看最终答案的问答基准，RAGBench将文档—问题—回答三元组变成评分器训练和测试数据，并拆分相关性、证据使用与忠实性。它位于“如何评价RAG”的支线，不能把评分器拟合标签的成绩当作生成系统能力提升。
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## 任务与证据如何构造

12个数据源统一为文档、问题、回答，并用GPT-4-0125-preview标相关句、使用句和回答支持。TRACe分别量相关比例、使用比例、相关内容覆盖及全回答忠实性。句标签广播到token后训练DeBERTa多头评分器。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 复现时必须保留的条件

训练、开发、测试分别约 7.8 万、1.2 万、1.1 万例，按问题在每个来源内划分。回答主要由 GPT-3.5-0125 和 Claude 3 Haiku 以温度 1 生成，部分来源沿用已有回答；监督标签由 GPT-4-0125-preview 产生。实际评分器为 DeBERTa-v3-Large NLI 检查点加三个预测头，在 A100 上训练三轮，二元阈值 0.5。幻觉检测用 AUROC，相关性及使用率用 RMSE；Completeness 有定义但主表没有独立预测成绩。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 优势与反例应同时保留

各来源测试集；幻觉 AUROC 越高越好，相关性 RMSE 越低越好，均为 0–1；标签来自 GPT-4，未逐行给出测试样本分母。

| 数据集／指标 | GPT3.5 | RAGAS | DeBERTa |
|---|---|---|---|
| HotpotQA/Hall_AUROC | 0.59 | 0.62 | 0.85 |
| DelucionQA/Hall_AUROC | 0.57 | 0.7 | 0.64 |
| PubMedQA/Rel_RMSE | 0.21 | 0.37 | 0.26 |

事实来源：表 3, 节 5 · [论文](https://arxiv.org/pdf/2407.11005v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 跨域训练的退化

同一来源测试集的幻觉 AUROC（0–1）；比较全部领域与仅通用知识的训练数据，逐来源测试分母未明确列出。

| 数据集 | 全领域训练 | 仅通用知识训练 |
|---|---|---|
| FinQA | 0.81 | 0.67 |
| TechQA | 0.86 | 0.76 |

事实来源：表 4, 附录 9.7 · [论文](https://arxiv.org/pdf/2407.11005v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## 这些比较支持什么结论

模型应写DeBERTa-v3-Large；摘要RoBERTa与方法不一致。优势集中在多数幻觉检测数据，不能称所有指标都胜。完整性指标被定义，但主表未给独立预测成绩。
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## 局限、来源冲突与下一步

GPT-4标签可能传递偏置；合成质量排序验证不等于逐例人工有效性。下一步用独立人工标签、留出生成器和等成本评分器复核。

摘要写RoBERTa，但方法与表3写DeBERTa；本文采用可定位的方法名称。表1称TechQA为5篇文档，附录9.2称10篇，未自行调和。论文的普遍优势措辞也有表3反例。
<!-- EVIDENCE:limitations:END -->

相关基准：[ragtruth](ragtruth.md) · [claimprobe](claimprobe.md)
