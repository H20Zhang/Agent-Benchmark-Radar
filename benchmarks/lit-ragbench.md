# LIT-RAGBench：先把 retriever 拿掉，单独测 generator 会不会用 RAG context

**中文** | [English](lit-ragbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2603.06198) · [代码](https://github.com/Koki-Itai/LIT-RAGBench)

## 它在测什么

LIT-RAGBench 有 114 个 human-constructed Japanese questions，并提供 machine-translated、human-curated English counterparts。它直接提供 positive/negative chunks，按 Logic、Integration、Table、Reasoning、Abstention 五类能力评价 generator，而不把 retrieval quality 混进结果。

## 相比什么前进了

很多 RAG benchmark 的 final answer 失败同时可能来自 retriever 和 generator。LIT-RAGBench 控制 context，让“证据已经在眼前，但模型仍不会整合、推理或拒答”的 failure 独立可测。

## 分数边界

category-wise accuracy 支持 generator 在 supplied-context contract 下的 context-use ability；它不支持 retriever 或 agentic-search claim。114 个问题规模较小，translation 与 fictional-task design 也可能改变语言间 difficulty。

## 公平比较条件

锁定 supplied chunks、prompt template、generator、judge 与语言版本，并分 capability category 与语言报告。

## 下一步评测坐标

下一步应把这些 generator diagnostics 接回真实 retrieval loop，验证识别到 integration/abstention failure 后能否主动补搜或修正 context。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合在不混入检索器差异的条件下诊断证据整合、表格、逻辑与弃答。其范围是给定上下文中的生成能力；较高分不能支持索引、检索或多步工具调度的改进主张。

### 一个具体任务长什么样

示意任务：给定文本与表格片段，模型需要联合条件推出答案，或在信息不够时拒绝猜测。每个片段都可见并不保证模型能执行跨片段逻辑，正是这一点使生成器诊断有意义。

### 最有判别力的实验

在相同上下文上独立改变片段顺序、干扰比例与语言，保持评分器一致。逐能力报告并复核语言版本差异；若研究目标是 RAG 系统，应再连接真实检索结果，检验局部优势是否保留。

### 建议搭配

[rgb](rgb.md) · [t2-ragbench](t2-ragbench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
