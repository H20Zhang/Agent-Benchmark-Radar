# SGR-Bench: search can fail after finding the right site but before reaching the right retrieval state

[中文](sgr-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.22219) · [Data](https://huggingface.co/datasets/PKUAIWeb/SGR-BENCH)

## What it measures

SGR-Bench contains 100 expert-curated tasks across six source families and 12 public data ecosystems. The hard part is not merely finding the right website: the agent must configure filters, hierarchy, scope, or view until the site exposes the answer-bearing state, then produce structured evidence scored with item-F1 or row-F1.

## Compared with what

BrowseComp-style benchmarks mostly ask whether a hidden fact can be found on the web. SGR-Bench decomposes the failure further: after source discovery, can the agent establish the correct site-specific retrieval state? Retrieval-state control therefore becomes an explicit capability rather than a browser implementation detail.

## Score boundary

Higher item/row F1 supports state-gated retrieval under the named browser tool, site snapshot, and harness. It does not establish stronger general web research because tasks concentrate on particular portals and site drift can change the interaction path.

## Fair comparison conditions

Align browser/tool interface, site version, task constraints, agent harness, and allowed actions. A changed page structure or filter API requires a new protocol snapshot.

## Next evaluation coordinate

The next step combines state-gated retrieval with cross-site evidence composition, freshness, and recovery: can the agent diagnose a wrong filter state and re-plan rather than merely be scored at the end?
