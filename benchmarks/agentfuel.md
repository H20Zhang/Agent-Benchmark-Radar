# AgentFuel：stateful analysis 的价值要通过跨 query 复用来证明

**中文** | [English](agentfuel.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2603.12483)

## 它在测什么

AgentFuel 当前包含 72 个 queries，来自 3 个 time-series domains、每域 24 个，其中 12 stateless、12 stateful/incident-oriented；生成数据约 13.5MB。它比较每个 query 从零开始和保留前序分析 state 的 agent，测试跨查询 state reuse 是否提升复杂 incident analysis。

## 相比什么前进了

多数 benchmark 把每个任务独立运行。AgentFuel 将 persistence 设为实验变量，直接问 notebook/context/memory state 是否减少重复探索并提高后续 query 质量。

## 分数边界

stateful advantage 支持在当前 synthetic time-series generation 与 query order 下的 reusable analysis state；公开 artifact 尚缺完整数据生成实现会限制复现，而且收益可能来自简单 cache 而不是更深 semantic memory。

## 公平比较条件

锁定 query order、state persistence policy、data generator、agent scaffold、model、budget 与 evaluator，并将 stateless/stateful matched pairs 一起报告。

## 下一步评测坐标

下一步应区分 cache、structured semantic state 与 learned workflow experience，并测试 stale state 在数据更新后是否反而伤害分析。
