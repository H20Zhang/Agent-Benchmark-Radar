# FDABench：Data Agent 的对象从 database query 扩到 heterogeneous analytical workflow

**中文** | [English](fdabench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[项目页](https://fdabench.github.io/) · [代码](https://github.com/fdabench/FDAbench)

## 它在测什么

FDABench 含 2,007 个 analytical tasks、50+ domains，覆盖 structured databases、documents、web、images、video 与 audio，并支持 single-choice、multiple-choice 与 report generation。官方框架提供 planning、tool-use、reflection、multi-agent 等 agent patterns，以及 DAG-based reasoning trace、accuracy、rubric report、latency/token/cost metrics。

## 相比什么前进了

Spider/BIRD 主要在数据库内回答问题；DataSciBench 扩展 data-science coding。FDABench 把数据源异构性和 report artifact 放进同一 suite，使 agent 需要选择工具、跨源分析并交付可评价结果。

## 分数边界

choice/report score 支持完整 agent system 在指定 task/data/tool setup 下的 analytical quality；不同 workflow pattern、model、tool availability 与 cost budget 都会改变结果，因此不能把一个 overall accuracy 归因给 planning 或 multi-agent 机制。

## 公平比较条件

锁定 Full/Lite data release、database/source availability、agent workflow、model、max rounds、evaluator、token/cost policy。report、single-choice、multiple-choice 应分 track。

## 下一步评测坐标

下一步需要更强的 business semantic truth、artifact correctness 与 repeated operational workflows，避免“报告写得像”替代真实业务正确性。
