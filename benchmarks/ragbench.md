# RAGBench：benchmark 不只评 RAG，也评“怎么评 RAG”

**中文** | [English](ragbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2407.11005) · [数据](https://huggingface.co/datasets/rungalileo/ragbench)

## 它在测什么

RAGBench 提供约 100K examples、五个 industry-oriented domains 和 trace-style labels，用来评价 retrieval/generation quality 以及 RAG evaluators 本身。它关注的不只是系统答对没有，而是 evaluator 是否能给出可解释、可行动的 failure signal。

## 相比什么前进了

许多 RAG benchmark 默认 judge 是可信的。RAGBench 把 judge/evaluator 本身变成被测对象，从而暴露 faithfulness、context relevance 等自动指标在不同 domain 上的一致性与失效模式。

## 决定性证据与分数边界

大规模 labeled examples 允许直接比较 evaluator 与人工/构造标签的一致性。Evaluator score 支持“这个 judge 在当前 domain mixture 上识别某类 failure”的判断，而不是“被它评高的 RAG architecture 因果上更好”。label construction 与 source systems 仍会塑造错误分布。

## 公平比较条件

锁定 dataset/domain subset、label schema、source RAG outputs 与 evaluator prompt/model。跨 judge generation 或不同 domain mixture 的分数应独立 tracking。

## 下一步评测坐标

下一步要验证 evaluator signal 是否真的能驱动 retrieval policy 改进：例如用 failure label 触发补搜后，最终 evidence coverage 与 task success 是否可重复提升。
