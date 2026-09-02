# DataSciBench：用程序化规则评估 multi-step data-science prompt

**中文** | [English](datascibench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2502.13897) · [项目页](https://datascibench.github.io/) · [代码](https://github.com/THUDM/DataSciBench)

## 它到底测什么

DataSciBench 评估 LLM/agent 对 **multi-step data-science prompt** 的完成能力，覆盖 6 类任务：cleaning/preprocessing、exploration/statistics、visualization、predictive modeling、data mining/pattern recognition、interpretability/report generation。

## 相比此前评测多测了什么

当 output 不再是一段有唯一答案的 code 时，data-science evaluation 很难自动化。DataSciBench 提出 Task–Function–Code (TFC)：用 25 个 aggregate function + programmatic rule，把 222 个 curated prompt 拆成 519 个可验证 ground-truth test case。

## 决定性证据

benchmark 一共评估 23 个模型：6 个 API model + 17 个 open-source general/code model。真正重要的贡献不是某个 leaderboard 数字，而是 measurement infrastructure：先用 LLM self-consistency + human verification 构造 GT，再由 TFC 多粒度判断 execution outcome。

## 这个分数能证明什么

DataSciBench 支持 TFC ontology 下较广的 data-science task completion，但如果 prompt 已经指定分析目标，它对 autonomous workflow control 的证明有限；visualization/report metric 也比 deterministic transformation 更依赖 evaluator assumption。

## 公平比较契约

应固定 prompt/data version、execution environment、TFC rule、model、tool access 与 retry budget，并按 task type / aggregate function 报告，而不是只给 final score；routine transform 强可能掩盖 modeling/interpretation 弱。

## 还没有测什么

long-horizon project state、repository maintenance、data discovery、business semantics、collaboration 与 production deployment 都超出 bounded prompt episode。

## 下一步最有判别力的验证

检查 TFC category 是否能预测更长 agent trajectory 的 failure：end-to-end project 做错后，benchmark 能不能正确指出缺的是哪种 primitive capability。

## 演化位置

`single code task → multi-step data-science prompt → decomposable execution evaluation`

DataSciBench 更持久的贡献，是让复杂分析 output 变得更可程序化验证。