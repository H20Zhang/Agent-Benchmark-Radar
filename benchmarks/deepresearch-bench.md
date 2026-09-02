# DeepResearch Bench：评估 evidence、citation 与最终研究报告

**中文** | [English](deepresearch-bench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2506.11763) · [项目页](https://deepresearch-bench.github.io/) · [代码](https://github.com/Ayanami0730/deep_research_bench)

## 它到底测什么

DeepResearch Bench 评估会多步 web exploration、最终产出 **长篇 citation-rich research report** 的 agent。100 个专家编写任务覆盖 22 个领域，同时评 report quality 和 citation/retrieval effectiveness。

## 相比此前评测多测了什么

BrowseComp 故意把 output 压成一个短事实答案；DeepResearch Bench 改变了 artifact：系统既要选 evidence，又要综合成 coherent analysis，还要让 claim 有 citation grounding，因此 information sufficiency 与 reporting quality 被一起测量。

## 决定性证据

任务由领域专家编写，topic distribution 还参考了大规模真实 web-search chatbot query。RACE 用 adaptive reference-based criterion 评报告，FACT 看 effective citation count 与 citation accuracy，从而避免“文笔很好”直接等价于“研究扎实”。

## 这个分数能证明什么

它支持特定 evaluator 下 deep-research agent 的 end-to-end quality，但 retrieval、planning、writing 都会影响最终报告，且 judge/evaluator 本身也有 assumption，因此很难从总分直接做 component attribution。

## 公平比较契约

应固定 search access、model/version、time/call/token budget、语言、报告长度约束与 evaluator version，并把 citation metric 与 holistic report quality 分开报告。web drift 与 search provider 差异应作为实验变量记录。

## 还没有测什么

100 个高成本任务限制统计分辨率；长报告 judge 仍可能漏掉细微事实/方法错误。真实研究还经常需要 clarification、private corpus、计算工具和与用户反复 review。

## 下一步最有判别力的验证

加入 claim-level evidence graph 与 retrieval-budget sweep，判断 report improvement 到底来自找到了更好的 evidence，还是只是在同一 evidence set 上写得更漂亮。

## 演化位置

`hard web answer finding → citation-grounded report generation → auditable research workflow`

它把 search benchmark 从“找到答案”推进到了“交付可审计的研究 artifact”。