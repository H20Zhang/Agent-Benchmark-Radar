# RGB：把 RAG 的“会不会用 context”拆成四种 failure modes

**中文** | [English](rgb.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2309.01431)

## 它在测什么

RGB 用中英文四组 diagnostic testbeds 分别检查 noise robustness、negative rejection、information integration 与 counterfactual robustness。它不问 retriever 找得多准，而是把 retrieved context 已经给到 generator 后，模型是否能正确使用、拒绝或整合这些证据。

## 相比什么前进了

普通 RAG benchmark 常把 retrieval 与 generation 压成一个 final-answer score。RGB 把 generator 对 context 的处理能力独立出来，使“检索到了但没用对”“没有答案却硬答”“多证据无法整合”等失败可以被区分。

## 决定性证据与分数边界

论文显示当 context 含噪、缺证据或存在 counterfactual information 时，主流 LLM 的行为明显不稳定。这个结论支持 RAG 需要 context-use diagnostics；它不能说明某个 retriever 更好，因为 evaluation 直接控制了 supplied context。不同 prompt 和 generator 的分数也不能归因给 retrieval。

## 公平比较条件

必须锁定 generator、prompt、constructed negatives/counterfactuals 与每个 diagnostic split。四种能力不应随意压成一个 SOTA 总分，否则会掩盖能力间的 trade-off。

## 下一步评测坐标

下一步要把这些 context-use failures 接回真实 retrieval loop：观察 agent 是否能发现证据冲突、主动补搜并在工具预算内恢复，而不只是被动读取固定 context。
