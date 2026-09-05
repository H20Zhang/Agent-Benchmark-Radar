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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究按不同研究意图迭代收集论文，而不只是标题相似度搜索。答案是一个集合，漏掉研究分支与多找几篇近重复论文不是同等结果；检索效率应与集合覆盖一并评价。

### 一个具体任务长什么样

示意任务：系统围绕一个主题搜集论文，沿引文关系扩展，再根据研究意图收紧或扩大范围。相同主题下的入门综述与全面相关工作检索，对集合边界和停止规则可能提出不同要求。

### 最有判别力的实验

固定论文后端和调用预算，对比关键词搜索、引用扩展与意图条件化策略，逐意图报告召回。人工检查金标外的有效论文，并记录去重后的覆盖增长，避免不完整答案集合或重复结果误导评价。

### 建议搭配

[sage](sage.md) · [autoresearchbench](autoresearchbench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
