# CAME-Bench: the same entity is not the same memory under different latent goals

[中文](came-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://aclanthology.org/2026.findings-acl.584/) · [Code](https://github.com/Seattleyrz/contextual-intent)

## What it measures

CAME-Bench has 14 goal-oriented trajectories and 373 questions with average contexts around 23K, 137K, and 408K tokens across travel planning and policy debate. Recurring entities appear under incompatible latent goals, requiring retrieval to use current intent rather than entity similarity alone.

## Compared with what

Standard vector retrieval treats same-name entities and nearby facts as similar candidates. CAME-Bench deliberately creates contextual interference, making failures caused by misunderstanding the current goal observable.

## Score boundary

QA/evidence retrieval and length scaling support context-aware retrieval under synthetic trajectories. They do not test real users, actions, or memory repair. Co-design with the STITCH method is also an interpretation variable.

## Fair comparison conditions

Align trajectory generation, domain, length bucket, judge, and evidence protocol, and report 23K/137K/408K conditions separately.

## Next evaluation coordinate

A stronger test uses real evolving projects with multiple competing goals and requires memory retrieval to support later action and conflict repair.
