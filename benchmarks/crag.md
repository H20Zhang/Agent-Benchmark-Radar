# CRAG：在 freshness、long-tail 与 abstention 压力下评估 RAG

**中文** | [English](crag.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2406.04744) · [代码](https://github.com/facebookresearch/CRAG)

## 它到底测什么

CRAG 评估动态事实、entity popularity、问题复杂度、web search、knowledge graph 与 abstention 条件下的 factual RAG。4,409 个 QA 覆盖 5 个 domain、8 类问题，事实变化速度从按年到按秒。

## 相比此前评测多测了什么

静态 QA 很容易把 model memorization 与 retrieval value 混在一起。CRAG 特意加入新鲜、长尾、动态事实，使 external retrieval 真正必要，并把 hallucination-sensitive correctness 放到核心位置。

## 决定性证据

论文报告 advanced LLM accuracy 不超过 34%，直接加 RAG 大约到 44%，当时最强 industry RAG 也只有 63% 的问题能在不 hallucinate 的情况下回答。事实越动态、越长尾、越复杂，准确率越低。

## 这个分数能证明什么

CRAG 能支持其 mock web/KG interface 下 trustworthy factual QA 的判断，也清楚证明 freshness 会改变 retrieval 的价值；但分数仍是系统级的，model cutoff、retrieval stack、source handling 与 answer policy 都在因果链上。

## 公平比较契约

必须固定 model snapshot/knowledge cutoff、mock API、retrieval budget、KG access 与 grading，并把 hallucination/abstention 与 raw accuracy 分开。激进猜答案不能和“证据不足时正确拒答”混成同一种能力。

## 还没有测什么

mock API 提高 reproducibility，却移除了 live web 的导航、interface variability、authentication 与 search-provider drift；任务也是 factual QA，不是长报告研究或开放式 tool use。

## 下一步最有判别力的验证

对同一批 factual target 同时跑 frozen mock API 与 live-web agent，测 source discovery/interface control 带来的额外 gap，定位现代 search agent 的难度到底有多少来自 retriever 之外。

## 演化位置

`static RAG QA → dynamic/long-tail factuality → live information-seeking reliability`

CRAG 把 knowledge freshness 从隐藏数据属性提升成了 RAG 的一等变量。