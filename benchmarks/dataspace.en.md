# DataSpace: Verifiable Analytics over Heterogeneous Workspaces

[中文](dataspace.md) | **English** · [Back to entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.03451) · **Area: Data Agent**

> **Measurement delta.** DataSpace asks agents to discover evidence across databases, structured files, long documents, and video, perform cross-source computation, and return a complete tabular result that can be checked deterministically.

## Predecessor / implicit critique

Text-to-SQL, table QA, RAG, and open-ended analysis benchmarks usually separate source discovery, structured computation, multimodal evidence, and final verification. DataSpace combines these stages inside a task-local workspace.

## What it actually measures

DataSpace contains **410 cross-language tasks, 7,439 artifacts, and 15.01 GB** across CSV, JSON, SQLite, Markdown, PDF, and video. Each agent receives a question plus workspace and must return the complete requested table. The evaluator uses header-invariant alignment, type/precision-aware normalization, and order-aware row comparison without an LLM judge.

## What a score supports

The best reported accuracy is **66.34%**. More importantly, changing the agent harness while holding the backbone fixed produces a **15.36-point spread**.

That makes the score a system-level measure of backbone × harness × discovery × multimodal handling × computation × verification rather than evidence for one retrieval/planning component.

## Strongest confounder

**Harness sensitivity is itself a validity finding.** Cross-system conclusions are weak unless harness/interface conditions are aligned. The frozen task-local workspace improves reproducibility but remains different from live enterprise data with permissions and drift.

## What remains unmeasured

Business-definition ambiguity, clarification, persistent workflow/project state, write-side irreversible actions, governance, and full tool/latency/token/recovery cost remain open.

## Genealogy consequence

`structured query/code → heterogeneous analytics → workspace-scale verifiable data work`

The durable coordinate is the combination of evidence discovery, cross-source computation, and deterministic verification.
