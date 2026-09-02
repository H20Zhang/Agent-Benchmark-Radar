# AgenticDataBench：给真实 data-science task 加上细粒度 skill 坐标

**中文** | [English](agenticdatabench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2607.01647) · [项目页](https://agenticdatabench.github.io/) · [代码](https://github.com/AgenticDataBench/AgenticDataBench)

## 它到底测什么

AgenticDataBench 在真实 data-science task 上增加 **fine-grained skill label**：344 个任务、15 个 domain、97 个真实 dataset，总数据量 27.3 GB / 123.1M row，并提供 433 个 ground-truth skill label。

## 相比此前评测多测了什么

end-to-end data-science benchmark 能说任务做没做对，却常说不清 benchmark 到底覆盖哪些能力。AgenticDataBench 加入 skill taxonomy，使 coverage 与 agent weakness 可以按更细粒度分析。

## 决定性证据

benchmark 同时提供 DevSet 标准提交与 TestSet sandboxed agent-code execution，后者会捕获 execution trace。官方报告 human performance 大约 84–90%，说明 benchmark 有明显 headroom，但不是不可达的封闭难题。

## 这个分数能证明什么

skill-level result 可以说明 coverage 与 recurring weakness，但不能把 skill label 当作独立 causal module：一个任务通常需要多个 skill 协同，agent scaffold 也会改变这些能力如何表现。

## 公平比较契约

应固定 dataset version、sandbox、tool availability、agent harness、model 与 execution budget，并同时看 skill distribution 与 aggregate accuracy；hidden TestSet 不能在调参过程中被反复消费。

## 还没有测什么

skill taxonomy 本身是设计者选择的 ontology；production business semantics、longitudinal data change、collaboration 与 data governance 只被部分覆盖。

## 下一步最有判别力的验证

用 skill label 构造只差一个 required competency 的 matched task pair，再验证 targeted intervention 是否只改善预测 slice，从而检验 taxonomy 真能否作为诊断工具。

## 演化位置

`end-to-end data tasks → skill-labeled coverage → capability-targeted data-agent improvement`

它让“data-agent benchmark 到底测了哪些技能”变成可量化问题。