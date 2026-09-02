# SearchAuditBench: final-answer scores do not explain why a deep-search agent failed

[中文](searchauditbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.05212) · [Code](https://github.com/lzzzx666/SearchAuditor)

## What it measures

SearchAuditBench collects 1,243 failed trajectories from eight open-weight models on five deep-search benchmarks, averaging 73.1 messages and 65.1K tokens. Experts annotate critical steps, a six-way root-cause taxonomy, and executable repairs, enabling localization, cause, diagnosis, and repair-pass metrics.

## Compared with what

Most benchmarks collapse failure to zero reward. SearchAuditBench makes the post-hoc auditor an evaluation object: can it find the earliest critical error, attribute the cause, and propose a repair that restores the trajectory?

## Score boundary

High diagnosis or repair scores support auditing on the failures-only mixture. They do not establish stronger original search agents or proactive prevention. Source-model, harness, and benchmark mixtures shape the failure distribution.

## Fair comparison conditions

Align trajectory corpus, failure sampling, cause taxonomy, repair execution/judge, and localization tolerance. Auditor scores from different failure mixtures are not directly comparable.

## Next evaluation coordinate

The next step places the auditor online and tests whether early intervention actually reduces final failures rather than merely explaining them after the fact.
