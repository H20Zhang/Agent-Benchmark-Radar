# MAPLE：RAG / 多 aspect 科学检索

**中文** | [English](maple.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.15624) · [代码](https://github.com/Ggballs/MAPLE) · [数据](https://huggingface.co/datasets/kai-02/MAPLE)

把单 query 的局部相关性拆成同一论文跨 motivation、method、result 的一致可检索性。

## 它接在什么之后

前一代评价通常把该问题压成较短的最终分数或单一 proxy。这个评测把 predecessor critique 变成 capability × environment × protocol 的显式差异，并保留可执行或可复核资产。

## 实际怎样评测

**问题：** 一个 retriever 能否在不同 aspect 的 query 下持续找回同一篇目标论文？

**测量对象：** 测量同一论文能否在动机、方法与结果等多个 aspect 下持续被找回的科学检索基准。

**规模与协议：** 2,095 queries over 210 positive papers, 73,973 corpus papers, and 23,739 hard negatives. 协议包括 allaspect-at-k, anyaspect-at-k, aspect-coverage, matched-single-query-control。

## 分数能说明什么

2,095 queries、210 papers 上，matched single-query recall 与 AllAspect gap 显示 one-hit relevance 会掩盖 cross-aspect failure。 它支持的是该环境、harness、model/tool/resource configuration 下的 system-level evidence；除非其他变量匹配，否则不能把榜单差异归因给单一组件。

## 最主要的混杂因素

generated queries、single domain 与 model-validated hard negatives 可能引入 style bias 和 label noise。 关键混杂包括 llm-generated-queries, single-domain-corpus, hard-negative-label-noise。

## 还没有覆盖什么

生成问题、相似度筛选、单一 ICLR 风格领域与模型核验负例可能造成风格偏差和假负例。

## 放进演化图怎么看

`map_delta=reinforces`。一篇论文只是一项 signal；持久方向判断必须由绑定同一 canonical direction key 的独立记录支撑。
