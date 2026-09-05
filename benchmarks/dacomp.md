# DAComp：Data Engineering 和 Data Analysis 不是同一种 agent 能力

**中文** | [English](dacomp.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2512.04324) · [项目页](https://da-comp.github.io/) · [代码](https://github.com/ByteDance-Seed/DAComp)

## 它到底测什么

DAComp 覆盖 **完整 data-intelligence lifecycle** 的两个不同 workload：repository-level Data Engineering (DE) 和 open-ended Data Analysis (DA)。DE 要设计/演化多阶段 SQL pipeline；DA 要规划、迭代 coding、解释中间结果并给 actionable recommendation。

## 相比此前评测多测了什么

Text-to-SQL / code benchmark 主要评局部 transformation。DAComp 把 enterprise data work 变成 repository/workflow problem，更关键的是它没有把 engineering correctness 与 analytical insight 混成一种能力。

## 决定性证据

benchmark 有 210 个任务。SOTA agent 在 DE 上 success rate 低于 20%，DA 平均也低于 40%。两边的差异说明 holistic pipeline orchestration 与 open-ended analytical reasoning 是两个独立瓶颈，而不是一个模糊的“data agent ability”。

## 这个分数能证明什么

DE 的 execution-based result 对 repository/workflow correctness 证据较强；DA 依赖经过验证的 rubric-guided LLM judge，所以 analytical quality claim 会继承 evaluator assumption。aggregate score 不应掩盖 DE/DA split。

## 公平比较契约

应固定 repository snapshot、environment、agent harness、model、execution budget 与 DA judge version，并分别报告 DE/DA 和成本；擅长 iterative coding 的 scaffold 与擅长 report synthesis 的 scaffold 可能有完全不同 economics。

## 还没有测什么

生产 enterprise system 还有 permission、production write、incident、stakeholder negotiation、semantic-layer evolution 与长期 maintenance；open-ended DA 也仍以 rubric 为主，而不是真实 business impact。

## 下一步最有判别力的验证

把 DE 与 DA 串起来：先要求 agent build/repair transformation pipeline，再从其产出回答 business question，直接测试真实 data lifecycle 中的 error propagation。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合在同一研究中同时覆盖数据工程与开放式分析，但两条轨道不宜用未经解释的均分合并。仓库转换主要依赖可执行验证，分析报告更依赖评分标准；不同评价机制决定了结论的不确定性。

### 一个具体任务长什么样

示意任务：工程任务要求修改数据管道并产生正确输出，分析任务则要求探索业务问题并形成报告。前者测试状态与代码变化，后者还涉及选择分析角度和解释证据，失败模式不能互换。

### 最有判别力的实验

分别固定工程测试环境与报告评分器，按轨道展示质量、时间和调用代价。对工程任务给定正确修改位置，对分析任务给定正确中间结果，诊断发现与推理瓶颈；跨轨道优势应分别成立再讨论通用性。

### 建议搭配

[data-eng-bench](data-eng-bench.md) · [insightbench](insightbench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`local code/SQL → repository data engineering + open-ended analysis → integrated data-intelligence lifecycle`

它说明“data agent”应该按 work product 分解，而不是只看一个 leaderboard number。