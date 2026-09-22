# Data Agent Benchmark (DAB)：跨异构数据库回答企业数据问题

**中文** | [English](data-agent-benchmark.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2603.20576) · [项目页](https://ucbepic.github.io/DataAgentBench/) · [代码](https://github.com/ucbepic/DataAgentBench)

## 它到底测什么

DAB 评估 enterprise data question 在 **多个异构 database system** 之间分散、引用不一致、部分信息还藏在 unstructured field 时，agent 能不能完成整合、转换与分析。

## 相比此前评测多测了什么

Text-to-SQL 通常假设一个 database 和已知 schema。DAB 同时覆盖 PostgreSQL、MongoDB、SQLite、DuckDB，把“数据到底在哪、不同系统里的 reference 怎么对应”也变成 task。

## 决定性证据

benchmark 有 54 个 query、12 个 dataset、9 个 domain、4 类 DBMS，设计来自 6 个行业 enterprise workload 的 formative study。论文初始实验报告 Gemini-3-Pro 的 pass@1 为 38%；这是当时模型与协议下的历史结果，不是当前能力上限。

## 这个分数能证明什么

它支持 heterogeneous backend 下 enterprise data QA 的 end-to-end 判断，但不能直接说失败来自 semantic mapping、integration、transformation、SQL/NoSQL generation 还是 answer synthesis，除非进一步看 trajectory。

## 公平比较契约

必须固定 database snapshot、credentials/access、tool interface、model、retry policy 与 trial 数；leaderboard 本身要求每题至少 5 次。应报告 pass@1 和 variance，不能用 best-of-n 掩盖 stochastic instability。

## 还没有测什么

任务数量小、主要是 read。生产 data agent 还会遇到 permission、write、lineage、semantic layer、schema evolution、成本约束与 business ambiguity。

## 下一步最有判别力的验证

给每题增加 ground-truth integration/semantic plan，在最终 execution 之前单独评分 relation resolution，区分主要瓶颈到底是 heterogeneous access 还是 business semantics。

<!-- PROTOCOL-AUDIT-20260923:START -->

## 2026-09-23 协议核验：先看分母、提示和评分版本

官方 Pass@1 是**先计算每题的重复运行通过率，再在数据集内平均，最后对数据集平均**，不是 5 次中成功一次就算成功。提交要求每题 5 次并提供轨迹；缺失、污染或无可验证推导的运行不能从分母中任意删除。[官方方法与提交规则](https://github.com/ucbepic/DataAgentBench/blob/main/README.md)

榜单明确分开 `Tuned prompt` 与 `Hints`。例如官方表中 2026-09-11 的 Permute EQ 记录为 0.9467，2026-09-08 的 Scout 为 0.9062；两者都标注专门调过提示、使用 hints、5 次运行。这里只记录带条件的来源快照，不把系统差异归因给单个模型，也不将其与旧论文的 38% 直接相减。

评分器也发生过实质修订：官方说明 2026-06-12 按更新的验证器及 PATENTS 标准答案重算旧提交；2026-08-18 又修正 DEPS_DEV_V1 第 1 题，接受第 5 名并列的 95 个 package，而不是只接受旧标准答案中的一个。**分数变化可以来自标签与验证器修正，而不是系统进步。** 应保存数据和验证器版本、完整逐题结果、提示与轨迹，才能公平比较。

这次更新保持 DAB 原有首发日期和引用快照不变。上述 2026-09-23 是本 Radar 的协议核验日期，不是新基准发布日期；未独立复跑官方提交。

<!-- PROTOCOL-AUDIT-20260923:END -->

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究多数据库之间的发现、转换与分析，而不只是单条 SQL。小题集上的排名很容易受提示、调参、重复次数和评分版本影响；旧论文成绩应保留为历史证据，不能当作当前能力上限。

### 一个具体任务长什么样

示意任务：同一分析问题需要跨不同数据库读取数据，统一格式后连接，并把半结构化内容转换成可计算字段。数据库连接成功只是起点；字段语义和结果验证才决定问题是否完成。

### 最有判别力的实验

固定数据和验证器版本，明确是否使用提示及任务特定调参，按官方聚合规则报告多次运行。对缺失、失败和污染运行保留分母，再比较无派生表示、静态派生表示与在线更新，检验收益是否超越答案或查询缓存。

### 建议搭配

[dataspace](dataspace.md) · [spider-2](spider-2.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`single-database text-to-SQL → cross-database integration → enterprise data agent`

它第一次把 backend heterogeneity 真正放进 data-agent 评测核心。
