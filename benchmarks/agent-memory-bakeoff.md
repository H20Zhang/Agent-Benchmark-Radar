# Agent Memory Bakeoff：跨词汇检索与写入时增强

**中文** | [English](agent-memory-bakeoff.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[代码、数据与协议](https://github.com/JaysonRawlins/agent-memory-bakeoff)

## 问题

当后续查询使用不同词汇时，记忆系统能否找回相关 incident 或 runbook；写入时 enrichment 是否改善这种访问？

## 证据

该套件在 225 个场景、497 份合成记忆文档和 390 个独立生成查询上，交叉比较 BM25、vector、hybrid retrieval 与 plain / write-enriched memory，并用 sibling-aware gold 报告 MRR@10 和 recall@1/@5。写入增强把 BM25 MRR 从 0.678 提高到 0.783，把 symptom query 的 recall@5 从 60.0% 提高到 83.8%。

## Caveat

语料是围绕 enrichment 机制构造的合成数据，只测试一个本地 embedder，协议也止于检索。因此结果支持该语料下的跨词汇可访问性，不能推出下游回答或行动更好。

## Map

`map_delta=early_signal`，绑定 `memory-component-attribution`。它增加了可控写入侧干预，但不修改持久记忆主干。
