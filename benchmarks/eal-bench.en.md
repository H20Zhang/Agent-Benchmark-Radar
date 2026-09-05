# EAL-Bench: when persistent memory creates authority that history never granted

[中文](eal-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2609.01836) · **Area: Agent Memory**

## What it measures
EAL-Bench narrows memory correctness to preservation of evolving authorization state and asks whether memory errors propagate into executable unauthorized actions. It separates the memory writer, downstream executor, canonical authorization ledger, and action predicate.

## Compared with what
AuthMem-Bench already makes source authority explicit. EAL-Bench adds evolving permissions, restrictions, and revocations, then tests both formation of false authority in memory and downstream propagation into actions.

## Protocol and decisive evidence
Across procurement, cybersecurity, and finance, five LLMs act as memory writers and two as executors. Under incremental memory updates, false authority is created for up to 50.2% of unauthorized requests in some settings; once present, executors act on it in 98.6% of trials.

## Score boundary
The result supports treating persistent memory as part of an agent's effective authorization policy, not merely as a performance component. It does not establish behavior across arbitrary enterprise authorization systems because writer, executor, update representation, and task construction remain load-bearing variables.

## Remaining gap and next validation
Longer deployments, multi-writer memory, broader tool stacks, and independent evaluation on real authorization systems remain open. The most discriminating next experiment holds the executor and authorization history fixed while changing only the memory representation/update mechanism, reporting false-authority formation separately from execution after formation.

Primary: https://arxiv.org/abs/2609.01836
