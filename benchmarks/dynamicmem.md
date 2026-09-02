# DynamicMem：跨数月维护不断变化的个人状态

**中文** | [English](dynamicmem.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2606.22877) · [代码](https://github.com/wenyaxie023/DynamicMem)

## 它到底测什么

DynamicMem 测 personal-assistant memory 能否从多个应用里分散的行为证据中，推断并维护 **会随时间变化的属性、习惯与偏好**。难点不是找回一个事件，而是判断哪些 observation 应该形成稳定 profile，以及什么时候新证据应该替换旧 belief。

## 相比此前评测多测了什么

conversation-memory benchmark 通常把显式事实放在一个对话流里。DynamicMem 把弱证据分散到 16 个应用和大约 15 个月里，并在多个时间 checkpoint 上检查 profile，因此 temporal supersession 与 evidence aggregation 成为主要测量对象。

## 决定性证据

每个模拟用户平均约 2.2M token、1,772 个 grounded event，并设置 5 个季度 checkpoint。论文观察到随着历史增长，profile reconstruction 持续下降，而 service-task accuracy 相对平；没有系统能同时很好地保留稳定事实并替换已经变化的事实。进一步的 error analysis 将超过 93% 的失败归到 retrieval，而不是最终 answer model。

## 这个分数能证明什么

这些结果能支持 benchmark 模拟活动分布下 **dynamic personal-state tracking** 的能力判断。retrieval attribution 比只看 end QA 更进一步，但仍依赖论文的诊断流程，不能直接推出某一种 index structure 就是根因。

## 公平比较契约

应固定 event stream、checkpoint、backbone、profile schema、retrieval budget，以及该时间点之前可见的 evidence；未来事件绝不能泄漏到早期 checkpoint。稳定属性 retention 与变化属性 replacement 要拆开报告，否则 append-only 系统会在前者看起来很好、在后者持续失败。

## 还没有测什么

真实个人数据还有 missingness、多设备/多账号矛盾、用户显式纠正、privacy constraint 和不确定 ground truth。benchmark 也没有量化 stale profile 相比 missing profile 会造成多大 downstream harm。

## 下一步最有判别力的验证

加入带明确 revocation time 的 counterfactual update，并设计只有使用最新状态才能做对的 downstream decision，把 profile maintenance 直接连接到 action utility 与 stale-memory harm。

## 演化位置

`event recall → personal profile extraction → temporally evolving user state`

它把瓶颈从“能否找到历史”推进到“现在到底哪个版本的用户状态才是真的”。