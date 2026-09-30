# LiveSQLBench：持续更新的跨数据库 SQL 评测

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2025-05-28<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://livesqlbench.ai/)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](livesqlbench.en.md) · [主入口](../README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已核对下述官方协议、实现配置和可获得结果；未独立复现实验，未声称完整论文阅读。

完整读取官方项目页、根 README、Agent 和 CLI 文档，以及基线调用与配置源码；官方论文链接仍标为 Coming Soon。

[官方仓库文档 · e15cd221267e06fabfaf6a3d4a69308280ce9a7c · 2026-09-30](https://github.com/bird-bench/livesqlbench/blob/e15cd221267e06fabfaf6a3d4a69308280ce9a7c/README.md)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

LiveSQLBench 是持续发布的数据集家族。Base-Lite 包含 18 个 PostgreSQL 数据库和 270 题（180 查询、90 管理操作）；Base-Full v1 为 22 库、600 题；Large-v1 为 18 库、480 题。问题依赖数据库模式、列解释与分层业务知识。每个发布可以固定下来运行；“持续更新”不意味着同一个代理必须跨多次发布保留状态并在线适应。

[来源](https://github.com/bird-bench/livesqlbench/blob/e15cd221267e06fabfaf6a3d4a69308280ce9a7c/README.md)

<!-- EDITORIAL-METHOD:START -->
编辑比较：Spider 和 BIRD 提供固定公开题集，LiveSQLBench 强调持续加入数据库与查询，并允许分版本观察 SQL 能力。演化坐标是测试集合的更新及时间可追踪性；这不自动等于对同一数据库模式／业务规则漂移做了受控实验，也不保证每版难度相同。
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 评分与实验条件

查询题比较执行结果，管理题检查定制后置条件。官方 Model Base 表示直接生成 SQL；Agent 和 CLI 则允许工具探索。当前 ADK 版本每次工具调用消耗一步、默认 30 步、最终 SQL 只提交一次；历史网站 Agent I 写 20 步，应分开记录。以下只引用根 README 明示的 Base-Lite 历史模型结果，不与当前动态榜或其他发布混合。

[来源](https://github.com/bird-bench/livesqlbench/blob/e15cd221267e06fabfaf6a3d4a69308280ce9a7c/README.md)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 官方 README 的 Base-Lite 历史结果（选取）

README 标为 2025-05-28 的 Base-Lite Model Base 结果；270 题，PostgreSQL；通过对应测试的任务占比；费用为历史作者报告值。确切模型快照、调用预算和重复次数缺失，不能据此做公平因果比较。

| 模型 | 成功率（%） | 平均费用（美元／题） |
| --- | --- | --- |
| o3-mini | 47.78 | 0.0233 |
| GPT-4.1 | 44.10 | 0.0336 |

事实位置：根目录 README 的模型表现部分；官方项目页的当前模型表现讨论 · [来源](https://github.com/bird-bench/livesqlbench/blob/e15cd221267e06fabfaf6a3d4a69308280ce9a7c/README.md)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## 结果解读、来源限定与下一步

项目官网仍将论文标为 Coming Soon，本页依据已完整读取的官方协议文档，不声称读完不存在的论文。历史结果没有完整的模型快照、预算和方差，且当前代码不足以独立重建所有行。版本刷新和隐藏答案降低某些泄露风险，但不是从未污染的证明。

根文档与 Agent 文档的数据库数／旧注释冲突，优先采用明确发布数据。当前基线代码不能直接运行所有历史模型行，故不擅自赋予统一预算。

固定任务、数据库、业务规则与评分器提交，在同一批任务上构造规则变化前后配对实验；分别测查询、管理后置条件和旧规则缓存失效。

[来源](https://github.com/bird-bench/livesqlbench/blob/e15cd221267e06fabfaf6a3d4a69308280ce9a7c/README.md)
<!-- EVIDENCE:limitations:END -->
