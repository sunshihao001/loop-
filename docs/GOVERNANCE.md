# 治理与 Proof Gate

## 为什么需要治理

没有治理层的 AI 执行容易出现：

- 意图没锁定就开始实现；
- 上下文漂移；
- 在主分支或错误目录直接修改；
- 没有证据就声称完成；
- demo 结果被误当作真实项目验证。

## Decapod Governance Loop

涉及代码修改、仓库结构修改、自动化脚本或多 agent 协作时，默认使用：

```text
todo add/claim → infer orientation → workspace ensure → implement → validate → done --validated
```

## Proof Gate 准入表

| 场景 | 是否需要 proof gate | 说明 |
|---|---|---|
| 单纯文档补充 | 可轻量验证 | read-back + verify.py |
| 多文件工程修改 | 必需 | 需要测试/脚本证据 |
| 生产服务/外部 API 写入 | 必需 + 人工授权 | 不能自动越权 |
| 删除/迁移/重命名大量文件 | 必需 + 人工确认 | 当前用户明确要求不主动迁移目录 |
| demo 仓库实验 | 需要标注限制 | 不等于真实项目验证 |
| 数据分析结论 | 需要 preregister → verify | 避免先看结果后补假设 |

## 完成状态

| 状态 | 含义 |
|---|---|
| `done` | 所有验收通过 |
| `partial` | 主要产物完成，但仍有明确缺口 |
| `blocked` | 被外部权限/信息/工具故障阻塞 |
| `rejected` | 验证失败或方向不符合意图 |

## 本仓库最低验证

```bash
python3 scripts/verify.py
```

这只是仓库结构验证，不替代真实项目的 Decapod validate。
