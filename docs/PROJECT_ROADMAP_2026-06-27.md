# 项目路线地图：从基础设施到完整循环

> **创建时间**：2026-06-27
> **来源**：综合三个来源——当前系统状态、6篇循环文章共识、AI Agent科研范式转变PDF
> **状态**：Phase 0 完成，Phase 1 待执行

## 三个来源的对齐

| 来源 | 核心贡献 | 对路线地图的影响 |
|------|---------|----------------|
| **6篇循环文章** | 4/4共识：Verifier + State外置；3/4共识：Stop Condition + Build Order(Prove→Harden→Automate) + Skill即程序性记忆 + 自动化是最后一步 | 路线地图本身必须遵循 Prove→Harden→Automate 顺序 |
| **AI Agent科研范式转变PDF** | 6步流水线：问题设定→资料理解→并行探索→守门互评→输出筛选→沉淀复用；人负责方向/边界/门槛，AI负责扩展/试跑/互评/回写 | 缺口在"候选发现"和"成本门禁"两个节点 |
| **当前系统** | Codex 25 hooks + Hermes 2 hooks + intent-discovery skill + /sci bundle + forgegod-bridge | 基础设施层已完成，方法论层和验证层未开始 |

## PDF理想流水线 vs 当前8层架构 vs 循环四机关

```
PDF流水线:    Signal → Evidence → Candidate → Adoption → CostGate → Governance → Trial → Validation → Artifact → Learning
                          ↓           ↓                                    ↓                              ↓
8层架构:     ⓪意图发现 → ①dbs → ②Sci.Super → ③Hermes → ④Decapod → ⑤Codex → ⑥Decapod → ⑦Obsidian → ⑧loop
                          ✅         ✅          ⚠️缺候选管理    ✅         ⚠️缺成本门禁   ✅(已被动化)  ✅         ⚠️仅ForgeGod
                          ↓           ↓           ↓              ↓           ↓              ↓              ↓           ↓
循环四机关:  ①状态外置90%  ②读回80%    ④回流写入70%    ③停止判断85%                                              ④回流写入70%
```

**关键发现**：PDF流水线比8层架构多两个节点——**候选发现管理**和**成本门禁**。这两个是当前体系真正缺的，不是基础设施缺的。

## Phase 0：基础设施层 ✅ 已完成

**做了什么**：把已有的显性调用改成被动触发

| 组件 | 循环机关 | 状态 |
|------|---------|------|
| Codex 25 hooks（8事件全覆盖） | ②③ | ✅ |
| Hermes 2 hooks（pre_llm_call + on_session_end） | ②④ | ✅ |
| intent-discovery skill（⓪层） | ⓪ | ✅ |
| /sci bundle（15个研究技能一键加载） | ② | ✅ |
| forgegod-bridge（harvest cron + loop-wrapper inject） | ④ | ✅ |
| hot.md 读回+写回追踪+新鲜度检查 | ②④ | ✅ |

**循环四机关覆盖率**：①90% ②80% ③85% ④70%

**Build Order 状态**：基础设施已 Automate，但从未 Prove（没在真实任务中验证过）

### 基础设施完整清单

#### Codex Hooks（25个，8事件）

| 事件 | Hook 数 | 组成 |
|------|---------|------|
| SessionStart | 3 | repo-harness + ai-memory + decapod-orient |
| PreToolUse | 4 | repo-harness(edit) + repo-harness(subagent) + ai-memory + maxcodex destructive_gate |
| PostToolUse | 4 | repo-harness(edit) + repo-harness(bash) + repo-harness(always) + ai-memory |
| UserPromptSubmit | 3 | repo-harness(default) + repo-harness(delegation) + ai-memory |
| SubagentStart | 1 | repo-harness(context) |
| SubagentStop | 1 | repo-harness(quality) |
| Stop | 8 | repo-harness + ai-memory + novibes_gate + no-phantom-tool-call + no-wrap-up + no-count-drift + no-fake-recall + decapod-validate |
| PreCompact | 1 | ai-memory |

#### Hermes Hooks（2个）

| 事件 | 脚本 | 功能 |
|------|------|------|
| pre_llm_call | hot-md-inject.py | 首次LLM调用注入hot.md前120行 + 新鲜度检查 + stale flag提醒 |
| on_session_end | hot-md-writeback-tracker.py | 检查hot.md是否在本session更新，未更新则设stale flag |

#### Skills & Bundles

| 组件 | 位置 | 功能 |
|------|------|------|
| intent-discovery | skills/routing/ | ⓪层意图发现 + 自动路由到dbs/Sci.Superpowers/Codex/Obsidian |
| /sci bundle | skill-bundles/sci.yaml | 一键加载15个Science Superpowers研究方法论技能 |

#### ForgeGod Bridge

| 组件 | 类型 | 功能 |
|------|------|------|
| harvest.py | cron 6h | 自动回收ForgeGod learnings到Obsidian |
| inject.py | loop-wrapper | forgegod loop前自动注入跨session learnings |
| forgegod-workflow.sh | 完整流程 | plan→inject→loop→harvest一键流程 |

## Phase 1：Real-run 验证 ⬅️ 当前最高优先级

**为什么**：循环文章 3/4 共识说 **Prove → Harden → Automate**。我们跳过了 Prove 直接 Automate。6 篇文章都强调"没有 real-run 的协议不宜升级为默认规则"。

**做什么**：选一个真实任务，完整跑一遍 ⓪→⑧，验证每个被动组件是否真的触发

| 验证项 | 怎么验证 | 成功标准 |
|--------|---------|---------|
| hot.md inject | 新 session 首次 LLM 调用是否自动注入 | 看到注入内容（✅ 已验证） |
| on_session_end writeback | session 结束后 stale flag 是否正确设置/清除 | 标记文件状态正确（✅ 已验证） |
| intent-discovery routing | 发一个模糊输入，看是否自动路由 | AI 主动生成候选理解+路由 |
| Codex SessionStart hooks | 跑 `codex --profile auto` | decapod-orient + ai-memory + repo-harness 全触发 |
| Codex Stop hooks | Codex 完成任务时 | 4 dark-pattern + novibes + decapod-validate 全触发 |
| forgegod-bridge | 跑一次 forgegod loop | inject 自动运行 + harvest 回流 |

**建议验证项目**：用一个真实的小任务（比如给某个项目加一个 feature 或修一个 bug），完整走一遍 ⓪→⑧

## Phase 2：方法论缺口补全

**为什么**：PDF 研究综合识别出 5 个协议缺口。这些不是基础设施问题，是"AI 知道怎么做但没有显式协议约束"的问题。

| # | 缺口 | PDF来源 | 循环文章来源 | 优先级 | 解决方式 |
|---|------|---------|-------------|--------|---------|
| 1 | **候选空间生成与收敛** | "先要候选问题" | State Outside Context 的最小字段 | **P0** | 已有草案协议，需 real-run 验证后固化 |
| 2 | **Generate→Critique→Decide Pattern** | "生成段/审查段分裂" | Maker/Checker Split (2/4) | **P0** | 已有草案 Pattern，需日常任务试跑 |
| 3 | **Gate 分级** | "证据链导向" | Verifier 的具体形式分类 (4/4) | P1 | 设计 gate 等级表：理解笔记 < 候选判断 < 路由建议 < 协议升级 < 默认规则 |
| 4 | **成本门禁** | PDF "stop condition + cost gate" | Cost/Risk Awareness (2/4) + Stop Condition (3/4) | P1 | 在 ③Hermes 和 ⑤Codex 层加 budget guard |
| 5 | **多Agent结果回收** | "并行探索默认化"的收敛端 | Branch convergence (隐含) | P2 | 设计多 Agent 输出的比较/冲突/盲区/回写格式 |

**Build Order**：每个协议都先 **Prove**（在一个真实任务中手动执行）→ **Harden**（写成 skill/protocol）→ **Automate**（做成 hook/cron 如果适用）

## Phase 3：通用学习闭环

**为什么**：当前 ⑧ 学习闭环只覆盖 ForgeGod（forgegod-bridge）。Hermes/Codex 日常 session 的经验没有自动回流。循环文章 3/4 共识说 Skill 是程序性记忆，需要生命周期管理（创建→验证→晋级→修剪）。

| # | 缺口 | 当前状态 | 目标 |
|---|------|---------|------|
| 1 | **通用经验回流** | 仅 ForgeGod 有 harvest→inject | Hermes session 结束时自动提取可复用经验 |
| 2 | **Skill 生命周期** | Curator 只管修剪 | 加"创建→验证→晋级"链 |
| 3 | **外部 prior-work** | 内部综合已完成，外部来源缺失 | 补 6-10 个外部 agentic workflow 先例 |
| 4 | **Decapod workspace 被动化** | 仍需显式调用 | 做成 PreToolUse hook |

## 完整路线地图一览

```
Phase 0: 基础设施 ✅ DONE
  Codex 25 hooks + Hermes 2 hooks + intent-discovery + /sci + forgegod-bridge
  循环四机关: ①90% ②80% ③85% ④70%
         ↓
Phase 1: Real-run 验证 ⬅️ NOW
  选一个真实任务，完整跑 ⓪→⑧
  验证每个被动组件是否真的触发
  暴露基础设施层的真实问题
         ↓
Phase 2: 方法论缺口
  P0: 候选空间协议 + GCD Pattern → real-run → 固化
  P1: Gate分级 + 成本门禁 → 设计 → real-run → 固化  
  P2: 多Agent回收协议 → 设计 → real-run → 固化
         ↓
Phase 3: 通用学习闭环
  通用经验回流 + Skill生命周期 + 外部prior-work + 剩余被动化
  循环四机关目标: ①95% ②95% ③95% ④90%
```

## 一句话总结

> **基础设施层（Automate）已完成，但从未在真实任务中 Prove。下一步最高杠杆是选一个真实任务完整跑一遍 ⓪→⑧，暴露真实问题后再补方法论缺口（候选空间 + GCD Pattern）。遵循 Prove→Harden→Automate 顺序，不要跳过验证直接写更多协议。**

## 相关文档

- `docs/WORKFLOW_PROTOCOL.md` — 8层架构完整定义
- `docs/ROUTING_MATRIX.md` — 路由矩阵
- `docs/RESEARCH_TOOL_ROUTING_PROTOCOL.md` — 研究工具路由协议
- `docs/PROTOCOL_CORRECTION_2026-06-27.md` — 协议修正记录
- `docs/RUNTIME_IMMEDIATE_ACTIVATION_PRINCIPLE.md` — 运行时立即生效原则
- Obsidian: `20_Notes/工作流架构修正_意图发现到治理证明.md` — 8层架构主协议
- Obsidian: `20_Notes/AI Agent科研范式转变_x_Hermes工作流_第一轮综合研究.md` — PDF研究综合
- Obsidian: `20_Notes/Loop_Research_Intake_四篇横向综合.md` — 循环文章横向综合
