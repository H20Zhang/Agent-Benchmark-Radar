# MultiHop-RAG：retrieval 要组合证据，而不只是排序 passage

**中文** | [English](multihop-rag.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2401.15391) · [代码](https://github.com/yixuantt/MultiHop-RAG)

## 它到底测什么

MultiHop-RAG 测 RAG pipeline 能否找到 **多条缺一不可的 supporting evidence**，再把它们组合推理。benchmark 同时提供 news knowledge base、multi-hop query、ground-truth answer 与 supporting evidence，因此 retrieval 和 answer reasoning 可以分别检查。

## 相比此前评测多测了什么

single-hop retrieval 即使很强，也可能在答案依赖多个、单独看和 query 并不高度相似的 evidence 时失败。MultiHop-RAG 把 evidence composition 提升成 retrieval target，而不是默认 top-1 relevant chunk 就够了。

## 决定性证据

论文分别评估 embedding retriever 与多种强 LLM reader，两个阶段在 multi-hop query 上都不理想。这提供了重要拆分：gold evidence 下 reader 做不好是 reasoning 问题；supporting evidence 根本没取到则不是换更强 answerer 就能解决。

## 这个分数能证明什么

retrieval metric 支持 evidence discovery 判断，answer metric 支持 retriever-reader 整体判断；由于 corpus 与 retrieval 是静态的，它们都还不能证明 adaptive search control 的能力。

## 公平比较契约

应固定 corpus snapshot、chunking、embedding/index 配置、top-k budget 与 reader model，并把 supporting-evidence recall 和 answer quality 一起报告。单纯增大 top-k 同时也增大 reader context，应视为 resource change。

## 还没有测什么

静态 news corpus 不要求 iterative query reformulation、source selection、tool call 或 stopping，因此测到了 multi-evidence composition，但还不是现代 agentic retrieval control loop。

## 下一步最有判别力的验证

在固定 retrieval/token budget 下允许 iterative search，对比 one-shot top-k 与 hop-by-hop adaptive retrieval。真正的问题是 adaptive control 能否减少 evidence volume，而不是仅靠更多调用换分数。

## 演化位置

`single-hop relevance → multi-evidence retrieval → adaptive multi-step search`

它为“retrieval 应该按 evidence coverage 而不是 passage similarity 来测”奠定了基础。