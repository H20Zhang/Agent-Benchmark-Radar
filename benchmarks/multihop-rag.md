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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合在可控语料上研究多跳证据发现与组合。它比只给定上下文的问答更接近 RAG，但仍不同于实时网页搜索；检索链设计与回答推理的贡献需要通过证据给定条件拆开。

### 一个具体任务长什么样

示意任务：几篇新闻分别提供事件、人物与时间信息，答案需要连接多处证据。先找到主题相关报道只是起点，后续检索还需要追踪缺失关系，而不是重复返回相似新闻。

### 最有判别力的实验

在同一语料与相同总检索预算下比较单次与迭代检索，按推理跳数分别报告完整支持链覆盖。给定全部支持事实后再测回答，判断主要瓶颈是缺证据还是不能组合证据。

### 建议搭配

[hotpotqa](hotpotqa.md) · [agenticragtracer](agenticragtracer.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`single-hop relevance → multi-evidence retrieval → adaptive multi-step search`

它为“retrieval 应该按 evidence coverage 而不是 passage similarity 来测”奠定了基础。