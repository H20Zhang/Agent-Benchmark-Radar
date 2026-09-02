# LiveSQLBench：在 schema 与 business-rule drift 下评估 SQL agent

**中文** | [English](livesqlbench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[项目页](https://livesqlbench.ai/) · [代码](https://github.com/bird-bench/livesqlbench)

## 它到底测什么

LiveSQLBench 面向 **持续演化的 industrial database**，而不是一份冻结 schema。它强调超大 schema、长 metadata/context、business-rule drift，以及 query 与 management-style interaction。

## 相比此前评测多测了什么

Spider/BIRD 主要冻结 database 与 task distribution；LiveSQLBench 把 temporal change 放进 benchmark lifecycle：schema complexity 增长、business rule 改变，agent 必须读取当前 context，而不能依赖 benchmark memorization。

## 决定性证据

LiveSQLBench-Large-v1 扩展到 18 个 database、每个约 1K column、480 个任务，平均 prompt 约 84K token，并显式加入 Business Rule Drift；项目还发布 per-task DB isolation、multi-provider 的 agent framework。

## 这个分数能证明什么

结果支持特定 evolving snapshot 下 text-to-SQL/data-agent robustness，但不能拆开 model reasoning、schema linking 与 harness quality；live benchmark 的不同版本也必须严格 pin 住才能比较。

## 公平比较契约

应固定 benchmark release、DB snapshot、business-rule document、SQL dialect、agent framework、model 与 execution budget。不同演化版本的分数不能假装来自同一个 static test set。

## 还没有测什么

enterprise analytics 还包括 semantic definition、permission、lineage、clarification、write safety 与 artifact delivery；超大 schema 也无法完全复刻组织内部 metadata/governance。

## 下一步最有判别力的验证

为 schema/business rule 更新前后构造 paired task，测 update latency：agent 多快能停止使用 obsolete semantics，同时保留不该变化的稳定知识。

## 演化位置

`static text-to-SQL → industrial-scale schema → continuously evolving data environment`

它把 benchmark freshness 本身变成了 data-agent 评测的一部分。