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
