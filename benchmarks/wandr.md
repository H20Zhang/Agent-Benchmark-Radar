# WANDR：RAG / 实时 wide-and-deep 搜索

**中文** | [English](wandr.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.14747) · [基准](https://github.com/perplexityai/wandr)

把答案搜索扩展为开放集合 discovery、分层 enrichment 与 record-level refetch verification。

## 它接在什么之后

前一代评价通常把该问题压成较短的最终分数或单一 proxy。这个评测把 predecessor critique 变成 capability × environment × protocol 的显式差异，并保留可执行或可复核资产。

## 实际怎样评测

**问题：** Agent 能否在不知道完整集合时发现、补全并逐条核验实时网页记录？

**测量对象：** 面向实时网页 wide-and-deep 记录收集的基准，包含分层任务和无需穷举金标的逐条核验。

**规模与协议：** 500 self-contained Harbor task packages for wide and deep live-web collection. 协议包括 required-volume-denominators, record-level-url-excerpt-refetch, soft-and-hard-f1。

## 分数能说明什么

500 Harbor task packages 使用 required-volume denominator 与 URL/excerpt refetch，分别暴露 discovery、support 和 enrichment 的损失。 它支持的是该环境、harness、model/tool/resource configuration 下的 system-level evidence；除非其他变量匹配，否则不能把榜单差异归因给单一组件。

## 最主要的混杂因素

unmatched stacks、shared fetch backend、web drift 与 LLM judge 使结果只能按 system-level evidence 解读。 关键混杂包括 unmatched-system-stacks, shared-fetch-backend, web-drift, llm-judge。

## 还没有覆盖什么

网页会漂移，评判器依赖 LLM 与抓取后端，被测系统的服务商、模型、搜索工具和 harness 也未匹配。

## 放进演化图怎么看

`map_delta=reinforces`。一篇论文只是一项 signal；持久方向判断必须由绑定同一 canonical direction key 的独立记录支撑。
