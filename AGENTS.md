# AGENTS.md — loop循环项目 AI 维护协议

本仓库用于维护 AI 工作流闭环的工程化控制面。所有 AI assistant / coding agent 在修改本仓库前必须遵守本文件。

## 最高原则

1. **Obsidian 是长期知识真源**：不要把 `/root/ObsidianVault` 整体复制进本仓库。
2. **本仓库是控制面真源**：GitHub 中维护可复用的协议、模板、验证脚本和示例 Instance。
3. **先读后改**：修改前先读 `README.md`、`docs/PROJECT_CHARTER.md`、`docs/WORKFLOW_PROTOCOL.md`、`docs/GOVERNANCE.md`。
4. **证据优先**：不得声称完成，除非运行 `python3 scripts/verify.py` 并记录结果。
5. **保持中文可读**：面向用户的主文档优先中文，关键技术词保留英文原词。

## 工作流

```text
Intent → Framework Selection → Pattern Selection → Instance Config → Execution → Verification → Persistence → Learning Loop
```

## 修改规则

- 文档变更：同步更新 `docs/SOURCE_INDEX.md` 或相关索引。
- 新增模式：必须写入 `docs/PATTERNS.md`，并给出适用条件、输入、输出、验收方式。
- 新增项目实例：放入 `examples/instances/`，使用 `templates/INSTANCE_TEMPLATE.json` 的结构。
- 新增脚本：放入 `scripts/`，必须能在无额外依赖的 Python 3 环境运行，除非 README 明确说明。

## 禁止事项

- 不要移动、删除或重命名用户本地知识库文件。
- 不要把 demo 跑通伪装成真实项目已验证。
- 不要把未验证规则升级为强制默认。
- 不要把 chat 上下文当作长期真源。

## 完成定义

一次有效变更至少满足：

- [ ] 改动目标清楚；
- [ ] 文档或配置已更新；
- [ ] `python3 scripts/verify.py` 通过；
- [ ] Git diff 只包含预期文件；
- [ ] 如有新认知，应回写 Obsidian hot/log 或对应协议页。
