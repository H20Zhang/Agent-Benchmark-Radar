# Data Exploration Benchmark：初步数据发现对后续分析的影响

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2026-08-17<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2608.16045)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](data-exploration-benchmark.en.md) · [主入口](../README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已完整阅读下述版本的正文与可用附录，并核对所用结果；未独立复现实验。

完整阅读第 1–8 节、评分公式和案例（9 页，含参考文献；无附录），逐项核对图 3–6 结果热图。

[arXiv 2608.16045v1 · 2026-08-17](https://arxiv.org/pdf/2608.16045v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

这项评测把“先理解数据”变成独立产物：模型从原始 Excel 生成固定格式的 JSON，描述逻辑表、字段语义、主外键、关系、来源位置和轻量数据剖析。实验包括一个真实 Vitamin D 研究工作簿和专门挑选的 12 个 DSBench 任务，按简单／中等／困难分为 4／5／3 个。主要模型为 Gemini 3.1 Pro、Claude Opus 4.6、GPT 5.4；GPT agent 只测困难组和真实工作簿。

[来源](https://arxiv.org/pdf/2608.16045v1)

<!-- EDITORIAL-METHOD:START -->
编辑比较：相较直接给模式和字段含义的分析题，这组任务先测初步发现如何影响后续分析；与 KramaBench 的完整数据旅程相比，它更适合检验小范围的探索或提示干预。演化坐标是分析前的信息形成，不能从少量任务推出通用探索策略或共享记忆收益。
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 评分与实验条件

结构评测先做最大权重表匹配、列匹配，再计算表／列／关系 F1、类型、语义、来源和数值剖析得分；摘要的 LLM 评分最多可让总分下降 30%。另一个下游实验保留问题和评分不变：Control 只给原文件，Middle 加入模型自己生成的探索 JSON，Treatment 加入正确元数据；正确元数据不含下游答案。这里没有固定总 token 成本。

[来源](https://arxiv.org/pdf/2608.16045v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 两个下游案例的正确答案数

论文第 6.2 节案例；每格为同一案例下正确回答数／问题数，非全基准总分；问题和评分固定，token 与探索工作量未固定；未给出重复运行方差。

| 模型 | 任务 | Control（正确／总数） | Middle（正确／总数） | Treatment（正确／总数） |
| --- | --- | --- | --- | --- |
| GPT 5.4 | 财务模型 | 15/20 | 16/20 | 17/20 |
| Claude Opus 4.6 | 仓库分配 | 6/9 | 7/9 | 9/9 |
| Gemini 3.1 Pro | 仓库分配 | 6/9 | 9/9 | 7/9 |

事实位置：第 6.2 节，PDF 第 7–8 页；干预设置见表 1，第 6 页 · [来源](https://arxiv.org/pdf/2608.16045v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## 结果解读、来源限定与下一步

下面两个具体任务同时展示收益与反例。显式元数据能改善依赖识别，但 Gemini 在调度任务中拿到正确元数据后反而少答对两题，表明提供表示并不保证正确使用。较小、定向的样本和未报告重复运行使这些结果更适合机制假设与案例研究，不能当作生产可靠性或长期共享状态的已验证结论。

GPT agent 未测全部 12 题；图 6 的 DeepAnalyze 仅覆盖一个简单任务、ai-analyst 仅两个，不能与四题主模型组直接排成等分母榜单。摘要裁判模型和重复运行次数未披露。

固定总预算，比较原始文件、自动 JSON、人工修订 JSON 和等长度普通摘要；在多个后续问题及数据变更后测量正确率、重复剖析成本和失效检测，验证可复用表示是否真正改善摊销成本。

[来源](https://arxiv.org/pdf/2608.16045v1)
<!-- EVIDENCE:limitations:END -->
