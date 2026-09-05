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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合把嵌入检索分数放回许可、查询格式与部署成本的实际约束中理解。精确检索条件下的原始模型比较有其价值，但单语料和不均等调参不能直接给出所有生产场景的模型排名。

### 一个具体任务长什么样

示意任务：多个嵌入模型在相同语料上建立索引，使用统一相似度搜索回答查询。模型质量之外，文档编码成本、在线查询成本和许可适用范围，都可能改变实际选型。

### 最有判别力的实验

为各模型提供相同查询格式调参预算，冻结版本与索引，再分别报告构建和查询成本。补充第二个分布不同的语料及近似检索条件，检查原始精确检索排名在实际延迟约束下是否保持。

### 建议搭配

[beir](beir.md) · [bright](bright.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
