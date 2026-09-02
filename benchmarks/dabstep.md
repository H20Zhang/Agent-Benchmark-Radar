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

## 演化位置

`single-table analysis → heterogeneous documented workspace → objectively graded multi-step data agent`

它说明 realistic agentic analysis 并不一定只能依赖主观 LLM judge。