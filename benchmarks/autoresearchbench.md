# AutoResearchBench：literature search 必须同时测 target finding 与 unknown-size set discovery

**中文** | [English](autoresearchbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2604.25256) · [代码](https://github.com/CherYou/AutoResearchBench) · **领域：RAG / Agentic Retrieval**

AutoResearchBench 把文献搜索拆成两个本质不同的问题：**找到一个目标论文**，以及**在不知道答案集合有多大的情况下，尽可能完整地找到一组相关论文**。后者把“什么时候停止搜索”变成了正式评测对象。

## 它到底测什么

Benchmark 有 **1,000 个 queries、8 个 computer-science areas**：

- 600 个 Deep Research tasks：寻找一个满足条件的 target paper；
- 400 个 Wide Research tasks：搜集一个未知大小的相关论文集合。

搜索环境使用超过 **3M full-text papers** 的固定 DeepXiv corpus。这个设计避免了 live web 的不可复现性，同时仍保留较大的候选空间和真实论文全文。

## 相比此前评测多测了什么

传统 known-item retrieval 的停止条件很简单：找到目标就可以停。很多 deep-research benchmark 也更偏向最终答案，而不是独立评价 literature collection 的 coverage。

AutoResearchBench 的关键增量是 **unknown-size set discovery**。Agent 不知道 gold set 到底有多少篇，因此必须自己权衡：

- 是否还存在遗漏的相关工作；
- 再搜一次的边际收益是否值得成本；
- query expansion 是否已经覆盖主要术语和子方向；
- 什么时候停止才不是过早停止，也不是无意义穷举。

这让 search stopping、coverage estimation 和 search breadth 成为可以单独研究的问题。

## 实际怎样评测

Deep track 更接近 target finding，可使用命中类指标；Wide track 则需要 IoU / recall 一类集合指标来衡量覆盖。

解释结果时必须固定 corpus snapshot、gold-set version、search/index backend、agent harness 和预算。尤其 Wide track 中，搜索次数或 token budget 会直接改变 recall，因此“更高分”可能只是使用了更多搜索资源。

Deep 与 Wide 不应合并成一个 headline score，因为两者要求的策略完全不同：一个强调定位，另一个强调 coverage 与 stopping。

## 分数能说明什么

Deep accuracy 可以说明 agent 在固定 scholarly corpus 中能否通过多步搜索找到目标文献。Wide recall / IoU 可以说明 agent 对一个相关文献集合的覆盖程度。

但 Wide 分数有一个根本边界：**gold set 未必是完备真值**。如果人工标注或构建过程漏掉了真实相关论文，agent 找到额外正确论文反而可能被当作 false positive。

因此 Wide Research 更适合解释为“相对于当前 reference set 的覆盖与精度”，而不是“真正找全了这个研究主题”。

## 最主要的混杂因素

第一是 **gold-set completeness**。unknown-size discovery 恰恰意味着真实集合很难完整枚举，所以 evaluator 自身可能低估 novel discoveries。

第二是 **retrieval backend**。如果不同系统使用不同 index、metadata fields、citation graph 或全文解析，最终差异并不只来自 agent policy。

第三是 **budget sensitivity**。多搜十轮通常更容易提高 recall，但可能不具备实际价值；不同时延和 API 成本下的结果不能只按 recall 排名。

第四是 corpus 边界。固定 DeepXiv 提高可复现性，但不覆盖 paywall、live scholarly APIs、最新论文、非 CS 领域和不断变化的引用网络。

## 公平比较条件

至少应对齐：

- DeepXiv / corpus snapshot；
- query 与 gold-set version；
- index、metadata 与全文可见范围；
- citation / graph navigation 是否允许；
- model、agent harness 与工具接口；
- search-call、token、wall-clock budget；
- stopping rule 是否由 agent 自主决定。

如果一个系统拿到 citation graph，而另一个只能 keyword search，应视为不同 tool setting。

## 还没有覆盖什么

AutoResearchBench 还没有完整测量：

- live literature drift 和刚发布论文；
- 相关论文的价值分级，而非所有 relevant item 等权；
- gold-set uncertainty；
- 重复、版本、survey 与原始工作之间的关系；
- 找到文献之后的证据抽取、观点冲突和 synthesis；
- 在固定质量目标下的真实搜索成本。

## 下一步最有判别力的验证

最值得增加的是 **marginal-value stopping**：在每一步搜索后记录新发现的高价值论文数量，让系统同时预测“还剩多少重要工作没找到”。

这样可以形成 coverage–cost curve，而不是只有最终 recall。更强的 agent 应该不仅搜得多，还能知道 **什么时候继续搜值得、什么时候已经足够**。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合区分找一篇目标论文与搜齐未知数量相关论文。宽检索中的停止条件和集合完整性往往比某一篇的排序更重要；静态计算机科学语料上的结果，不应扩展为所有学科的完整文献调研能力。

### 一个具体任务长什么样

示意任务：深查任务沿线索定位一篇工作，广搜任务则要求搜集满足条件的一组论文并判断何时足够。相同搜索循环可能很快找到首个命中，却迟迟发现不了另一个研究分支。

### 最有判别力的实验

固定语料和总预算，分别记录首次目标命中、集合召回及集合交并比随调用数的曲线。对停止时遗漏的论文做人工复核，区分金标不完整与系统漏查，并检查引用扩展是否导致单一研究簇偏置。

### 建议搭配

[sage](sage.md) · [scholarquest](scholarquest.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`known-item scholarly retrieval → unknown-size literature discovery → value-aware, live, cost-sensitive research search`

AutoResearchBench 的核心贡献在中间一步：它让“找全多少”和“什么时候停止”成为一等评测对象。
