# MemGUI-Bench: executable GUI memory across attempts and sessions

[中文](memgui-bench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2602.06075) · [Project](https://lgy0404.github.io/MemGUI-Bench/) · [Code](https://github.com/lgy0404/MemGUI-Bench)

## What it actually measures

MemGUI-Bench tests memory inside **mobile GUI action trajectories**. Agents must retain information across steps, applications, repeated attempts, and sessions, then use that experience while navigating real interfaces. The relevant memory can be visual state, a prior interaction outcome, an app-specific procedure, or information observed in another application.

## What changed relative to prior evaluation

Most mobile-agent benchmarks emphasize current-screen grounding and one-shot task completion. The benchmark audit behind MemGUI-Bench finds only a small fraction of existing mobile tasks are genuinely memory-dependent and that cross-session learning is largely absent. MemGUI-Bench therefore makes temporal/spatial retention and experience reuse the task property rather than an incidental side effect of a long trajectory.

## Decisive evidence

The suite contains 128 tasks across 26 apps and 68 scenarios; 89.8% are classified as memory-intensive. It evaluates 11 agents from five architectural families and uses progressive scrutiny with multiple memory-oriented metrics. The reported results show large headroom even for strong GUI agents, especially when information must cross temporal or application boundaries.

## What the score supports

Task success and p@k-style repeated-attempt measures support an end-to-end claim about **GUI perception × memory × planning × execution**. They do not isolate a memory module because OCR/vision, app grounding, click execution, and recovery can fail after the correct memory was available.

## Fair comparison contract

Fix device/emulator state, app versions, login/data state, action budget, retry count, observation resolution, and model/harness. Report first-attempt success separately from improvement over repeated attempts; otherwise a stronger base GUI policy can masquerade as better experience reuse.

## What remains unmeasured

Live mobile applications drift, so reproducibility depends on environment snapshots. The benchmark does not yet establish long-term retention over weeks or months, privacy-aware memory across apps, or whether learned procedures transfer to unseen app versions.

## Next discriminating validation

Add paired fresh-agent versus experienced-agent runs with identical initial UI states, plus oracle-memory injection. This would quantify the marginal value of retained experience separately from stronger generic GUI competence.

## Genealogy

`single-session GUI grounding → cross-step retention → cross-session experience reuse`

MemGUI-Bench turns repeated GUI interaction into a memory-learning problem rather than a longer one-shot trajectory.