# StructMemEval：把 memory structure 本身变成评测对象

**中文** | [English](structmemeval.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2602.11243)

## 它在测什么

StructMemEval 选择人类天然会用 ledger、to-do list、tree 等结构组织信息的任务，检查 agent 能否把长期记忆组织成与任务匹配的 representation，而不是仅把历史切块后做相似度 retrieval。评测因此首次把“memory 组织结构是否合适”从实现细节提升成独立 capability。

## 相比什么前进了

LoCoMo、LongMemEval 和许多 RAG-style memory benchmark 主要能被“存下来 + 找回来”解决。StructMemEval 故意选择需要结构化维护的任务，使 simple retrieval 的上限暴露出来；它把问题从 retrieval quality 推进到 representation selection 与 structured state tracking。

## 决定性证据与分数边界

论文初步实验显示：简单 retrieval-augmented LLM 在这些任务上表现不佳，而 memory agents 在被明确提示应该如何组织 memory 时可以可靠解决；但不给 structure hint 时，现代 LLM 又经常无法自行识别合适结构。最重要的结论因此不是某个系统的绝对 SOTA，而是“structure selection 本身是瓶颈”。它同时暴露一个 ceiling：prompted structure success 不能证明 agent 能自主发现 representation。

## 公平比较条件

必须对齐是否提供 structure hints、task template、backbone reasoning 与允许的 memory operations。把“告诉模型用 ledger”与“让模型自己发现 ledger”放在同一排行榜会混掉 benchmark 最关键的因果变量。

## 下一步评测坐标

下一步要从 narrow structure-sensitive tasks 推进到开放环境：结构应由 agent 自主诱导，并在数据更新、冲突与 schema 演化中持续调整，而不是一次选择后固定。
