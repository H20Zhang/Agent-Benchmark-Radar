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

## 演化位置

`library-level code → grounded multi-operation analysis code → iterative data-analysis agent`

DA-Code 是 executable coding benchmark 与完整 data-agent workflow 之间的一座桥。