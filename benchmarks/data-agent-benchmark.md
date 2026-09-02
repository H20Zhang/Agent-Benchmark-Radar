# Data Agent Benchmark (DAB)：真正的 enterprise data question 往往跨多个 DBMS 与数据形态

**中文** | [English](data-agent-benchmark.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2603.20576) · [代码与榜单](https://github.com/ucbepic/DataAgentBench)

## 它在测什么

DAB 有 54 个 queries、12 个 datasets、9 个 domains、4 个 DBMS（PostgreSQL、MongoDB、SQLite、DuckDB）。任务来自 enterprise workload study，集中测试 multi-database integration、ill-formatted key joins、unstructured-text transformation 与 domain knowledge，而不是只把自然语言翻译成一条 SQL。

## 相比什么前进了

Spider/BIRD 假设主要事实在一个 relational database 内。DAB 让同一个问题跨 database systems、异构 key 和文本字段，迫使 agent 做 integration、transformation 与 analysis，measurement object 更接近企业数据问题本身。

## 当前成绩如何解释

官方 leaderboard 用 Pass@1，并要求提交至少 5 trials/query；官方页面还会用当前 validators 重新计算历史 submissions。因此 result track 必须保存 recompute/protocol date，而不能只抄 submission 当天数字。高 Pass@1 支持完整 agent stack 在 54-query suite 下的可靠性，不定位 integration、reasoning 或 model 的单一贡献。

## 公平比较条件

锁定 dataset/ground-truth revision、validators、trials/query、是否使用 hints、DBMS versions、agent scaffold 与 model mix。5-trial submissions 与 50-trial paper baselines应分 protocol。

## 下一步评测坐标

DAB 已覆盖跨库复杂性，但 query 数仍少。下一步需要更多真实 schema drift、permissions、writes、analyst artifacts 与业务语义 correctness。
