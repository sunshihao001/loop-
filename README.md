# loop循环项目

> 面向 AI 维护的工作流闭环项目：把 Obsidian 知识库里的新工作流协议、Trellis/Decapod/repo-harness/Codex/Hermes 本地实践，整理成一个可版本化、可验证、可继续演化的 GitHub 仓库。

## 项目定位

`loop循环项目` 不是一个新的工具，也不是把知识库复制到 GitHub。它是一个 **workflow control-plane repository**：

- **Framework 层**：记录当前使用的机制能力，如 Hermes、Trellis、Decapod、Codex、Obsidian、repo-harness。
- **Pattern 层**：沉淀可复用工作流模式，如 Plan-Act-Verify、State Outside Context、Clean-Context Continuation、Decapod Governance Loop、学习闭环。
- **Instance 层**：把具体项目如何选择 Framework / Pattern / Design Axes 写成可审计配置。

## 为什么叫 loop

当前工作流的核心不再是“一次性让 AI 回答问题”，而是形成循环：

```text
Intent → Route → Plan → Act → Verify → Govern → Persist → Learn → Next Intent
```

也就是：

1. 先发现真实意图；
2. 再选择机制和模式；
3. 执行时要求证据；
4. 结果沉淀到知识库/任务系统；
5. 从错误和样本里学习，回写下一轮规则。

## 仓库职责

| 目录 | 职责 |
|---|---|
| `docs/` | 项目章程、架构、协议、治理准入、沉淀规则 |
| `templates/` | 后续新项目/新任务可复用模板 |
| `examples/` | 示例 Instance，用于说明如何落地 |
| `scripts/` | 轻量验证脚本，确保文档和配置可被 AI 稳定读取 |
| `.github/workflows/` | GitHub Actions 文档结构验证 |

## 当前重点文档

- `docs/LEGACY_PROJECT_ACTIVATION.md`：把旧 8 层框架中已安装但未调用起来的项目，转成新框架下可触发、可验证、可沉淀的 Framework Cards / Routing Matrix / Instance。
- `docs/ROUTING_MATRIX.md`：自然语言输入到 Framework / Pattern / Instance 的默认路由。
- `docs/RESEARCH_TOOL_ROUTING_PROTOCOL.md`：研究任务从问题澄清、资料基线、结构化辩论、异质补盲、深度验证到真实试跑与规则提升的控制面协议。
- `docs/FUZZY_INPUT_RESEARCH_ROUTING_AUDIT.md`：模糊自然语言输入下，哪些研究工具真正已工作流化、哪些还只是已安装或仅在协议中有位置的控制面审计。
- `docs/frameworks/`：核心旧项目的 Framework Cards。
- `examples/instances/legacy-project-activation.json`：旧项目激活任务的实例配置。
- `examples/instances/research-tool-routing.json`：研究工具路由协议的实例配置，明确何时允许从研究结论升级为 repo 默认规则。

## 快速开始

```bash
python3 scripts/verify.py
```

验证会检查：

- 关键文档是否存在；
- README 是否包含核心循环；
- docs 中是否声明 Framework / Pattern / Instance；
- 示例配置是否为合法 JSON；
- 所有 Markdown 是否不为空。

## 当前状态

- 初版来源：`/root/ObsidianVault` 中的新工作流协议与本地集成实践。
- 关键知识库协议：`20_Notes/AI_Agent工作流_Framework_Pattern_Instance三层协议.md`。
- 关键验证实践：`/root/workflow-integration-demo/docs/integrated-workflow-protocol.md`。
- 版本：`v0.1.0-draft`。
- GitHub 仓库名：`loop-`（GitHub/gh 对中文仓库名做了 ASCII 兼容处理；本地项目目录仍为 `/root/loop循环项目`）。

## AI 维护原则

1. 不复制整个 ObsidianVault；只保留 GitHub 项目需要的协议摘要、引用和执行模板。
2. Obsidian 仍是长期知识真源；本仓库是工程化控制面。
3. 任何“完成”都必须有验证证据。
4. 涉及代码修改时，应使用 Decapod Governance Loop 或等价 proof gate。
5. 规则更新必须写清来源、变更原因和验证方式。
