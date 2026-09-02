# InsightBench: from answering queries to discovering business insights

[中文](insightbench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2407.06423) · [Code](https://github.com/ServiceNow/insight-bench)

## What it actually measures

InsightBench evaluates **end-to-end business analytics**: formulate useful questions, run analyses, interpret results, synthesize insights, and propose actionable next steps. It contains 100 datasets representing business use cases such as finance and incident management, each with curated planted insights.

## What changed relative to prior evaluation

Most data-analysis benchmarks hand the model a precise query. InsightBench moves agency upstream: the agent must decide what to investigate and communicate a coherent set of findings, not merely compute a requested statistic.

## Decisive evidence

Because open-ended insight generation lacks one deterministic answer, the benchmark introduces a two-way LLaMA-3-based evaluator and extensive dataset quality assurance. AgentPoirot, the proposed end-to-end baseline, outperforms approaches such as Pandas Agent that focus on resolving single queries.

## What the score supports

The benchmark supports discovering benchmark-authored business insights and packaging them into analysis. It is weaker evidence for genuinely novel or decision-useful discovery because the planted-insight set defines what counts as relevant and evaluator judgments mediate credit.

## Fair comparison contract

Fix datasets, agent starting prompt, toolset, exploration budget, evaluator model/version, and report format. Report planted-insight coverage separately from presentation quality; otherwise fluent summaries can obscure missed evidence.

## What remains unmeasured

Real business insight depends on stakeholder objectives, causal validity, opportunity cost, and whether a recommendation changes a decision. A planted insight can be statistically recoverable yet economically unimportant.

## Next discriminating validation

Add blinded domain-expert scoring of unseen insights and downstream decision tasks. The key test is whether an agent finds something worth acting on, not only whether it rediscovers what benchmark designers planted.

## Genealogy

`answer a data query → discover a set of insights → decision-oriented business analysis`

InsightBench moves data agents from execution toward analytical agenda setting.