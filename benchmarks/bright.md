# BRIGHT：当 relevance 本身需要 reasoning

**中文** | [English](bright.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2407.12883) · [官方榜单](https://brightbenchmark.github.io/)

## 它在测什么

BRIGHT 包含 1,384 个来自 economics、psychology、math、coding 等真实领域的 queries。与普通 lexical/semantic match 不同，相关文档往往只有在理解问题、推导隐含需求后才显得相关，因此 nDCG@10 同时暴露 query reasoning 与 ranking quality。

## 相比什么前进了

BEIR 主要问 zero-shot domain generalization；BRIGHT 进一步问“即使 domain 已知，relevance 是否需要推理才能识别”。这让仅靠 embedding similarity 的上限可见，并推动 reasoning-augmented retrieval 成为独立方向。

## 决定性证据与当前成绩

原始论文显示当时强 retrievers 在 BRIGHT 上远低于传统 retrieval benchmarks 的水平。官方 leaderboard 仍持续更新；截至 2026-09-02，本 Radar 单独追踪 short-document 12-dataset mean nDCG@10，Mira-Reasoning-Retrieval 66.9、INF-X-Retriever 63.4 等。这里的“当前最好”只指该 leaderboard track，不外推到 long-document、不同 dataset subset 或 agentic search。

## 公平比较条件

必须锁定 short/long document setting、12-dataset subset、是否使用 reasoning expansion/reranking、index preprocessing 与 aggregation。不同 track 的 nDCG 不应混排。

## 下一步评测坐标

BRIGHT 仍是 static ranking。下一步是让 reasoning 不只发生在 query expansion，还能控制 multi-step evidence discovery，并同时计算 latency/token/tool cost。
