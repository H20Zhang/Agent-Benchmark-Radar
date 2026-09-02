# DSAEval：累积式、多模态 data-science project

**中文** | [English](dsaeval.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2601.13591) · [项目页](https://dsaeval.github.io/DSAEval/)

## 它到底测什么

DSAEval 评估 **真实 data-science project**：包含 multimodal environment perception、cumulative multi-query interaction，并分别评分 reasoning、code 与 result。共有 641 个问题、285 个 structured/unstructured dataset。

## 相比此前评测多测了什么

one-shot coding task 每题都会 reset；DSAEval 让后续 query 依赖此前分析，并把 observation 从 table 扩展到 image/text data，更接近连续的数据科学工作 session。

## 决定性证据

论文评估 11 种先进 agentic LLM：Claude-Sonnet-4.5 overall 最强，GPT-5.2 efficiency 最好，MiMo-V2-Flash cost-effectiveness 最好；multimodal perception 对 vision-related task 带来 2.04–11.30% 提升。structured/routine analysis 明显比 unstructured workload 容易。

## 这个分数能证明什么

benchmark 支持 cumulative project competence，并暴露 quality–efficiency–cost trade-off；但 model/scaffold 仍是一个组合系统，multi-dimensional grading 也可能包含 deterministic execution 之外的 evaluator assumption。

## 公平比较契约

应固定 dataset、query order、accumulated workspace state、tool environment、model、budget 与 evaluator，并精确保留 prior-query output；如果不同系统采用不同 reset/summary 策略，累计任务本身已经变了。

## 还没有测什么

真实项目会跨数周，有 stakeholder feedback、data update、version control 与 production deployment；这里的 cumulative interaction 仍是 bounded benchmark episode。

## 下一步最有判别力的验证

在早期分析里人为注入可控错误，测后续 recovery 与 error propagation，验证 agent 是否维护可信 analytical state，而不只是累积 conversation context。

## 演化位置

`one-shot data analysis → cumulative multimodal project → persistent analytical state`

它把跨请求的 state continuity 变成 data-agent 的显式能力。