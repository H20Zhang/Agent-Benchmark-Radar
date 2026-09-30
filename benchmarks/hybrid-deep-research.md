# HybridDeepResearch：SQL 与搜索之间的约束传递

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2026-06<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2609.09410)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](hybrid-deep-research.en.md) · [主入口](../README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已完整阅读下述版本的正文与可用附录，并核对所用结果；未独立复现实验。

完整阅读 20 页正文与附录 A–H，涵盖构造、审核、工具接口、模型配置、补充结果和轨迹案例；核对表 1–5。

[arXiv 2609.09410v1 · 2026-09-08](https://arxiv.org/pdf/2609.09410v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

HybridDeepResearch 将数据库计算与文本证据衔接分成三种任务：先 SQL 后检索（SQL2S，203 题）、先检索后 SQL（S2SQL，58 题）及两路结果求交集（Parallel，119 题），合计 380 题，基于九个 LiveSQLBench-Base-Lite 数据库。生成流程用实体锚点和 SQL 模板构造问题，通过执行校验、单工具排除测试和人工审核筛选。困难集共 120 题，每类 40 题。smolagents 使用共享上下文中的单代理；MiroFlow 采用主代理与工作代理。两者得到同类数据库和搜索工具，但保留各自原生提示和上下文组织。

[来源](https://arxiv.org/pdf/2609.09410v1)

<!-- EDITORIAL-METHOD:START -->
编辑比较：BrowseComp 类搜索题和 BIRD 类数据库题通常分开评，HybridDeepResearch 把二者衔接成 SQL→搜索、搜索→SQL 或候选交集。新增坐标是跨工具传递实体与约束；总体检索、数据库执行和多代理调度都可能影响分数，不能把改进独占归因于某种共享上下文设计。
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 评分与实验条件

只读 SQLite 查询最多返回 500 行，代理自行发现模式。Real Web 用实时搜索和页面读取；Corpus Search 限定到 Wikipedia 与 FineWeb10BT 的固定索引。每题至多 300 次工具调用轮次、3,600 秒；主实验独立运行八次。Pass@8 是至少答对一次的题数比例，Avg@8 是所有题的八次平均成功率，分别以 N 题和 8N 次尝试为基础。S2SQL 比较执行后且列对齐的结果；其余两类用 Qwen3-30B-A3B-Instruct-2507 作答案裁判。Qwen 启用 thinking；闭源模型采用 medium reasoning effort，其他采样和量化设置也不完全相同。

[来源](https://arxiv.org/pdf/2609.09410v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 固定主干与索引：至少一次成功与平均成功分开看

全量 380 题，每题八次；Qwen3.5-397B-A17B-FP8，Corpus Search；每题 300 轮／3,600 秒上限，实际消耗未配平。

| 框架 | Pass@8（%） | Avg@8（%） |
| --- | --- | --- |
| smolagents | 56.58 | 32.43 |
| MiroFlow | 63.42 | 32.76 |

事实位置：表 1，第 7 页；第 6.1–6.2 节 · [来源](https://arxiv.org/pdf/2609.09410v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 困难子集的选取模型结果

困难子集 120 题，三类各 40 题，每题八次；全部用 smolagents + Corpus Search；GLM 最大推理设置，闭源模型 medium，非同等推理预算。

| 模型 | Pass@8（%） | Avg@8（%） |
| --- | --- | --- |
| GLM-5.2-FP4 | 50.83 | 25.00 |
| Claude-Sonnet-4.6 | 52.50 | 28.12 |
| GPT-5 | 54.17 | 27.40 |

事实位置：表 3，第 8 页；附录 E · [来源](https://arxiv.org/pdf/2609.09410v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## 多代理的运行代价：完成轨迹均值与全部尝试的超时

仅困难 120 题 × 八次，共每框架 960 次；Qwen3.5-397B-A17B、Corpus Search。调用和 token 均值只统计在一小时内完成的轨迹，超时率则以全部 960 次为分母；不是上表全量 380 题的费用统计。

| 框架 | 完成／总尝试 | 超时（%） | 模型调用均值 | 工具调用均值 | 输入 token 均值（百万） | 输出 token 均值（千） |
| --- | --- | --- | --- | --- | --- | --- |
| smolagents | 800/960 | 16.7 | 52.5 | 78.1 | 2.78 | 34.9 |
| MiroFlow | 564/960 | 41.3 | 120.1 | 210.0 | 2.06 | 46.1 |

事实位置：附录 G.1、表 5 及其相邻完成次数说明，第 18 页 · [来源](https://arxiv.org/pdf/2609.09410v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## 结果解读、来源限定与下一步

固定 Qwen 主干和检索后端时，MiroFlow 的 Pass@8 较高，但 Avg@8 只小幅变化，支持的是“多次尝试至少成功一次”的改善，不能读成单次可靠性大幅提升。困难集的最高 Pass@8 与最高 Avg@8 分属不同模型。轨迹统计进一步显示，多代理增加了调用和超时；输入 token 较少来自较短的工作代理上下文，并不意味着整体更便宜。不同工具、模型和原生框架设置，及未报告的不确定区间，限制了因果归因。

困难子集同时依据题目复杂度和预试代理失败挑选，并非无偏随机样本。单工具排除测试只支持被测配置下的工具必要性；四位审核者是作者中的博士研究者。完整集闭源模型补充结果只有两次尝试，不能与主实验 Pass@8 直接拼榜。

在预先冻结且不依赖待测模型失败的题集上，匹配总 token、时间和工具预算；同时报告平均成功、至少一次成功、超时与费用。分别检查实体锚点保留、SQL 约束翻译和候选交集，验证中间证据共享能否提高单次成功，而非仅增加重试。

[来源](https://arxiv.org/pdf/2609.09410v1)
<!-- EVIDENCE:limitations:END -->
