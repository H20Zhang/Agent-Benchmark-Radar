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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合检验预测质量与数据科学过程遵从，而不是只追求一个好看的模型指标。规定流程被忽略时，偶然高分不代表任务完成；论文完整集合与公开子集也应明确区分。

### 一个具体任务长什么样

示意任务：用户要求使用特定数据处理或建模流程，系统需按要求生成预测，并由隐藏标签或确定性结果验证。换用另一条更容易的流程可能提高指标，却违反了实际交付要求。

### 最有判别力的实验

固定公开版本、运行预算与包环境，分别报告过程遵从和预测质量。设计结果相似但过程不同的对照，确认验证器能识别违规；训练与评测数据严格隔离，防止把训练任务效果当成泛化。

### 建议搭配

[tml-bench](tml-bench.md) · [statabench](statabench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
