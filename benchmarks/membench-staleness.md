# membench（staleness）：让当前事实排在过期事实之前

**中文** | [English](membench-staleness.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[代码、场景与结果](https://github.com/Ps23102004/membench)

## 问题

面对更新、否定、实体混淆、时间范围与干扰项时，memory store 能否让当前事实排在禁止使用的 stale fact 之前？

## 证据

60 个可执行 probe 通过可插拔 write/query/reset 接口报告 recall、precision、`staleness@1`、leakage、abstention、contradiction resolution 与 Wilson interval。公开修订替换了无效的 top-k staleness，并堵住用弃答刷分的路径。Embedding baseline 在 12 个 supersession probe 中有 11 个返回 stale answer；recency reranking 将其降到 0/12。

## Caveat

基准只有 60 个彼此相关的手写 probe，使用精确 substring 评分、很小的 memory store，并且只有一位作者。Recency 的效果对 k 敏感，也没有长时程下游任务证明排序改善确实帮助 agent。

## Map

`map_delta=early_signal`，绑定 `memory-update-and-staleness`。修正后的指标适合作为 component diagnostic，还不足以构成持久领域迁移。
