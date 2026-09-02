# Spider 2.0：text-to-SQL 从 benchmark schema 走向 enterprise database workflows

**中文** | [English](spider-2.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[项目](https://spider2-sql.github.io/)

## 它在测什么

Spider 2.0 面向更接近 enterprise 的 SQL agent tasks。当前官方 families 包括 Spider 2.0-Snow、Spider 2.0-Lite 与 Spider 2.0-DBT；公开规模约为 Snow 547、Lite 547、DBT 68，并持续版本演化。任务覆盖大型 schema、多 SQL dialect、复杂 analytics 与 database-management/DBT-style work。

## 相比什么前进了

Spider 主要是静态 text-to-SQL。Spider 2.0 把 schema 规模、真实 database systems、dialect 与 multi-step operations 拉进环境，使 agent 需要探索和操作，而不只生成一条 SQL。

## 分数边界

success rate 只能绑定具体 family、release、context setting 与 evaluator。官方还存在 oracle-table 等辅助条件，这些不是 standard-agent track，不能和完整 schema-discovery 结果混排。

## 公平比较条件

锁定 Snow/Lite/DBT family、release、database version、schema/table hints、agent scaffold、step budget 与 evaluator。oracle conditions 必须单独标记。

## 下一步评测坐标

下一步从 SQL-centric workflow 推进到跨数据库、非结构化文档和业务语义，这正是 DAB / AgenticDataBench 等 benchmark 的重点。
