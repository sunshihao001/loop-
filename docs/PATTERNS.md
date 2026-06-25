# Patterns

## Plan-Act-Verify

- 适用：所有任务。
- 输入：目标、范围、验收标准。
- 输出：已验证产物或 blocked 状态。
- 验收：必须有真实工具输出。

## State Outside Context

- 适用：跨会话、多轮、异步任务。
- 输入：任务状态文件、hot/log、Trellis task。
- 输出：可从文件恢复的任务状态。
- 验收：新会话只读文件即可续跑。

## Clean-Context Continuation

- 适用：长任务、夜间任务、cron。
- 输入：精简上下文包。
- 输出：下一轮可执行指令。
- 验收：上下文重置后不丢目标和边界。

## Decapod Governance Loop

- 适用：代码修改、多 agent 并发、proof-required 任务。
- 输入：task id、intent、workspace。
- 输出：orientation、隔离 worktree、validate 证据。
- 验收：Decapod validate 或等价证明通过。

## Learning Loop

- 适用：复杂任务完成后。
- 输入：失败、摩擦、成功 pattern。
- 输出：协议候选、skill 更新、Obsidian 复盘。
- 验收：只升级经过样本验证的规则。
