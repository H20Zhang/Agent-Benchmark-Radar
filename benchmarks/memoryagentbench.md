# MemoryAgentBench：不同记忆任务与预算要分开读

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（历史参考）** · 2025-07 · 论文 v1<br>
> **NV-Embed-v2 RAG / GPT-4o-mini — RULER-QA: 83.0**；**Contriever RAG / GPT-4o-mini — FactCon-MH accuracy: 7.0%**<br>
> 主表 2 中两个子任务的最佳配置；不把整套基准的不同能力合成一个总分。 [原始来源](https://arxiv.org/html/2507.05257v1)<br>
> 仅指表 2 的比较范围，不含后续消融；多跳冲突按表中 7.0 记录，正文“至多 6”与表格不一致。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](memoryagentbench.en.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已核对所述论文版本的方法、实验设置、关键结果与局限；未独立复现实验。

已阅读v4正文第1—5节与附录A—L，包括PDF图4—5的提示。只使用表格及明确报告的数值，未复现实验。

[arXiv 2507.05257v4 (2026-06-28)](https://arxiv.org/html/2507.05257v4)

[补充来源 2507.05257v4，2026-09-30 核对](https://arxiv.org/pdf/2507.05257v4)

页首历史参考原样保留；正文的新版本结果不能代替原始发布成绩。
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 任务怎样产生记忆需求

将来源任务转换成附带记忆指令的有序片段，再测试检索、示例学习、全局理解及冲突更新。FactConsolidation给更新的反事实更大序号。

定位比较：相较LongMemEval式会话问答，MemoryAgentBench把信息逐块交给记忆系统，并扩展为检索、测试时学习、长程理解和选择性遗忘。任务来源和指标不同，所以要按子任务解释；不能把一个总体均值当成统一的记忆容量。 这里是评测坐标比较，不表示直接继承了前者的数据。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置与评分对象

异质任务共2,071题。默认RAG骨干GPT-4o-mini；合成QA/遗忘任务多为512token片段，其他任务4096；Mem0/Cognee/Zep/MIRIX统一4096。通常检索top10。LME(S*)是5条重构历史上的300题，并非原始LongMemEval-S。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 同一回答器在不同任务上没有统一赢家

QA/遗忘采用子串匹配准确率；MCC是分类准确率均值。默认回答器相同，记忆与证据预算不同，不作跨任务总排名。

单跳QA为100题；MCC为5个数据集各100题；两种FactCon各100题、各自使用约262K词元流。

| 系统 | 单跳文档QA（%） | MCC（%） | FactCon-SH（%） | FactCon-MH（%） |
|---|---|---|---|---|
| GPT-4o-mini (128K) | 64.0 | 82.0 | 45.0 | 5.0 |
| BM25 / GPT-4o-mini | 66.0 | 75.4 | 48.0 | 3.0 |
| HippoRAG-v2 / GPT-4o-mini | 76.0 | 61.4 | 54.0 | 5.0 |

定位：v4表3：部分子任务 · [原文](https://arxiv.org/html/2507.05257v4)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 匹配处理词元，不等于匹配全部成本

Banking77为准确率，摘要为论文尺度的流畅度加权F1。匹配处理词元量，但未匹配前向调用次数与索引生命周期成本。

Banking77为100题，摘要使用随机30本书子集；不是主表100本书。

| 系统 | Banking77 4K（%） | Banking77 104K（%） | 摘要113K分数 |
|---|---|---|---|
| Long-Context / GPT-4.1-mini | 74.0 | 93.0 | 39.7 |
| BM25 / GPT-4.1-mini | 83.0 | 88.0 | 38.0 |
| MIRIX / GPT-4.1-mini | 52.0 | 67.0 | 38.8 |

定位：v4表18、附录J · [原文](https://arxiv.org/html/2507.05257v4)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## 改变更新提示，并不自动解决遗忘

准确率为0–100。GPT-4.1-mini提示策略干预；仅承认显式否定的规则可能与“最新事实”金标准不一致。

两种FactCon各100题，长输入流。

| 提示配置 | FactCon-SH（%） | FactCon-MH（%） |
|---|---|---|
| GPT-4.1-mini / baseline | 36.0 | 5.0 |
| GPT-4.1-mini / always prefer later | 40.0 | 4.0 |
| GPT-4.1-mini / explicit-negation only | 28.0 | 4.0 |

定位：v4表19 · [原文](https://arxiv.org/html/2507.05257v4)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## 结论边界与下一步验证

表现随任务与证据预算变化。共用提示不等于隔离架构因果效应。短上下文可解不能定位长流中的失败机制。成本估算排除了索引，并假设历史缓存价格。

表16将五个分类任务均值82.0误标为Banking77，而Banking77单项为93.0；本页不使用这组有歧义的零样本比较。推荐指标是Recall@5，不能通称准确率。摘要提示要求1000—1200词，但输出上限为1200词元。主表重复总分42.2/42.3和EventQA跨表67.6/67.4也不能静默合并。

下一步：匹配骨干、分块、检索和全生命周期计算，对比增量与延后索引。除最新答案准确率外，单独检查旧事实是否仍在存储；可搭配MemProbe区分保留与更新。
实际流程先逐块摄入，再回答留出问题；第3.2节允许结构化RAG在全部片段到齐后才建立结构。选择性遗忘只检查最新事实答案，不验证旧事实是否从存储删除。
<!-- EVIDENCE:limitations:END -->
