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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合在固定语料中比较深度搜索策略与检索基础设施，比实时网页更有利于归因。控制语料带来了可复现性，也去掉了部分网页漂移与接口复杂性；因此它应与实时搜索互补，而不是替代后者。

### 一个具体任务长什么样

示意任务：系统在一个固定文档集合中多轮搜索，逐步满足问题的间接约束并找到答案。检索器能否找出关键材料与智能体能否正确追问，可以在共同语料和接口下分别观察。

### 最有判别力的实验

交叉替换检索器与智能体，固定可见文档、top-k 和总调用预算，联合报告证据召回、答案与成本。再扩大干扰语料或换独立语料，检查收益是否只在精心构建的候选集合中成立。

### 建议搭配

[browsecomp](browsecomp.md) · [browsecomp-plus-cm](browsecomp-plus-cm.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
