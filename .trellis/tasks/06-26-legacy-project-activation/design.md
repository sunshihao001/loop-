# Design: 激活旧项目到新工作流框架

## Design Goal

把“旧项目激活”从一次性文档整理，变成可持续维护的控制面模块。

## Architecture

```text
User language
  ↓
docs/ROUTING_MATRIX.md
  ↓
docs/frameworks/<framework>.md
  ↓
examples/instances/legacy-project-activation.json
  ↓
scripts/verify.py
  ↓
GitHub + Obsidian hot/log
```

## Component Responsibilities

| Component | Responsibility |
|---|---|
| `docs/LEGACY_PROJECT_ACTIVATION.md` | 解释问题、激活公式、批次计划 |
| `docs/ROUTING_MATRIX.md` | 自然语言到 Framework/Pattern/Instance 的路由 |
| `docs/frameworks/*.md` | 每个旧项目的触发、输入、输出、验证、失败模式 |
| `examples/instances/legacy-project-activation.json` | 本任务的机器可读配置 |
| `scripts/verify.py` | 最低结构验证 |
| Trellis task | 保存 PRD/design/implement/verification 任务状态 |
| Obsidian hot/log | 跨会话接续和操作记录 |

## Data / Knowledge Flow

1. 用户提出模糊需求或工作流缺口；
2. Hermes 先查 `ROUTING_MATRIX.md` 判断 intent type；
3. 根据 intent type 读取对应 Framework Cards；
4. 若已有 Instance，则按 Instance 执行；否则创建最小 Instance；
5. 执行后跑验证；
6. 结果写入 GitHub + Obsidian。

## Boundaries

- GitHub repo 是工程控制面，不是 ObsidianVault 的替代品。
- Framework Card 是调用协议，不是上游项目完整文档。
- Routing Matrix 是默认路由，不替代用户当前意图判断。
- Trellis 记录任务状态，不替代 Decapod 的代码级 proof。

## Tradeoffs

| Option | Decision | Reason |
|---|---|---|
| 一次性全自动接入所有项目 | 不采用 | 容易空跑 demo，缺真实价值 |
| 先文档化再试跑 | 采用 | 可读、可版本化、低风险 |
| 直接让 Codex 批量实现 | 暂缓 | 现在主要缺路由和激活协议，不是代码量 |
| 把旧 8 层保留为历史 | 采用 | 历史层有用，但不作为执行控制面 |

## Future Extension

- 为每张 Framework Card 增加 YAML frontmatter；
- 让 `scripts/verify.py` 检查每张卡是否包含 Role/Trigger/Inputs/Outputs/Verification；
- 为每次真实调用生成 `runs/*.json`；
- 在代码阶段加入 Decapod workspace / validate。
