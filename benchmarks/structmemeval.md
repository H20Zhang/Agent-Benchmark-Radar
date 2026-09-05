# StructMemEval：评估 agent 如何组织 memory，而不只是找事实

**中文** | [English](structmemeval.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2602.11243)

## 它到底测什么

StructMemEval 测 agent 能否选择并维护 **适合任务的 memory structure**，例如 transaction ledger、to-do list、tree，而不是把所有信息塞进无结构 store 后再做通用 retrieval。这里真正被测的是 representation organization。

## 相比此前评测多测了什么

fact retention、multi-hop recall、temporal update 很多时候都可以用 generic RAG 解。StructMemEval 专门选择天然依赖某种组织方式的任务，让 memory structure 本身变成可观测能力，而不再只是 implementation detail。

## 决定性证据

论文初步实验显示 simple retrieval-augmented LLM 在这些结构任务上较弱；如果显式提示正确 organization，memory agent 可以可靠完成，但现代 LLM 在没有提示时并不总能识别应该采用哪种结构。这把 **执行已知 representation** 和 **发现正确 representation** 两件事拆开了。

## 这个分数能证明什么

benchmark 能证明 structured state 是否有用、系统是否能实例化指定结构；如果 prompt 已经透露正确 structure，它对 autonomous representation learning 的证明就比较弱。

## 公平比较契约

应固定 backbone、task instruction、是否提供 structure hint、memory operation 与 token/storage budget，并把 oracle structure hint 与 autonomous selection 分开报告，否则最重要的研究问题会被掩盖。

## 还没有测什么

任务集有意偏窄，结构也都是人类可解释的。真实 agent 可能需要 hybrid / learned representation，并且 workload 变化后还要迁移结构；这些能力尚未覆盖。

## 下一步最有判别力的验证

隐藏 structure identity，加入多种合理 representation 都能工作的任务，并在 query distribution shift 后测 adaptation。真正的问题不是“会不会用 ledger”，而是“知不知道什么时候 ledger 才是正确表示”。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合检验记忆组织是否影响任务完成，尤其适合表、清单、树等显式结构研究。最重要的区分是‘会使用已指定的结构’与‘能自主发现适合的结构’；带结构提示的成绩不能替代后者。

### 一个具体任务长什么样

示意任务：多轮输入包含新增、撤销与调整事项，系统需要维持一份可查询的有效状态。流水记录保存了所有话语，却未必像交易账本或树结构那样直接支持后续运算。

### 最有判别力的实验

分开报告无结构提示、自主选择结构与给定正确结构三种条件。让输入内容相同，只改变后续查询类型，观察系统是否迁移结构；将迁移成本和错误状态修复纳入评价，才能判断组织机制是否真正自适应。

### 建议搭配

[memoryagentbench](memoryagentbench.md) · [kbgym](kbgym.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`retrieve facts → maintain structured state → autonomously choose memory representation`

它把 representation selection 单独提升成了一项 memory 能力。