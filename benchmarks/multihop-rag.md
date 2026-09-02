# MultiHop-RAG：把 multi-hop retrieval failure 放回 RAG pipeline

**中文** | [English](multihop-rag.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2401.15391) · [代码](https://github.com/yixuantt/MultiHop-RAG)

## 它在测什么

MultiHop-RAG 构造 news-based knowledge base 与需要多份 supporting evidence 的问题，同时评价 retrieval 与 answer。它要求系统跨 hop 找到证据并组合，而不是只在最终 generation 端做 multi-hop reasoning。

## 相比什么前进了

HotpotQA 已有 multi-document QA，但 MultiHop-RAG 更直接以 RAG pipeline 为对象，把 retriever failure 与 answer failure并列观察。它使“reader 很强但第一 hop 没找到证据”的问题不会被 final answer score 完全掩盖。

## 决定性证据与分数边界

论文的关键价值是显示 single-shot retrieval 在多跳问题上存在系统性缺口。Retrieval recall 与 answer accuracy 支持 fixed news corpus/fixed pipeline 下的证据发现能力；它们不支持 live web、adaptive search policy 或 tool orchestration 的结论。若 retriever 与 reader 同时更换，端到端差值仍是 packaged evidence。

## 公平比较条件

锁定 corpus、query set、retriever-reader separation、candidate budget 与 answer evaluator。不同 corpus snapshot 或 externally searched evidence 应拆 track。

## 下一步评测坐标

下一步要允许 agent 根据已找到证据决定下一 hop，并测 stopping、query reformulation、evidence sufficiency 与搜索成本。
