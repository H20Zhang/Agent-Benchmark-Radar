# LongMemEval-V2：memory 从聊天历史推进到 115M-token agent trajectories

**中文** | [English](longmemeval-v2.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[项目页](https://longmemeval.github.io/)

## 它在测什么

LongMemEval-V2 使用 451 个 curated questions、最多 500 条 trajectories、总计约 115M tokens，覆盖 web 与 enterprise agent experience，并区分 small/medium scales。评测不只问事实，还问跨轨迹的 workflow knowledge，并把 accuracy 与 latency 同时放进 contract。

## 相比什么前进了

原 LongMemEval 的 evidence 是 conversational history。V2 把 evidence 改成真实 agent trajectories，比较 no retrieval、RAG slice retrieval、带 notes 的 RAG、AgentRunbook 与 Codex 等不同 memory/context strategies；官方还用 accuracy-latency frontier/LAFS 避免“越慢越高分”被误当 progress。

## 当前成绩

Radar 在网页将 small/medium 的 accuracy 与 latency 拆为四条 track。官方 snapshot 中，small accuracy 从 no retrieval 1.3%、RAG slice 42.8%、RAG+notes 51.0% 到 AgentRunbook-R 58.6%、Codex 69.9%、AgentRunbook-C 74.9%；medium 对应 1.3%、38.1%、45.9%、57.0%、68.7%、70.1%。同一方法 latency 差异从 0.1–0.3s 到 25–186s，因此单看 accuracy 会漏掉主要 trade-off。

## 公平比较条件

锁定 small/medium scale、trajectory corpus、retrieval/context strategy、agent/model 与 latency definition；accuracy 与 latency 都必须随 protocol version 一起追踪。

## 下一步评测坐标

下一步要让 memory 不只回答 trajectory questions，而是直接执行新 task，并将 experience reuse 的收益与构建/检索成本一起评价。
