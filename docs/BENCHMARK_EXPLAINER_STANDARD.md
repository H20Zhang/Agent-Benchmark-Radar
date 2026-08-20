# Benchmark Explainer Standard

Use this standard for high-value benchmark notes, README folds, genealogy arguments, and field-level benchmark synthesis. The structure fixes the reasoning, not the prose template.

## 1. Measurement delta

State the smallest change that makes the benchmark worth knowing:

`previous evaluation object → newly observable capability/environment/protocol → consequence`

More examples alone are not a new coordinate unless scale repairs a known validity problem.

## 2. Predecessor / implicit critique

Identify the closest earlier benchmark and answer what became insufficient: too easy, too narrow, too static, too synthetic, too opaque, too contaminated/saturated, or too weakly diagnosed.

## 3. What it actually measures

Describe:

- target capability;
- environment and accessible state;
- task/trajectory;
- expected output/action/artifact;
- scale/data construction only when interpretation depends on it.

## 4. Protocol

Extract the variables that can change score interpretation:

`model/backbone × accessible context/state × tools/interface × prompts/hints × retries/trials × stopping rule × metrics/judge × executable validation × token/latency/tool budget`

A benchmark is not fully described by dataset size + metric.

## 5. What a score supports

State the causal boundary. If the harness, model, tools, or budget differ, treat a leaderboard gap as **system-level evidence**. Attribute to memory/retrieval/planning/tooling only under sufficiently matched conditions.

## 6. Strongest confounder / validity risk

Name the load-bearing threat: contamination, saturation, LLM-judge dependence, environment drift, hidden hints, harness sensitivity, synthetic shortcuts, stochastic retries, or omitted lifecycle cost.

## 7. What remains unmeasured

Every useful benchmark should expose the next missing coordinate. State what important capability or deployment property still lies outside the protocol.

## 8. Genealogy consequence

Assign `precursor / foundation / transition / frontier` analytically, not as prestige. Explain the nearest predecessor and continuation.

## README compression

A 60–90 second fold should explain predecessor limitation, capability × environment × protocol delta, what the score supports, strongest confounder, and field consequence in 2–4 natural paragraphs. Do not repeat a note verbatim.

## Epistemic discipline

Keep protocol facts, curator interpretation, and open measurement hypotheses distinct. Never convert leaderboard rank into component evidence by prose alone.
