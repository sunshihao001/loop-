# 架构：Framework · Pattern · Instance

## 核心模型

本项目采用三层架构：

```text
Framework  = 机制层：工具原生能做什么
Pattern    = 模式层：如何把机制组合成可复用工作方式
Instance   = 实例层：具体项目如何选择和配置
```

## Framework 层

| Framework | 当前角色 | 典型能力 |
|---|---|---|
| Hermes | 宏观协调与会话宿主 | tools、skills、memory、cron、Telegram gateway |
| Trellis | 工程任务生命周期 | PRD → design → implement → verify |
| Decapod | 治理与证明 | todo claim、orientation、workspace ensure、validate、proof gate |
| Codex | 实现层 | 代码修改、调试、长任务执行 |
| ObsidianVault | 长期知识库 | source → note → wikilink → index → hot/log |
| repo-harness | 传输/交接层 | handoff、resume、checks、events |
| dbskill | 快速诊断/分诊 | 商业、内容、决策、执行力等诊断工具 |
| Science Superpowers | 深度方法论 | framing、prior work、design、preregister、verify、red-team |

## Pattern 层

| Pattern | 解决的问题 | 默认状态 |
|---|---|---|
| Plan-Act-Verify | 防止直接执行无验收 | 每个任务必需 |
| State Outside Context | 防止上下文丢失 | 长任务必需 |
| Clean-Context Continuation | 跨会话续跑 | 超过 2 轮必需 |
| Decapod Governance Loop | 代码执行的定界和 proof | 代码修改必需 |
| Preregister → Verify | 先锁定假设再看结果 | 数据/分析任务必需 |
| Learning Loop | 从任务错误回写规则 | 重要任务后必需 |
| Human Approval Checkpoint | 控制副作用 | 生产/外部写入必需 |

## Instance 层

Instance 是一个具体项目的选择记录。它回答：

- 选了哪些 Framework？
- 选了哪些 Pattern？
- 10 个 Design Axes 的值是什么？
- 验收证据在哪里？
- 沉淀真源在哪里？

示例见：`examples/instances/basic-loop.json`。

## 分层边界

- Framework 不直接等于工作流；它只提供机制。
- Pattern 不直接等于项目；它是可复用做法。
- Instance 才是具体项目配置，不应反向污染通用协议。
