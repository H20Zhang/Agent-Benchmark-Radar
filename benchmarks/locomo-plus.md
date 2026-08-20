# LoCoMo-Plus：从 Factual Recall 到 Latent Constraint Consistency

**中文** | [English](locomo-plus.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[ACL Paper](https://aclanthology.org/2026.acl-long.1150/) · **Area: Agent Memory**

> **Measurement delta.** LoCoMo-Plus 不再要求后续问题直接“提示”旧事实，而是构造 **cue–trigger semantic disconnect**：用户过去的 state / goal / value 形成 latent constraint，之后 query 没有重述它，agent 仍应让 remembered constraint 正确约束当前回答。

## Predecessor / implicit critique

LoCoMo 等长期 memory benchmark 已经把 multi-session recall、temporal reasoning、long context 做成可重复 evaluation object。但很多 task 仍然可以被理解为“找到过去明确出现的事实”。

LoCoMo-Plus 的批评是：真实 personalization 更常见的是**隐式约束被未来场景触发**，而不是用户直接问“你还记得我说过什么吗？”

## What it actually measures

Benchmark 面向 long conversational context，要求系统保持并应用 latent constraints。作者同时指出 conventional string-matching metric 与 explicit task-type prompting 与这种 cognitive-memory setting 不匹配，因此用 **constraint consistency** 作为统一 evaluation view。

## What a score supports

LoCoMo-Plus score 更接近“系统是否在当前回答中保持过去约束的一致性”，而不是纯 retrieval accuracy。

但它仍然是 conversational QA/response evaluation；一个系统得分更高，可能来自 retrieval、state reconstruction、stronger parametric reasoning 或 prompt/harness，而不自动证明 memory storage component 更好。

## Strongest confounder

**Constraint consistency 的 evaluator 与 task construction** 是 load-bearing 部分。隐式约束如果本身存在歧义，judge 必须区分合理 adaptation 与 inconsistency。

另一个 confounder 是 explicit task prompting：如果告诉模型“这是 memory test”，会改变行为，因此 benchmark protocol 本身会影响 measured capability。

## What remains unmeasured

- user preference 真正随时间 drift / conflict；
- tool/action 级别的 constraint application；
- permissions / authority / revocation；
- 长期错误 constraint 的 downstream harm；
- matched retrieval/state-reconstruction cost。

## Genealogy consequence

`multi-session factual recall → temporal/update reasoning → latent user-state constraint → future memory-guided action`

它是从“记住过去”走向“过去的 state 是否正确约束未来行为”的重要 transition/frontier signal。
