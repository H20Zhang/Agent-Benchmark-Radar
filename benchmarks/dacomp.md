# DAComp：Data Agent 既要通过 executable checks，也要交付开放式 analysis artifact

**中文** | [English](dacomp.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

## 它在测什么

DAComp 含 210 个 tasks，跨 data engineering 与 open-ended analysis。benchmark 将可执行 transformation/query checks 与 judge-based analytical rubrics 结合，避免把所有数据工作都压成单一 SQL 或单一自然语言评分。

## 相比什么前进了

DABStep 更偏 deterministic workflow，InsightBench 更偏开放 insight。DAComp 将 hard execution checks 与 soft analytical-quality evaluation 放在同一 suite，直接暴露“代码正确但分析差”或“解释好看但数据处理错”的分离。

## 分数边界

execution + rubric score 支持完整 system 在当前 datasets、runtime 与 judge 下的任务质量；judge-based analysis 仍可能受 style 影响，不能覆盖真实 stakeholder value。

## 公平比较条件

锁定 task release、runtime、data-engineering validators、analysis judge/rubric、agent tools 与 budget，并分别报告 executable/open-ended slices。

## 下一步评测坐标

下一步应加入 business invariants 和 artifact-level reproducibility，让报告中的每个关键 claim 可回溯到执行结果。
