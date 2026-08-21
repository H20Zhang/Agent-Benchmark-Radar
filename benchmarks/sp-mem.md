# SP-Mem Privacy-Aware Memory Benchmark：Agent Memory / 生命周期隐私

**中文** | [English](sp-mem.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.16551) · [代码与数据](https://github.com/Jensassss/SP-Mem)

把记忆有用性与 consent、authorization、exact-value exposure、cost 放进同一协议。

## 它接在什么之后

前一代评价通常把该问题压成较短的最终分数或单一 proxy。这个评测把 predecessor critique 变成 capability × environment × protocol 的显式差异，并保留可执行或可复核资产。

## 实际怎样评测

**问题：** 个性化记忆能否只在被授权且确有必要时被使用，同时避免暴露？

**测量对象：** 联合测量回答质量、个性化、同意处理、精确值暴露与成本的隐私感知记忆基准。

**规模与协议：** 1,000 synthetic profiles, 5,400 queries, four domains, and 376 subtasks. 协议包括 matched-privacy-preference-modes, pairwise-quality, exact-value-leakage, cost-accounting。

## 分数能说明什么

1,000 profiles、5,400 queries、four domains 的匹配模式同时评分 response quality、authorization request 与 exact-value exposure。 它支持的是该环境、harness、model/tool/resource configuration 下的 system-level evidence；除非其他变量匹配，否则不能把榜单差异归因给单一组件。

## 最主要的混杂因素

explicit consent labels 与 exact-string leakage proxy 没有覆盖 inference、re-identification 和 adversarial multi-turn disclosure。 关键混杂包括 synthetic-consent-labels, benchmark-system-codesign, exact-string-leakage-proxy。

## 还没有覆盖什么

显式同意标签与精确字符串泄露指标没有覆盖推断、重新识别和对抗性多轮披露。

## 放进演化图怎么看

`map_delta=early_signal`。一篇论文只是一项 signal；持久方向判断必须由绑定同一 canonical direction key 的独立记录支撑。
