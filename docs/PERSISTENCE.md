# 沉淀规则

## 核心边界

- ObsidianVault：长期知识、协议、理解笔记、hot/log。
- GitHub 仓库：可协作、可版本化的工程控制面。
- Trellis：任务生命周期和工程交付证据。
- Hermes memory：少量稳定偏好和环境事实。
- Hermes skill：可复用操作流程。

## 分流表

| 内容 | 放哪里 | 不放哪里 |
|---|---|---|
| 用户长期偏好 | Hermes memory | 项目 README |
| 协议理论正文 | Obsidian 20_Notes | hot.md |
| 工程控制面模板 | 本仓库 templates/ | Obsidian 10_Articles |
| 任务执行证据 | Trellis task / repo docs | memory |
| 最近续跑指针 | hot.md | 长篇理论页 |
| 可复用操作流程 | Hermes skill | 临时聊天上下文 |

## hot.md 使用规则

hot.md 只保存“下次接续需要知道的指针”，不保存整篇报告。

## log.md 使用规则

log.md 记录发生了什么、改了哪些文件、验证结果是什么。

## GitHub 使用规则

本仓库用于：

- 对外版本化协议；
- 让 AI coding agent 能按 AGENTS.md 维护；
- 保存模板和轻量验证脚本；
- 作为未来 workflow control-plane 的可协作入口。
