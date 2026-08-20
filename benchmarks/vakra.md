# VAKRA：Cross-Source Executable Agent Evaluation

**中文** | [English](vakra.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[Paper](https://arxiv.org/abs/2608.12282) · [Code](https://github.com/IBM/VAKRA) · **Area: RAG / Agentic Retrieval**

> **Measurement delta.** VAKRA 把 API interaction、multi-hop reasoning、document retrieval 与 natural-language tool-use policy 组合进同一条**可执行 trajectory**，评估 agent 能否维持 cross-source identity、grounding 与 policy consistency。

## Predecessor / implicit critique

过去的 API benchmark、RAG benchmark 与 tool-policy benchmark 往往分开测 primitive skill。VAKRA 的批评是：这些 isolated score 不能告诉我们 agent 在真实 enterprise workflow 中能否把多个 access mode 串起来。

## What it actually measures

VAKRA 提供 **8,000+ locally hosted executable APIs、62 个 domains**，覆盖：

- diverse API interaction styles；
- 1–3 API 的 multi-hop structured reasoning；
- API + RAG + policy constraint 的 multi-turn multi-source reasoning。

Predicted tool calls 会被重新执行，允许多条合法 tool path，而不是只 string-match final answer。

## What a score supports

论文使用固定 ReAct harness，降低一部分 agent-architecture confounding。最佳 model 在 single-hop endpoint-style task 上为 **70.4%**，到 compositional APIs 降至约 **50–51%**；某些 policy-constrained unanswerable setting 低至 **2.4%**。

Trace analysis 指向 entity disambiguation、cross-source grounding 等 language-mediated reasoning，而不只是 tool invocation mechanics。

但 score 仍然是 model + fixed harness 的 system-level evidence，不能直接推出“retrieval policy”或“planner”哪个 component 是瓶颈。

## Strongest confounder

固定 ReAct harness 有利于比较 model，但也把结论绑定到一个特定 interface/controller contract。API/tool schema、policy wording 与 document collection 也会影响 reasoning difficulty。

## What remains unmeasured

- controller / retrieval / identity memory 的 component attribution；
- long-running persistent state；
- live enterprise API drift 与 permissions；
- tool latency/cost；
- irreversible external actions 与 recovery。

## Genealogy consequence

`document retrieval / API use in isolation → multi-hop agent trajectories → cross-source executable coherence under policy`

VAKRA 把 RAG evaluation 从“找对 evidence”推向“在异构 access mode 中维持可执行信息状态”。
