# DABstep：多步金融数据分析，同时保留 objective grading

**中文** | [English](dabstep.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2506.23719) · [Benchmark](https://huggingface.co/spaces/adyen/DABstep)

## 它到底测什么

DABstep 来自金融 analytics platform 的 **realistic multi-step data analysis**：450+ 个 challenge 要同时处理 transaction data、heterogeneous documentation、cross-source lookup，并通过 code 得到精确结果。

## 相比此前评测多测了什么

很多 open-ended analytics benchmark 强依赖 LLM judge。DABstep 保留较长 agentic workflow，却把最终答案设计为 factoid，并可自动 correctness check，因此把 realistic multi-step analysis 与 objective grading 放到了一起。

## 决定性证据

最强被测 agent 在 hardest task 上 accuracy 也只有 14.55%。环境不仅有 transaction record，还有 fee structure、merchant metadata、category/country lookup table 与 documentation，因此必须同时完成 executable data manipulation 与 semantic cross-reference。

## 这个分数能证明什么

DABstep 对 bounded financial workspace 下 end-to-end analytical execution 证据很强，但不能单独定位 planning、code quality、documentation retrieval 或 semantic interpretation；synthetic benchmark environment 也绝不能被理解成真实金融系统访问能力。

## 公平比较契约

应固定 benchmark version、file/documentation、tool interface、model、trajectory/call budget 与 final scorer，并按 difficulty slice 报告。预先给某个系统 parsed relation 或手工 semantic mapping，会把 cross-source 难度直接降低。

## 还没有测什么

生产金融 analytics 还有 live schema、permission、PII、governance、write、audit trail 与变化的 business logic；factoid grading 也不能覆盖完整 analyst-facing deliverable 的质量。

## 下一步最有判别力的验证

在 source selection、join/mapping、computed quantity 等中间步骤加入 deterministic checkpoint，既保留 objective grading，又能定位 multi-step workflow 到底在哪一步失败。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合检验文档中的业务规则能否贯穿多步数据分析。单一支付领域有利于深入诊断，但不应当作通用行业能力；精确答案背后的规则选择和中间转换，比最终字符串匹配更能解释失败。

### 一个具体任务长什么样

示意任务：系统从交易文件和规则文档中确定计算口径，处理例外条件并汇总成一个精确答案。漏掉一个规则例外，可能让所有代码都成功执行但结果整体偏离。

### 最有判别力的实验

固定公开数据版本和步骤预算，比较原文档、结构化规则与正确中间表给定。按任务难度与规则组合分项，记录格式错误和数值错误，判断方法是在读懂规则还是仅改善输出规范。

### 建议搭配

[warehouse-reliability-bench](warehouse-reliability-bench.md) · [dataspace](dataspace.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`single-table analysis → heterogeneous documented workspace → objectively graded multi-step data agent`

它说明 realistic agentic analysis 并不一定只能依赖主观 LLM judge。