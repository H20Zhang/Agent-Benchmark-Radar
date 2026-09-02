# BEIR：把 retriever 的 zero-shot generalization 拉到异构领域

**中文** | [English](beir.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2104.08663) · [代码](https://github.com/beir-cellar/beir)

## 它在测什么

BEIR 汇集最初 18 个来自不同领域与任务的 retrieval datasets，用统一 ranking evaluation 检查 retriever 从训练分布迁移到 unseen domain 的能力。它把“在 MS MARCO 上强”与“跨领域仍能找到相关证据”明确区分开。

## 相比什么前进了

此前 dense retrieval 进展经常围绕单一训练/测试分布报告。BEIR 的关键增量是 heterogeneous zero-shot suite，使 domain robustness 成为 retriever 的一等要求，并让 lexical、dense 与 reranking 方法在同一组跨域任务上暴露 trade-off。

## 决定性证据与分数边界

BEIR 最重要的历史结论是：单一 benchmark 上的 dense-retrieval 优势不能保证 zero-shot 跨域优势，BM25 等 lexical baseline 在不少 domain 仍很强。现代 leaderboard 已经历大量模型、训练数据与 reranker 更新，因此一个 aggregate nDCG 只能支持“在指定 BEIR task mixture 和 index 设置下的 ranking quality”，不能直接说明 agentic search 或 end-to-end RAG 更好。

## 公平比较条件

锁定 dataset subset、版本、indexing/preprocessing、是否使用 reranker、训练数据与 aggregate rule。只在部分 BEIR datasets 上评测的模型不能与 full-suite average 直接排名。

## 下一步评测坐标

BEIR 是 retriever-only 静态评测。下一步要把 cross-domain robustness 延伸到 iterative retrieval、query reformulation、latency/cost 与 downstream evidence use。
