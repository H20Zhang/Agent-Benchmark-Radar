# RealMem：面向持续演化长期项目的 memory

**中文** | [English](realmem.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2601.06966) · [ACL 2026](https://aclanthology.org/2026.findings-acl.703/) · [代码](https://github.com/AvatarMemory/RealMemBench)

## 它到底测什么

RealMem 评估 **long-term project-oriented interaction** 中的 memory：agent 要跨 session 跟踪目标、schedule、决策、不断变化的项目属性和依赖关系，并针对“当前项目状态”回答自然用户 query。

## 相比此前评测多测了什么

casual conversation / task dialogue 可以把 session 看成个人事实集合；project memory 则不同：状态由多轮协作共同产生，承诺有 deadline，后续决策会覆盖前面决策，relevance 取决于当前 project phase。RealMem 显式模拟这种 evolution。

## 决定性证据

benchmark 包含 11 类项目场景、超过 2,000 段 cross-session dialogue。合成 pipeline 结合 project foundation construction、multi-agent dialogue generation、memory/schedule management，使 project state 真正随时间变化。实验显示当前 memory system 在动态 context dependency 与长期 project state 管理上仍明显困难。

## 这个分数能证明什么

RealMem 能支持对 evolving project history 的 retrieval/reasoning 能力判断；但最终仍以 query answering 为主，因此只能间接说明 memory 会不会改善真正的项目执行、排程或 artifact delivery。

## 公平比较契约

应固定 project history、time checkpoint、backbone、retrieval budget、schedule visibility 与 query evaluator，并把 superseded 与 still-active fact 分开评估，防止后续项目状态泄漏到早期 checkpoint。

## 还没有测什么

项目成功远不只是回答问题：还需要创建 artifact、协商 scope、管理权限、失败恢复和执行不可逆 action，这些 operational loop 基本还没有进入 benchmark。

## 下一步最有判别力的验证

在每个 checkpoint 附加 executable project task，例如更新计划、修改 artifact、选择下一步行动，并检查是否与当前 project state 一致。这样才能验证 memory 是否真正减少协作错误，而不只是提高 QA。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究长期项目中的目标、产物和进度状态，而不是只记住用户静态属性。选型关键是后续问题是否依赖项目状态演化；同名项目的旧安排被正确召回却错误采用，也应视为记忆失败。

### 一个具体任务长什么样

示意任务：用户先确定项目方向，随后调整交付物和优先级，再询问下一步。系统需要区分已经完成、已经取消和仍然有效的事项，而不是把所有曾出现过的要求拼成一份清单。

### 最有判别力的实验

让相同项目经历不同修订顺序，比较原始日志检索、状态摘要与显式状态维护。单独评分已取消要求是否重新出现，并在新项目上测试；只在同一项目模板上改进，无法证明跨项目泛化。

### 建议搭配

[longmemeval](longmemeval.md) · [statemembench](statemembench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`casual conversation memory → cross-session project state → persistent work context`

它把 evolving project state 变成一个独立 memory object，更接近 workplace agent 的真实使用方式。