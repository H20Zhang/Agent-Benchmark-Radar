# PerMemSafe: when a benign query becomes risky because of long-term user state

[中文](permemsafe.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://aclanthology.org/2026.findings-acl.320/) · [Code](https://github.com/Greysahy/permemsafe)

## What it measures

PerMemSafe derives 750 test instances from 276 user-assistant conversations across five safety-risk domains, with irrelevant exchanges exceeding 90% of each history. A system must retrieve implicit and evolving risk state and respond safely and helpfully even when the query looks benign in isolation.

## Compared with what

Conventional safety benchmarks focus on the current prompt, while memory benchmarks rarely score safety. PerMemSafe couples the two: the same query can be risky for one history and safe for another, and stale risk memory can also be harmful after the state resolves.

## Score boundary

Safety/helpfulness and recall@3 support personalized safety under the synthetic histories, fixed judge, and retrieval budget. They do not establish real-user safety because the base model's safety policy, conversation synthesis, and judge are load-bearing variables.

## Fair comparison conditions

Align risk histories, base model, retrieval budget, judge, and safety policy. Static perception and dynamic evolution belong in separate tracks.

## Next evaluation coordinate

The stronger test adds real tool consequences, access control, deletion, and adversarial memory poisoning to measure how incorrect risk state changes actions.
