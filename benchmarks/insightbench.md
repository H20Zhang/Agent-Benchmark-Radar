# InsightBench：多步业务分析中的洞察发现与覆盖

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2024-07<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2407.06423)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](insightbench.en.md) · [主入口](../README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已完整阅读下述版本的正文与可用附录，并核对所用结果；未独立复现实验。

本次复核阅读 v4 全部正文与附录 A–D、十个提示模板；以 HTML 与 PDF 文本交叉核对所用表格，未独立检查图表像素。

[arXiv 2407.06423v4 · 2025-02-27](https://arxiv.org/pdf/2407.06423v4)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

InsightBench 的 100 组合成业务数据借鉴 ServiceNow 模式，植入 475 个参考洞察。AgentPoirot 先读取模式，根据高层目标提出三个主问题，每个再做四次跟进，最多形成 15 项洞察后汇总。它通过 Python 与定制 cba 工具分析和绘图；对照包括修改过的迭代式 Pandas Agent，以及改用泛化目标的同框架版本。

[来源](https://arxiv.org/pdf/2407.06423v4)

<!-- EDITORIAL-METHOD:START -->
编辑比较：固定问题的数据问答给定要找的答案，InsightBench 让代理围绕业务目标自行提出分析问题并发现洞察。它新增的是探索与见解覆盖坐标；软匹配参考洞察不证明因果发现、商业价值或不存在未标注的正确新发现。DDR-Bench 可作为另一种隐藏事实覆盖参照。
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 评分与实验条件

实验温度为 0，报告五个种子的均值与标准差。LLaMA-3-70B 裁判为每条参考洞察寻找最相符的预测，另行比较摘要；这是带参考的软相似度，不是双向精确率／召回率或商业收益。裁判提示使用 1–10，结果表报告归一化软分。未给出各框架匹配的 token 或时间上限。

[来源](https://arxiv.org/pdf/2407.06423v4)
例如，面对含处理时长变化的事件表，智能体需要自行选择分析问题、执行计算、解释趋势，再给出摘要。评分先对每条参考洞察选取最高分预测，再在数据组内、数据组间分别取均值；475项参考不是微平均分母。多报的错误洞察不会在这个单向匹配中逐项直接扣分，因此输出数量和预算必须控制。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## GPT-4o控制组的选定软评分，表1

100 组数据、475 项参考洞察；GPT-4o；五个种子的均值±标准差，不是置信区间；AgentPoirot 最多 15 项洞察，裁判 LLaMA-3-70B；无匹配的 token／时间上限。

| 代理／条件 | 洞察 LLaMA-3-Eval（均值±SD，0–1） | 摘要 LLaMA-3-Eval（均值±SD，0–1） |
| --- | --- | --- |
| Pandas Agent / GPT-4o | 0.54±0.01 | 0.40±0.04 |
| AgentPoirot / GPT-4o | 0.60±0.03 | 0.44±0.03 |
| AgentPoirot / GPT-4o／泛化目标 | 0.40±0.03 | 0.33±0.12 |

事实位置：第 2.2、3.1–3.2 节；表 1，PDF 第 8 页；附录 D 提示模板 1–10 · [来源](https://arxiv.org/pdf/2407.06423v4)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:backbone-results:START -->
## 模型骨干对照与结果赛道

v4完整100组数据；AgentPoirot；定制SMART目标与多样化后续问题；生成与裁判温度0；五个种子的均值±标准差，非置信区间。

| 模型骨干 | 洞察软评分（0–1，均值±SD） | 摘要软评分（0–1，均值±SD） |
|---|---|---|
| gpt-4o | 0.60±0.03 | 0.44±0.03 |
| gpt-4-turbo-2024-04-09 | 0.56±0.02 | 0.35±0.04 |
| gpt-3.5-turbo-0125 | 0.50±0.02 | 0.31±0.06 |
| llama-3-70b | 0.52±0.04 | 0.33±0.01 |

两个指标分别记录；泛化目标、仅描述性后续问题、Pandas Agent和前十组数据的裁判消融不并入。未确定等额时间、词元或重试预算；不是准确率、可相加总分或当前排行榜。

[Table 1](https://arxiv.org/pdf/2407.06423v4) · [JSON](../data/results/insightbench.json)
<!-- EVIDENCE:backbone-results:END -->

<!-- EVIDENCE:limitations:START -->
## 结果解读、来源限定与下一步

特定业务目标优于泛化目标，但不能把一个指标上的优势推广到所有指标：GPT-4o 的洞察 ROUGE-1 中，Pandas Agent 为 0.35，AgentPoirot 为 0.32。合成趋势与参考洞察覆盖限制了对开放业务发现的外推。

算力描述有两处不一致：正文写四块 A100，复现部分写两块 80 GB A100，不能拼成确定的统一硬件配置。

固定洞察数量与计算预算，加入没有预埋趋势的数据和专家未知的新趋势，盲审新洞察的证据、正确性与价值，并区分参考覆盖率和错误发现率。

[来源](https://arxiv.org/pdf/2407.06423v4)
<!-- EVIDENCE:limitations:END -->
