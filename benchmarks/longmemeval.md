# LongMemEval：检索键、时间筛选与回答证据的作用

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（历史参考）** · 2024-10-14 · 论文 v1<br>
> **GPT-4o + round values / fact-expanded keys (top-10) — LongMemEval-M QA accuracy: 72.0%**<br>
> 表 2 索引设计实验的最佳端到端 QA；不是 LongMemEval-S、oracle 条件或跨所有预算的统一上限。 [原始来源](https://arxiv.org/html/2410.10813v1)<br>
> 仅供了解当时难度，不代表当前最佳；不同任务、版本和实验条件不能直接混比。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](longmemeval.en.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已核对所述论文版本的方法、实验设置、关键结果与局限；未独立复现实验。

已阅读v2正文第1—6节、可复现性与伦理说明以及附录A—E；补读PDF图7—8、10—13的提示文字，并检查官方README中的2025年9月数据清理说明。未复现，未把曲线估算为精确数值。

[arXiv 2410.10813v2 (2025-03-04)](https://arxiv.org/html/2410.10813v2)

[补充来源 2410.10813v2，2026-09-30 核对](https://arxiv.org/pdf/2410.10813v2)

[官方来源，2026-09-30 所见内容（可变页面）](https://github.com/xiaowu0162/LongMemEval)

页首历史参考原样保留；正文的新版本结果不能代替原始发布成绩。
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 任务怎样产生记忆需求

把人工策划的证据会话嵌入带时间戳的用户—助手历史，再提出500道涵盖提取、跨会话综合、时间推理、更新和弃答的问题。框架区分存储内容、索引键、检索查询和读取策略。一轮包含一条用户消息及其助手回复。

定位比较：相较LoCoMo的长对话记忆，LongMemEval更集中地操纵检索表示、时间推理、知识更新和弃答，区分约115K与更大历史档位。它把记忆流程拆成可比较的检索与阅读环节，但总体QA分数仍不能单独定位哪一步失效。 这里是评测坐标比较，不表示直接继承了前者的数据。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置与评分对象

S每题约115ktokens；M有500会话、约1.5Mtokens。主要记忆实验采用Stella V5 1.5B检索、Llama3.1 8B Instruct提取，并将值按时间排序，以JSON及Chain-of-Note读取。索引键与提取仅使用用户侧消息；返回内容保持所选粒度。贪心生成，上限800tokens。GPT-4o-2024-08-06按题型规则作二元正确性判断。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 扩展索引键，可同时改善召回与回答

数值为0–1比例。事实只扩展检索键，返回值仍是原始轮次；同一回答器内比较，GPT-4o提高5.0个百分点。

LongMemEval-M的500题；每题检索前10个轮次片段。

| 索引配置 | Recall@10 | GPT-4o QA@10 | Llama3.1-70B QA@10 | Llama3.1-8B QA@10 |
|---|---|---|---|---|
| Stella V5 / K=V | 0.692 | 0.67 | 0.624 | 0.534 |
| Stella V5 / K=V+fact | 0.784 | 0.72 | 0.682 | 0.572 |

定位：v2表3：轮次级检索 · [原文](https://arxiv.org/html/2410.10813v2)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 证据存在，也不保证完整历史读得好

数值为0–1比例。直接回答87.0%到60.6%是26.4个百分点差距，不是26.4%的相对下降；该差距不能单独归为写入或检索失败。

500题；理想条件只提供证据会话，S条件提供完整历史。

| 回答配置 | 理想证据QA | LongMemEval-S QA |
|---|---|---|
| GPT-4o / direct | 0.87 | 0.606 |
| GPT-4o / Chain-of-Note | 0.924 | 0.64 |

定位：v2图3(b) · [原文](https://arxiv.org/html/2410.10813v2)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## 时间筛选首先改善的是证据召回

数值为0–1比例。Stella V5与事实扩展键固定，改变查询时间范围提取模型；这是召回指标，不是最终QA。

时间推理子集；表格未给各配置实际有效题数。

| 时间筛选 | Recall@10 |
|---|---|
| 无时间筛选 | 0.55 |
| GPT-4o时间筛选 | 0.722 |
| Llama3.1-8B时间筛选 | 0.57 |

定位：v2表4：轮次级检索与事实扩展键 · [原文](https://arxiv.org/html/2410.10813v2)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## 结论边界与下一步验证

在这些固定配置中，扩展索引键同时改善召回和QA，但证据可见仍不保证读对。严格召回判失败时，也可能只是缺少旧事实，而更新后的答案已经正确。裁判允许时长差一单位，且答案同时包含旧信息与正确新信息也可得分，因此该指标不是严格时间精度或彻底删除测试。Oracle是模型条件下的参考。

表9的Stella检索数值与主表3/表10存在差异，本页明确使用表3。2024年8月商业产品试验只有97条缩短历史，排除了若干题型，不是完整500题，也不是当前产品比较。2025年9月清理后的数据与论文运行版本需分开。

下一步：固定清理后数据版本、读取器和token预算。在返回内容不变的条件下对比原始索引键与事实扩展键，再加入直接提供证据的对照。更新能力可搭配StateMemBench，隐式使用可搭配InMind；分别报告题型分数与成本。
<!-- EVIDENCE:limitations:END -->
