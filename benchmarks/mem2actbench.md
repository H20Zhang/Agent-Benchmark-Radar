# Mem2ActBench：从记住事实到正确调用工具

**中文** | [English](mem2actbench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2601.19935) · [ACL 2026](https://aclanthology.org/2026.acl-long.370/)

## 它到底测什么

Mem2ActBench 测的是长期 memory 能不能被 **主动转化为 tool use**：agent 不仅要选对工具，还要把过去交互里学到的信息正确落到工具参数里。任务不会直接提示“请回忆某条 memory”，因此 memory relevance 必须由 agent 在行动时自己识别。

## 相比此前评测多测了什么

多数 memory benchmark 停在 retrieval 或 answer generation；多数 tool-use benchmark 又把当前调用所需信息直接放在 prompt 里。Mem2ActBench 把二者连接起来：必须先找到此前学到的个人/上下文信息，再把它映射到正确的 action schema。

## 决定性证据

数据构造得到 2,029 个多轮 session 和 400 个 memory-dependent tool-use task；人工检查中 91.3% 被确认具有强 memory dependency。论文比较 7 类代表性 memory framework，并发现当前系统在主动利用 memory、尤其是 parameter grounding 上仍明显不足。

## 这个分数能证明什么

它能比 recall accuracy 更直接地证明 memory 是否具有 operational utility，即 **memory → tool selection / argument grounding** 的整体链路是否有效。但它仍不能把 retrieval 与 reasoning 完全拆开：取对 memory 后也可能填错参数；行动失败也可能来自 planning，而不是存储本身。

## 公平比较契约

应固定 tool schema、backbone、可用工具集合、session history、retrieval budget 与 action attempt 数，并尽量拆分 tool-selection 与 parameter-grounding 错误。如果某个系统可以额外查看工具文档或多次 retry，它面对的是不同难度的 action problem。

## 还没有测什么

这些任务围绕 benchmark tool schema 合成，不等价于长期真实账户里的权限、不可逆副作用和 API 演化；它主要测“能否使用已记住的信息”，而不是数月尺度上 memory 是否被正确写入、更新和删除。

## 下一步最有判别力的验证

加入 oracle-retrieval 与 oracle-planning 对照。若 oracle memory 仍无法显著提升 tool success，瓶颈在 action grounding；若大幅补齐差距，则 write/retrieval policy 才是主要研究对象。

## 演化位置

`memory QA → memory-conditioned decision → memory-grounded tool action`

这里把“memory 有用”从抽象说法变成了：它有没有真正改变正确的工具行动。