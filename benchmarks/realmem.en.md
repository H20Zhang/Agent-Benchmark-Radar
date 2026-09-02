# RealMem: moving from casual chat to evolving project state

[中文](realmem.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://aclanthology.org/2026.findings-acl.703/) · [Code](https://github.com/AvatarMemory/RealMemBench)

## What it measures

RealMem covers 11 realistic project scenarios and more than 2,000 cross-session dialogues in which goals, artifacts, and relevant state evolve over time. The target is project dependencies and changing objectives rather than facts from casual conversation.

## Compared with what

Benchmarks such as LoCoMo primarily evaluate conversational memory. RealMem moves toward persistent project state, where an old goal may be obsolete and an artifact may have a current version, closer to production collaboration.

## Score boundary

Natural-user-query performance supports project-state tracking under the synthetic trajectory and judge. It does not establish reliability of permissions, writes, or external tools in real collaboration because trajectories are multi-agent generated and interaction remains dialogue-only.

## Fair comparison conditions

Align trajectory generation, dialogue model, project scenario, history visibility, and judge. A different synthetic generator can change dependency density and difficulty.

## Next evaluation coordinate

The next step connects project memory to real files, code, calendars, database writes, and permissions so the operational consequences of stale state become measurable.
