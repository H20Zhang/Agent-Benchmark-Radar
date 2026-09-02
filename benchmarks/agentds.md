# AgentDS：Data Agent benchmark 也应该比较 human-only、AI-only 与 human-AI collaboration

**中文** | [English](agentds.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2603.19005)

## 它在测什么

AgentDS 基于 17 个 data-science challenges、6 个 industries，包含 29 teams / 80 participants，并比较 AI-only 与 human-AI collaboration 等工作方式；任务使用 synthetic enterprise-pattern data 与 hidden leaderboard 评价完整分析/建模成果。

## 相比什么前进了

多数 benchmark 只排名 agents。AgentDS 把 augmentation 本身设为 measurement object：AI 独立完成多少、与人协作是否更好、哪些任务需要 human judgment，从而更接近实际 data-team adoption question。

## 分数边界

challenge score 支持当前 participant pool、hidden tests 与 collaboration protocol 下的 performance；小规模 team sample、synthetic data 与 human skill variance 都限制因果结论，不能用一次竞赛证明“agent 可替代 data scientist”。

## 公平比较条件

锁定 challenge release、human participant selection、AI tools/models、time budget、collaboration rules 与 hidden evaluator。AI-only/human-AI/human-only 必须分 track。

## 下一步评测坐标

下一步需要 longitudinal team productivity、review burden、error severity 与 decision impact，测 AI 是减少还是转移人的工作量。
