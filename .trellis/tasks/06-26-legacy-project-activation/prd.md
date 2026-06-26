# 激活旧项目到新工作流框架

## Problem / Intent

旧 8 层框架已经识别出 Hermes、dbskill、Science Superpowers、Trellis、Decapod、Codex、ObsidianVault、repo-harness 等关键项目，但这些项目多数仍停留在“已安装 / 已分析 / 已记录”的资产状态，没有被日常工作流稳定调用。

本任务要把这些旧项目纳入新的 Framework · Pattern · Instance 控制面，让它们具备自然语言触发、输入输出、验证证据和沉淀路径。

## Desired Outcome

当任务完成后，`loop循环项目` 仓库应能回答：

1. 用户一句自然语言应该触发哪些 Framework；
2. 每个旧项目什么时候被调用、输入是什么、输出是什么；
3. 旧项目参与哪些 Pattern；
4. 一个具体 Instance 如何记录这些选择；
5. 什么证据证明项目已经从“资产”变成“工作流组件”。

## Scope

### In scope

- 在 `loop循环项目` 中维护旧项目激活文档。
- 建立或完善：
  - `docs/LEGACY_PROJECT_ACTIVATION.md`
  - `docs/ROUTING_MATRIX.md`
  - `docs/frameworks/*.md`
  - `examples/instances/legacy-project-activation.json`
- 使用 Trellis task 记录本次激活任务。
- 运行 `python3 scripts/verify.py` 验证仓库结构。
- 推送 GitHub，并将关键状态回写 Obsidian hot/log。

### Out of scope

- 不移动或重构 `/root/ObsidianVault`。
- 不把所有旧项目一次性做成全自动系统。
- 不在本阶段强行启用 Decapod/Codex 代码实现，除非后续进入脚本/自动化修改。
- 不把 demo 结果声称为所有真实项目已验证。

## Acceptance Criteria

- [x] `docs/LEGACY_PROJECT_ACTIVATION.md` 存在，并说明旧项目为什么没有被调用起来。
- [x] `docs/ROUTING_MATRIX.md` 存在，并把自然语言映射到 Framework / Pattern / Instance。
- [x] `docs/frameworks/` 下至少有 Hermes、Trellis、Decapod、Codex、Obsidian、dbskill、Science Superpowers、repo-harness 8 张 Framework Card。
- [x] `examples/instances/legacy-project-activation.json` 存在，并记录 Framework、Pattern、Design Axes、source_of_truth、activation_batches、verification。
- [x] `scripts/verify.py` 将新增关键文档纳入 required files。
- [x] `python3 scripts/verify.py` 输出 `VERIFY OK`。
- [x] 变更已提交并推送到 GitHub `https://github.com/sunshihao001/loop-`。
- [ ] Obsidian `hot.md` 与 `20_Notes/log.md` 记录本次 Trellis task 建立和激活状态。

## Constraints

- 保持现有目录结构，不迁移用户项目或 ObsidianVault。
- 面向用户的文档优先中文，关键术语保留英文。
- 任何“已激活”声称必须对应文件、路由、Instance 或验证证据。
- 对外部副作用和代码实现阶段，后续再启用 Human Approval / Decapod Governance Loop。

## References

- `/root/loop循环项目/docs/LEGACY_PROJECT_ACTIVATION.md`
- `/root/loop循环项目/docs/ROUTING_MATRIX.md`
- `/root/loop循环项目/examples/instances/legacy-project-activation.json`
- `/root/ObsidianVault/20_Notes/AI_Agent工作流_Framework_Pattern_Instance三层协议.md`
- `/root/ObsidianVault/20_Notes/已安装项目工作流化问题.md`
- GitHub: `https://github.com/sunshihao001/loop-`

## Open Questions

- 第一个真实 verified run 选择哪个项目链路：建议 `Trellis + Obsidian + GitHub loop repo`。
- 后续是否将 Framework Card 质量检查也写入 `scripts/verify.py`。
- 何时把 Decapod + Codex 接入本项目的脚本/自动化阶段。
