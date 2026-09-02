# WorldMemArena：在演化多模态世界里拆开完整 memory lifecycle

**中文** | [English](worldmemarena.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2605.29341) · [项目页](https://worldmemarena-mem.github.io/)

## 它到底测什么

WorldMemArena 在 **不断变化的多模态 action-world trajectory** 上评估 memory，并明确拆成 write、maintain、retrieve、use 四个 lifecycle stage。通过 gold memory point、state update、distractor 和 evidence chain，可以检查 agent 是否写对、是否保持最新、之后是否取对，以及最终是否真的用上。

## 相比此前评测多测了什么

传统 long-memory QA 往往把 history 当静态 corpus，只看最终答案。WorldMemArena 把 memory 视为和世界一起变化的 mutable state；Lifelong Evolution 与 Agentic Execution 两种 regime 让过时证据、视觉观察和状态转移成为一等对象，而不是默认“过去所有事实一直有效”。

## 决定性证据

benchmark 包含 400 个 multi-session multimodal task，并比较 long-context、人工构造的 retrieval/external memory 与专门 memory harness。分析发现：写得/存得更好并不自动带来更好最终性能；visual evidence 常被低利用；跨 domain 稳定性不足；真实 trajectory 更难。这直接说明 memory quality 是 pipeline property，而不是 retrieval score。

## 这个分数能证明什么

最终分数支持 whole-system memory performance，而 stage annotation 比 end QA 提供更强诊断信息。但要做因果 attribution 仍需 matched backbone 与 stage-level intervention：系统可能 retrieve 对了但 use 错，也可能一开始写对后来 maintain 错。

## 公平比较契约

应固定 backbone、trajectory、visual observation、session segmentation、memory budget、retrieval budget 与 action protocol，同时报告 write/maintenance 和 read-time 成本。不同系统必须看到同样 modality；若只给某一边额外高质量 image caption，证据通道已经不同。

## 还没有测什么

它仍是有限任务空间；policy governance、deletion rights、跨用户边界、数月级存储经济性和灾难性 corruption recovery 不是主要目标。

## 下一步最有判别力的验证

对四个 lifecycle stage 分别注入 oracle intervention，测每个阶段修正后能恢复多少最终 task success，从而形成 write / maintain / retrieve / use 的 error budget，直接指导系统研究投入。

## 演化位置

`static history QA → mutable multimodal state → lifecycle-diagnostic memory`

它的重要性在于第一次把 memory lifecycle 的失败位置真正变成可观测对象。