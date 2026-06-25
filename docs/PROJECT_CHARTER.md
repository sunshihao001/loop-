# 项目章程

## 项目名

loop循环项目

## 一句话定义

把当前 AI 工作台从“有很多工具和协议”推进为“可版本化、可验证、可维护的循环工作流控制面”。

## 背景

当前本地系统已经有：

- Hermes：宏观协调、记忆、技能、Telegram gateway、cron；
- Codex：实现和调试；
- Decapod：治理、orientation、workspace isolation、validate、proof gate；
- Trellis：任务生命周期、PRD/design/implement/verify、长期任务骨架；
- ObsidianVault：长期知识沉淀；
- repo-harness：agent 之间的 handoff / resume / checks 传输层；
- dbskill / Science Superpowers / STORM：不同层级的问题澄清、方法论和验证模式。

问题不再是“缺一个工具”，而是这些能力需要被组织成可重复执行的 loop。

## 目标

1. 给 AI 和人类都能读懂的工作流协议入口。
2. 把 Framework / Pattern / Instance 三层模型工程化。
3. 建立最小验证脚本，防止仓库变成无约束文档堆。
4. 为后续真实项目接入提供模板。
5. 保持和 Obsidian 知识库的清晰边界。

## 非目标

- 不替代 ObsidianVault。
- 不替代 Trellis / Decapod / Hermes。
- 不承诺自动完成所有 workflow。
- 不在初版引入复杂依赖、数据库或服务。

## 成功标准

| 标准 | 验收方式 |
|---|---|
| 有清晰入口 | README + AGENTS + docs/PROJECT_CHARTER |
| 有架构定义 | docs/ARCHITECTURE.md |
| 有工作流协议 | docs/WORKFLOW_PROTOCOL.md |
| 有治理准入 | docs/GOVERNANCE.md |
| 有沉淀规则 | docs/PERSISTENCE.md |
| 有示例 Instance | examples/instances/basic-loop.json |
| 可被 CI 验证 | scripts/verify.py + GitHub Actions |
