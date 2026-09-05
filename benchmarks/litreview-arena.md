# LitReview Arena / LitReviewBench / LitJudge

## 它到底测什么

这组 benchmark/evaluator 测的是 **开放式文献综述作为研究 artifact 的真实专家 utility**，而不是只检查 citation 数量或静态 rubric。领域专家做 pairwise preference，评价 coverage、claim support、结构、研究建议与总体 usefulness；与此同时，LitJudge 用这些专家偏好去校准自动 evaluator。

## 相比前身多测了什么

DeepSurveyBench 等评测通常依赖固定 rubric 或自动 judge，缺少大规模 topic-matched expert preference；SciArena 虽有竞技式比较，但并不专门针对完整 literature review 拆解证据覆盖、claim support 与研究建议。这里的核心增量是让“专家到底更愿意采用哪份综述”成为 ground truth，并单独测试 judge 与专家偏好的一致性。

## 决定性证据

公开结果显示，非人工系统对 human draft 的 **decisive overall win 仅 23.0%**；通用 judge 与专家 utility 的相关性只有 **ρ=.467**，而 LitJudge 提升到 **ρ=.792**。这两个数字分别揭示了 system quality ceiling 和 evaluator mismatch：自动系统在专家偏好下仍明显落后，而 generic judge 也不能可靠代理专家判断。

## 这个分数支持什么判断

它支持“在该 topic set 与专家标注协议上，expert-calibrated evaluator 更接近专家排序”，以及“当前自动 literature-review system 在专家整体 utility 上仍有明显 headroom”。它不能把 agentic system 与 base model 的差距归因于某种 agent architecture，因为不同系统的 token、tool、search 与 retrieval budget 并未严格匹配。

## 公平比较条件

比较生成系统时至少要固定 topic、可访问 corpus/search API、token budget、检索轮数、citation policy 与最大运行时间。比较 evaluator 时要固定 pair set、专家群体、维度定义和 tie policy，并报告 held-out calibration，而不是只在训练 LitJudge 的偏好集上给相关性。

## 研究上怎么用

这套评测最有价值的地方是把 deep-research system 的目标从“写得像综述”推进到 **专家是否觉得它覆盖了关键证据、支持了 claim，并产生可用研究判断**。如果研究一个新的 agentic search / report-writing 方法，应同时报告 retrieval evidence quality、最终 report expert preference，以及自动 judge 与专家的 calibration gap，避免只优化 evaluator proxy。

## 下一步最有价值的验证

当前缺口包括领域规范差异、living review、citation verification、cost matching 与真正 held-out judge validation。最高杠杆问题是：LitJudge 的高相关性能否跨领域、跨 topic distribution 和新系统 family 保持，而不是只在当前专家偏好分布上拟合得更好。

## 谱系位置

它把 deep-research 评价从结果 rubric 推进到专家偏好校准；`map_delta=early_signal`。如果后续多个独立 benchmark 都证明 generic LLM judge 与专家 research utility 存在系统性偏差，这条线才值得升级为 durable evaluator shift。

Primary: https://arxiv.org/abs/2608.21374

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合检验自动文献综述评价是否与领域专家判断一致。专家校准提高了评价的实际意义，但模型之间的配对胜率仍会受生成预算、来源与文本风格影响；它不等于某个内部检索组件的分数。

### 一个具体任务长什么样

示意任务：同一主题下两份匿名综述由专家比较，分别考虑组织、论证、支持关系等维度，再用这些判断校准自动评价器。文章读起来更顺并不必然意味着文献更完整或研究缺口更可靠。

### 最有判别力的实验

在未参与校准的主题与专家上验证评价器，并控制报告长度、来源池和生成预算。将引用核验与专家偏好分开报告，检查模型排名是否在不同学科和评价器下保持，而非只符合校准集偏好。

### 建议搭配

[das-bench](das-bench.md) · [deepresearch-bench](deepresearch-bench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
