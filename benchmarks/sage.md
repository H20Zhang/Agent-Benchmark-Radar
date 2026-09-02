# SAGE：学术检索要区分“找到指定论文”和“尽可能完整地找齐一组论文”

**中文** | [English](sage.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2602.05975) · [代码](https://github.com/HughieHu/Sage)

## 它在测什么

SAGE 提供 1,200 个 expert queries，覆盖 computer science、healthcare、humanities 与 natural science：600 个 short-form target-paper queries 和 600 个 open-ended discovery queries，基于约 200K papers 的 controlled corpus。前者看 exact paper retrieval，后者用 weighted recall 看是否找全高价值 evidence。

## 相比什么前进了

一般 literature search benchmark 常只测 title/known-item retrieval。SAGE 把 targeted lookup 与 open-ended evidence collection 分开，并做 agent-retriever ablation，因此可以观察同一个 search agent 换 backend 后能力如何变化。

## 分数边界

exact-paper/weighted-recall 支持在给定 corpus snapshot、index 与 retrieval budget 下的 scientific discovery quality；开放式 gold set 本身可能不完备，而且 released repo 并未 turnkey 提供完整 200K corpus/environment，因此 artifact packaging 是复现边界。

## 公平比较条件

锁定 corpus snapshot、indexing configuration、agent subquery generation、budget 与 gold-set version。short-form 与 open-ended 不能压成一个 SOTA 数字。

## 下一步评测坐标

下一步应接入 citation graph、full text 与动态 scholarly databases，同时明确 completeness ceiling 和 search cost。
