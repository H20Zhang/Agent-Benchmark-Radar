# MTRAG-UN：多轮 RAG 不应假设每一轮都可回答、完整且 standalone

**中文** | [English](mtrag-un.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://aclanthology.org/2026.findings-acl.503/) · [代码](https://github.com/IBM/mt-rag-benchmark)

## 它在测什么

MTRAG-UN 从 666 段 conversations 构造 666 tasks、超过 2,800 turns、覆盖六个 domains，并显式加入 unanswerable、underspecified、non-standalone 与 unclear turns。它同时评价 retrieval ranking、answer generation、IDK detection 与 faithfulness。

## 相比什么前进了

一般 multi-turn RAG benchmark 默认当前 query 能被历史消歧且 corpus 中有答案。MTRAG-UN 把现实对话中“不该立即回答”的状态加入 protocol，使 clarification、abstention 与 context resolution 不再被错误答案分数掩盖。

## 分数边界

IDK/faithfulness/retrieval metrics 支持在固定 corpus、conversation history 与 judge 下的 uncertainty handling；query rewriting、collection-model bias 和 inherited corpus 都会改变 difficulty，因此一个 overall score 不足以说明哪一层改进。

## 公平比较条件

锁定 conversation version、query-rewriting policy、corpus、retriever、answerer 与 judge，并分别报告 answerable/unanswerable/underspecified 等 slices。

## 下一步评测坐标

下一步应让 clarification 真的改变之后的 dialogue state 与 retrieval query，并评价一次追问是否减少后续搜索成本和错误。
