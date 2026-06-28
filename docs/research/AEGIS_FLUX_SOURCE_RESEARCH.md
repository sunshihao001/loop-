---
title: Aegis Flux 源码级架构研究报告
status: complete (第9-10章因消息长度截断，核心1-8章完整)
created: 2026-06-28
source: github.com/FamilOrujov/multi-agent-hedgefund
research_by: subagent deleg_c7553424
---

# Aegis Flux 源码级架构研究报告

## 第一章 Agent 基类设计

### 1.1 接口结构

`BaseAgent(ABC)` 定义在 `src/agents/base.py`，是所有 agent 的抽象基类：

```python
class BaseAgent(ABC):
    def __init__(self, ollama_client, model=None, temperature=None):
        self.ollama_client = ollama_client
        self.model = model
        self.temperature = temperature
        self._llm = None  # 懒加载

    @property
    @abstractmethod
    def name(self) -> str: ...        # agent 标识符

    @property
    @abstractmethod
    def role(self) -> str: ...        # 角色描述

    @property
    @abstractmethod
    def system_prompt(self) -> str: ...  # 系统提示词

    @property
    def llm(self) -> ChatOllama:
        if self._llm is None:
            self._llm = self.ollama_client.get_llm(model=self.model, temperature=self.temperature)
        return self._llm

    def invoke(self, user_message, context=None) -> str:
        messages = [SystemMessage(content=self._build_system_prompt(context)),
                    HumanMessage(content=user_message)]
        response = self.llm.invoke(messages)
        return response.content

    def _build_system_prompt(self, context=None) -> str:
        base_prompt = self.system_prompt
        if context:
            context_str = "\n\n## Current Context:\n"
            for key, value in context.items():
                context_str += f"- **{key}**: {value}\n"
            return base_prompt + context_str
        return base_prompt

    @abstractmethod
    def analyze(self, state: dict[str, Any]) -> dict[str, Any]: ...
```

### 1.2 关键设计点

- **system prompt 注入方式**：每个子类通过 `@property system_prompt` 返回静态角色定义。`_build_system_prompt()` 在基础 prompt 后追加 `## Current Context` 段落，将 context dict 键值对格式化注入。「静态角色定义 + 动态上下文拼接」模式。
- **analyze() 方法签名**：`analyze(self, state: dict) -> dict`，接收整个状态字典，返回更新后的状态字典。遵循 `return {**state, "new_field": value}` 模式，保证状态不丢失。
- **LLM 懒加载**：通过 `@property llm` 懒加载，首次访问时创建 `ChatOllama` 实例，之后缓存。
- **temperature 分层**：DataScout/Technical/Fundamental/Sentiment 用 0.3（偏事实分析），PortfolioManager 用 0.4，辩论用 0.6-0.7。

---

## 第二章 各 Agent 的 System Prompt

### 2.1 Data Scout（数据侦察）

```
You are the Data Scout agent in a hedge fund analysis team.

Your responsibilities:
1. Fetch and organize raw financial data from various sources
2. Retrieve historical price data, volume, and basic metrics
3. Gather recent news and announcements related to the ticker
4. Compile company information and key statistics

You provide factual, well-organized data summaries without making investment recommendations.
Focus on accuracy and completeness of data retrieval.

When presenting data:
- Use clear formatting with sections
- Include data timestamps and sources
- Flag any missing or unavailable data
- Highlight unusual patterns in raw data (e.g., volume spikes)
```

**设计意图**：DataScout 被严格限定为「只提供事实，不做推荐」。第4条「Highlight unusual patterns」暗示数据预筛功能，类似 meme 项目的证据包预检。

### 2.2 Technical Analyst（技术分析师）

```
You are the Technical Analyst agent in a hedge fund analysis team.

CRITICAL: You will be provided with REAL-TIME technical insights fetched from the web.
Use this provided data to supplement your indicator-based analysis.

Your responsibilities:
1. Calculate and interpret technical indicators (RSI, MACD, Bollinger Bands, etc.)
2. Identify chart patterns and trend directions
3. Determine support and resistance levels
4. Provide technical-based trading signals
5. Incorporate REAL-TIME market insights when available

Output format:
- Current trend direction
- Key indicator readings with interpretation
- Technical signal (Bullish/Bearish/Neutral) with confidence
- Key price levels to watch
```

**设计意图**：开头 `CRITICAL` 强调必须使用 web 获取的实时数据而非训练数据，防止 LLM 幻觉。输出格式强制要求带 confidence 的三值信号。

### 2.3 Fundamental Analyst（基本面分析师）

```
You are the Fundamental Analyst agent in a hedge fund analysis team.

CRITICAL: You will be provided with REAL-TIME market research data fetched from the web.
You MUST use this provided research as your PRIMARY source of information.
DO NOT rely on your training data for recent events, earnings, or market conditions.

Your responsibilities:
1. Analyze financial statements (income statement, balance sheet, cash flow)
2. Calculate and interpret key financial ratios
3. Assess company valuation metrics (P/E, P/B, EV/EBITDA, etc.)
4. Evaluate long-term financial health and growth prospects
5. Use the PROVIDED market research for current context

Output format:
- Financial health score (Strong/Moderate/Weak)
- Key metrics with interpretation
- Valuation assessment (Undervalued/Fair/Overvalued)
- Fundamental signal (Bullish/Bearish/Neutral) with reasoning
```

**设计意图**：双重防幻觉约束（`CRITICAL` + `DO NOT rely on your training data`）。基本面数据时效性最强，最强调「不要用训练数据」。

### 2.4 Sentiment Analyst（情绪分析师）

```
You are the Sentiment Analyst agent in a hedge fund analysis team.

CRITICAL: You will be provided with REAL-TIME news and sentiment data fetched from the web.
You MUST use this provided data as your PRIMARY source of information.

Your responsibilities:
1. Analyze news headlines and articles for sentiment
2. Gauge retail and institutional sentiment
3. Identify sentiment trends and shifts
4. Detect potential catalysts from news flow

Output format:
- Sentiment score with confidence
- Key themes summary from REAL-TIME news
- Catalyst identification
- Sentiment signal (Bullish/Bearish/Neutral)
```

**设计意图**：输出数值化 sentiment_score (-1.0~+1.0)，用正则解析作为信号判定依据。

### 2.5 Portfolio Manager（组合经理/决策综合）

```
You are the Portfolio Manager facilitating a hedge fund analysis team discussion.

You speak on behalf of the TEAM, not as an individual. Always use "We" not "I".

Your responsibilities:
1. Synthesize reports from Technical, Fundamental, and Sentiment analysts
2. Facilitate discussion to resolve disagreements
3. Present the TEAM's collective investment decision
4. Provide clear reasoning based on team consensus

Your output must include:
- Final Decision: BUY / SELL / HOLD (as a TEAM decision)
- Confidence Score: 0-100%
- Position Size Recommendation: Conservative / Moderate / Aggressive
- Key Reasoning: Why WE (the team) made this decision
- Risk Factors: What could go wrong
- How consensus was reached or dissenting views

IMPORTANT: Always say "We have decided" or "The team recommends" - NEVER "I have decided".
This is a collaborative multi-agent decision, not an individual one.
```

**设计意图**：强制使用「We」而非「I」，将 Portfolio Manager 定位为**团队代言人**而非独立决策者。最终决策表述中嵌入多 agent 协作痕迹，增强可审计性。

---

## 第三章 State Schema

### 3.1 状态字段定义

| 字段 | 类型 | 写入者 | 读取者 | 用途 |
|------|------|--------|--------|------|
| `ticker` | str | 初始化 | 所有 agent | 输入标的 |
| `price_data` | dict | DataScout | Technical | 原始价格数据 |
| `company_info` | dict | DataScout | Fundamental, Sentiment | 公司信息 |
| `financials` | dict | DataScout | Fundamental | 财务报表 |
| `news_data` | list[str] | DataScout | Sentiment | 新闻标题 |
| `market_research` | dict | DataScout | 所有 analyst | **深度市场研究(核心分发字段)** |
| `technical_signal` | dict | Technical, Debate | PM, Guardrails | 技术信号 |
| `fundamental_signal` | dict | Fundamental, Debate | PM, Guardrails | 基本面信号 |
| `sentiment_signal` | dict | Sentiment, Debate | PM, Guardrails | 情绪信号 |
| `manager_decision` | dict | PortfolioManager | Guardrails | **最终决策(含confidence/decision/position_size)** |
| `iteration_count` | int | PM(refine节点) | should_continue | **迭代计数器(循环控制)** |
| `requires_human_review` | bool | Guardrails | should_continue | **HITL触发标记** |
| `review_triggers` | list | Guardrails | human_review | 审查触发原因列表 |
| `consensus_reached` | bool | Debate | PM | **共识是否达成** |
| `consensus_decision` | str | Debate | PM | **共识决策** |
| `debate_history` | list | Debate | 报告 | 辩论历史 |
| `human_feedback` | str | refine节点 | Technical(回环) | 精炼反馈 |

### 3.2 状态流转路径

```
初始化 → [ticker, analysis_depth, iteration_count=0, ...空字段]
    ↓
DataScout 写入: price_data, company_info, financials, news_data, market_research
    ↓
Technical 读取: price_data, market_research → 写入: technical_signal, technical_analysis
Fundamental 读取: company_info, financials, market_research → 写入: fundamental_signal
Sentiment 读取: company_info, news_data, market_research → 写入: sentiment_signal
    ↓
[Debate 读取: 三个signal + analysis → 写入: consensus_reached, consensus_decision]
    ↓
PortfolioManager 读取: 所有signal + consensus → 写入: manager_decision, iteration_count+1
    ↓
Guardrails 读取: manager_decision, signals → 写入: requires_human_review, review_triggers
    ↓
should_continue → human_review / refine / end
```

### 3.3 关键设计：market_research 作为分发中心

DataScout 一次性获取5类研究数据，写入 `state["market_research"]`，所有下游 agent 从这个字段读取自己需要的数据。避免每个 agent 各自调用 API 导致重复查询。

```python
research = {
    "technical_insights": "",      # → 给 Technical Analyst
    "fundamental_research": "",    # → 给 Fundamental Analyst
    "sentiment_sources": "",       # → 给 Sentiment Analyst
    "risk_factors": "",            # → 给 Portfolio Manager
    "competitor_analysis": "",     # → 给 Fundamental Analyst
}
```

---

## 第四章 工作流编排

### 4.1 LangGraph 图结构

```
data_scout → technical_analyst → fundamental_analyst → sentiment_analyst
    → portfolio_manager → guardrails
        → [conditional] → human_review → finalize → END
                        → refine → technical_analyst (回环)
                        → finalize → END
```

```python
graph = StateGraph(dict)
graph.add_node("data_scout", data_scout_node)
graph.add_node("technical_analyst", technical_node)
graph.add_node("fundamental_analyst", fundamental_node)
graph.add_node("sentiment_analyst", sentiment_node)
graph.add_node("portfolio_manager", manager_node)
graph.add_node("guardrails", guardrails_node)
graph.add_node("human_review", human_review_node)
graph.add_node("refine", refine_node)
graph.add_node("finalize", finalize_node)

graph.set_entry_point("data_scout")
graph.add_edge("data_scout", "technical_analyst")
graph.add_edge("technical_analyst", "fundamental_analyst")
graph.add_edge("fundamental_analyst", "sentiment_analyst")
graph.add_edge("sentiment_analyst", "portfolio_manager")
graph.add_edge("portfolio_manager", "guardrails")

graph.add_conditional_edges("guardrails", should_continue, {
    "human_review": "human_review",
    "refine": "refine",
    "end": "finalize",
})
graph.add_edge("human_review", "finalize")
graph.add_edge("refine", "technical_analyst")  # ← 回环!
graph.add_edge("finalize", END)
```

### 4.2 条件路由逻辑

```python
def should_continue(state) -> Literal["human_review", "refine", "end"]:
    confidence = state.get("manager_decision", {}).get("confidence", 0)
    iteration_count = state.get("iteration_count", 0)
    max_iterations = state.get("max_iterations", 5)
    requires_review = state.get("requires_human_review", False)

    if iteration_count >= max_iterations: return "end"        # 达到最大迭代
    if requires_review and enable_hitl: return "human_review" # 护栏触发
    if confidence >= 75: return "end"                          # 高置信度自动通过
    if confidence >= 50: return "end"                          # 中置信度结束
    return "refine"                                            # 低置信度回环
```

### 4.3 循环回环实现

回环路径：`guardrails → refine → technical_analyst → ... → guardrails`

```python
def refine_node(state):
    feedback = portfolio_manager.get_critique_feedback(state)
    state["human_feedback"] = feedback  # 传递具体改进方向
    state["iteration_count"] += 1
    return state

def get_critique_feedback(self, state) -> str:
    if not aggregation.get("has_consensus"):
        return "The analysts have conflicting views. Please re-examine the data..."
    if decision.get("confidence", 0) < 60:
        return "The confidence level is too low. Please gather additional data..."
    return "Analysis needs refinement. Please review and strengthen your conclusions."
```

回环不是简单重跑——通过 `human_feedback` 传递**具体改进方向**，迭代计数器最多5轮强制结束。

### 4.4 重要发现：辩论不在主图中

辩论仅在 `workflow_streaming.py` 中实现。主图通过 `refine→technical_analyst` 回环替代辩论。**meme 版本应把辩论放进主图。**

---

## 第五章 辩论/共识机制（核心！）

### 5.1 辩论触发条件

```python
signals = [tech_sig, fund_sig, sent_sig]
has_conflict = len(set(signals)) > 1  # 三个信号不全相同
if has_conflict:
    # 启动辩论
else:
    state["consensus_reached"] = True
    state["consensus_decision"] = signals[0]
```

### 5.2 AgentDebate 类

```python
class AgentDebate:
    def __init__(self, ollama_client):
        self.llm = ollama_client.get_llm(temperature=0.6)  # 辩论用较高温度
        self.debate_history = []
        self.max_rounds = 5
```

### 5.3 辩论流程（每轮3阶段）

**阶段A：各 agent 陈述论点**

```python
prompt = f"""You are the {agent_name} in a hedge fund team debating about {ticker}.
Assigned signal to argue: {position}
Your analysis summary: {analysis[:500]}
Previous debate points: {history[-2:] if history_text else "First round."}

IMPORTANT:
- If real-time market data is provided, CITE IT in your argument.
- Argue for the {position} case in 3-5 sentences. Keep it balanced.
- Speak in first person ("I analyzed", "My conclusion").
- If you see strong counter-arguments, you may acknowledge them.
- Focus on the strongest evidence supporting this view."""
```

关键：只取最近2轮历史（避免上下文爆炸）；每个 agent 获取对应类型的 market_research 数据。

**阶段B：立场评估**

```python
prompt = f"""Based on the following debate about {ticker}, determine if any analyst should change their position.
...
Only change a position if there's a strong reason.
Analysts tend to hold their views unless convinced."""
```

**惯性约束**——最后一句防止 agent 轻易动摇，确保只有真正有力的论据才能改变立场。

**阶段C：收敛检查**

```python
if len(set(positions)) == 1:
    return {**state, "consensus_reached": True, "consensus_decision": positions[0]}
```

### 5.4 最大轮次后多数投票

```python
final_decision = self._majority_vote(tech_pos, fund_pos, sent_pos)
return {**state, "consensus_reached": False, "consensus_decision": final_decision, "majority_vote": True}
```

### 5.5 共识影响 PortfolioManager

```python
if consensus_decision == "Bullish":
    decision = "BUY"
    confidence = 75 if state.get("consensus_reached") else 65  # 共识75%, 多数65%
```

共识决策置信度75%（自动通过阈值边缘），多数投票65%。

---

## 第六章 HITL 护栏（核心！）

### 6.1 GuardrailConfig 默认配置

```python
@dataclass
class GuardrailConfig:
    min_confidence_for_auto_approve: float = 0.75    # 自动通过阈值
    min_confidence_for_action: float = 0.50           # 可行动阈值
    max_position_size_auto: str = "Moderate"           # 最大自动仓位
    volatility_threshold: float = 3.0                  # 波动率阈值
    require_consensus_for_auto: bool = True            # 自动通过需共识
    min_agreeing_signals: int = 2                      # 最少同意信号数
    always_review_decisions: list[str] = ["SELL", "STRONG_SELL"]  # 必审决策
```

### 6.2 五类检查

| 检查 | 触发条件 | 严重度 |
|---|---|---|
| 置信度 | <50%严重(不通过)，50-75%需审查 | warning/info |
| 信号一致性 | 多空同时出现/同意数<2 | warning |
| 仓位大小 | >Moderate | warning |
| 决策类型 | SELL/STRONG_SELL必审 | info |
| 波动率 | High volatility | warning |

### 6.3 中断工作流等待人工

```python
def human_review_node(state):
    review_request = hitl_manager.create_review_request(state)
    state["pending_review_id"] = review_request["review_id"]
    state["status"] = "awaiting_review"
    return state
```

LangGraph MemorySaver checkpointer 在 `human_review` 节点暂停。`HITLManager.submit_review()` 允许人工提交（批准/拒绝/修改），之后恢复执行。

### 6.4 ReviewTrigger 枚举（7种触发器）

```python
class ReviewTrigger(Enum):
    LOW_CONFIDENCE = "low_confidence"
    HIGH_RISK = "high_risk"                     # SELL必审
    CONFLICTING_SIGNALS = "conflicting_signals"
    LARGE_POSITION = "large_position"
    VOLATILE_MARKET = "volatile_market"
    UNUSUAL_PATTERN = "unusual_pattern"
    DATA_QUALITY = "data_quality"
```

---

## 第七章 数据采集层

### 7.1 DataScout 双数据源

- **FinancialDataAggregator (yfinance)**：价格/公司信息/估值/财务报表/分析师推荐
- **TavilyClient (Web研究)**：5类深度研究（技术/基本面/情绪/风险/竞争对手）

### 7.2 域名白名单

```python
# 新闻搜索限定权威财经媒体
include_domains=["reuters.com", "bloomberg.com", "cnbc.com", "wsj.com", ...]
# 情绪搜索限定社交平台
include_domains=["reddit.com", "twitter.com", "stocktwits.com", ...]
```

### 7.3 数据降级策略

优先使用 DataScout 分发的 market_research，不可用时 fallback 直接调用 Tavily 工具。

---

## 第八章 本地 LLM 集成

- **完全本地**：所有 LLM 调用走 Ollama，零 API 费用
- **懒加载**：`_llm` 属性首次使用时创建
- **单例缓存**：`@lru_cache` 避免重复实例化
- **temperature 分层**：事实分析0.3，辩论0.6-0.7
- **内容截断**：多处 `[:500]`/`[:1500]` 控制 prompt 长度

---

## 第九章 可审计输出

> 注：原报告此章因消息长度截断，以下为摘要补充

PDF报告结构：封面(决策+置信度) → 执行摘要 → 数据概览 → 各分析师报告 → 辩论记录 → 最终决策 → 风险因素 → 附录。推理链通过 state 字段完整追踪（每个 agent 的 signal/analysis/debate_history 都保留）。

---

## 第十章 meme Paper-Only 映射建议

### 10.1 HITL 护栏 → meme 拒绝门禁 + Paper-Only 边界

| Aegis Flux | meme 映射 |
|---|---|
| 置信度<50% → 不通过 | 证据包 INSUFFICIENT/EMPTY → DROP |
| 置信度50-75% → 需审查 | 证据包 PARTIAL → NEED_MORE_EVIDENCE |
| 置信度≥75% → 自动通过 | 证据包 COMPLETE → PAPER_REVIEW |
| SELL必审 | PAPER_LONG_CONDITIONALLY 必审（附带失效条件清单） |
| 信号冲突 → 需审查 | 多策略Agent分歧 → 触发辩论 |
| 波动率检查 | meme: 流动性检查（池子深度/滑点） |
| 仓位大小检查 | meme: 不适用（Paper-Only无仓位）→ 替换为风险等级检查 |

### 10.2 辩论共识 → meme 多空对抗

| Aegis Flux | meme 映射 |
|---|---|
| 技术/基本面/情绪3分析师辩论 | FCZ结构/资金流/情绪热度多策略Agent辩论 |
| Bullish/Bearish/Neutral 三值信号 | FAVORABLE/UNFAVORABLE/NEUTRAL 结构判断 |
| 5轮辩论+惯性约束 | 同样5轮+惯性约束（agent不轻易动摇） |
| 多数投票(65%) vs 共识(75%) | 多数→WATCH，共识→PAPER_REVIEW |
| debate_history 保留 | 完整推理链可审计 |

### 10.3 循环回环 → meme 验证门禁 + 学习闭环

| Aegis Flux | meme 映射 |
|---|---|
| refine节点传递human_feedback | 验证门禁传递"缺失证据类型" |
| 迭代计数器max 5 | 同样max 5，防止无限循环 |
| 低置信度回环 | 证据不足回环补充数据 |
| 信号冲突回环 | 多策略分歧回环重新分析 |
| — | 学习闭环：每轮回写08_LEARNING_LOOP |

### 10.4 架构差距与改进建议

1. **辩论应放进主图**（Aegis Flux 只在流式版本有，主图用 refine 回环替代）
2. **meme 需要多策略Agent可扩展**（Aegis Flux 固定3个分析师，meme 需要可加新策略Agent）
3. **meme 输出不固定买卖**（Aegis Flux 输出 BUY/SELL/HOLD，meme 输出 nuanced 判断推理）
4. **meme 数据源不同**（Aegis Flux 用 yfinance+Tavily，meme 用 GMGN/Helius/DexScreener）
5. **meme 无仓位概念**（Paper-Only，用风险等级替代仓位大小）
