# membench（staleness）：让当前事实排在过期事实之前

**中文** | [English](membench-staleness.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[代码、场景与结果](https://github.com/Ps23102004/membench)

## 它到底测什么

这个 component benchmark 测的是 **memory update / supersession 的排序正确性**：当 store 中同时存在旧事实、新事实、否定信息、实体相近项和时间范围不同的记录时，系统能否让当前有效事实排在禁止使用的 stale fact 之前，并在证据不足时正确 abstain。它不把“retrieved something relevant”当成功，而是关心 retrieval result 是否仍然会泄漏过期状态。

## 相比常规 recall benchmark 多测了什么

普通 memory recall 往往只问 gold fact 有没有出现在 top-k；如果 stale 和 current 两条都被召回，recall 仍可能很好。membench 显式报告 `staleness@1`、leakage、abstention 和 contradiction resolution，因此把 **更新语义** 从 relevance 里拆出来。公开修订还替换了无效的 top-k staleness 指标，并堵住通过大量弃答刷高分的路径。

## 决定性证据

60 个可执行 probe 通过可插拔 write/query/reset 接口运行，并报告 recall、precision、`staleness@1`、leakage、abstention、contradiction resolution 与 Wilson interval。Embedding baseline 在 **12 个 supersession probe 中有 11 个返回 stale answer**；加入 recency reranking 后降到 **0/12**。这说明对该小型受控 store，更新-aware ranking 可以解决单纯 semantic similarity 明显处理不好的冲突。

## 这个分数支持什么判断

结果支持“在这组手写 probe 与小 memory store 上，纯 embedding retrieval 对 supersession 很脆弱，而 recency-aware reranking 显著降低 stale top-1”。它不能推出更大规模长期 memory 中 recency 一定足够：真实更新可能不是单调时间覆盖，旧事实也可能在特定时间范围或上下文重新变得正确。

## 公平比较条件

需要固定 memory records、时间戳语义、write/query API、embedding model、top-k、abstention policy 和 exact-substring evaluator。不同方法应同时报告 current recall 与 stale leakage，避免通过激进过滤把两者一起降下来。recency 方法还必须报告 k 敏感性，因为 candidate set 变化本身会影响是否看到 current fact。

## 研究上怎么用

它适合作为 **update mechanism 的 unit test**，尤其适合测试 timestamp-aware scoring、conflict resolution、versioned memory、forgetting policy 或 memory consolidation。一个完整 memory system 可以先在这里证明 component correctness，再到长时程 agent benchmark 验证这种排序改善是否真的提升未来行动。

## 下一步最有价值的验证

当前主要缺口是规模、自然语料、复杂有效期和 downstream action。最高杠杆实验是构造多轮 supersession 链、非单调回滚、时间区间事实和实体冲突，并在相同 retrieval budget 下比较 recency、explicit version graph 和 learned conflict resolver，观察谁能同时维持 current accuracy 与历史可追溯性。

## 谱系位置

`map_delta=early_signal`，绑定 `memory-update-and-staleness`。修正后的指标适合作为 component diagnostic，但 **60 个相关手写 probe + 单作者 + 小 store** 还不足以构成持久领域迁移；需要更广泛证据证明 update-aware evaluation 是长期 memory benchmark 的必需坐标。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合给记忆存储做过期事实的快速回归测试，不宜承担通用记忆性能主结论。它关注当前事实能否排在被替代事实之前；小规模精确匹配探针的通过，不等于复杂历史中的状态理解已经可靠。

### 一个具体任务长什么样

示意任务：同一实体的一项事实先写入，之后被否定或替代，当前查询应优先返回有效值而避开禁止的旧值。全部不返回虽然能减少旧事实出现，却并未完成正常检索任务。

### 最有判别力的实验

在相同探针上同时记录当前事实命中、旧事实排位和弃答；扫描 top-k 时保持指标定义不变。再加入近义改写与更大干扰库，检查通过是否依赖精确子串和小存储规模。

### 建议搭配

[statemembench](statemembench.md) · [longmemeval](longmemeval.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
