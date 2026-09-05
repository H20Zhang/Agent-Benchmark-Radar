# BrowseComp-Plus_CM：把 agentic search 投到独立大语料

**中文** | [English](browsecomp-plus-cm.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.20317) · [代码](https://github.com/castorini/cmass) · [数据](https://huggingface.co/datasets/castorini/cmass)

用同一组 BrowseComp-Plus 问题和同一 BM25 工具接口，把检索语料从约 10 万篇、按问题构造的文档集换成独立生成的 5.53 亿篇 ClimbMix 文档。

## 它接在什么之后

BrowseComp 把深度搜索放到实时网页上，但搜索 API、网页漂移与答案泄露使 agent、retriever 和环境难以拆开。BrowseComp-Plus 固定了语料，却把正例和 hard negative 都围绕测试问题收集，语料规模也只有约 10 万篇。BrowseComp-Plus_CM 保留前者的 830 个问题，只接受能在 ClimbMix 中逐 hop 找到证据、经过独立 agent 与人工复核的投影；最终留下 57 题并发布 question-level qrels。

## 实际怎样评测

**问题：** 当答案问题、agent、搜索/取文接口和 judge 不变，只扩大并独立化语料时，证据发现会变得多难？

**测量对象：** 在 400B-token、5.53 亿文档的固定网页语料中，用 agentic search 找全多跳问题所需证据，并同时报告答案正确率、证据 recall 与工具调用数。

**规模与协议：** 投影流程从 830 题出发，326 题通过 answerability，65 题通过逐 hop 自动核验，57 题通过人工复核。对照实验只替换 BrowseComp-Plus 与 ClimbMix 的 BM25 index；agent、search/get_document 工具和 GPT gold-answer judge 保持一致。

## 分数能说明什么

同一 GPT-5.6 Sol agent 的证据 recall 从 84.3% 降到 21.4%，平均检索调用从 60.2 增到 98.3，而答案正确率只从 86.0% 降到 80.7%。这支持“按题构造的小语料会显著低估 evidence discovery 难度”，也说明 final-answer accuracy 不能替代检索过程指标；它不证明某一种 retriever 或 agent 架构普遍更优。

## 最主要的混杂因素

57 题是经过投影存活筛选的子集；GPT-5.6 Sol 对该子集闭卷正确率已达 70.2%。Hop 分解、证据支持判断和 qrel 扩展还包含 GPT-5.5 / Claude Opus 5 判断，最终对比只使用 BM25 接口。当前 Hugging Face card 还同时声称 qrels 为 6,695 行、又称 duplicate expansion 后应为 12,140 行；实际下载规模与复现文档指向 6,695，故重复扩展版本不能作为已解决事实。Corpus swap 的结论很强，但跨检索器、跨模型和抗污染外推仍有限。

## 还没有覆盖什么

需要在更大的独立题集、更多检索接口和要求显式 citation 的协议上复验；尤其要区分“看到了证据”“实际使用了证据”和“本来就记得答案”。

## 放进演化图怎么看

`map_delta=revises`，绑定 `retrieval-harness-validity`。它以 matched corpus swap 直接限定 BrowseComp-Plus 的持久主张：固定语料是控制 drift 与 attribution 的必要条件，但 query-conditioned construction、规模和 qrels 仍是 load-bearing variables。地图只增加这一最小限定，不把单一投影写成新的普遍趋势。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合检验固定问题进入独立大语料后，证据发现难度如何改变。语料规模变大不只增加干扰，也可能改变证据覆盖；投影筛选和闭卷可解性限制了它对一般网页搜索的外推。

### 一个具体任务长什么样

示意任务：保留同一个问题和搜索智能体，把候选文档集合换成更大的独立语料。系统既可能需要排除更多干扰，也可能找不到原语料中的同一证据，因此必须同时核对问题和相关性标注。

### 最有判别力的实验

固定问题、智能体、搜索 API 与预算，仅替换语料，并把证据覆盖变化单独列出。对投影保留题做闭卷检查，按已知与未知答案分项报告，避免参数记忆掩盖真实大规模检索失败。

### 建议搭配

[browsecomp-plus](browsecomp-plus.md) · [livebrowsecomp](livebrowsecomp.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
