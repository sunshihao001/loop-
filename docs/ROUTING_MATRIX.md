# Routing Matrix：自然语言 → Framework / Pattern / Instance

## 目的

本矩阵把用户的自然语言输入，路由到新框架中的：

```text
Intent Type → Framework → Pattern → Instance → Verification → Persistence
```

它解决旧项目“知道存在但不会被调用”的问题。

---

## 路由总表

| 用户自然语言 | Intent Type | Frameworks | Patterns | Instance | 是否需要确认 | 最低输出 | 验证 |
|---|---|---|---|---|---|---|---|
| “我有个想法” / “我感觉可以做个东西” | idea-intake | Hermes + dbskill + Obsidian | Intent Triage + State Outside Context | idea-to-project | 通常需要 | 问题边界 / 方向候选 | 写入 Obsidian 或明确不沉淀 |
| “帮我把这个想法变成项目” | projectization | Hermes + Trellis + Obsidian | Plan-Act-Verify | project-bootstrap | 需要 | PRD / design / task skeleton | task 文件完整 + read-back |
| “查一下有没有现成方案” | reuse-review | Hermes + Obsidian + external search/agent-reach | Reuse-first Review | reuse-before-build | 不一定 | 现有方案对比 / 是否自建判断 | 来源可追溯 |
| “让 GPT/Claude 批评一下” | external-review | Hermes + 外部 AI 协商层 + Obsidian | Planner/Evaluator Split | external-ai-review | 需要用户协助或授权 | 外部问题包 / 回收表 | 回收内容被筛选并沉淀 |
| “多角度看看” / “找矛盾” | multi-perspective | Hermes + STORM + Obsidian | Multi-perspective Scan | storm-scan | 不一定 | 视角扫描 / 矛盾地图 | 至少有反例/风险项 |
| “继续推进” / “接着上次” | continuation | Hermes + Obsidian hot/log + Trellis | Clean-Context Continuation | active-project | 不一定 | 当前状态 / 下一步动作 | 读 hot/log/task 后行动 |
| “执行吧” | implementation | Hermes + Codex + Decapod + Trellis | Decapod Governance Loop + Plan-Act-Verify | implementation-task | 视副作用 | diff / 测试 / 实现说明 | tests/verify/validate |
| “修 bug” | debugging | Hermes + Codex + Decapod | Systematic Debugging + Governance Loop | bugfix-task | 视副作用 | root cause / patch / test | 复现失败→修复→通过 |
| “写进知识库” / “保存这次认知” | persistence | Hermes + ObsidianVault | Persist + Learning Loop | knowledge-persistence | 通常不需要 | note / hot / log | read-back + search |
| “做成长任务” | long-task | Hermes + Trellis + repo-harness | State Outside Context + Handoff | long-task-handoff | 需要 | task package / resume.md | 新会话可恢复 |
| “定时提醒/自动跑” | scheduled-loop | Hermes cron + Obsidian/Trellis | Loop Engineering + Human Approval | scheduled-loop | 需要 | cron job / prompt / output sink | cron run 或 dry-run |
| “验证这个结论” | claim-verification | Hermes + Science Superpowers | Preregister → Verify | research-verification | 视影响 | verification plan / report | claim 前有证据 |
| “这个项目哪些工具没用起来” | framework-activation | Hermes + loop repo + Obsidian | Framework Activation + Learning Loop | legacy-project-activation | 不一定 | activation map / cards / runs | verify.py + GitHub push |

---

## 路由执行步骤

1. **识别 Intent Type**：不要直接按工具名执行。
2. **选择 Frameworks**：只选本轮需要的机制。
3. **选择 Patterns**：至少包含 Plan-Act-Verify 或说明为什么不需要。
4. **绑定 Instance**：若没有现成 Instance，先创建最小配置。
5. **执行并验证**：真实文件、命令、读回或 proof。
6. **沉淀**：按 `docs/PERSISTENCE.md` 分流。

---

## 失败处理

| 失败 | 处理 |
|---|---|
| Intent 不清楚 | 回到 Stage 0，不交给 Codex |
| Framework 缺卡 | 创建或更新 `docs/frameworks/*.md` |
| Pattern 不明确 | 更新 `docs/PATTERNS.md` |
| Instance 缺失 | 新建 `examples/instances/*.json` |
| 验证失败 | 标记 partial/blocked，不声称完成 |
| 结果无法沉淀 | 先写 hot/log 指针，后续补正式文档 |
