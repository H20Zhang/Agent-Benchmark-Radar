# ClaimProbe：Deep Research 报告的 claim-source 忠实度审计

**中文** | [English](claimprobe.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.28643) · [代码](https://github.com/SalesforceAIResearch/claimwriter-deep-research)

## 它到底测什么

ClaimProbe 测的是 **retrieved evidence 到最终 report claim 之间的信息转译是否忠实**。在检索证据固定以后，它逐 claim 审计：陈述有没有来源支持、引用是否归到了正确 source、已有支持是否漏引、关键必要事实是否真正写进报告。这样可以把 writer-side evidence materialization / attribution 与 retrieval/search quality 分离。

## 相比前身多测了什么

DeepResearch Bench、DAS-Bench 与 LitReview Arena 已经覆盖整体报告质量、citation/discourse 与专家偏好，但 holistic score 往往把多个 failure layer 压成一个数字：证据没找到、找到了但没写、写了但引错、写得不好看都可能一起扣分。ClaimProbe 增加了 **`retrieved evidence → written claim → cited source`** 的细粒度诊断坐标，因此更适合做 causal-ish system debugging。

## 决定性证据

在 Enterprise Deep Research 的 **fixed-evidence writer intervention** 中，上游 evidence 保持不变，hallucination 从 **15.89 降到 5.02**，misattribution 从 **18.94 降到 5.43**，necessary fact recall 从 **36.83 提高到 45.85**。由于检索集合固定，这组结果比端到端总分更能支持“writer-side evidence materialization / attribution 改善”这一层的增益，而不是把变化误归因于 search 或 planning。

## 这个分数支持什么判断

ClaimProbe 可以支持“给定同一 evidence set，某个 writer / synthesis mechanism 更少 hallucinate、更少错引、能覆盖更多必要事实”。它不能支持“整个 deep-research agent 更会找证据”，也不能把最终 report utility 完全还原成这些局部指标：holistic RACE 改善较小，readability 还有时下降，说明局部 faithfulness 与整体可读/有用性并非同一个目标。

## 公平比较条件

比较 writer 时需要固定 evidence set、claim segmentation、support-search procedure、citation availability、writer token budget、prompt 与 judge。尤其不能让一个 writer 获得更多或更相关 evidence，再把 hallucination 下降解释为 writing mechanism 更强。若比较 evaluator，也应报告人类一致性与 support-retrieval recall，因为 judge 的错误会直接进入 benchmark score。

## 证据强度与限制

主 hallucination judge 与人工的一致性只有 **Cohen κ=0.484**，support search 受 **top-20 embedding shortlist** 限制；dynamic-update study 只覆盖 **5 个 DeepResearch Bench tasks**。因此当前最可信的是 fixed-evidence 条件下的 writer-layer相对差异，而不是所有 claim-level error 的绝对 prevalence。

## 研究上怎么用

如果研究新的 agentic retrieval / report generation 系统，ClaimProbe 很适合作为 **failure-layer attribution benchmark**：先固定 retrieval 判断 writer，再固定 writer 改 retrieval，最后才看端到端 report utility。这样可以避免“最终报告更好”这种 package-level claim 无法回答到底是 search、evidence selection、synthesis 还是 citation grounding 在起作用。

## 下一步最有价值的验证

最高杠杆的缺口有两个：一是把 claim-support judge 做到更高的人类一致性并验证 shortlist recall；二是在更大规模 held-out deep-research tasks 上测试局部 faithfulness 改善是否稳定转化为专家 report preference。若二者不相关，未来 benchmark 需要把 factual faithfulness 与 research usefulness 保持为两个独立坐标。

## 谱系位置

`map_delta=early_signal`。ClaimProbe 新增了 `retrieved evidence → written claim → cited source` 的独立诊断层，但单篇证据不足以改 durable Benchmark Map。它的潜在重要性在于：未来 Deep Research benchmark 可能从“评一个最终 artifact”演化成**按 retrieval、materialization、attribution、utility 分层评测**。

**Primary:** https://arxiv.org/abs/2608.28643 · **Code:** https://github.com/SalesforceAIResearch/claimwriter-deep-research

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合把研究报告中的不支持、错引与遗漏分开审计，尤其适合固定证据后的写作侧改进。主张找不到支持既可能是生成错误，也可能是审计器的候选来源搜索漏检；两者需要独立验证。

### 一个具体任务长什么样

示意任务：报告中的一个主张确实被某份材料支持，但引用指向另一份不支持它的文档；另一个主张则在所有已检索材料中都没有支持。两种错误都会影响可信度，但修复路径不同。

### 最有判别力的实验

固定证据集合比较写作方法，对被判不支持的主张增加全来源人工复核，估计候选检索漏检。联合报告必要事实覆盖、主张支持与可读性，防止通过少写或把所有内容拆得极碎来优化忠实性分数。

### 建议搭配

[deepresearch-bench](deepresearch-bench.md) · [ragtruth](ragtruth.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
