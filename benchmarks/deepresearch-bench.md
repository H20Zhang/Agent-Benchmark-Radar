# DeepResearch Bench：从“找到答案”转向可引用的长文 research artifact

**中文** | [English](deepresearch-bench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2506.11763) · [代码](https://github.com/Ayanami0730/deep_research_bench)

## 它在测什么

DeepResearch Bench 用 100 个跨 22 个领域的 PhD-level research tasks，评价多步 web research、evidence collection、citation accuracy/effectiveness 与 long-form report quality。evaluation object 不再是一个短答案，而是接近 analyst deliverable 的 research report。

## 相比什么前进了

BrowseComp 强调 search persistence，但不要求完整 research artifact。DeepResearch Bench 把 retrieval、citation 与 synthesis 连起来，因此“答案有道理但 citation 不支持 claim”可以单独成为失败。

## 决定性证据与成绩边界

该 benchmark 的 evaluator 仍在演进：官方仓库 2026-05 切换到 GPT-5.5，并同时维护迁移期 leaderboard；GPT-5.5 evaluator 与 human IAA 的 overall alignment 约 71.82 vs human baseline 68.78。这个变化说明 evaluator version 是 load-bearing variable。Radar 不把旧 judge 与新 judge 的 agent scores混为一个当前榜单，而应分 evaluator-generation tracking。

## 公平比较条件

锁定 task set、web/search provider、report budget、citation extraction、judge generation 与 scoring rubric。不同 evaluator 版本的分数必须带日期和 protocol version。

## 下一步评测坐标

100 个高成本 tasks 足以测系统，但不利于细粒度 causal attribution。下一步需要可重放 evidence snapshots 和 component-level intervention，区分 search、source selection、writing 与 citation verifier 的贡献。
