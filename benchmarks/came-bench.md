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
