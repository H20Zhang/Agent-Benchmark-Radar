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
