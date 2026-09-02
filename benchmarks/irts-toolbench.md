# IRTS-ToolBench：irregular time series 的难点是先把时间轴处理对，再谈分析

**中文** | [English](irts-toolbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2606.15107)

## 它在测什么

IRTS-ToolBench 包含 1,700 个 questions、10 种 tasks、13 个 domains，并提供 30 个 tools：7 个 irregularity-handling operations 与 23 个 analytical tools。agent 需要先处理不规则采样、缺失/时间对齐，再完成统计或预测分析。

## 相比什么前进了

普通 time-series benchmark 往往给已规整矩阵。IRTS-ToolBench 把 preprocessing/tool routing 设为 agent responsibility，使“时间序列本身没处理对”与后续 analytical method failure 可以区分。

## 分数边界

task success 支持当前 irregularity generator、tool library 与 data domains 下的 tool-use competence；它不证明对真实 sensor/finance systems 的 robustness，因为 drift、streaming 和 operational latency 被弱化。

## 公平比较条件

锁定 task/domain split、tool library/version、irregularity pattern、agent budget、runtime 与 grader。

## 下一步评测坐标

下一步应加入 streaming updates、concept drift 与 delayed labels，评价 agent 是否能维护持续时间状态而非一次性清洗数据。
