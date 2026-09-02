# Agent Memory Bakeoff：跨词汇检索与写入时增强

**中文** | [English](agent-memory-bakeoff.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[代码、数据与协议](https://github.com/JaysonRawlins/agent-memory-bakeoff)

## 它到底测什么

这个 benchmark 测的是 **memory write representation 是否改变未来可访问性**：当后续 query 不再复用原 incident / runbook 的词汇时，系统还能不能找回相关记忆；以及在写入时做 enrichment，是否比原文直接存储更能跨越 lexical mismatch。它把 memory pipeline 里经常被忽略的 write-side representation 变成可控变量。

## 相比常规 memory benchmark 多测了什么

LoCoMo / LongMemEval 一类 benchmark 更多从最终 QA 看“记住了没有”，但 retrieval failure 与 answerer failure 很容易混在一起。Agent Memory Bakeoff 停在 retrieval 层，交叉比较 **BM25、vector、hybrid retrieval × plain / write-enriched memory**，因此可以更直接地问 enrichment 是否真的让同一事实更容易被不同表达方式访问。

## 决定性证据

套件包含 **225 个场景、497 份合成记忆文档和 390 个独立生成查询**，采用 sibling-aware gold，报告 MRR@10 与 recall@1/@5。写入增强把 **BM25 MRR 从 0.678 提升到 0.783**，并把 symptom query 的 **recall@5 从 60.0% 提升到 83.8%**。这一结果说明在所构造的 lexical-shift 场景中，write-time enrichment 能显著改变传统 lexical retriever 的可访问性。

## 这个分数支持什么判断

它支持“在该 synthetic corpus 和一个本地 embedder 下，写入增强提高了跨词汇 retrieval accessibility”。它不支持“下游 agent 一定回答或行动得更好”，因为 protocol 终止于 retrieval；也不能证明 enrichment 普遍优于更强的 embedding / reranker，因为语料本身围绕 enrichment 机制构造。

## 公平比较条件

比较不同 write representation 时，应固定 query set、gold definition、retrieval top-k、embedder、BM25 配置和文档粒度。尤其不能一边改变 memory enrichment，一边更换 embedder 或 reranker，再把全部增益归因于 write-side mechanism。最好分别报告 lexical、semantic 与 hybrid retriever，观察 enrichment 的收益是否只集中在某一种 retrieval family。

## 研究上怎么用

它适合做 **memory component attribution**：当一个 memory system 声称“写入阶段做摘要、实体扩展或语义重写可以改善未来 recall”时，可以先用这个层级的 retrieval-only benchmark 隔离验证，再进入 LongMemEval/MemoryAgentBench 等 downstream benchmark 看 accessibility 是否真的转化为 task utility。

## 下一步最有价值的验证

最关键的缺口是自然语料、多 embedder、多 query distribution，以及 retrieval gain 是否传导到最终 answer / action。一个高判别力实验是：在相同 memory corpus 和 query 上，对比 write enrichment、query expansion、reranking 三种 intervention 的等预算收益，回答“应该把计算花在写入、查询还是读取阶段”。

## 谱系位置

`map_delta=early_signal`，绑定 `memory-component-attribution`。它增加了可控的 write-side intervention coordinate，但还不足以修改持久记忆主干；真正的 durable shift 需要证明 write representation 对跨任务、跨模型的长期 utility 有稳定增益。
