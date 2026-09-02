# RAGTruth：把 RAG hallucination 从 answer-level 拉到 word-level

**中文** | [English](ragtruth.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2401.00396)

## 它在测什么

RAGTruth 收集近 18K 条自然生成的 RAG responses，并由人工在 case 与 word level 标注 hallucination 与严重程度。它的测量对象是生成结果相对 retrieved evidence 的局部 grounding failure，而不是只给整段回答一个 faithful/unfaithful 标签。

## 相比什么前进了

早期 hallucination evaluation 常依赖自动 judge 或粗粒度 answer labels。RAGTruth 提供细粒度人工标注，使 detector 可以定位哪一段文字超出了证据，并比较不同领域和 source LLM 的 hallucination pattern。

## 决定性证据与分数边界

它证明“RAG 生成了看似正确的长回答”仍可能包含局部、不同严重度的 unsupported spans。Detector 分数支持 hallucination detection under the annotated distribution；它不衡量 adaptive retrieval policy，也不能把 hallucination 率变化直接归因给 retriever，因为 source LLM 与 retrieval setup 都是 confounders。

## 公平比较条件

锁定 source-response set、annotation policy、severity definition 与 detector input。换一批生成模型或 retrieval setup 后，hallucination distribution 本身就变了，应分 track 报告。

## 下一步评测坐标

下一步要从事后 detector 推进到闭环 correction：检测到 unsupported claim 后，agent 是否能找到缺失证据、修订答案并保留 citation-level trace。
