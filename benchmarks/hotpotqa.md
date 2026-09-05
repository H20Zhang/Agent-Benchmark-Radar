# HotpotQA：把 multi-hop evidence composition 变成显式评测目标

**中文** | [English](hotpotqa.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://aclanthology.org/D18-1259/)

## 它在测什么

HotpotQA 包含约 113K 个 Wikipedia 问题，并给出 sentence-level supporting facts。它要求系统跨多个文档找到互补证据并完成 multi-hop reasoning，因此不仅看最终答案，也能检查支撑答案的 evidence 是否被找到。

## 相比什么前进了

早期 open-domain QA 很容易把 retrieval 与 reasoning 压成一次单跳命中。HotpotQA 把跨文档组合与 supporting-fact supervision 变成 benchmark contract，成为后来 MultiHop-RAG、agentic retrieval 与 evidence-grounded QA 的重要前驱。

## 决定性证据与分数边界

它最持久的价值是让 answer accuracy 与 evidence coverage 可以分开观察：答对不等于找对 supporting facts。与此同时，今天的模型可能利用 dataset shortcuts、参数记忆或更强 reader，因此现代高分不能直接证明 retriever 或 multi-hop policy 更好。没有锁定 retriever-reader interface 时，端到端 EM/F1 只能支持 packaged QA system 的判断。

## 公平比较条件

必须对齐 fullwiki/distractor setting、corpus snapshot、retriever、reader、supporting-fact metric 和允许的 candidate budget。静态 Wikipedia 上的结果不能直接与 live-web search agent 的成绩横比。

## 下一步评测坐标

HotpotQA 不覆盖动态网页、工具状态、搜索成本与 query reformulation。后续 benchmark 应让系统自己决定何时继续搜索、如何修正检索路径，并验证 evidence portfolio 是否真正驱动最终答案。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合检验多文档证据组合，是多跳检索的基础参照，而不是实时搜索智能体能力的完整代表。尤其要区分候选段落已给定与全库检索；两者对检索器的要求不同，不能把答案分数直接混比。

### 一个具体任务长什么样

示意任务：问题需要先通过一篇文档确定中间实体，再用另一篇文档取得最终属性。系统既要输出答案，也要找到足够支持两步推理的事实；猜中答案不等于证据链正确。

### 最有判别力的实验

固定回答模型，比较单次检索、迭代检索和给定支持事实，分别报告证据召回与答案质量。另做移除一个必要证据的检查，验证问题是否存在捷径；不要把更大候选池带来的收益全归给多跳规划。

### 建议搭配

[multihop-rag](multihop-rag.md) · [browsecomp-plus](browsecomp-plus.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
