# BrowseComp：为难找事实持续搜索，而不是只做一次检索

**中文** | [English](browsecomp.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[OpenAI 发布页](https://openai.com/index/browsecomp/) · [论文](https://arxiv.org/abs/2504.12516) · [评测代码](https://github.com/openai/simple-evals)

## 它到底测什么

BrowseComp 有 1,266 个很难找的 factual question，需要 agent 持续、创造性地浏览多个 web source。答案刻意设计成短且可验证，因此 grading 很简单，真正困难的是 **evidence discovery**。

## 相比此前评测多测了什么

简单 factual QA / shallow web search 在模型能发几次 search 后很快接近饱和。BrowseComp 把难度放到 persistence、query reformulation、source chaining 和 obscure evidence discovery，而不是长文本生成。

## 决定性证据

题目围绕单一、稳定、可验证的短答案构造，很多题需要浏览大量网页才能定位。这种设计的重要价值是把“搜索难”与“长报告主观评分难”拆开：多数失败首先是没有找到答案，而不是 prose judge 不同意。

## 这个分数能证明什么

分数证明特定 search provider、browser interface、时间点、model 下 browsing agent 的整体能力，不能干净归因给 retriever，因为 web navigation、query generation、model prior 与 tool implementation 是耦合的。

## 公平比较契约

必须记录 model/version、search provider、tool interface、运行日期、call/token budget，以及能否 fetch page。web drift 使历史分数只能近似比较；同一个 answer grader 并不意味着信息访问条件相同。

## 还没有测什么

OpenAI 自己也指出短答案分布和真实 open-ended user query 的相关性未知。BrowseComp 不测 citation quality、长文 synthesis、ambiguity clarification、artifact generation 或用户需求完整性。

## 下一步最有判别力的验证

给题目增加 evidence-set scoring，并固定 search budget，区分“靠 prior/运气猜到答案”和“高效找到了足够 supporting evidence”。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究持续搜索和难找证据的发现能力。短答案让终点容易判断，却不能覆盖完整研究报告质量；成绩同时受搜索后端、工具接口、模型已有知识和调用预算影响，不能只按模型名称归因。

### 一个具体任务长什么样

示意任务：问题给出多个间接约束，系统需要反复改写查询、筛除候选并追到一个可验证答案。正确停止和证据核对与搜索次数同样重要；更多调用不保证找到真正支持答案的来源。

### 最有判别力的实验

在相同搜索后端、抓取接口和总预算下比较策略，并加入闭卷条件和来源移除诊断。报告准确率、调用数与失败轨迹；若闭卷已能答对，应谨慎解释该样本对搜索能力的区分度。

### 建议搭配

[browsecomp-plus](browsecomp-plus.md) · [livebrowsecomp](livebrowsecomp.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`factual QA → persistent web search → evidence-aware research agents`

它是一个很干净的 search-hardness benchmark，但不是完整 research-usefulness benchmark。