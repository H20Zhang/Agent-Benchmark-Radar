# DAS-Bench / DAS-Eval：RAG / 学术综述成品

**中文** | [English](das-bench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.18034) · [基准与评测器](https://github.com/ZhikaiXu24/DAS) · [数据](https://huggingface.co/datasets/ZhikaiXu24/DAS-Bench)

把 retrieval/drafting 扩展为可共享修订的 literature、taxonomy、claim、citation、discourse 与 PDF 成品协议。

## 它接在什么之后

前一代评价通常把该问题压成较短的最终分数或单一 proxy。这个评测把 predecessor critique 变成 capability × environment × protocol 的显式差异，并保留可执行或可复核资产。

## 实际怎样评测

**问题：** 系统能否把文献证据组装成可审计、可阅读的 publication-oriented survey？

**测量对象：** 对文献覆盖、taxonomy、claim、citation、discourse 与渲染成品质量评分的学术综述基准及评测器。

**规模与协议：** 30 topics across computer science and non-CS fields, with a matched 21-topic comparison subset. 协议包括 sixteen-criterion-evaluator, semantic-and-deterministic-checks, blinded-expert-comparison。

## 分数能说明什么

30 topics、16 criteria 加 deterministic citation checks 与 blinded expert comparison，覆盖 evidence、taxonomy、claim、discourse 和 artifact。 它支持的是该环境、harness、model/tool/resource configuration 下的 system-level evidence；除非其他变量匹配，否则不能把榜单差异归因给单一组件。

## 最主要的混杂因素

generation backbone 与 main judge coupling、closed-system native configs 意味着跨系统差距仍是 system-level。 关键混杂包括 generator-judge-coupling, closed-system-native-configurations, judge-sensitivity。

## 还没有覆盖什么

生成方法尚未公开，共用的生成 backbone 同时还是主要自动评判器。

## 放进演化图怎么看

`map_delta=early_signal`。一篇论文只是一项 signal；持久方向判断必须由绑定同一 canonical direction key 的独立记录支撑。
