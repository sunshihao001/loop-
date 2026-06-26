# Patterns

## Plan-Act-Verify (Verifier-first Loop)

- 适用：所有任务。
- 输入：目标、范围、验收标准。
- 输出：已验证产物或 blocked 状态。
- 验收：必须有真实工具输出。
- Verifier 形式分类：
  - hard test：代码测试是否通过；
  - measurable condition：数字是否超过阈值；
  - rubric：模型按标准评分；
  - linter / typecheck / build。
- 失败 action rule：verify 失败后不是直接重试，而是先识别最弱项并优先修复。
- 来源：原 Pattern + Loop Research Intake S3（Anatoli）、S4（yibie）。

## State Outside Context

- 适用：跨会话、多轮、异步任务。
- 输入：任务状态文件、hot/log、Trellis task。
- 输出：可从文件恢复的任务状态。
- 验收：新会话只读文件即可续跑。
- 最小字段定义：
  - done：已完成什么；
  - failed：失败过什么；
  - next：下一步是什么；
  - iteration / cost：当前轮次和累计成本。
- 来源：原 Pattern + Loop Research Intake 全 4 篇共识。

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
- Maker/Checker Split：实现者（maker）和验证者（checker）必须分离，不能自己验自己。

## Learning Loop

- 适用：复杂任务完成后。
- 输入：失败、摩擦、成功 pattern。
- 输出：协议候选、skill 更新、Obsidian 复盘。
- 验收：只升级经过样本验证的规则。

## Stop Condition / Budget Guard

- 适用：所有自动化 loop、cron、长任务。
- 输入：max iterations、token/cost budget、success criteria。
- 输出：loop 终止信号 + 失败原因报告。
- 验收：loop 不能无限运行；超限必须报告而非静默继续。
- 停止类型：
  - success：目标达成，loop 正常结束；
  - hard limit：达到 max iterations / token budget / cost cap；
  - human review required：主观判断仍需人介入。
- 来源：Loop Research Intake S3（Anatoli hard limit）、S4（yibie 8 分门槛）、S1（0xJeff promotion gate）。

## Build Order (Prove → Harden → Automate)

- 适用：任何新 loop、新 cron、新自动化规则。
- 输入：手动跑通的样本。
- 输出：经过验证的自动化 loop。
- 验收：必须先有 1 次手动成功样本，才能进入 harden；harden 通过后才能 automate。
- 四步顺序：
  1. Prove：手动跑通一次，证明可靠；
  2. Harden：把手动流程变成 skill（保存指令、规则、禁止项）；
  3. Loop：把 skill 包进 loop，加上门控和停止条件；
  4. Automate：把 loop 放到 schedule / cron / trigger 上。
- 元规则：本项目自身的规则升级也必须遵循此顺序。
- 来源：Loop Research Intake S3（Anatoli）、S4（yibie）、S2（Akshay 先候选再固化）。

## Loop Worthiness Check

- 适用：决定一个任务是否值得做成 loop。
- 输入：任务特征（频率、可验证性、端到端能力、Done 客观性）。
- 输出：loop-worthy / not-loop-worthy 判定 + 理由。
- 验收：四条件中至少满足 3 个才值得做 loop。
- 四条件：
  1. 任务至少每周重复（一次性不值得）；
  2. 能自动拒绝坏输出（有 fail signal）；
  3. agent 能端到端执行（不需半路交还人）；
  4. Done 是客观的（主观品味仍需人）。
- 来源：Loop Research Intake S3（Anatoli 四条件）、S4（yibie "不要把没验证过的东西排进 schedule"）。

## Skill Lifecycle (Create → Verify → Promote → Prune)

- 适用：所有 skill / procedural memory 的生命周期管理。
- 输入：可复用流程、验证样本、使用记录。
- 输出：经过验证的 skill 或被修剪的废弃 skill。
- 验收：skill 必须经过至少 1 次真实任务验证才能晋级为默认；长期未使用的 skill 应被修剪。
- 四阶段：
  1. Create：从成功任务中提取可复用流程；
  2. Verify：在真实任务中验证 skill 是否有效；
  3. Promote：验证通过后升级为默认行为；
  4. Prune：定期修剪、合并、去重，不只增不减。
- 来源：Loop Research Intake S2（Akshay skills + curator）、S3（Anatoli skill building block）、S4（yibie 变 skill）。
