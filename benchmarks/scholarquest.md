# ScholarQuest：academic search 的答案往往是一个 intent-conditioned paper set

**中文** | [English](scholarquest.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2606.20235) · [代码](https://github.com/pty12345/ScholarQuest)

## 它在测什么

ScholarQuest 包含 1,111 个 queries、超过 1,000 个 CS topics、四种 research intents；每个 answer set 有 5–200 篇 arXiv papers，基于约 3M-paper shared backend 与 citation graph。指标包括 recall@100、recall@all 与 search efficiency。

## 相比什么前进了

SAGE/AutoResearchBench 已开始测 open-ended literature discovery。ScholarQuest 进一步把 user intent 显式放进 set retrieval：同一个 topic 下，survey、method comparison 或 specific evidence 可能需要不同 paper sets。

## 分数边界

recall 支持当前 generated queries、LLM relevance adjudication 与 corpus snapshot 下的 set retrieval。开放 literature 的 gold set 天然不完备，因此绝对 recall 既反映 agent，也反映 reference construction。

## 公平比较条件

锁定 intent slice、corpus/citation graph、gold-set version、search budget 与 relevance adjudicator。不同 intents 应单独呈现。

## 下一步评测坐标

下一步应评价 evidence-set marginal utility：多找一篇论文是否填补新的 claim/aspect，而不仅是 reference set 中又命中一篇。
