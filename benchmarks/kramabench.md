# KramaBench：真实 Data Agent 先要在 data lake 里找到、清理并整合数据

**中文** | [English](kramabench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[项目页](https://kramabench.org/)

## 它在测什么

KramaBench 含 104 个 tasks、633 subtasks、1,764 files（约 1.7GB）、24 个 sources、6 个 domains。agent 需要在 data lake 中 discovery、cleaning、integration、analysis、modeling，而不是预先得到一张整理好的表。

## 相比什么前进了

多数 benchmark 从“data 已经找到”开始。KramaBench 把 file/source discovery 和 heterogeneous integration 放在 workflow 前半段，使 data selection 错误与 downstream analysis 错误都可被观察。

## 分数边界

subtask/task completion 支持该 data-lake artifact、tooling 与 harness 下的 end-to-end workflow；它不直接说明哪种 catalog/retrieval/cleaning mechanism 因果更优。

## 公平比较条件

锁定 file corpus、source connectors、tool set、subtask definitions、agent budget 与 evaluator。给 agent 额外 schema/catalog hints 会改变 measurement object。

## 下一步评测坐标

下一步应增加 access control、schema drift、incremental data updates 与 derived artifact lineage，使 data lake 更接近长期生产环境。
