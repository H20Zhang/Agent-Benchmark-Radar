# MemEvoBench：当 memory 朝错误方向演化时是否仍然安全

**中文** | [English](memevobench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2604.15774)

## 它到底测什么

MemEvoBench 测的是 agent 在多轮交互中 memory **逐渐被错误演化** 后还能不能保持安全。误导性 memory、带噪 tool output 和 biased feedback 会跨轮积累，因此攻击对象不再是一条 prompt，而是不断被污染并再次使用的内部 evidence base。

## 相比此前评测多测了什么

静态 safety benchmark 通常测试单 episode 是否抵抗 harmful prompt；memory benchmark 又通常只看 retention utility。MemEvoBench 把两者交叉起来：agent 开始时可能是安全的，但因为早期观察被写入、强化、再次检索，之后越来越不安全。这样 memory update policy 本身也成为 attack surface。

## 决定性证据

benchmark 包含覆盖 7 个领域、36 类风险的 QA 任务，以及由 20 个 Agent-SafetyBench environment 改造的 workflow task；它构造 benign / misleading memory 混合池并追踪多轮行为。论文观察到随着误导信息持续进入 memory，安全性显著下降，而只在 prompt 层做静态防御不足以消除这种长期效应。

## 这个分数能证明什么

跨轮 degradation curve 能支持特定 corruption process 下 **memory-update robustness** 的系统级判断，但不能单独定位根因究竟是 write admission、consolidation、retrieval、trust calibration，还是 backbone 在读到错误 memory 后本身容易被带偏。

## 公平比较契约

应固定 corruption schedule、benign/malicious memory 比例、tool output、backbone、retrieval budget 与轮数，并同时报告 benign utility 与安全指标。一个简单“不存、不用 memory”的系统可能很安全，却把 memory 的价值一起消灭了。

## 还没有测什么

真实攻击者可能会根据 agent 行为自适应，而不是遵循固定生成器；memory 还涉及 access control、deletion 等治理问题，poisoning 不能覆盖全部。发现矛盾后的 recovery 也不同于一开始就抵御 corruption。

## 下一步最有判别力的验证

把 lifecycle 拆成 admission、consolidation、retrieval、use，并在同一证据上逐阶段注入 corruption。最高杠杆的问题是：长期鲁棒性主要应该靠写入过滤，还是靠使用时的验证与信任校准。

## 演化位置

`memory utility → memory update dynamics → adversarial memory evolution`

它把 memory maintenance 从工程细节提升成了安全评测坐标。