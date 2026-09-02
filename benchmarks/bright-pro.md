# Bright-Pro：retrieval 不只要找到 relevant passage，还要覆盖完整 reasoning aspects

**中文** | [English](bright-pro.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://aclanthology.org/2026.acl-long.1705/) · [代码](https://github.com/yale-nlp/Bright-Pro)

## 它在测什么

Bright-Pro 含 739 个 queries、7 个 StackExchange domains、2,763 个 reasoning aspects、5,272 个 gold passages 和 526,319 篇文档；其中 175 queries 构成 agentic-search subset。它用 α-nDCG 与 weighted aspect recall 评价 evidence portfolio 是否覆盖互补 reasoning aspects，并同时提供 fixed-round/adaptive agentic search。

## 相比什么前进了

BRIGHT 证明 relevance 本身需要 reasoning，但 relevance set 仍较窄。Bright-Pro 把每个 query 拆成多个 weighted aspects，因此系统不能靠重复找同类 passage 获得高分；retriever 是否为 agent 提供 complementary evidence 变成独立坐标。

## 分数边界

高 α-nDCG/aspect recall 支持在 fixed corpus 与 annotation version 下的 evidence-portfolio coverage；agentic-search success 还取决于 agent-retriever coupling、round budget 与 judge。static retrieval 与 175-query agentic subset 不是同一 evaluation object，应分 track。

## 公平比较条件

锁定 corpus、aspect annotations、search-round budget、agent backbone、judge 与 static/adaptive protocol。annotation version drift 必须和分数一起记录。

## 下一步评测坐标

下一步应把 aspect coverage 与最终 answer claim coverage 对齐：哪些 reasoning aspects 真正改变了结论，哪些只是冗余 evidence。
