# GroupMemBench：多人对话里“谁知道什么”本身就是 memory state

**中文** | [English](groupmembench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2605.14498) · [代码](https://github.com/UCSB-NLP-Chang/GroupMemBench)

## 它在测什么

GroupMemBench 在四个 synthetic enterprise domains 中发布 745 个问题，覆盖 multi-hop、update、temporal、user-implicit、ambiguity 与 abstention。答案依赖 speaker identity、reply structure、group state 和 audience-specific terminology，因此 memory 不再只是全局事实集合。

## 相比什么前进了

一对一 memory benchmark 默认同一事实对所有 query 都同义。GroupMemBench 让 participant identity 与 asker conditioning 成为 evaluation contract，测 agent 能否区分“谁说的、谁相信、对谁该怎么表达”。

## 分数边界

asker-conditioned QA 支持 group-state tracking under synthetic conversation graph；它不测试真实 organizational permission、deletion 或 collaborative writes。metadata-rich retriever 也可能利用 speaker tags，因此需要把 metadata access 视为协议变量。

## 公平比较条件

锁定 conversation graph、asker role、retriever metadata、answerer 与 judge，并按六种 question type 报告。

## 下一步评测坐标

下一步应将 participant-conditioned memory 与真实权限、shared artifacts 和 group actions 结合，区分 belief tracking 与 access control。
