# DreamBench-SWE

## 它到底测什么

DreamBench-SWE 测的是 **跨会话软件工程中的 memory hygiene**：后续代码任务需要决定，早期会话留下、而且无法从当前 repository 状态重新推断的证据，现在是否仍然 current、scoped、authorized / relevant；该用时要正确利用，不该用时要抑制。最终修改由隐藏可执行 oracle 评分，因此 memory 的影响落到真实代码 action，而不是停留在 QA。

## 相比前身多测了什么

MemoryArena / WorldMemArena 已经把 memory 与后续行动连接起来，SWE-bench 则提供真实可执行代码任务。DreamBench-SWE 将两者交叉成 **repository-continuation memory trap**：控制早期会话给了什么、当前 repo 能重新推出什么，以及哪些旧证据在 successor task 中已经失效。后来出现的 Agent Memory Bench (coding agents) 使用真实仓库，构成外部有效性的互补对照。

## 决定性证据

v2 的每个完整 condition 包含 **60 traps × 3 seeds = 180 个 S3 cells**。successor 中 B0 为 **21/180**，B5 为 **82/180**，typed-plus-raw reference probe 为 **83/180**，一个 pinned Mem0 literal-storage 配置为 **97/180**；所有可用 memory-vs-B0 比较在 Holm 校正后都拒绝零假设。核心结论是 benchmark 对“保留了可用历史证据”这一 treatment 有足够区分力。

## 这个分数支持什么判断

这些结果支持 DreamBench-SWE 是一个有区分力的、可执行的 memory profile benchmark，也支持“某些任务如果没有跨会话证据几乎无法完成”。它不支持 B5、typed-plus-raw、Mem0 等 memory-bearing condition 之间的机制优越性或等价性，更不能直接外推到一般 coding product，因为 memory configuration 与 coding harness 一起构成 treatment。

## 公平比较条件

需要固定 wake/judge/model stack、coding harness、tool permissions、filesystem/network access、trap set、seed、memory injection format 和 oracle。尤其要区分 **memory availability** 与 **memory policy quality**：如果一个 condition 拿到了更多原始证据，胜过 B0 只能说明历史信息有价值，不说明某种 memory architecture 更好。

## 研究上怎么用

它适合验证 coding-agent memory 的三个不同 claim：第一，跨会话保留的信息是否真的能改变 future action；第二，旧信息失效后能否抑制 harmful reuse；第三，scope / authorization metadata 是否影响正确行为。研究者应分别报告 use-when-needed、suppress-when-invalid 和最终 executable success，而不是只给一个总体成功率。

## 下一步最有价值的验证

当前缺口是生产级真实 repository、跨模型 / 跨 harness 迁移，以及 C9/C10 缺乏 B0 headroom，因此暂时不能做广义 rejection / abstention 结论。最高杠杆验证是把同一 memory-hygiene protocol 移到真实 repo continuation 上，并让不同 coding harness 在相同 evidence access 下比较，分离 benchmark trap 与 harness-specific effect。

## 谱系位置

它把“过去记忆是否帮助后续行动”继续拆成：retained evidence 是否仍然 **current、scoped、authorized / relevant，以及何时应该被抑制**；`map_delta=early_signal`。这是从 memory QA 走向 action-grounded lifecycle evaluation 的一个重要但仍待外部复现的坐标。

Primary: https://arxiv.org/abs/2608.20664

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合检查多会话编码记忆的作用域、权威性、过期处理与错误经验拒绝。它的价值不只是任务成功，而是用不可从当前仓库推断的历史证据和隐藏检查器检验记忆是否必要；构造场景仍限制外推。

### 一个具体任务长什么样

示意任务：早期会话确定一个有效规则，之后出现冲突或作用域不同的经验，最终编码任务要求采用正确的那条。保存全部内容并不够，系统必须判断哪项记忆有权影响当前修改。

### 最有判别力的实验

保留无记忆与确定性原样记忆两种强对照，按陷阱类型报告结果和无记忆余量。对于无记忆也能完成的类型，不应声称测出了记忆收益；按任务而非单次随机运行聚类估计不确定性。

### 建议搭配

[agent-memory-bench-coding](agent-memory-bench-coding.md) · [memtrapbench](memtrapbench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
