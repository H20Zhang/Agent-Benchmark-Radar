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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合检验不规则采样时序中的时间推理与工具选择。规则网格上的方法可能隐含插值或同步假设；答案正确之外，还要确认选择的工具没有抹掉具有信息量的观测间隔。

### 一个具体任务长什么样

示意任务：观测时间间隔不均匀，系统需判断变化趋势或事件模式，并选择适用的分析工具。直接把相邻记录当作等时间间隔，可能得到计算可运行但时间含义错误的结果。

### 最有判别力的实验

对同一底层信号改变采样模式，比较原时间戳、规则化插值与不规则工具，保持问题和预算一致。评分时允许功能等价的工具组合，并区分工具选择错误、参数错误与问题格式捷径。

### 建议搭配

[agentfuel](agentfuel.md) · [statabench](statabench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
