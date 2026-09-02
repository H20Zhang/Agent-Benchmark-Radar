# DDR-Bench: can a data agent decide what is worth investigating?

[中文](ddr-bench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2602.02039) · [Code](https://github.com/thinkwee/DDR_Bench)

## What it actually measures

DDR-Bench targets **investigatory intelligence**: the agent is given data/entity context but not a predefined analytical question, and must set goals, explore, and discover verifiable insights. This differs from executional intelligence, where the user already specifies what analysis to perform.

## What changed relative to prior evaluation

Most data-agent benchmarks start with a well-formed task. Real analysts often begin with “what is happening here?” DDR makes problem formulation itself part of the agent loop and uses checklist-based evaluation to keep open-ended discovery partially verifiable.

## Decisive evidence

The benchmark covers real-world data domains including healthcare records, SEC 10-K/XBRL financial data, and behavioral data. The paper reports emerging capability in frontier models but persistent difficulty with long-horizon exploration; performance depends on intrinsic agentic strategies rather than only larger scaffolds or scale.

## What the score supports

DDR-Bench can support claims about autonomous exploration under its checklist of target insights. It does not prove genuinely novel discovery: any checklist necessarily defines a latent set of expected findings, and evaluator/judge choices influence open-ended credit.

## Fair comparison contract

Fix data snapshot, starting metadata, toolset, model, exploration budget, and evaluator. Do not provide one agent with candidate goals or schema interpretations absent from another. Report discovered-insight coverage together with cost and exploration depth.

## What remains unmeasured

Business value, causal validity, novelty beyond the checklist, and stakeholder relevance are not fully captured. Real investigations also include interactive clarification and decisions about when evidence is sufficient.

## Next discriminating validation

Mix planted verifiable insights with genuinely unlabeled datasets and use blinded expert review for novelty. The key distinction is whether an agent can hunt for important unknowns, not merely rediscover benchmark authors' checklist items.

## Genealogy

`answer a specified query → choose analytical subgoals → autonomous data investigation`

DDR-Bench shifts agency upstream from execution into deciding what to analyze.