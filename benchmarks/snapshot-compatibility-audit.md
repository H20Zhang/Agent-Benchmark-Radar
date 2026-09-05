# Snapshot Compatibility Audit

## 它到底测什么

这个 audit 测的不是“更大的 corpus 平均分是否更高”，而是 **RAG corpus snapshot 增长之后，同一个 agent 对同一问题的答案是否出现超出自身采样波动的稳定翻转**。因此它把部署中的 corpus version 当成一个显式 regression variable：即使 aggregate accuracy 几乎不变，个体 query 也可能发生大量不兼容变化。

## 相比前身多测了什么

Stable-RAG / Con-RAG 一类工作通常控制固定证据扰动；这里使用 nested corpus snapshot 模拟真实部署中的索引升级，并用 within-snapshot disagreement 估计 agent 自己的随机波动，再从跨 snapshot churn 中扣掉这部分噪声。这样问的是 **excess churn**，而不是把所有答案变化都归因于 corpus 更新。

## 决定性证据

在 NQ 上，报告的 excess churn 为 **6.438pp exact** 与 **10.250pp semantic**，即使 aggregate EM 只变化 **−1.50pp**。其中 **40 个稳定翻转贡献了 10.00pp semantic churn**。这说明“平均 benchmark 分数接近”并不意味着两个 corpus snapshot 对用户是行为兼容的。

## 结论边界：这个分数支持什么判断

它支持“在所测 nested-snapshot 升级中存在超出同 snapshot 随机波动的 compatibility failure”。它不支持“所有翻转都是事实性伤害”：有些回答可能只是等价表达、合理更新或从错误变正确，因此 churn 需要和 correctness / harm 分开解释。

## 公平比较条件

必须固定 generator、retriever、query set、sampling configuration、snapshot nesting rule 和 semantic evaluator。尤其需要报告 temperature / top-p 等生成参数；否则 within-snapshot disagreement 本身都可能变化。不同 shard ordering 或不同文档进入顺序也会改变“snapshot growth”实际代表的干预。

## 研究上怎么用

这个指标适合作为生产 RAG 的 **compatibility regression test**。当系统更新 corpus、embedding 或 index 时，只报告整体 accuracy 可能漏掉用户级 breakage；更合理的 release gate 是同时报告 aggregate quality、within-snapshot variance、cross-snapshot excess churn，以及稳定翻转中有多少是 harmful / beneficial。

## 下一步最有价值的验证

当前缺口包括 live refresh、多步 agent trajectory、对具体 document 的因果 attribution 与 harm measurement。最高杠杆的下一步，是把“哪个新增/重排文档造成了稳定翻转”定位出来，并区分正确更新、无害表述变化与真正 regression。

## 谱系位置

它把 corpus version 本身纳入 RAG regression contract；`map_delta=reinforces`。这条线补的是传统静态 benchmark 很少测量的 **deployment compatibility**，不是替代常规 answer quality。

Primary: https://arxiv.org/abs/2608.22856

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究语料增长是否在总体准确率稳定时仍改变具体答案。跨快照不一致既可能是正确更新，也可能是错误翻转；只有减去同快照随机波动并检查答案方向，才能讨论真实版本兼容性。

### 一个具体任务长什么样

示意任务：同一问题在旧语料和包含更多文档的新语料上重复回答，总体正确率差不多，但部分样本稳定地改成另一个答案。系统需要判断变化是新证据纠正旧错，还是新增干扰造成退化。

### 最有判别力的实验

在每个快照内重复采样，并把跨快照翻转拆为正确到错误、错误到正确和其他变化。固定生成参数与检索预算，再移除新增的可疑文档，定位语料变化的实际原因，而不只报告不一致比例。

### 建议搭配

[crag](crag.md) · [rag-collapse](rag-collapse.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
