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
- 补充约束（来自多智能体辩论实验）：
  - 对消费级预算用户，token/cost budget 不是脚注，而是第一约束；
  - 需要显式预算熔断机制，而不是笼统的“be careful”；
  - 如果 loop 的 accepted change rate 长期低于 50%，应停止并重新评估，而不是继续空转。
- 来源：Loop Research Intake S3（Anatoli hard limit）、S4（yibie 8 分门槛）、S1（0xJeff promotion gate）、Addy Osmani 三方辩论实验。

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

## Multi-Agent Structured Debate

- 适用：重要文章/概念入库后、Pattern 固化前、主张有争议时。
- 输入：源材料、单模型理解笔记（基线）、角色配置。
- 输出：矛盾地图、遗漏洞察清单、经多视角验证的 Pattern 候选。
- 验收：辩论必须产出至少 1 个单模型笔记遗漏的洞察；无矛盾的辩论视为失败。
- 核心原理：单模型有同源偏见；不同视角产生不同盲区；矛盾比共识更有价值。
- 流程：独立分析（隔离子代理）→ 综合对比（矛盾+共识+独有）→ 异质验证（可选，外部 AI）→ 产出。
- 来源：Loop Engineering 辩论实验（2026-06-26），3 视角产出 12 个遗漏洞察。
- 已知局限：同源模型共享盲区；综合仍由单一模型完成；3 倍 token 成本。
- 协议详情：`ObsidianVault/20_Notes/多智能体结构化辩论协议V1.md`

## Token Budget Circuit Breaker

- 适用：所有消耗 token 的自动化流程（loop、cron、子代理、长任务）。
- 输入：单次预算上限、累计预算上限、单次迭代成本估算。
- 输出：预算耗尽时终止信号 + 消耗报告。
- 验收：任何 loop/cron 必须有预算熔断；超限时停止并报告，不静默继续。
- 三层熔断：
  1. 单次迭代上限：单轮 token 超过阈值 → 停止本轮；
  2. 累计预算上限：总 token 超过预算 → 停止整个 loop；
  3. 低效燃烧检测：连续 N 轮无进展 → 停止并报告。
- 来源：Loop Engineering 辩论实验，实践工程师视角——文章只说"be careful"没有可操作方案。

## Trust Transfer Awareness

- 适用：使用 maker/checker split、verifier sub-agent、外部审查时。
- 输入：信任链结构（A 信任 B，B 信任 C...）。
- 输出：信任链中每一环的可靠性评估 + 未验证环节标注。
- 验收：不能假设 checker 可靠；必须标注 checker 自身的可信度来源。
- 核心问题："loop 的问题用更多 loop 解决"是循环信任转移——你不信任 agent A，所以信任 agent B，但 B 的可信度从未被独立验证。
- 缓解：用不同模型做 checker（异质验证）；用确定性工具（test/build）做 checker 而非另一个 LLM。
- 来源：Loop Engineering 辩论实验，怀疑论者视角。

## Cognitive Guard

- 适用：所有自动化 loop、cron、unattended 任务。
- 输入：使用者理解力基线、loop 产出的代码/文档、使用者审查记录。
- 输出：理解力退化警告 + 强制审查触发。
- 验收：loop 产出的变更必须有人类审查记录；长期未审查的产出触发警告。
- 三个风险概念：
  1. **Comprehension Debt**：loop 越快产出你不懂的代码，理解缺口越大。对应 technical debt (Cunningham 1992) 的自然延伸。
  2. **Cognitive Surrender**：loop 自己跑起来后人容易放弃判断力。对应 Bainbridge (1983) "Ironies of Automation"——自动化程度越高，人越脱离回路，但人在需要介入时最无力。
  3. **Intent Debt**：agent 每次冷启动都用猜测填补意图空洞。skill 是把意图写到外部。
- Loop 悖论：最需要 loop 的人（理解力不足）最容易被 loop 伤害；能安全使用 loop 的人本来就不那么需要它。
- 来源：Loop Engineering 辩论实验，学术研究者（40 年人因学文献）+ 怀疑论者（loop 悖论）。

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
