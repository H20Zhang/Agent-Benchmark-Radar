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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合比较静态视觉文档排序与多轮页面检查，但应严格对齐最终排序协议与行动预算。迭代智能体使用更强模型或更多工具时，成绩差异首先是整个系统的差异，不足以单独证明迭代策略更优。

### 一个具体任务长什么样

示意任务：系统需要从科学文档页面中找出支持问题的页面，既可以依赖静态表征，也可以打开页面查看图表或 OCR 内容后再排序。检查页面产生的新证据应改变候选选择，而不只是增加调用。

### 最有判别力的实验

让静态与迭代方法共享候选集合、视觉骨干和最终 top-k，再增加支持页面直接给定条件。记录每次检查带来的排序改进，并分别报告可公开页面子集与完整页面集合，避免资料可得性影响比较。

### 建议搭配

[mc-search](mc-search.md) · [maple](maple.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
