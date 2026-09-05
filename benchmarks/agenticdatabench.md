# AgenticDataBench：给真实 data-science task 加上细粒度 skill 坐标

**中文** | [English](agenticdatabench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2607.01647) · [项目页](https://agenticdatabench.github.io/) · [代码](https://github.com/AgenticDataBench/AgenticDataBench) · **领域：Data Agent**

AgenticDataBench 的核心价值不是又增加一组 end-to-end data-science tasks，而是给这些任务加上 **fine-grained skill labels**：不仅看“做没做对”，还试图回答“到底是哪类能力在拖后腿”。

## 它到底测什么

Benchmark 包含 **344 个任务、15 个 domain、97 个真实 dataset**，总数据量约 **27.3 GB / 123.1M rows**，并提供 **433 个 ground-truth skill labels**。

任务仍然是较真实的数据科学工作，但每个任务同时被映射到更细的 competency taxonomy。这样可以从两个层面观察 agent：

- end-to-end：任务是否最终成功；
- diagnostic：失败是否集中在某些 recurring skills。

这比只给一个 aggregate accuracy 更适合做能力覆盖分析。

## 相比此前评测多测了什么

很多 data-science benchmark 的一个根本问题是：**task distribution 本身不透明**。

一个系统总分提高 5 个点，可能只是它擅长的任务比例更高；一个 benchmark 很难，也可能只是被少数特殊任务主导。没有 skill annotation 时，很难回答：

- benchmark 到底覆盖多少数据理解、清洗、统计、建模、调试等能力；
- agent 的错误是广泛能力缺失，还是一个高频 bottleneck；
- 新方法改善的是核心能力，还是只针对某一类 task pattern。

AgenticDataBench 用显式 taxonomy 把这些问题变成可以统计的对象。

## 实际怎样评测

Benchmark 同时提供 DevSet 与 TestSet。TestSet 使用 sandboxed agent-code execution，并捕获 execution trace，因此评价不只依赖模型最终声称“完成了”，而可以检查实际执行结果。

解释结果时应同时记录：

- dataset / task version；
- sandbox 与 package environment；
- tool availability；
- model 与 agent harness；
- execution / retry budget；
- skill distribution；
- aggregate metric 与 per-skill breakdown。

如果只报告总分，会丢掉这个 benchmark 最重要的 diagnostic value。

## 决定性证据与分数边界

官方报告 human performance 约 **84–90%**。这个数字的重要含义不是“人类上限是多少”，而是 benchmark 仍有明显 headroom，同时并非完全脱离现实可完成范围。

skill-level score 可以支持“某类任务在当前系统上反复失败”这样的诊断；它不能自动支持“模型缺少一个独立 skill module”。

原因是同一个任务往往需要多个能力协同，某个 skill label 只是对任务要求的描述，而不是对系统内部因果机制的分解。

## 最主要的混杂因素

第一是 **skill ontology 本身**。taxonomy 是设计者选择的抽象方式；不同 taxonomy 可能把同一个 failure 切成不同类别。

第二是 **multi-skill interaction**。任务失败可能发生在数据理解，但最终表现为代码执行失败；仅靠标签无法确定真正 root cause。

第三是 **agent harness sensitivity**。相同 model 在不同 scaffold、tool contract、retry policy 下可能暴露完全不同的 skill profile。

第四是 **hidden-set consumption**。如果 TestSet 被反复用于 prompt / tool / policy 调参，skill-level diagnostic 也会逐渐变成 benchmark-specific optimization。

## 公平比较契约

至少应固定：

- task / dataset version；
- sandbox、依赖和资源限制；
- tool set 与数据访问接口；
- model、agent harness 与 system prompt；
- execution / retry / token budget；
- evaluator；
- Dev/Test 使用边界。

除了 aggregate score，最好同时报告每个 skill slice 的样本数、准确率和置信区间，避免用极小 slice 得出过强结论。

## 还没有测什么

AgenticDataBench 已经提升了 coverage transparency，但仍没有完整测量：

- skill label 是否具有真正 causal diagnostic value；
- business semantics 与含糊需求澄清；
- longitudinal data / schema change；
- collaboration 与 review workflow；
- governance、权限与不可逆 data operation；
- 不同 skill failure 的严重度是否相同。

此外，真实生产系统最关心的往往不是“平均缺哪个 skill”，而是 **哪个 failure 会让最终决策错误且难以发现**。

## 下一步最有判别力的验证

最值得做的是 **skill intervention test**：构造 matched task pairs，使两组任务只在一个 required competency 上存在系统差异，然后针对该 skill 加一个明确 intervention。

如果 intervention 主要改善预测中的 skill slice，而对其他 slice 影响较小，taxonomy 才更像真正有解释力的诊断坐标，而不是事后分类标签。

进一步还可以构建一个 `skill × harness × backbone` 矩阵，检查所谓 skill weakness 是否跨系统稳定。

## 演化位置

`end-to-end data tasks → skill-labeled coverage → causal capability diagnosis → capability-targeted improvement`

AgenticDataBench 完成了第二步：它让“这个 benchmark 到底测了哪些数据工作能力”变得可量化。下一步关键不是增加更多标签，而是验证这些标签能否真的指导系统改进。
