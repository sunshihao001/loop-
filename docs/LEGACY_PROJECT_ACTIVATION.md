# 旧项目激活方案：用新框架把已安装能力调用起来

## 这页解决的问题

旧 8 层框架里已经识别出很多项目：Hermes、dbskill、Science Superpowers、Trellis、Decapod、Codex、Obsidian、repo-harness 等。但它们多数只是“被安装 / 被理解 / 被记录”，并没有变成日常默认调用动作。

本页用新的 **Framework · Pattern · Instance** 框架回答：

> 已安装项目如何从“资产”变成“被正确调用的工作流组件”？

核心结论：

> 不是把旧项目塞进新框架，而是给每个旧项目补齐 **Framework 定位 → Pattern 触发 → Instance 配置 → 验证证据** 四步。

---

## 1. 旧问题：项目安装了，但没有被调用

旧框架的问题不在“层级错了”，而在于它停在了概念映射：

```text
⓪ 意图发现 → ① dbs → ② Science Superpowers → ③ Hermes → ④ Decapod → ⑤ Codex → ⑥ Decapod → ⑦ Trellis/Obsidian → ⑧ 学习闭环
```

这张图说明了“应该有哪些层”，但没有说明：

- 用户哪句话触发哪个项目？
- 输入文件从哪里来？
- 输出文件写到哪里？
- 哪个项目是机制，哪个是模式，哪个只是实例配置？
- 失败怎么处理？
- 验证通过的证据是什么？

所以它容易变成：

```text
知道项目存在 ≠ 日常会调用
知道项目定位 ≠ 有可执行入口
有一次 demo ≠ 成为默认机制
```

---

## 2. 新框架下的激活公式

每个旧项目必须补齐这张卡，才算“进入新框架”：

```text
Framework Card
├── 它提供什么机制？
├── 由哪些自然语言触发？
├── 参与哪些 Pattern？
├── 在 Instance 里需要哪些配置？
├── 输出什么工件？
├── 如何验证？
└── 沉淀到哪里？
```

换句话说：

| 旧做法 | 新做法 |
|---|---|
| “装了 Trellis” | Trellis = task lifecycle Framework；工程任务默认生成 task/prd/design/verify |
| “装了 Decapod” | Decapod = governance Framework；代码修改默认进入 orientation/worktree/validate |
| “有 Obsidian” | Obsidian = persistence Framework；稳定知识和 hot/log 有明确分流 |
| “Codex 能写代码” | Codex = execution Framework；只能接收边界清楚的 Instance |
| “dbskill 能诊断” | dbskill = fast routing Framework；模糊商业/内容/行动问题先分诊 |

---

## 3. 旧项目 → 新框架映射表

| 旧项目/能力 | 新框架中的身份 | 应触发的 Pattern | 默认触发句式 | 输出工件 | 验证方式 |
|---|---|---|---|---|---|
| Hermes | Framework：宿主/总控/上下文 | Progressive Disclosure, State Outside Context | “继续推进 / 帮我判断 / 接着上次” | 路由决策、最终汇报、hot/log 更新 | 工具调用记录 + 文件读回 |
| dbskill | Framework：快速分诊 | Intent Triage | “我有个商业/内容/行动问题” | 诊断状态、问题说明书 | 是否输出可执行下一步 |
| Science Superpowers | Framework：深度方法论 | Preregister → Verify, Red Team | “需要严谨分析 / 验证结论 / 不想拍脑袋” | framing、prior work、analysis plan、verification report | 是否先锁定假设再验证 |
| Trellis | Framework：任务生命周期 | Plan-Act-Verify, State Outside Context | “变成项目 / 长任务 / 需要 PRD” | task.json、prd.md、design.md、verify.md | task 文件完整 + 验收表 |
| Decapod | Framework：治理/证明 | Decapod Governance Loop | “要改代码 / 多 agent / 需要 proof” | todo、orientation、worktree、validate proof | decapod validate / proof gate |
| Codex | Framework：实现 | Act under bounded Instance | “执行实现 / 修 bug / 写代码” | diff、测试输出、实现说明 | 测试/脚本真实运行 |
| ObsidianVault | Framework：知识沉淀 | Persist, Learning Loop | “写入知识库 / 保存这次认知 / 下次接上” | source/note/index/hot/log | read-back + search |
| repo-harness | Framework：交接/恢复 | Handoff, Clean-Context Continuation | “多 agent 接力 / 恢复上下文 / 长任务交接” | resume.md、checks、events | handoff 文件存在 + 可读 |
| STORM | Pattern/方法，不是独立 Framework | Multi-perspective Scan | “多角度看 / 帮我找矛盾” | 视角扫描、矛盾地图、综合简报 | 是否产生反例和矛盾 |
| 外部 AI 协商层 | Pattern/外部评审通道 | Planner/Evaluator Split | “让 GPT/Claude 批评 / 补盲” | 外部 AI 问题包、回收表 | 是否回收并筛选观点 |

---

## 4. 真正要做的不是“再整理一遍”，而是做 Project Activation

旧项目要被调用起来，需要分 5 批激活。

### Batch 1：入口激活

目标：让自然语言能进入正确项目，而不是靠临场猜。

交付物：`docs/ROUTING_MATRIX.md`

最小内容：

| 用户说法 | 判型 | Framework | Pattern | 是否需要确认 |
|---|---|---|---|---|
| “我有个想法” | idea-intake | Hermes + dbskill + Obsidian | Intent Triage | 通常需要 |
| “变成项目” | projectization | Trellis + Obsidian | Plan-Act-Verify | 需要 |
| “执行吧” | implementation | Codex + Decapod | Governance Loop | 视副作用 |
| “保存下来” | persistence | Obsidian | Persist | 不一定 |

### Batch 2：能力卡激活

目标：每个项目都有一张 AI 可读卡。

交付物：`docs/frameworks/*.md`

每张卡包含：

```markdown
# Framework Card: Trellis

## Role
## Trigger phrases
## Inputs
## Outputs
## Patterns
## Instance fields
## Verification
## Failure modes
```

### Batch 3：Pattern 激活

目标：不只列 Pattern，而是写清“什么时候必须用”。

交付物：补强 `docs/PATTERNS.md`

重点补：

- Intent Triage
- Framework Activation
- Handoff
- Planner/Evaluator Split
- Multi-perspective Scan
- Human Approval Checkpoint

### Batch 4：Instance 激活

目标：选 1 个真实项目，不再停在 demo。

建议第一个真实 Instance：

```text
loop-control-plane-self-activation
```

它自己的目标就是：

> 用本仓库的新框架，反过来激活旧 8 层项目。

交付物：

```text
examples/instances/loop-control-plane-self-activation.json
```

### Batch 5：证据层激活

目标：每次调用一个项目，都留下证据。

交付物：

```text
docs/ACTIVATION_CHECKLIST.md
```

必须检查：

- 是否真的调用了对应项目？
- 是否产生了该项目应有输出？
- 是否有验证结果？
- 是否沉淀到正确真源？
- 是否回写 Learning Loop？

---

## 5. 用新框架推进“把旧项目调用起来”这个想法

这个想法本身应该被建成一个 Instance，而不是继续停留在讨论。

### Instance 名称

```text
legacy-project-activation
```

### Framework 选择

| Framework | 是否启用 | 原因 |
|---|---|---|
| Hermes | ✅ | 负责总控、读取上下文、最终判断 |
| ObsidianVault | ✅ | 旧协议和项目理解真源在知识库 |
| GitHub loop repo | ✅ | 新控制面要版本化维护 |
| Trellis | ✅ 下一步 | 需要把激活做成任务生命周期 |
| Decapod | ⚠️ 代码修改时启用 | 当前主要是文档；未来改脚本/集成时启用 |
| Codex | ⚠️ 批量生成/重构时启用 | 当前 Hermes 可直接完成文档；批量化时交给 Codex |
| dbskill | ⚠️ 需求不清时启用 | 当前意图已经清楚，不必强行诊断 |
| Science Superpowers | ⚠️ 做验证研究时启用 | 当前不是数据/统计 claim |

### Pattern 选择

| Pattern | 是否启用 | 原因 |
|---|---|---|
| Plan-Act-Verify | ✅ | 每次激活都要有验收 |
| State Outside Context | ✅ | 状态写入 repo/docs，不靠聊天记忆 |
| Framework Activation | ✅ | 本任务核心 Pattern |
| Learning Loop | ✅ | 激活经验要回写规则 |
| Human Approval Checkpoint | ✅ | 涉及外部推送/删除/生产变更时需要 |
| Decapod Governance Loop | 暂不启用 | 当前不是代码实现任务 |

### Design Axes

| Axis | 本 Instance 选择 |
|---|---|
| topology | single-agent 起步，后续可 multi-agent |
| coordination | orchestration，由 Hermes 主导 |
| session_span | multi-session |
| control_loop | Plan-Execute-Verify-Learn |
| autonomy | approval-required |
| execution_isolation | docs-only 阶段无需 worktree；代码阶段用 Decapod worktree |
| memory | long-term-file：GitHub docs + Obsidian hot/log |
| verification | computational + read-back |
| compaction | sliding-window：每轮读激活文档和 Instance |
| tool_type | workflow + verify |

---

## 6. 推荐下一步执行顺序

### P0：先把“怎么调用旧项目”写成控制面文档

已由本页完成初版。

### P1：补路由矩阵

创建：

```text
docs/ROUTING_MATRIX.md
```

目标：用户自然语言 → Framework / Pattern / Instance 的默认路由。

### P2：补 Framework Cards

创建：

```text
docs/frameworks/hermes.md
docs/frameworks/trellis.md
docs/frameworks/decapod.md
docs/frameworks/codex.md
docs/frameworks/obsidian.md
docs/frameworks/dbskill.md
docs/frameworks/science-superpowers.md
docs/frameworks/repo-harness.md
```

### P3：建立真实 Instance

创建：

```text
examples/instances/legacy-project-activation.json
```

这个 Instance 专门跟踪“旧项目激活”任务。

### P4：选择一个真实项目试跑

不要先全量自动化。先选一个最有价值、低风险的项目：

```text
Trellis + Obsidian + GitHub loop repo
```

跑通：

```text
用户想法 → 路由矩阵 → Trellis task → 文档改动 → verify.py → GitHub push → Obsidian hot/log → Learning Loop
```

### P5：再接 Decapod + Codex

当进入代码/脚本/自动化层时，再启用：

```text
Decapod todo/orientation/worktree/validate + Codex implementation
```

---

## 7. 判断标准：什么叫“旧项目真的被调用起来”

一个项目从“已安装”变成“已激活”，至少满足：

- [ ] 有 Framework Card；
- [ ] 有自然语言触发句；
- [ ] 有输入/输出定义；
- [ ] 有参与的 Pattern；
- [ ] 有 Instance 配置字段；
- [ ] 有真实调用样本；
- [ ] 有验证证据；
- [ ] 有沉淀位置；
- [ ] 有失败模式记录。

低于这个标准，只能叫“资产已记录”，不能叫“工作流已调用”。

---

## 8. 本页结论

对你这个想法，新框架下的正确做法是：

```text
不要再问旧框架里哪个项目重要；
而是把每个旧项目做成 Framework Card，
把自然语言触发写成 Routing Matrix，
把调用组合写成 Instance，
每次调用必须留下验证和沉淀。
```

最终目标：

```text
资产清单 → Framework Cards → Routing Matrix → Instance Registry → Verified Runs → Learning Loop
```

这才是“旧项目在新框架里真正用起来”。
