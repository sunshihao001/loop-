# Source Index

本仓库初版依据以下本地资料整理。这里只保存引用和摘要，不复制整个知识库。

## Obsidian 主协议

| 来源 | 作用 |
|---|---|
| `/root/ObsidianVault/20_Notes/AI_Agent工作流_Framework_Pattern_Instance三层协议.md` | 当前最新三层协议：Framework / Pattern / Instance |
| `/root/ObsidianVault/20_Notes/工作流架构修正_意图发现到治理证明.md` | 旧 8 层协议，已被三层协议吸收但仍是历史脉络 |
| `/root/ObsidianVault/20_Notes/Hermes工作流闭环化详细版理论.md` | 控制面闭环：路由、验收、委派、gate、沉淀、学习 |
| `/root/ObsidianVault/20_Notes/Hermes_L分层_结合最新工作流协议_1小时梳理任务.md` | Hermes L 分层与工作流协议对齐 |

## 本地工程验证

| 来源 | 作用 |
|---|---|
| `/root/workflow-integration-demo/docs/integrated-workflow-protocol.md` | repo-harness + Decapod 分层互补协议 |
| `/root/Trellis/.trellis/tasks/06-25-repo-harness-decapod-integration/` | 端到端集成验证任务包 |
| `/root/AGENTS.md` | VPS 目录与迁移偏好、当前工作流主协议 |
| `/root/ObsidianVault/20_Notes/已安装项目工作流化问题.md` | 旧项目已安装但未工作流化的根因分析 |

## 维护原则

当源资料更新时，本仓库不自动复制全部内容，而是：

1. 更新相关 docs 摘要；
2. 在本文件补充来源；
3. 运行 `python3 scripts/verify.py`；
4. Git commit 记录变更原因。
