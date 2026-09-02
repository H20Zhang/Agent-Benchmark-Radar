# DARE-bench：real-world data transformation 需要 exact outputs，而不是 judge impression

**中文** | [English](dare-bench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

## 它在测什么

DARE-bench 的 paper 描述约 6,300 tasks（5,948 train + 352 eval），当前 public repo 规模较小（约 4,274 train + 324 eval）。任务来自真实数据变换/建模需求，并用 exact reference outputs、macro-F1 或 clipped-R² 等 executable/data metrics，多次运行观察稳定性。

## 相比什么前进了

开放式 Data Agent benchmark 常依赖 LLM judge。DARE-bench 更接近“给定 raw data，产出可验证 target artifact”，使 transformation correctness 与 stochastic agent behavior 可以直接量化。

## 分数边界

exact/numerical metrics 支持当前 task/data release 下的 artifact correctness；paper/public repo 规模差异本身要求版本化，不能把结果跨 release 混排。

## 公平比较条件

锁定 task release、runtime/packages、reference outputs、number of runs、agent scaffold 与 resource budget。

## 下一步评测坐标

下一步应在 exact artifact 之外加入 source discovery、business semantics 与 downstream use，避免只验证“输出匹配”而忽略分析目标是否正确。
