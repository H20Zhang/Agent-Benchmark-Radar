# GroupMemBench: in multi-party dialogue, who knows what is part of memory state

[中文](groupmembench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.14498) · [Code](https://github.com/UCSB-NLP-Chang/GroupMemBench)

## What it measures

GroupMemBench releases 745 questions across four synthetic enterprise domains covering multi-hop, update, temporal, user-implicit, ambiguity, and abstention cases. Answers depend on speaker identity, reply structure, group state, and audience-specific terminology, so memory is no longer one global fact set.

## Compared with what

One-to-one memory benchmarks implicitly treat a fact as having the same meaning for every query. GroupMemBench makes participant identity and asker conditioning part of the contract, testing who said or believes something and how it should be expressed to a particular audience.

## Score boundary

Asker-conditioned QA supports group-state tracking under the synthetic conversation graph. It does not test real organizational permissions, deletion, or collaborative writes. Speaker metadata can also make retrieval easier and must be treated as protocol state.

## Fair comparison conditions

Align conversation graph, asker role, retriever metadata access, answerer, and judge, and report the six question types separately.

## Next evaluation coordinate

The next step combines participant-conditioned memory with real authorization, shared artifacts, and group actions, separating belief tracking from access control.
