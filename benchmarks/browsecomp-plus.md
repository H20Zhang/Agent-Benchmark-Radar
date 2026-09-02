# BrowseComp-Plus：固定语料后，才能更清楚地问 agent 还是 retriever 在进步

**中文** | [English](browsecomp-plus.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2508.06600) · [代码](https://github.com/texttron/BrowseComp-Plus)

## 它在测什么

BrowseComp-Plus 将 BrowseComp-style deep search 转成约 830 个 queries、约 100K 篇固定且人工核验的 documents，并同时保留 positives 与 hard negatives。它报告 retrieval recall、answer accuracy 与 controlled retriever 条件，目标是把 live-web stack 中纠缠的 retriever、agent 与环境因素拆开。

## 相比什么前进了

BrowseComp 很真实，但 provider ranking 与 web drift 使复现实验和归因困难。BrowseComp-Plus 用 fixed corpus 换取 reproducibility，使同一 agent 换 retriever、同一 retriever 换 agent 成为更可信的 matched comparison。

## 决定性证据与当前成绩

ACL 2026 版本显示在该 fixed-corpus protocol 下，Search-R1+BM25 仅 3.86%，GPT-5 benchmark agent 55.9%，GPT-5 配 Qwen3-Embedding-8B retrieval 达 70.1%，且搜索调用更少。Radar 将这组数字作为独立 paper snapshot；它们不能与 live BrowseComp 51.5% 或不同 corpus variants 直接排名，因为 evaluation object 已改变。

## 公平比较条件

锁定 corpus/qrels、830-query subset、context cap、judge、search budget 与 retriever. 不同 query-conditioned corpus construction 或 corpus scale 应分 track。

## 下一步评测坐标

固定语料提升 attribution，却去掉 freshness 与真实 provider interface。BrowseComp-Plus_CM 进一步指出 query-conditioned small corpus 会低估 evidence-discovery difficulty，因此 corpus construction 本身仍需成为可见变量。
