# 工作流协议

## 总循环

```text
Intent → Route → Framework → Pattern → Instance → Execute → Verify → Persist → Learn
```

## 1. Intent：意图发现

当用户输入模糊、只有感觉或方向时，不应直接交给 Codex。先做 Stage 0：

- 用户到底想达到什么？
- 不想做什么？
- 这是不是旧问题反复？
- 哪些偏好或约束没有说出来？
- 是否需要外部 AI 协商或多视角 STORM 扫描？

输出不是完整文档，而是更清楚的任务边界。

## 2. Route：路由

按任务类型选择能力：

| 任务类型 | 默认路由 |
|---|---|
| 模糊想法/项目方向 | Stage 0 + dbskill + Obsidian |
| 复杂研究/验证 | Science Superpowers + Obsidian |
| 工程任务 | Trellis + Codex + Decapod |
| 知识沉淀 | Obsidian + hot/log + index |
| 多 agent 交接 | repo-harness + Trellis |
| 持续循环/定时任务 | Hermes cron + State Outside Context |
| 研究协议/研究路由升级 | `docs/RESEARCH_TOOL_ROUTING_PROTOCOL.md` + Obsidian 真源 + real-run verification |

## 3. Framework Selection

选择机制层，而不是凭工具印象执行。

规则：

1. 涉及代码修改：Codex + Decapod。
2. 涉及可交付工程项目：Trellis。
3. 涉及长期知识：Obsidian。
4. 涉及跨会话/平台入口：Hermes。
5. 涉及分析 claim：Science Superpowers。

## 4. Pattern Selection

每个任务至少有：

- Plan：目标、范围、禁止项、验收标准；
- Act：执行动作；
- Verify：命令、读回、proof 或人工检查；
- Persist：写入正确真源；
- Learn：是否产生可复用经验。

## 5. Instance Config

把具体项目的选择写进 JSON 或 Trellis task 文件。至少包括：

- framework 列表；
- pattern 列表；
- design_axes；
- source_of_truth；
- verification；
- persistence_sinks。

## 6. Execute

执行阶段必须保留边界：

- Hermes 保留意图、授权、最终关闭；
- Codex 执行明确任务；
- Decapod 对代码执行提供 orientation/workspace/validate；
- Trellis 保存任务生命周期；
- Obsidian 保存长期知识。

## 7. Verify

完成声明必须对应证据：

- 文件存在 + 内容读回；
- 脚本/测试真实运行；
- Decapod validate 或等价 proof gate；
- Git diff 范围符合预期；
- 未完成边界明确标注。

## 8. Persist

结果按类型分流：

| 信息类型 | 真源 |
|---|---|
| 稳定知识/协议 | Obsidian 20_Notes / docs |
| 项目任务状态 | Trellis task / repo docs |
| 临时热上下文 | Obsidian hot.md |
| 可复用流程 | Hermes skill |
| 代码和工程控制面 | GitHub repo |

## 9. Learn

一次任务结束后问：

- 哪个判断错了？
- 哪个 pattern 有用？
- 哪个规则需要修改？
- 是否需要创建/更新 skill？
- 是否只是一例样本，不能升级默认？
