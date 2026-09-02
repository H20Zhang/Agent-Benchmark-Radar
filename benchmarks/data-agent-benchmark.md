# Data Agent Benchmark (DAB)：跨异构数据库回答企业数据问题

**中文** | [English](data-agent-benchmark.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2603.20576) · [项目页](https://ucbepic.github.io/DataAgentBench/) · [代码](https://github.com/ucbepic/DataAgentBench)

## 它到底测什么

DAB 评估 enterprise data question 在 **多个异构 database system** 之间分散、引用不一致、部分信息还藏在 unstructured field 时，agent 能不能完成整合、转换与分析。

## 相比此前评测多测了什么

Text-to-SQL 通常假设一个 database 和已知 schema。DAB 同时覆盖 PostgreSQL、MongoDB、SQLite、DuckDB，把“数据到底在哪、不同系统里的 reference 怎么对应”也变成 task。

## 决定性证据

benchmark 有 54 个 query、12 个 dataset、9 个 domain、4 类 DBMS，设计来自 6 个行业 enterprise workload 的 formative study。论文报告最好的 frontier model Gemini-3-Pro pass@1 也只有 38%，说明即使 query 数不大，跨系统整合仍远未解决。

## 这个分数能证明什么

它支持 heterogeneous backend 下 enterprise data QA 的 end-to-end 判断，但不能直接说失败来自 semantic mapping、integration、transformation、SQL/NoSQL generation 还是 answer synthesis，除非进一步看 trajectory。

## 公平比较契约

必须固定 database snapshot、credentials/access、tool interface、model、retry policy 与 trial 数；leaderboard 本身要求每题至少 5 次。应报告 pass@1 和 variance，不能用 best-of-n 掩盖 stochastic instability。

## 还没有测什么

任务数量小、主要是 read。生产 data agent 还会遇到 permission、write、lineage、semantic layer、schema evolution、成本约束与 business ambiguity。

## 下一步最有判别力的验证

给每题增加 ground-truth integration/semantic plan，在最终 execution 之前单独评分 relation resolution，区分主要瓶颈到底是 heterogeneous access 还是 business semantics。

## 演化位置

`single-database text-to-SQL → cross-database integration → enterprise data agent`

它第一次把 backend heterogeneity 真正放进 data-agent 评测核心。