# AgenticDataBench：Data Agent 的目标是完整 deliverable，而不是单一 query success

**中文** | [English](agenticdatabench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[项目页](https://agenticdatabench.github.io/)

## 它在测什么

AgenticDataBench 覆盖 344 个 end-to-end realistic data tasks、97 个 datasets、15 domains、约 27.3GB / 123.1M rows，并用 433 skill labels 描述数据工作。它评价完整 data-agent workflow，而不是 text-to-SQL 子任务；官方 leaderboard 比较 Codex、Claude Code、Smolagents、DA-Agent 等 agent scaffold 与不同 backbone 组合。

## 相比什么前进了

DAB 聚焦跨数据库 enterprise questions；AgenticDataBench 更强调完整分析工作流与技能覆盖。一个 agent 可能 SQL 很强，但在 data understanding、transformation、analysis 或 delivery 上失败，因此 overall accuracy 是更严格的 system-level signal。

## 当前成绩如何解释

官方 2026-07-02 snapshot 中最好结果约 49.39%，其余 agent/model combinations 分布到约 31.83%–47.77%。这些是 scaffold+model 的 packaged-system comparison，不能把差值归因于某个 orchestration idea。网页保存完整官方 12-row snapshot，而 README 不承载榜单。

## 公平比较条件

锁定 benchmark snapshot、agent scaffold、model、tool/runtime、task limits 与 evaluator。不同 agent+model 组合应作为 system entries，而非模型裸能力排名。

## 下一步评测坐标

下一步要进一步区分 business truth、artifact correctness、recovery 与 cost，让 end-to-end 失败可被定位到具体 workflow stage。
