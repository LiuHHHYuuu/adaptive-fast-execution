# X 发布文案草案

状态：待人工确认；尚未发布。

## 中文单帖

我给 Codex 做的不是一个“永远更快”的 prompt，而是一个油门/刹车路由器：

小型、局部、可逆任务：少规划，直接实现，再做针对性验证。  
架构、生产、安全、数据、计费：自动切回严格模式。

6 场景 pilot：
- 小任务完成 2/2（旧强制设计流程 0/2）
- 严格路由检查 12/12

限制也很重要：每配置只跑了 1 次，没有可靠 latency/token 遥测，所以我暂时不声称“省了多少时间和 token”。

源码、评测和完整报告：https://github.com/LiuHHHYuuu/adaptive-fast-execution

## 中文 Thread

### 1/4

Codex 有时不是能力不够，而是流程过重：一个小时内能完成的局部修改，也可能先经历方案、设计文档和多轮确认。

我做了一个 Adaptive Fast Execution Skill，目标不是取消严谨，而是把严谨用在真正需要的地方。

### 2/4

快速路径只有在这些条件同时成立时启用：局部、可逆、低风险、目标清楚、预计一小时内。

流程压缩为：
Inspect → Implement → Verify → Handoff

生产、发布、权限、安全、删除、迁移、计费等全部硬性排除。

### 3/4

受控 pilot 共 6 个场景：

- 2 个小任务：新版完成并验证 2/2；旧强制设计基线 0/2
- 4 个复杂/高风险任务：新版严格路由断言 12/12
- 全部断言：新版 20/20，旧基线 12/20

### 4/4

我没有把输出字符数冒充 token，也没有用文件时间戳冒充真实性能。

当前结论只到这里：流程分流有效，未观察到安全路由退化。下一轮需要原生 tracing、重复运行和真实大型仓库，才能量化时间/token 收益。

源码与报告：https://github.com/LiuHHHYuuu/adaptive-fast-execution

## English post

I built a throttle/brake router for Codex—not a prompt that claims to be “always faster.”

Local, reversible, low-risk work takes a compact path: Inspect → Implement → Verify → Handoff. Architecture, production, security, data, billing, and publishing automatically fall back to strict mode.

6-scenario pilot:
- Small tasks completed: 2/2 vs 0/2 under the old mandatory-design baseline
- Strict-routing checks: 12/12

Honest limitation: one run per configuration and no reliable latency/token telemetry, so there is no speed or token-savings claim yet.

Source, evals, and report: https://github.com/LiuHHHYuuu/adaptive-fast-execution

## 配图

使用 `media/adaptive-fast-execution-social-card.png`。图片已经写明 `6 scenarios · 1 run/config · no latency/token claim`，发布时不要裁掉底部限制说明。
