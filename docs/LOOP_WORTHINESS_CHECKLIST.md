# Loop Worthiness Checklist

## 目的

在决定一个任务是否值得做成 loop 之前，必须通过本检查表。

## 四条件检查

| # | 条件 | 解释 | 判定 |
|---|---|---|---|
| 1 | 任务至少每周重复 | 一次性任务不值得搭 loop | ☐ 是 ☐ 否 |
| 2 | 能自动拒绝坏输出 | 没有 fail signal 就会空转 | ☐ 是 ☐ 否 |
| 3 | agent 能端到端执行 | 不能半路一直交还给人 | ☐ 是 ☐ 否 |
| 4 | Done 是客观的 | 主观品味仍需人类判断 | ☐ 是 ☐ 否 |

## 判定规则

- **4/4 满足**：强烈推荐做 loop。
- **3/4 满足**：可以做 loop，但需标注缺失条件的风险。
- **2/4 或更少**：不建议做 loop，应保持手动或半自动。

## 补充检查

### 成本意识

- [ ] 预估每轮 token / cost 消耗？
- [ ] 设定了 max iterations / budget cap？
- [ ] 定义了 accepted change rate 的最低门槛（建议 ≥ 50%）？

### 建设顺序

- [ ] 已手动跑通至少 1 次？
- [ ] 手动流程已保存为 skill（指令、规则、禁止项）？
- [ ] skill 已包进 loop 并加了门控和停止条件？
- [ ] 以上都完成后才考虑放入 schedule / cron？

### 风险检查

- [ ] loop 没有 verifier？→ 不是 loop，只是自我同意的重复。
- [ ] loop 没有 state 记录？→ 下一轮会重复犯错。
- [ ] loop 没有 stop condition？→ 会静默烧钱。
- [ ] agent 会过早声称完成？→ Ralph Wiggum loop 风险。

## 使用示例

### 示例 1：每日研究简报 cron

| # | 条件 | 判定 | 理由 |
|---|---|---|---|
| 1 | 每周重复 | ✅ 是 | 每日运行 |
| 2 | 能自动拒绝坏输出 | ⚠️ 部分 | 可以检查格式和来源，但内容质量需人审 |
| 3 | agent 能端到端执行 | ✅ 是 | 搜索→抽取→整理→写入 Obsidian |
| 4 | Done 是客观的 | ⚠️ 部分 | 格式可验证，但"是否有价值"主观 |

判定：3/4，可以做 loop，但需标注内容质量仍需人审。

### 示例 2：代码修复 loop

| # | 条件 | 判定 | 理由 |
|---|---|---|---|
| 1 | 每周重复 | ✅ 是 | 多次 bug 修复 |
| 2 | 能自动拒绝坏输出 | ✅ 是 | test / typecheck / build |
| 3 | agent 能端到端执行 | ✅ 是 | Codex 可端到端 |
| 4 | Done 是客观的 | ✅ 是 | tests pass |

判定：4/4，强烈推荐做 loop。

## 来源

- Loop Research Intake S3（Anatoli Kopadze《Loops explained》四条件）
- Loop Research Intake S4（yibie "不要把没验证过的东西排进 schedule"）
- Loop Research Intake 四篇横向综合（`20_Notes/Loop_Research_Intake_四篇横向综合.md`）
