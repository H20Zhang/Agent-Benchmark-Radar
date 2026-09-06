# SearchAuditBench: final-answer scores do not explain why a deep-search agent failed

[中文](searchauditbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.05212) · [Code](https://github.com/lzzzx666/SearchAuditor)

## What it measures

SearchAuditBench collects 1,243 failed trajectories from eight open-weight models on five deep-search benchmarks, averaging 73.1 messages and 65.1K tokens. Experts annotate critical steps, a six-way root-cause taxonomy, and actionable repair directives, enabling localization, cause, diagnosis, and rubric-pass metrics.

## Compared with what

Most benchmarks collapse failure to zero reward. SearchAuditBench makes the post-hoc auditor an evaluation object: can it find the earliest critical error, attribute the cause, and propose a repair that satisfies the reference rubrics?

## What the reported results show

With GPT-5.5 held fixed as the auditor backbone, the strongest baseline’s Fully-Passed Score (FPS) is 26.55%, versus 32.26% for SearchAuditor; strict critical-step localization is 44.89%. SearchAuditor’s FPS is 18.91% with Gemini 3.1 Pro and 24.62% with Claude Opus 4.8. Backbone changes cannot be attributed to the auditing framework.

FPS combines correct diagnosis with passing all expert-written repair rubrics. DeepSeek-V4-Flash judges the proposed repair; this score does not measure successful re-execution of the original search. [Paper v1, §5.1 and Table 2](https://arxiv.org/html/2608.05212v1#S5.SS1).

## Score boundary

High scores support post-hoc diagnosis and rubric-satisfying repair suggestions on this failures-only mixture. They do not establish restored execution success, a stronger original search agent, or effective online intervention. Source models, harnesses, and the benchmark mixture determine the failure distribution.

## Fair comparison conditions

Align the failed-trajectory corpus, sampling, root-cause taxonomy, localization tolerance, expert repair rubrics, grader, and auditor backbone. Comparing a GPT-5.5 framework with a Gemini 3.1 Pro framework does not isolate the framework. Actual re-execution is a separate next experiment, not the current FPS evaluator.

## Next evaluation coordinate

The next step places the auditor online and tests whether early intervention actually reduces final failures rather than merely explaining them after the fact.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use SearchAuditBench for post-hoc localization, attribution, and repair of search failures, not general success of the original search agent. Failure-only sampling changes the distribution. A strong failure auditor may still over-correct successful trajectories.

### What a concrete task looks like

Illustrative task: an auditor receives a long failed search trace and must locate the decisive deviation, explain its cause, and propose an actionable repair directive. The wrong final answer may be a symptom of an earlier incorrect assumption rather than the root cause.

### Most discriminating experiment

Evaluate localization, cause classification, and post-repair execution separately, adding successful traces to measure false alarms. Fix the original agent and remaining budget and compare audit-guided repair with restarting, ensuring gains do not merely come from more search compute.

### Pair with

[agenticragtracer](agenticragtracer.en.md) · [deepresearch-bench](deepresearch-bench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
