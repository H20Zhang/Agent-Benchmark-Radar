# CausalDS: data agents across all three rungs of causal reasoning

[中文](causalds.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2607.08093)

## What it actually measures

CausalDS evaluates tool-using data-science agents on **causal tasks across all three of Pearl's rungs**. Each scene contains a sampled structural causal model, generated observational data, and a graph-faithful natural-language story; tasks include prediction, structure recovery, identification, effect estimation, bias diagnosis, counterfactuals, mediation, uncertainty, and warranted abstention.

## What changed relative to prior evaluation

Symbolic causal benchmarks often omit realistic data analysis, while data-science benchmarks lack known causal ground truth. CausalDS generates the SCM itself, allowing deterministic evaluation of causal correctness while still forcing agents to work with imperfect observations and code/tools.

## Decisive evidence

A reported 100-task exam across six contemporary agents finds symbolic causal reasoning comparatively strong while abstention, uncertainty quantification, and coding/tool-use efficiency still separate models. Non-answerable questions are first-class scored outcomes rather than evaluation errors.

## What the score supports

The benchmark provides unusually clean ground truth for causal reasoning and tool-grounded analysis. Because scenes are synthetic, it supports algorithmic competence more strongly than ecological validity on messy observational science.

## Fair comparison contract

Fix generated exam seed/version, observation model, tool environment, model, token/tool budget, and grader. Report Pearl rung and abstention/uncertainty metrics separately; average score can hide dangerous overclaiming on non-identifiable queries.

## What remains unmeasured

Real causal inference includes ambiguous assumptions, measurement error not captured by the generator, experiment design, domain expertise, and disputes about the causal graph itself.

## Next discriminating validation

Pair synthetic scenes with real datasets whose assumptions are deliberately underspecified, scoring whether the agent asks for missing identification assumptions rather than inventing them. This bridges causal correctness and scientific judgment.

## Genealogy

`symbolic causality ↔ data-science execution → agentic causal analysis with abstention`

CausalDS makes “knowing when causality is not identified” as important as producing an estimate.