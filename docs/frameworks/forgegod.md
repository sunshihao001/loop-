# Framework Card: ForgeGod

## Role

⑤ 执行层（Python 循环）：多模型自主编码引擎，24/7 loop，PRD 驱动，内置验证 gate 和跨 story learning 回流

## 适用条件

- 项目语言：Python（通过 bash 工具可执行任意命令，但代码生成针对 Python 优化）
- 任务类型：有明确 PRD 的多 story 编码任务
- 需要循环：多轮迭代 + 验证 + 学习回流
- 不适合：Rust/JS/TS/Go 的直接代码生成（用 Codex）

## Trigger phrases

- 用 ForgeGod 跑
- 编码循环
- PRD 驱动开发
- 自动编码 + 验证

## Inputs

- PRD（`forgegod plan` 生成或手写 prd.json）
- 项目目录（已 git init + forgegod init）
- 跨 session learnings（通过 forgegod-bridge inject.py 注入）

## Outputs

- 代码文件（agent 自动 write_file/edit_file）
- git commits（agent 自动 commit）
- `.forgegod/prd.json`（story 状态 + learnings）
- `.forgegod/progress.txt`（人类可读进度）
- `.forgegod/state.json`（循环状态）
- `.forgegod/costs.db`（成本追踪）

## 循环四机关

1. **状态外置**：progress lives in git + prd.json + learnings, NOT in LLM context. 每轮 fresh agent.
2. **状态读回**：`_build_story_prompt()` 注入最近 5 条 learnings + 最近 2 条 error_log
3. **停止判断**：killswitch + budget HALT + reviewer REJECT/retry + retry limit BLOCKED + all done + max iterations
4. **回流写入**：`_append_learning()` → prd.learnings + progress.txt；跨 session 通过 forgegod-bridge harvest→Obsidian→inject

## 参与的 Patterns

- State Outside Context
- Plan-Act-Verify
- Learning Loop
- Reflexion（3-attempt code gen）

## Instance fields

```json
{
  "framework": "ForgeGod",
  "enabled": true,
  "config": {
    "venv": "/root/forgegod-venv",
    "models": {
      "planner": "openai:glm-5.2",
      "coder": "openai:glm-5.2",
      "reviewer": "openai:glm-5.2"
    },
    "env": {
      "OPENAI_API_KEY": "<from Hermes custom provider>",
      "OPENAI_BASE_URL": "https://ai.input.im/v1"
    },
    "bridge_skill": "devops/forgegod-bridge"
  },
  "inputs": [],
  "outputs": [],
  "verification": [],
  "persistence_sinks": []
}
```

## Verification

- `forgegod doctor` 通过
- pytest 测试通过
- git log 有自动 commit
- `forgegod memory` 有 episodic 记录（注意：v0.1.0 loop 不触发 SQLite memory，用 prd.learnings 替代）

## 已知问题

- `forgegod init` 有 bug：`budget.mode` 被写成字符列表，需手动修为 `"normal"`
- SQLite 4-tier memory 在 loop 中不触发（v0.1.0）；跨 session 回流依赖 forgegod-bridge
- GLM-5.2 响应较慢，每个 story 3-7 分钟
- 不支持 Rust/JS/TS 直接代码生成

## 与 Codex 的分工

| 条件 | 用 ForgeGod | 用 Codex |
|---|---|---|
| Python 项目 | ✓ | |
| Rust/JS/TS/Go 项目 | | ✓ |
| 需要 PRD 驱动多 story 循环 | ✓ | |
| 单次编码任务 | `forgegod run` | ✓ |
| 需要 24/7 自主循环 | ✓ | |
