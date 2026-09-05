# MemBench：从“答对”扩到 memory 的 effectiveness、efficiency 与 capacity

**中文** | [English](membench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2506.21605) · [代码](https://github.com/import-myself/Membench)

## 它在测什么

MemBench 同时覆盖 factual / reflective memory，并区分 participation 与 observation 两类交互场景；评价也不只看 task accuracy，而是把 effectiveness、efficiency 和 capacity 都纳入 memory capability。它试图回答的不是“这个 agent 会不会回忆”，而是不同层级、不同交互角色下 memory 是否仍有效且可承受。

## 相比什么前进了

LoCoMo、LongMemEval 主要把长期历史 QA 做得更难、更细。MemBench 的增量是把 memory level、interaction scenario 与资源维度并列成评测轴，因此一个方法不能再仅凭某个 QA 数据集上的最高准确率声称“memory 更好”。

## 决定性证据与分数边界

论文最重要的贡献是 evaluation decomposition 本身：同一个 memory system 需要在 factual/reflective、participation/observation 以及效率/容量之间同时接受检查。当前主来源没有提供一个可长期维护、协议稳定的统一公开 leaderboard，因此网页不会制造 Overall SOTA；系统级结果只在模型、harness 和 metric aggregation 对齐时可比。

## 公平比较条件

对齐 backbone、agent harness、memory budget、交互场景和 metric aggregation。若一个系统以更多 tokens、更多 memory capacity 或不同任务混合换来更高 effectiveness，单一 accuracy 不足以支持 architecture-level claim。

## 下一步评测坐标

MemBench 增加了评价维度，但仍难定位 write、organization、retrieval、update 中哪个机制导致结果。下一步需要 matched component interventions，并把长期 maintenance cost 与行为改善联系起来。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合为记忆系统建立多维画像，尤其在效果、容量和代价必须同时考虑时。广覆盖不等于能直接归因到某个记忆组件；使用它时应把任务类别和资源曲线作为主结果，而不是只比较打包系统总分。

### 一个具体任务长什么样

示意任务：系统既要记住直接参与的交流，也要利用旁观得到的信息，并从多次经历提炼较高层判断。相同记忆预算可能更利于事实保存，却不利于反思性信息，因此两类任务需要分别观察。

### 最有判别力的实验

在相同回答模型下扫描记忆容量，分别绘制事实型与反思型任务的质量—写入成本—检索延迟关系。若优势只在更大容量下出现，就不能把收益简单归为更好的组织方法；应加入等容量、等查询预算的对照。

### 建议搭配

[memoryagentbench](memoryagentbench.md) · [evomembench](evomembench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
