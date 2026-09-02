# EvoMemBench：用 scope × content 统一比较 memory systems

**中文** | [English](evomembench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2605.18421) · [代码](https://github.com/DSAIL-Memory/EvoMemBench)

## 它在测什么

EvoMemBench 用两条轴组织 memory：in-episode vs cross-episode，以及 knowledge-oriented vs execution-oriented。发布套件含 5,754 samples、六个 settings，paper 比较 15 个代表性 memory methods，同时报告 answer/execution success 与 token efficiency。

## 相比什么前进了

memory literature 常在不同源 benchmark 上各自报告结果，导致“方法 A 更强”其实可能只是 task 类型不同。EvoMemBench 的核心增量是统一 taxonomy 与 comparison protocol，把 declarative knowledge 与 procedural/tool-use experience 放在同一个坐标系中。

## 分数边界

跨方法比较提高了可读性，但 suite 聚合了 heterogeneous source benchmarks，因此 aggregate rank 仍会受 source mixture、preprocessing 与 task backbone 影响。它适合说明 coverage profile，不适合把单一总分解释为 universal memory quality。

## 公平比较条件

锁定 source benchmark version、preprocessing、backbone、agent harness 与 long-context budget，并同时报告四个 scope/content cells，而不是只给 aggregate。

## 下一步评测坐标

下一步需要同一个 controlled environment 内同时产生四类 memory demand，从而进行真正 matched 的 component comparison。
