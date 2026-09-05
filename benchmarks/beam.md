# BEAM：把长期记忆压力推到 10M-token coherent conversations

**中文** | [English](beam.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2510.27246) · [代码](https://github.com/mohammadtavakoli78/BEAM)

## 它在测什么

BEAM 用 100 段连贯对话和 2,000 个验证问题，把历史长度分到 128K、500K、1M 和 10M tokens，并覆盖十类 memory abilities。相比随机拼接 needle，它强调 narrative coherence、跨事件关系以及随长度增长的退化，因此能直接观察 long-context / RAG 在极长历史上的 scaling failure。

## 相比什么前进了

LoCoMo 把 multi-session 对话拉到约 16K tokens；BEAM 把同类问题推进到百万乃至千万 token，并让 conversation 仍保持主题和互动结构。它测的是“memory quality 随 horizon 扩大是否崩掉”，而不只是某个固定 context size 的最终准确率。

## 决定性证据与分数边界

论文报告：即使支持 1M context 的 LLM、包括带 retrieval augmentation 的版本，也会随着 dialogue length 增长明显退化；作者的 LIGHT memory framework 相比各 backbone 的 strongest baseline 平均提升约 3.5%–12.69%，且 episodic memory、working memory、scratchpad 的 ablation 显示三者均有互补贡献。这证明 BEAM 能暴露 scale-induced failure；但 LIGHT 的增益仍是 bundled design evidence，不能从总分单独推导某个 component 的普遍因果优势。

## 公平比较条件

必须锁定 backbone、context-window support、conversation length bucket、retrieval budget 与问题类型。128K 与 10M 的分数不能混成一个不加权的“当前最好”；不同模型是否真正支持完整输入也会改变系统可见证据。

## 下一步评测坐标

BEAM 仍以 synthetic coherent conversation + QA 为主。下一步需要把同样的 million-token pressure 放到真实 agent trajectories、持续写入/更新以及未来 action success 上。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合检验记忆质量如何随历史长度退化。超长历史是压力变量，不应自动解释为更接近真实部署；应同时问新增内容是有效经历、重复内容还是干扰，以及系统为处理这些内容支付了多少写入成本。

### 一个具体任务长什么样

示意任务：一条跨很长时间的连贯对话中，少量早期事件决定当前答案，大量后续交流与之弱相关。把历史拉长后仍找到关键词不够，系统还需要保留事件关系与时间位置。

### 最有判别力的实验

对同一问题与支持事实构造多个历史长度，固定查询阶段的上下文预算，并把写入成本单列。比较原始检索、摘要记忆与分层记忆的退化斜率；不要把题目变难和历史变长混在一次横向对比中。

### 建议搭配

[longmemeval](longmemeval.md) · [scale-qa](scale-qa.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
