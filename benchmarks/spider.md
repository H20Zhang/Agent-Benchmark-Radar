# Spider：从单表 SQL 走向 unseen database 的 compositional generalization

**中文** | [English](spider.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

## 它在测什么

Spider 包含 10,181 个 questions、5,693 条 unique complex SQL，覆盖 200 个 databases 与 138 个 domains。train/test 按 database 切分，系统必须对从未见过的 schema 生成 joins、nested queries、aggregation 等复杂 SQL。

## 相比什么前进了

WikiSQL 主要是单表操作且 train/test schema 高度相似。Spider 把 cross-database generalization 与 multi-table compositional SQL 设为核心，使 schema grounding 本身成为难点。

## 分数边界

execution/exact-match 支持在静态 relational schema 上的 text-to-SQL generalization；它不测数据库探索、外部文档、业务规则、写操作或多轮 analysis。更强 prompt/schema linking 也会改变 comparison contract。

## 公平比较条件

锁定 Spider version、schema/value access、execution evaluator、test DBs 与是否允许 external retrieval。不同 schema hints 不能直接混排。

## 下一步评测坐标

BIRD 增加大规模真实数据库与 external knowledge；Spider 2.0 再把任务扩到 enterprise SQL、multi-dialect 与 database operations。
