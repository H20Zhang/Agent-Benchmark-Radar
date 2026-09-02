# CausalDS: data-science agents should not collapse association, intervention, and counterfactual reasoning

[中文](causalds.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2607.08093) · [Code](https://github.com/andleb/causalds)

## What it measures

CausalDS samples structural causal models, generates observational data and graph-faithful realistic stories, and derives tasks across all three of Pearl's rungs: prediction/association, causal structure and effect identification/estimation, and counterfactual or mediation reasoning. The frozen main exam has 100 tasks, treats abstention on non-identifiable questions as first-class, and usually requires coding/tool use.

## Compared with what

Symbolic causal benchmarks lack realistic data analysis, while data-science benchmarks often lack principled causal ground truth. A hidden SCM supplies exact causal truth while retaining executable data work, separating numerical solvability from whether a causal answer is warranted.

## Score boundary

CausalDSScore or accuracy supports causal data-science competence under the synthetic SCM generator, observation model, and frozen exam. It does not establish correct causal assumptions in real domains, where model specification itself is often the hard problem.

## Fair comparison conditions

Align main exam or ablation configuration, public/private boundary, observation variant, runtime/tools, agent budget, and grader. Clean, noisy, and proxy observations require separate tracks.

## Next evaluation coordinate

The next step adds imperfect causal assumptions, human domain constraints, and intervention cost, testing whether an agent can challenge the SCM rather than only reason inside a supplied one.
