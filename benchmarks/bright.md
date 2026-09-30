# BRIGHT：需要推理才能识别的相关文档

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2024-07<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2407.12883)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](bright.en.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已阅读下述主论文全文的方法、实验设置、结果与局限；未独立复现实验。

v4正文及附录A–I、表1–49；镜像缺失的表18以后内容由51页PDF补齐。

[arXiv v4 (2025-03-26)，ICLR 2025；不是首版成绩](https://arxiv.org/pdf/2407.12883v4)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## 与相邻评测相比改变了什么

以下为基于所读协议的编辑比较，不表示论文宣称直接继承。

与BEIR所代表的异质零样本检索相比，BRIGHT专门让相关性依赖问题求解，主题或词面相近并不足够。它把测量重心推向推理型相关性；对话代理和下游问答仍需各自受控实验。
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## 任务与证据如何构造

1384查询分12任务：七个StackExchange领域通过答案引用和人工核验建立证据，其余按代码算法、语法或共同定理定义相关。难负例主题相似但无解题帮助；部分数学/代码候选按查询排除潜在假负例。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 复现时必须保留的条件

本文采用 v4：1384 查询、12 个任务，主分数为各数据集等权宏平均 nDCG@10×100。SFR 使用 SFR-Embedding-Mistral，输入上限 4096 token；Qwen 为 gte-Qwen1.5-7B-instruct，上限 8192 token。重排比较 MS-MARCO MiniLM-L12 与 gpt-4-0125-preview，候选数必须保留。下游问答只覆盖七个 StackExchange 领域，由 Claude 3.5 Sonnet 同时生成和按参考内容覆盖量表评分；它不是二元答案正确率。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 原查询排序

12 个数据集的宏平均 nDCG@10（0–100）；v4 共 1384 个查询，各数据集权重相同。

| 系统 | 分数 |
|---|---|
| BM25 | 14.5 |
| SFR | 18.3 |
| Qwen | 22.5 |

事实来源：表 2 · [论文](https://arxiv.org/pdf/2407.12883v4)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 独立重排实验块

12 个数据集宏平均 nDCG@10（0–100）；该独立实验块 BM25 基线为 14.3，不应与表 2 的 14.5 混用。

| BM25 重排器 | 候选文档数 k | 分数 |
|---|---|---|
| 无 | — | 14.3 |
| MiniLM-L12 | 100 | 8.3 |
| GPT-4 | 10 | 17.4 |

事实来源：表 3/表 41 · [论文](https://arxiv.org/pdf/2407.12883v4)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## 初步下游评价

7 个 StackExchange 领域的平均参考内容覆盖评分（0–100）；Claude 3.5 Sonnet 同时生成与评分，逐领域查询数见数据表，不能解释为二元正确率。

| 检索条件 | 平均分 |
|---|---|
| 无 | 77.7 |
| Qwen | 79.6 |
| 标准证据 | 81.8 |

事实来源：表 4, 表 46 · [论文](https://arxiv.org/pdf/2407.12883v4)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:interpretation:START -->
## 这些比较支持什么结论

原文已有初步下游QA，不能写成完全未测证据使用；但同模型生成/判分及内容覆盖量表不能证明独立事实正确率或智能体策略因果优势。
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## 局限、来源冲突与下一步

相关性仍含主观性；GritLM继续训练只检验特定无查询-文档映射泄露，不证明普遍抗污染。下一步固定候选、版本和计算预算，分开测检索与答案。

v1为1398题/SFR18.0，v4为1384题/SFR18.3。v4表2最高行是22.5，正文/表注却称24.3；重排块BM25为14.3，不能与原查询表14.5混用。表46把predicted_answer放入PROBLEM和STUDENT ANSWER，需实现核验；长上下文表6/39的一些均值也不同。
<!-- EVIDENCE:limitations:END -->

相关基准：[beir](beir.md) · [bright-pro](bright-pro.md)
