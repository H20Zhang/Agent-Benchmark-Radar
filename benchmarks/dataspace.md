# DataSpace：Heterogeneous Workspace 上的 Verifiable Analytics

**中文** | [English](dataspace.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[Paper](https://arxiv.org/abs/2608.03451) · **Area: Data Agent**

> **Measurement delta.** DataSpace 把 data-agent target 从“给定一张表做分析”扩展成：只给 question + task-local workspace，agent 自己从 DB、structured files、long documents、video 中发现 evidence、做 cross-source computation，并返回可 deterministic 验证的完整 tabular result。

## Predecessor / implicit critique

Text-to-SQL、table QA、RAG 或 open-ended analysis benchmark 往往把 source discovery、structured computation、multimodal evidence 与 final verification 分开。DataSpace 的隐含批评是：真实 analytics 的难点恰恰在这些阶段的组合。

## What it actually measures

DataSpace 包含 **410 个 cross-language tasks、7,439 个 artifacts、15.01 GB workspace data**，格式覆盖 CSV、JSON、SQLite、Markdown、PDF 与 video。

每个 agent 只拿到问题与对应 workspace，最终输出完整 tabular result。Evaluator 做 header-invariant alignment、type/precision-aware normalization 与 order-aware row comparison，不依赖 LLM judge。

## What a score supports

论文报告最佳 accuracy **66.34%**；更重要的是，**固定 backbone 时更换 agent harness 可以产生 15.36 points 的差距**。

因此 leaderboard score 首先反映 `backbone × harness × source discovery × multimodal handling × computation × verification` 的整套系统，而不能直接归因给某个 data-retrieval 或 planning component。

## Strongest confounder

**Harness sensitivity 本身就是最大的 validity signal。** 如果同一个 backbone 因 harness 变化产生十几个点差距，那么跨论文/跨系统比较必须非常谨慎。

另外，task-local frozen workspace 提高 reproducibility，但与真实 enterprise live data、权限与持续 drift 仍有距离。

## What remains unmeasured

- business-definition ambiguity 与 clarification；
- persistent workflow/project state；
- write/update data 的不可逆 action；
- production data governance / permissions；
- total tool/latency/token cost 与 failure recovery。

## Genealogy consequence

`structured query/code → heterogeneous analytics → workspace-scale verifiable data work`

DataSpace 的主要贡献是把 **evidence discovery + cross-source computation + deterministic verification** 放进同一个 evaluation object。
