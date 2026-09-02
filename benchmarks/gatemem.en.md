# GateMem: shared memory needs utility, access control, and forgetting at once

[中文](gatemem.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2606.18829) · [Code](https://github.com/rzhub/GateMem)

## What it measures

GateMem contains 91 multi-party episodes and 2,218 hidden checkpoints across medical, office, education, and household settings. It jointly evaluates legitimate utility, unauthorized disclosure, and recovery after deletion, making multi-principal governance part of the memory contract.

## Compared with what

Traditional memory benchmarks treat retrievability as uniformly good. GateMem makes one fact potentially visible, forbidden, or deleted depending on the principal, so memory quality must be optimized together with access boundaries and active forgetting.

## Score boundary

The Memory Governance Score supports behavioral access/forgetting under the synthetic policy and harness. It does not prove physical erasure or real authentication/authorization security. Deletion success means non-retrievability under the protocol, not storage-layer deletion proof.

## Fair comparison conditions

Align authorization policy, harness, backbone, judge, and retrieval budget. Different principal policies or deletion semantics require distinct tracks.

## Next evaluation coordinate

The next step integrates real identity, authorization, and storage lifecycle so revocation removes information consistently from caches, indexes, and derived representations.
