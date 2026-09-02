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
