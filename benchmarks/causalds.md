# CausalDS：让 data agent 真正跨过 Pearl 三层因果推理

**中文** | [English](causalds.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2607.08093)

## 它到底测什么

CausalDS 评估 tool-using data-science agent 在 **Pearl 三个 rung** 上的 causal task。每个 scene 包含 sampled structural causal model、生成的 observational data 与 graph-faithful natural-language story；任务覆盖 prediction、structure recovery、identification、effect estimation、bias diagnosis、counterfactual、mediation、uncertainty 与 warranted abstention。

## 相比此前评测多测了什么

symbolic causal benchmark 常缺真实 data analysis，data-science benchmark 又没有已知 causal ground truth。CausalDS 直接生成 SCM，因此既能 deterministic 地判断因果答案，又要求 agent 面对 imperfect observation、coding 和 tool use。

## 决定性证据

论文的 100-task exam 评估 6 个 contemporary agent：symbolic causal reasoning 相对接近解决，而 abstention、uncertainty quantification 与 coding/tool-use efficiency 仍明显拉开模型差距。不可回答问题也被作为一等 scored outcome，而不是 evaluator exception。

## 结论边界：这个分数能证明什么

它对 causal reasoning + tool-grounded analysis 提供非常干净的 ground truth；但 scene 是 synthetic，因此对 algorithmic competence 的证据比对真实 messy observational science 的 ecological validity 更强。

## 公平比较契约

应固定 generated exam seed/version、observation model、tool environment、model、token/tool budget 与 grader，并按 Pearl rung、abstention、uncertainty 分开报告；平均分会掩盖在 non-identifiable query 上危险的过度断言。

## 还没有测什么

真实 causal inference 还有 ambiguous assumption、generator 未覆盖的 measurement error、experiment design、domain expertise，以及“causal graph 本身就有争议”的情况。

## 下一步最有判别力的验证

把 synthetic scene 与 assumption 故意不完整的真实 dataset 配对，测试 agent 会不会主动询问缺失 identification assumption，而不是自己编出来，连接 causal correctness 与 scientific judgment。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究数据智能体是否知道哪些因果结论可以从给定信息中识别。预测准确不等于因果推断正确；合理弃答和不确定性表达是能力的一部分，不应被一律作答的高覆盖率掩盖。

### 一个具体任务长什么样

示意任务：系统获得带领域故事的观测数据，需要判断能否估计某项干预效果或反事实。相关关系可被准确计算，但缺少识别条件时，给出精确因果数字仍是错误行为。

### 最有判别力的实验

按预测、干预和反事实层级分别报告，把正确图或识别假设给定作为诊断。比较可识别与不可识别的配对场景，联合评分估计误差、区间和弃答；不要以合成数据上的表现替代真实干预验证。

### 建议搭配

[statabench](statabench.md) · [insightbench](insightbench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`symbolic causality ↔ data-science execution → agentic causal analysis with abstention`

它把“知道什么时候因果不可识别”提升到和给出 estimate 同样重要。