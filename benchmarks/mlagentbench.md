# MLAgentBench：从“会写 ML code”推进到 iterative experimentation

**中文** | [English](mlagentbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2310.03302) · [代码](https://github.com/snap-stanford/MLAgentBench)

## 它在测什么

MLAgentBench 设计 13 个 machine-learning experimentation tasks，agent 需要读已有实验资产、提出修改、写/执行代码、检查结果并迭代，而不是一次生成最终程序。evaluation 关注能否在给定 compute/time budget 内改善目标 metric。

## 相比什么前进了

DS-1000 测局部 code correctness。MLAgentBench 把 data science 改写成 sequential experiment loop，使 planning、execution、observation 与 iteration 的耦合成为评测对象。

## 分数边界

最终 metric improvement 支持 agent 在给定 task repo、compute、baseline 与 scaffold 下开展实验；它不等于 general data analysis，且不同 hardware/time budget 会直接改变可探索空间。

## 公平比较条件

锁定 task repository/version、baseline、compute/time budget、agent scaffold、model 与 retry policy。多轮实验数量应和结果一起报告。

## 下一步评测坐标

后续 benchmark 应扩大 task diversity，并把实验 validity、artifact quality 与可解释报告纳入，而不仅是最终 metric。
