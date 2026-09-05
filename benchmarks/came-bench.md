# CAME-Bench：同一个 entity 在不同 latent goal 下并不是同一条 memory

**中文** | [English](came-bench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://aclanthology.org/2026.findings-acl.584/) · [代码](https://github.com/Seattleyrz/contextual-intent)

## 它在测什么

CAME-Bench 有 14 条 goal-oriented trajectories 与 373 questions，context 平均约 23K、137K、408K tokens，覆盖 travel planning 与 policy debate。 recurring entities 会在不同 latent goals 下反复出现，系统必须结合当前 intent 取回正确版本的 evidence。

## 相比什么前进了

普通 vector retrieval 把同名实体或相近 fact 当成相似候选。CAME-Bench 专门制造 contextual interference，使 retrieval 错误可以归因于“没理解当前 goal”，而不是单纯找不到 entity。

## 分数边界

QA/evidence retrieval 与 length-scaling 支持 context-aware retrieval under synthetic trajectories。它不测试真实用户、actions 或 memory repair；benchmark 与 STITCH 方法共设计也意味着方法/benchmark coupling 是解释变量。

## 公平比较条件

锁定 trajectory generation、domain、length bucket、judge 与 evidence protocol，并将 23K/137K/408K 分开报告。

## 下一步评测坐标

下一步应在真实 evolving projects 中同时有多条竞争 goals，并要求 memory retrieval 支持后续 action 与 conflict repair。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合诊断同一实体反复出现在不同目标中引发的检索串扰。它针对的是‘看起来相关，却属于另一个情境’；扩大 top-k 可能同时加入更多冲突证据，因此不能只把失败归为召回不足。

### 一个具体任务长什么样

示意任务：同一个地点出现在两次目的不同的计划中，当前只追问其中一次安排。系统需要识别问题绑定的目标与情境；按地点名汇总所有记录，可能得到事实真实但任务错误的答案。

### 最有判别力的实验

保持实体与事实不变，只改变查询绑定的目标，并比较纯相似度检索、带目标元数据的检索和正确情境直接给定。若第二种条件明显改善，应进一步检验目标标签是系统推断的还是人工提供的。

### 建议搭配

[scale-qa](scale-qa.md) · [locomo-plus](locomo-plus.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
