# VisDocAgentBench：RAG / Agentic visual-document retrieval

**中文** | [English](visdocagentbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.17889) · [代码](https://github.com/hulx2002/VisDocAgentBench) · [数据](https://huggingface.co/datasets/hulx2002/VisDocAgentBench)

在同一 ranked-page 输出上比较 static ranker 与 search/inspection agent。

## 它接在什么之后

前一代评价通常把该问题压成较短的最终分数或单一 proxy。这个评测把 predecessor critique 变成 capability × environment × protocol 的显式差异，并保留可执行或可复核资产。

## 实际怎样评测

**问题：** Agent 能否通过搜索、视觉检查与 OCR，把分散证据页排入 top 10？

**测量对象：** 在统一页面排序协议下比较静态 ranker 与迭代视觉/OCR agent 的视觉文档检索基准。

**规模与协议：** 2,375 pages from 100 documents and 120 queries, with 1,469 redistributable page images. 协议包括 shared-top-10-contract, twelve-action-agent-budget, support-provided-intervention。

## 分数能说明什么

2,375 pages、120 queries 使用 shared top-10 contract；support intervention 与 ablations 使 discovery 和 inspection 可见。 它支持的是该环境、harness、model/tool/resource configuration 下的 system-level evidence；除非其他变量匹配，否则不能把榜单差异归因给单一组件。

## 最主要的混杂因素

120 queries、six cross-document paths，且 agent routes 未 capacity-matched，限制 planner 或 vision 的因果归因。 关键混杂包括 small-query-set, planner-model-tool-mismatch, few-cross-document-paths。

## 还没有覆盖什么

只有 120 条 query 和 6 条跨文档路径，planner、模型与工具路径也没有按容量匹配。

## 放进演化图怎么看

`map_delta=reinforces`。一篇论文只是一项 signal；持久方向判断必须由绑定同一 canonical direction key 的独立记录支撑。
