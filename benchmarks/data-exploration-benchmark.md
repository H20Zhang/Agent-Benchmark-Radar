# Data Exploration Benchmark：先探索数据，才能知道后面的分析到底建立在什么 schema 上

**中文** | [English](data-exploration-benchmark.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.16045)

## 它在测什么

Data Exploration Benchmark 直接评估 agent 在分析前的 data exploration。当前 suite 包含一个真实 Vitamin-D multi-sheet workbook，以及 12 个 DSBench workbook tasks（4 easy、5 medium、3 hard），要求系统理解 sheets、columns、relationships 与 data quality，并生成 schema-fixed JSON exploration artifact。

## 相比什么前进了

大量 Data Agent benchmark 默认 agent 已经知道正确 schema 或相关表。这里把“先看清数据是什么”设为单独 stage，并通过 raw/self-exploration/oracle-exploration downstream ablation 检查探索质量是否真的影响后续任务。

## 分数边界

artifact score 与 downstream delta 支持在 workbook-style data、固定 schema 与 evaluator 下的 exploration quality；它不说明 large database/data lake discovery 已解决，且 oracle exploration 只是 upper bound。

## 公平比较条件

锁定 workbook release、exploration JSON schema、token/tool budget、downstream agent 与 evaluator。raw/self/oracle conditions 应单独报告。

## 下一步评测坐标

下一步要扩到大规模多源 catalog、权限和 schema drift，并测试 exploration artifact 是否能被持续更新而不是一次性生成。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究先理解数据再分析的中间表征，尤其是混乱工作簿中的逻辑表、键和列语义。规模小且表格特定，适合作为机制诊断；中间摘要写得完整，不等于它对下游任务真正有帮助。

### 一个具体任务长什么样

示意任务：一个工作簿中包含多个逻辑表、合并表头和隐含关系，系统先生成结构化理解，再处理分析问题。若把展示区域误当作数据表，后续查询即使执行正确也可能使用错误数据。

### 最有判别力的实验

保留原始数据、系统生成探索结果和 oracle 探索结果三种条件，固定下游分析器。逐项检查键、关系与质量问题，并在不同工作簿上验证；计入探索成本，判断可复用表征何时值得预先构建。

### 建议搭配

[kramabench](kramabench.md) · [dataspace](dataspace.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
