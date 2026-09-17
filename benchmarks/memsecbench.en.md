# MemSecBench

## Measurement object

Tracks malicious memory from task-mediated writing through persistence and external consequences to selective repair with benign-memory preservation.

## What changed compared with predecessors

Compared with poisoning or utility tests alone, links consequence and repair to the same verified post-write state.

## Protocol and comparison controls

Execute and Forget fork independently from verified poisoned memory. Success separates W1 write, W2 persistence, E1 exposure, E2 adoption, E3 externalization, F1 repair and F2 benign preservation. State evidence and programmatic gates constrain an external judge.

## Decisive evidence and score ceiling

Reported persistence is 84.2% and full Write–Execute success 50.3% over all configurations/cases. Execute and selective-repair rates instead condition on successful poisoning; they must not be compared as if their denominators were identical.

## Strongest confounders and limitations

The backend treatment includes its adapter and active settings. Matched comparisons support differences between evaluated stacks, not a universal ranking of pure storage mechanisms. Public protocol details are verified; a downloadable implementation was not independently located.

## Coverage gap and next experiment

Conditional lifecycle risk after attacker content enters a supported carrier is not an estimate of real-world compromise frequency.

Fix harness, model and initialization, then report unconditional harm plus conditional repair and retained benign utility. Add a no-attack control to expose destructive defenses.

## Genealogy and use

[MPBench](mpbench.en.md) · [Utility Under Attack](utility-under-attack.en.md)

This entry is an `early_signal`: acceptance of a useful evaluation object does not promote one paper into a durable field-map claim.

## Primary sources and version

[Paper](https://arxiv.org/abs/2607.27080) · [Reviewed full text](https://arxiv.org/html/2607.27080v1)

First public event: **2026-07-29**. Reviewed: **2026-09-17**. Source release and Radar acceptance are separate events.

[中文](memsecbench.md) · [Complete index](../library/README.en.md)
