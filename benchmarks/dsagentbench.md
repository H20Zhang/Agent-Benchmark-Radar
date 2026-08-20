# DSAgentBench：Real-Computer End-to-End Data Science

**中文** | [English](dsagentbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[Paper](https://arxiv.org/abs/2608.10366) · **Area: Data Agent**

> **Measurement delta.** DSAgentBench 把 data-agent evaluation 从 isolated SQL/code/analysis stage 推到**真实 computer environment 里的完整 data-science workflow**，要求 agent 在多工具之间执行并根据 intermediate outputs 持续决策。

## Predecessor / implicit critique

此前 benchmark 常把 Text-to-SQL、code generation、单步分析或特定 tool use 分开测。DSAgentBench 的批评是：这些 setting 看不到 OS grounding、tool orchestration、long-horizon dependency 与 artifact-level verification。

## What it actually measures

Benchmark 包含 **275 个任务**，覆盖 data wrangling、exploration、modeling、visualization、validation 等生命周期阶段。Agent 在真实 computing environment 中使用 notebook、IDE、terminal、browser、database 等工具，并需要把 intermediate output 带入后续 decision。

Evaluator 不是只跑代码，而是 deterministic 地检查 analytical correctness、visual output 与 model performance。

## What a score supports

论文报告最强 evaluated agent 的 task success 为 **56.70%**，open-source agents 低于 1%。这个 gap 很大，但它首先是 **end-to-end system-level evidence**：base model、tool-use reliability、OS grounding、planning、recovery 与 harness 都共同影响结果。

它不能单独证明某个 planning 或 tool-routing component 的优势。

## Strongest confounder

**Harness / computer-use stack 与 model capability 高度耦合。** 如果不同 agent 使用不同 scaffolding、tool policy 或 recovery strategy，leaderboard score 不能直接解释成 model reasoning ranking。

另外，real-computer realism 会引入 environment reproducibility 与 tool-version drift。

## What remains unmeasured

- 长时间、多 session 的 persistent project state；
- enterprise business semantics 与 ambiguous requirements；
- human clarification / approval；
- deployment/monitoring 与 failure recovery cost；
- real organization 中的权限、安全与不可逆 action。

## Genealogy consequence

`DS-1000 / executable code → workflow-oriented data-agent benchmarks → DSAgentBench real-computer end-to-end execution`

它目前更适合作为 **frontier environment/protocol benchmark**，而不是把 56.70% 当作某个 component 的 progress metric。
