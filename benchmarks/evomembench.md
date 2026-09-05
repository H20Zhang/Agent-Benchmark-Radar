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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合为不同记忆系统建立共同坐标：回合内或跨回合，知识型或执行型。它是组合评测框架，不是所有方法都处于同一个实验条件的单一任务；解读总分前，应先看收益集中在哪个坐标。

### 一个具体任务长什么样

示意任务：一种设置要求在当前长任务内保持证据，另一种要求把先前任务的经验带到新任务。两者都叫记忆，但写入时机、可见历史和最终输出不同，不宜直接用一个检索分数替代。

### 最有判别力的实验

在四个坐标分别保持相同骨干、工具和预算，报告逐坐标结果及成本。对跨回合设置加入无持久状态对照，对回合内设置加入完整上下文对照；不要让来源数据集的规模决定研究结论的权重。

### 建议搭配

[memoryagentbench](memoryagentbench.md) · [memoryarena](memoryarena.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
