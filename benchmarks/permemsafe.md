# PerMemSafe：benign query 是否因长期用户状态而变成 personalized risk

**中文** | [English](permemsafe.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://aclanthology.org/2026.findings-acl.320/) · [代码](https://github.com/Greysahy/permemsafe)

## 它在测什么

PerMemSafe 从 276 段 user-assistant conversations 构造 750 个 test instances，覆盖五类 safety risks，且 history 中超过 90% 是 irrelevant exchanges。系统必须从噪声中找出隐含且会演化的 risk state，并在 query 单独看似 benign 时仍给出安全且有帮助的响应。

## 相比什么前进了

传统 safety benchmark 把当前 prompt 当成主要风险载体；传统 memory benchmark 又很少评价安全。PerMemSafe 将两者耦合：同一个 query 对不同 user history 可能有不同风险，而且 risk 可能已经解除，错误保留旧状态同样有害。

## 分数边界

safety/helpfulness 与 recall@3 支持在 synthetic risk history、固定 judge 与 retrieval budget 下的 personalized safety；不能外推真实用户安全，因为 base-model safety policy、conversation synthesis 与 judge 都是关键变量。

## 公平比较条件

锁定 risk history、base model、retrieval budget、judge 与 safety policy。static perception 与 dynamic evolution tracks 应分开报告。

## 下一步评测坐标

下一步需要真实 tool consequences、access control、deletion 与 adversarial memory poisoning，测错误风险状态如何影响行动。
