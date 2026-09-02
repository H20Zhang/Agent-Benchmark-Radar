# KILT：用统一 Wikipedia snapshot 把 provenance 纳入知识密集型评测

**中文** | [English](kilt.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2009.02252) · [代码](https://github.com/facebookresearch/KILT)

## 它在测什么

KILT 把 open-domain QA、fact checking、entity linking、slot filling 等多种 knowledge-intensive tasks 映射到同一个 Wikipedia snapshot，并同时评价 downstream task quality 与 provenance。系统不仅要给出答案，还要说明答案来自共享知识源中的哪些页面。

## 相比什么前进了

此前各任务通常使用不同 corpus、retriever 与 evidence definition，跨任务很难判断 retrieval infrastructure 是否真正可复用。KILT 用统一 snapshot 和 provenance contract 把“知识从哪里来”变成跨任务公共坐标，为后来的 RAG evaluation 提供了基础。

## 决定性证据与分数边界

KILT 的核心证据不是今天某个饱和 leaderboard 数字，而是统一 retrieval source 后可以同时比较 task performance 与 provenance quality。一个高 KILT 分数支持系统在固定 snapshot 上完成多种 knowledge-intensive tasks；它不支持 freshness、live search 或 agentic retrieval 的结论。不同 retriever-generator stacks 的端到端差值也不能自动归因给 retrieval。

## 公平比较条件

必须锁定 KILT Wikipedia snapshot、task split、retrieval index、provenance metric 和 generator。更新 corpus 或改用外部搜索已经改变 evaluation object，不能与原始 KILT 排名直接横比。

## 下一步评测坐标

KILT 消除了 snapshot 差异，却也因此避开 freshness 与 environment drift。后续需要在可复现的同时引入时间、版本变化和交互式 search control。
