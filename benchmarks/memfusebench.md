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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究多来源记忆之间的连接、冲突处理与溯源。更长的上下文不是充分基线：真正需要比较的是同样证据在保留或丢失来源关系时，能否支持正确的跨来源结论。

### 一个具体任务长什么样

示意任务：一个来源记录事件发生，另一个解释原因，第三个给出修订信息。系统需要把记录对齐并说明为何采用某一版本；简单拼接来源可能把不同事件或权威层级混在一起。

### 最有判别力的实验

对相同事件集合比较无来源标识、带来源标识和显式跨来源关系，并逐类报告连接、融合、裁决和溯源结果。增加来源间矛盾但文本相似的对照，检验方法是否真正使用来源结构而非依赖生成文本风格。

### 建议搭配

[lifebench](lifebench.md) · [gatemem](gatemem.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
