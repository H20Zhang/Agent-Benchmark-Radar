# DA-Code：在真实数据上生成 grounded executable data-science code

**中文** | [English](da-code.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2410.07331) · [项目页](https://da-code-bench.github.io/)

## 它到底测什么

DA-Code 在真实、diverse data 上评估 **grounded executable data-science code**，覆盖较难的 data wrangling、exploratory analysis 与 machine-learning operation，并放在可控 execution environment 中验证。

## 相比此前评测多测了什么

DS-1000 更偏 realistic library-level coding problem；DA-Code 把工作单位往 agentic analysis 推进：任务必须 grounded 到给定 dataset，规划多步 operation，并通过较复杂的数据科学程序产出目标答案，而不只是补一个局部 code hole。

## 决定性证据

benchmark 的 evaluation suite 由 annotator 仔细设计，以保证 executable checking 的准确与鲁棒。论文实验里即使用当时最强 LLM，accuracy 也只有 30.5%，说明在可客观执行验证的任务上仍有很大 gap。

## 这个分数能证明什么

DA-Code 支持 bounded analysis task 上 grounded program synthesis，但仍不等于完整 data-agent loop：发现问题、长期观察中间结果、维护 project state、交付用户 artifact 都不是核心对象。

## 公平比较契约

应固定 data file、runtime/library version、allowed language/tool、execution budget、retry policy 与 answer evaluator，并区分 one-shot generation 与 iterative repair；给 execution feedback 会实质改变任务。

## 还没有测什么

repository-scale engineering、heterogeneous documentation、business semantics、long-lived state 与 open-ended insight discovery 都超出核心 benchmark。

## 下一步最有判别力的验证

构造 paired task：同一目标分别要求 one monolithic program 与 multi-step inspect-and-repair workflow，直接测 agentic iteration 相比更强 code generation 的额外价值。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究面向真实数据的规划与可执行代码，而不是只评语言形式。清洗、探索和建模的结果类型不同；一个总体正确率不足以说明方法改善的是数据理解、代码生成还是故障恢复。

### 一个具体任务长什么样

示意任务：系统根据任务数据构造处理流程，可能先修正类型或缺失值，再进行分析或训练。代码能运行却悄悄丢弃关键行，仍可能使最终结果偏离要求。

### 最有判别力的实验

固定数据与运行环境，按清洗、探索和机器学习分别报告，并加入正确数据摘要给定条件。限制并对齐调试次数，单独记录代码成功执行和结果正确，防止把运行率当作分析质量。

### 建议搭配

[ds-1000](ds-1000.md) · [datascibench](datascibench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`library-level code → grounded multi-operation analysis code → iterative data-analysis agent`

DA-Code 是 executable coding benchmark 与完整 data-agent workflow 之间的一座桥。