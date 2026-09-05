# DataClawBench：长时间 data work 应该看 progress curve，而不只是超时前最后一答

**中文** | [English](dataclawbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2605.02503)

## 它在测什么

DataClawBench 有 492 个 tasks、7 个 categories，每题包含 2–9 个 gold milestones，底层约 2.06M 条真实 records，并给 agent 最长约 1,200 秒 budget。evaluation 同时看 milestone progress、final correctness 与 efficiency，因此可以观察长任务在何处停滞。

## 相比什么前进了

很多 Data Agent benchmark 只给 binary final success。DataClawBench 把 partial progress 变成显式信号，使“已经完成数据发现/清洗但卡在最后分析”和“从一开始就没走对”不再同为 0。

## 分数边界

progress/final/efficiency 支持当前 milestone annotations、records 与 time budget 下的 long-horizon performance；gold milestones 不是唯一有效 workflow，因此 path-sensitive interpretation要谨慎。

## 公平比较条件

锁定 1,200s/step/tool budget、task data、milestone version、runtime、agent scaffold 与 final evaluator。

## 下一步评测坐标

下一步应允许 multiple valid workflows，并用 counterfactual intervention 判断哪些 milestone 真正决定 final success。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究在先验提示很少、原始数据有噪声时的自主探索。里程碑进度可以区分有效调查与无目的调用，但命中里程碑并不必然意味着最终结论正确；领域与时间范围也限制外推。

### 一个具体任务长什么样

示意任务：系统进入陌生金融数据环境，自主发现表、文档和相关政策，再逐步形成可验证结论。探索过程中可能找到正确来源，却误解字段或过早停止，需同时观察中间进度和终点。

### 最有判别力的实验

固定工具、网页访问政策和时间预算，比较完全自主、正确来源提示与正确模式提示。联合报告里程碑进度、最终正确性和时间，并复核高进度低正确率样本，定位探索与推理之间的断点。

### 建议搭配

[kramabench](kramabench.md) · [ddr-bench](ddr-bench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
