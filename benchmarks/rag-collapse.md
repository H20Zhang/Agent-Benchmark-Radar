# RAG Collapse

## 它到底测什么

RAG Collapse 不是在测一次检索是否找到了相关文档，而是在测一个**固定模型 + 递归检索语料**形成反馈环以后，独立来源会不会被模型自己生成的来源逐轮挤出。它把 model-collapse 研究里的递归机制从“训练数据 → 新模型”迁移到“检索语料 → 上下文 → 新来源”，因此测量对象是 corpus provenance 与 retrieval feedback dynamics，而不是基础模型权重退化。

## 相比前身多测了什么

最近的概念前身是 recursive-training / model-collapse 工作；那些研究关注模型在反复训练于合成数据后的分布退化。这里保持模型权重固定，只让后续检索越来越可能读到先前模型生成的内容，因此能单独问：**即使模型本身没有继续训练，retrieval context 是否也会自我收缩。**

## 决定性证据

论文报告 1,528 次 simulation 中总体 collapse 率为 **79.6%**；Replace-All、Replace-One 与 Search 三类协议均出现高比例 collapse。真正重要的不是某个单点 accuracy，而是多个 corpus-update protocol 下都观察到 independent-source displacement，说明反馈现象不依赖单一替换策略。

## 这个分数支持什么判断

它支持“在论文构造的 synthetic recursive-retrieval loop 中，self-authored source feedback 足以造成来源多样性坍缩”。它**不支持**“live web 已经发生同样规模的 RAG collapse”，也不能把 collapse 归因于某个 retrieval algorithm：同一模型家族同时承担写入和后续读取，collapse/quality 还依赖 model judge。

## 公平比较条件

比较不同系统时至少要固定模型家族、初始 corpus、source replacement/search policy、循环轮数、生成预算和 collapse evaluator。只要这些条件变化，结果首先是 system-level evidence。尤其需要区分“模型偏好自己的写作风格”与“语义内容真正被反馈放大”这两个 competing explanations。

## 研究上怎么用

这个 benchmark 更适合作为 **RAG validity / deployment-regression coordinate**，而不是常规 answer-quality leaderboard。若研究声称长期运行的 agentic retrieval 可以持续从开放语料学习，应同时报告 provenance diversity、independent-source survival 和最终任务质量，否则平均 QA 分数可能掩盖语料来源逐步单一化。

## 下一步最有价值的验证

最关键的缺口是 longitudinal live-web evidence、cross-model authorship、style/content 分离以及人工 provenance 标签。真正能改变结论的实验不是再增加一种 synthetic replacement rule，而是证明在真实刷新语料、不同作者模型和真实搜索排序下仍存在超出自然语料漂移的 excess collapse。

## 谱系位置

它把 corpus provenance 与反馈动态变成 RAG validity coordinate；当前 `map_delta=reinforces`。它补强的是“语料随 agent 运行而变化时，静态 benchmark score 不够”的方向，而不是替代传统 retrieval relevance 评测。

Primary: https://arxiv.org/abs/2608.22118

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究模型自产内容回流语料后的递归反馈，而不是模型参数训练造成的退化。关键变量是独立证据是否被逐步挤出；质量下降可能同时涉及来源同质化、检索偏好和生成风格，不能只归因于一个环节。

### 一个具体任务长什么样

示意任务：系统检索材料生成回答，随后这些回答又成为下一轮可检索来源。多轮后，系统可能越来越依赖自己的说法；表面上有更多文档和引用，独立证据的数量却可能减少。

### 最有判别力的实验

固定模型和问题，对照独立来源、同模型生成来源与跨模型生成来源，独立改变回流比例和检索策略。逐轮报告事实质量、来源多样性和独立证据占比，避免用同一模型的风格偏好充当退化判据。

### 建议搭配

[snapshot-compatibility-audit](snapshot-compatibility-audit.md) · [kbgym](kbgym.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
