# MemFuseBench：Agent Memory / 跨来源融合

**中文** | [English](memfusebench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.18704) · [数据](https://github.com/Darwin-Agent/Mi-Memory/tree/master/MemFuse/MemFuseBench)

把评价对象从单历史召回推进到跨设备、用户与时间的 linking、causal fusion、conflict 和 provenance。

## 它接在什么之后

前一代评价通常把该问题压成较短的最终分数或单一 proxy。这个评测把 predecessor critique 变成 capability × environment × protocol 的显式差异，并保留可执行或可复核资产。

## 实际怎样评测

**问题：** 系统能否在来源互异且可能冲突的事件流中找对证据、融合因果并保留出处？

**测量对象：** 跨异构事件流的来源连接、因果融合、冲突裁决与溯源记忆基准。

**规模与协议：** 357 questions over 7,823 source-tagged events with six diagnostic categories. 协议包括 evidence-checklists, adversarial-distractors, six-diagnostic-categories。

## 分数能说明什么

357 questions、7,823 events 与 six diagnostics 分别观察 linking、causal fusion、conflict 和 provenance。 它支持的是该环境、harness、model/tool/resource configuration 下的 system-level evidence；除非其他变量匹配，否则不能把榜单差异归因给单一组件。

## 最主要的混杂因素

synthetic generation 与 model-guided verification 仍缺 human ceiling，不能证明真实用户历史上的外部效度。 关键混杂包括 synthetic-generator-style, model-guided-verification, missing-human-ceiling。

## 还没有覆盖什么

合成构造与模型引导核验缺少人类上限，也尚未证明真实世界外部效度。

## 放进演化图怎么看

`map_delta=early_signal`。一篇论文只是一项 signal；持久方向判断必须由绑定同一 canonical direction key 的独立记录支撑。
