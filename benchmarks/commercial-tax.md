# The Commercial Tax：RAG / deployment validity

**中文** | [English](commercial-tax.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.16096) · [代码](https://github.com/Toryx-AI/commercial-tax-multihop-retrieval) · [复现实验](https://doi.org/10.5281/zenodo.21972866)

把 raw retrieval number 重新绑定到 license、query format、index construction 与 recurring cost。

## 它接在什么之后

前一代评价通常把该问题压成较短的最终分数或单一 proxy。这个评测把 predecessor critique 变成 capability × environment × protocol 的显式差异，并保留可执行或可复核资产。

## 实际怎样评测

**问题：** 一个 benchmark embedding score 能否在许可、格式与成本约束下迁移到生产？

**测量对象：** 把原始 embedder 分数绑定到许可、query format、索引构造与部署成本的检索复现性审计。

**规模与协议：** Thirteen embedders on the same 11,656-passage, 1,000-question retrieval floor. 协议包括 exact-cosine-search, paired-bootstrap, license-provenance, separate-construction-query-cost。

## 分数能说明什么

13 embedders 使用 paired bootstrap、license provenance 与 separated construction/query cost，显示接近的 raw recall 不等于相同部署含义。 它支持的是该环境、harness、model/tool/resource configuration 下的 system-level evidence；除非其他变量匹配，否则不能把榜单差异归因给单一组件。

## 最主要的混杂因素

uneven format tuning、hosted drift 与 single corpus 限制了跨模型、跨系统和长期可迁移性。 关键混杂包括 uneven-query-format-search, hosted-endpoint-drift, single-corpus。

## 还没有覆盖什么

不均衡的 query-format 调优、会漂移的托管端点与单一主语料，使结论仅适用于原始 exact-search retrieval。

## 放进演化图怎么看

`map_delta=reinforces`。一篇论文只是一项 signal；持久方向判断必须由绑定同一 canonical direction key 的独立记录支撑。
