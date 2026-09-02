# MedMemoryBench：streaming clinical memory 的 saturation 曲线

**中文** | [English](medmemorybench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2605.11814) · [代码](https://github.com/AQ-MedAI/MedMemoryBench)

## 它在测什么

MedMemoryBench 构造 20 个 longitudinal patient personas、约 2,020 sessions、16K turns 与 1,986 个中英文 queries。它在 memory 持续构建过程中周期性 evaluation，测 clinical-state tracking、update、temporal localization、medical reasoning、noise resilience 与 saturation。

## 相比什么前进了

传统 medical QA 只看一次性病例；静态 memory QA 也不观察随时间增长的性能曲线。MedMemoryBench 用 evaluate-while-constructing protocol 直接显示随着临床信息流入，memory 何时开始退化。

## 分数边界

streaming QA 支持在 synthetic patient trajectory、medical reader 与 judge 下的 longitudinal retention；它不是 clinical deployment safety 证据，也不能说明真实 health outcome。不同 memory adapter 或 reader 会改变 saturation point。

## 公平比较条件

锁定 patient generation、stream checkpoints、reader、memory adapter、judge 与 noise setting，并按 time checkpoint 报告而不是只给最终平均。

## 下一步评测坐标

下一步应连接真实 clinical tools、provenance、consent 与 decision consequence，尤其测试过期医学状态是否能安全纠正。
