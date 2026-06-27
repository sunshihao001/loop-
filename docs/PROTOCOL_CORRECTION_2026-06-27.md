# 协议修正：8 层框架项目分配纠正

> 日期：2026-06-27
> 来源：VPS 项目全景扫描（25 个项目）+ ForgeGod 循环验证
> 状态：立即生效（遵循 RUNTIME_IMMEDIATE_ACTIVATION_PRINCIPLE）

## 三个错误分配

### 修正 1：Trellis 从 ⑦ 移到 ③

**之前**：⑦ Trellis + Obsidian（并列在沉淀层）

**之后**：③ Hermes + Trellis（并列在协调层）；⑦ Obsidian 独立

**证据**：
- Trellis 官方定位："An out-of-the-box engineering framework for AI coding. Trellis persists specs, tasks, and memory into your repo, so any coding agent works to your engineering standards."
- Trellis 做的事：持久化 specs、管理 tasks、管理 workspace、skill routing — 全部是**协调**职责，不是知识沉淀
- Obsidian 做的事：长期知识库、文章、笔记、概念链接 — 才是真正的**沉淀**
- 两者性质完全不同，不应并列

### 修正 2：loop循环项目填入 ⑧

**之前**：⑧ 学习闭环 = 空缺

**之后**：⑧ 学习闭环 = loop循环项目（控制面）+ forgegod-bridge（回流机制）

**证据**：
- loop循环项目本身就是 Framework/Pattern/Instance 三层结构的控制面仓库
- forgegod-bridge skill 闭合了 ForgeGod 的跨 session 回流（harvest→Obsidian→inject）
- ⑧ 不再是空缺，而是有工程载体的

### 修正 3：⑤执行层按语言路由

**之前**：⑤ Codex（单一执行层）

**之后**：⑤ ForgeGod（Python 循环）+ Codex（Rust/JS/TS）

**证据**：
- ForgeGod loop 验证通过：PRD 内四机关闭合，GLM-5.2 可用
- ForgeGod 只支持 Python（通过 bash 工具执行）
- Codex 原生支持 Rust/JS/TS/Go 等多语言
- 两者不竞争，按项目语言分工

## 修正后的 8 层协议

```
⓪ 意图发现          空缺 — 需要补
① dbs 路由          dbskill ✓
② Science Superp.   部分 — 需要接入
③ Hermes 协调        Hermes + Trellis（工程任务/规格/workspace）    ← Trellis 从 ⑦ 移入
④ Decapod 治理前     decapod ✓
⑤ 执行              ForgeGod（Python循环）+ Codex（Rust/JS/TS）     ← 按语言路由
⑥ Decapod 治理后     decapod validate ✓
⑦ 知识沉淀           Obsidian（独立）                                ← Trellis 移走后独立
⑧ 学习闭环           loop循环项目（控制面）+ forgegod-bridge（回流）  ← 从空缺变实有
```

## 项目 → 工具路由矩阵

| 项目 | 语言 | 协议层 | 执行工具 | 理由 |
|---|---|---|---|---|
| EverOS | Python | ⑤ | ForgeGod | Python DDD + pytest + make CI |
| EverOS-Hermes | Python | ⑤ | ForgeGod | Python 插件 + tests |
| decapod | Rust | ④⑥ | Codex | ForgeGod 不支持 Rust |
| hermes-studio | Vue/Koa/TS | ⑤ | Codex | ForgeGod 不支持 JS/TS |
| FastNodeSync-CLI | Python | ⑤ | ForgeGod | 小型 Python CLI |
| meme-repo | — | ⑦⑧ | Hermes+Obsidian | Paper-only 策略，不编码 |
| loop循环项目 | — | ⑧ | Hermes+Obsidian | 控制面文档，不编码 |
| Trellis | — | ③ | 基础设施 | 给其他项目提供工程框架 |
| ObsidianVault | — | ⑦ | Hermes+Obsidian | 长期知识库 |
| ai-workflow-repo | — | ⑧ | 待合并 | 方法论参考，合并进 loop循环项目 |

## 待处理项

1. ai-workflow-repo 的方法论内容合并进 loop循环项目
2. test-harness-integration（1 commit）和 workflow-integration-demo（3 commits）评估是否归档
3. ⓪意图发现层仍然空缺，需要设计
4. ②Science Superpowers 需要接入工作流
