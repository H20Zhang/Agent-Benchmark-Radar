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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合检验多轮 RAG 中省略、歧义与无答案情形的处理。当前话轮不一定是独立查询；直接检索原句可能失败，错误改写也可能引入用户从未提出的假设。

### 一个具体任务长什么样

示意任务：用户在前一轮讨论某个对象，随后只问‘那另一种情况呢’，但历史可能不足以唯一确定范围。系统应先恢复必要上下文，证据或意图仍不明确时采取适当澄清，而不是补造问题。

### 最有判别力的实验

比较原话轮检索、自动改写与正确独立问题给定条件，分别统计检索、回答和澄清行为。按可回答、不可回答和欠明确任务拆分，防止一律改写或一律弃答在总体指标中隐藏失败。

### 建议搭配

[rgb](rgb.md) · [longmemeval](longmemeval.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
