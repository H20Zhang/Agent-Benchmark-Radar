# data-eng-bench：Data Agent / 可执行数据工程

**中文** | [English](data-eng-bench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[基准仓库](https://github.com/Snowflake-Labs/data-eng-bench) · [协议修复](https://github.com/Snowflake-Labs/data-eng-bench/commit/35b83370bd9ae06d9ac8a2beb95d2544c90d88a5)

把 code generation 推到 repository-scale dbt transformation 与 hidden row-level verification。

## 它接在什么之后

前一代评价通常把该问题压成较短的最终分数或单一 proxy。这个评测把 predecessor critique 变成 capability × environment × protocol 的显式差异，并保留可执行或可复核资产。

## 实际怎样评测

**问题：** Agent 能否在真实项目约束下实现、执行并修复数据转换？

**测量对象：** 面向仓库规模 dbt 转换的可执行数据工程基准，在 DuckDB 与 Snowflake 上做隐藏行级核验。

**规模与协议：** 103 dbt tasks with hidden verifier coverage across DuckDB and Snowflake. 协议包括 hidden-pytest-verifiers, row-level-output-comparison, dual-backend-execution。

## 分数能说明什么

103 dbt tasks 覆盖 DuckDB/Snowflake；hidden row-level verifiers 检查产物，而 8 月修复揭示 evaluator reliability 本身也是测量条件。 它支持的是该环境、harness、model/tool/resource configuration 下的 system-level evidence；除非其他变量匹配，否则不能把榜单差异归因给单一组件。

## 最主要的混杂因素

Snowflake verifier fix without rerun 意味着修复前 leaderboard 不能直接与修复后环境比较。 关键混杂包括 backend-environment-drift, verifier-defects, missing-post-fix-rerun。

## 还没有覆盖什么

8 月 verifier 修复后尚无公开榜单重跑，因此更早的 Snowflake 结果需要加注限制。

## 放进演化图怎么看

`map_delta=early_signal`。一篇论文只是一项 signal；持久方向判断必须由绑定同一 canonical direction key 的独立记录支撑。
