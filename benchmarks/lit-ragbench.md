# LIT-RAGBench：先把 retriever 拿掉，单独测 generator 会不会用 RAG context

**中文** | [English](lit-ragbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2603.06198) · [代码](https://github.com/Koki-Itai/LIT-RAGBench)

## 它在测什么

LIT-RAGBench 有 114 个 human-constructed Japanese questions，并提供 machine-translated、human-curated English counterparts。它直接提供 positive/negative chunks，按 Logic、Integration、Table、Reasoning、Abstention 五类能力评价 generator，而不把 retrieval quality 混进结果。

## 相比什么前进了

很多 RAG benchmark 的 final answer 失败同时可能来自 retriever 和 generator。LIT-RAGBench 控制 context，让“证据已经在眼前，但模型仍不会整合、推理或拒答”的 failure 独立可测。

## 分数边界

category-wise accuracy 支持 generator 在 supplied-context contract 下的 context-use ability；它不支持 retriever 或 agentic-search claim。114 个问题规模较小，translation 与 fictional-task design 也可能改变语言间 difficulty。

## 公平比较条件

锁定 supplied chunks、prompt template、generator、judge 与语言版本，并分 capability category 与语言报告。

## 下一步评测坐标

下一步应把这些 generator diagnostics 接回真实 retrieval loop，验证识别到 integration/abstention failure 后能否主动补搜或修正 context。
