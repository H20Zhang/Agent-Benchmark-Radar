# MLAgentBench: iterative machine-learning experimentation as an agent task

[中文](mlagentbench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2310.03302) · [Code](https://github.com/snap-stanford/MLAgentBench)

## What it actually measures

MLAgentBench evaluates agents that **iteratively conduct machine-learning experiments**: read/write files, modify code, execute experiments, inspect outputs, form hypotheses, and try again. Its 13 tasks range from CIFAR-10 to more recent challenges such as BabyLM.

## What changed relative to prior evaluation

Code-generation benchmarks ask for a solution once. ML experimentation is a closed loop: choose an intervention, pay execution cost, interpret noisy feedback, and update the plan. MLAgentBench therefore makes experiment iteration and long-term planning the evaluation object.

## Decisive evidence

Among the evaluated agents, Claude 3 Opus reaches the highest average success rate at 37.5%. Performance varies from 100% on well-established older datasets to 0% on some recent Kaggle challenges, while the authors identify long-term planning and hallucination as central failure modes.

## What the score supports

The benchmark supports end-to-end experimentation ability under a fixed repository/task setup. It cannot isolate model research skill from scaffold, compute budget, starting code quality, or benchmark familiarity; the age-dependent result also warns about contamination/prior-knowledge effects.

## Fair comparison contract

Fix repository snapshot, starting baseline, hardware, wall-clock/experiment budget, agent tools, model, and success threshold. Report number of experiments and compute consumed, not only whether the final score crosses the target.

## What remains unmeasured

Thirteen tasks provide limited coverage, and benchmark success is not equivalent to scientifically valid research: hypothesis novelty, robustness, reproducibility, negative-result interpretation, and anti-gaming safeguards need stronger treatment.

## Next discriminating validation

Use hidden post-cutoff repositories and hold compute fixed while varying only planning/recovery mechanisms. This would better separate research-agent competence from pretrained familiarity and brute-force experimentation.

## Genealogy

`one-shot ML code → iterative experiment loop → autonomous research engineering`

MLAgentBench established experimentation—not code generation—as a distinct agent capability.