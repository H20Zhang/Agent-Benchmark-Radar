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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合从混乱异构文件湖出发研究数据发现与流程构造。完整输入、裁剪输入和 oracle 输入代表不同发现难度；只在相关文件已经筛好的条件下提升，不能证明系统更善于理解真实数据湖。

### 一个具体任务长什么样

示意任务：请求的答案需要从许多文件中找到相关数据，清洗并连接后构造分析流程。某个子任务的代码写对了，但选错文件或误解列含义，仍会让整个数据到洞察链路失败。

### 最有判别力的实验

对相同任务比较完整文件湖、正确文件集合和正确中间表三种输入，逐子任务记录产物。固定模型与预算，计算发现成本和重复查询的摊销收益，检验预构建表示是否真正提高后续任务效率。

### 建议搭配

[dataspace](dataspace.md) · [data-exploration-benchmark](data-exploration-benchmark.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
