# WorldMemArena：把 multimodal memory failure 定位到 lifecycle stage

**中文** | [English](worldmemarena.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2605.29341) · [代码](https://github.com/UCSB-AI/WorldMemArena)

## 它在测什么

WorldMemArena 基于 multi-session action-world trajectories 与 visual observations，按 writing、maintenance、retrieval、use 四阶段检查 memory lifecycle。当前 artifact 含 461 samples，并有 balanced 150-sample subset；paper 描述约 400 个 annotated multimodal tasks。

## 相比什么前进了

多数 multimodal memory benchmark 只给最终 QA score。WorldMemArena 引入 gold memory points 与 stage-level diagnosis，使“写错了”“旧状态没更新”“没检索到”和“检索到了但推理错”可以分开。

## 分数边界

stage-level accuracy 支持 failure localization under constructed trajectories；它仍不能说明真实 persistent environment 的 action utility，因为 checkpoint QA、judge、multimodal backbone 与 storage representation 都会影响结果。

## 公平比较条件

锁定 sample version、backbone、memory representation、judge 与 compute budget，并保持四阶段评测接口一致。不同 artifact/sample count 应明确 version。

## 下一步评测坐标

下一步要把 lifecycle diagnosis 接到不可逆 future actions、权限和 recovery，使每类 memory failure 的后果直接可测。
