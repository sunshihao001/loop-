# Fuzzy Input Research Routing Audit

## Purpose

This document promotes the Obsidian-side `研究工具工作流化与模糊表达路由审计` into the repo control-plane.

Its purpose is to answer a stricter question than “what research tools are installed?”

The real question is:

> When the user only provides a vague idea, a partial concept, or a direction-feel, can Hermes actually route that natural-language input into the right research tools, and which tools have truly been workflowized versus merely installed?

---

## The Three-Level Standard

A research tool should be judged on three levels:

1. **Installed** — the tool or package exists locally.
2. **Routable** — the workflow docs define where it belongs.
3. **Workflowized** — vague natural language can reliably trigger it, produce a meaningful artifact, and land in a verification + persistence path.

Repo control should care mostly about level 3.

---

## The Real Failure Being Audited

The current risk is not only “missing tools”.

The deeper failure is:

- the user often does not start with a well-formed research question;
- the user may provide only a concept fragment or discomfort signal;
- if Hermes asks the user to finish the research question first, the workflow breaks at the entry layer.

So the correct requirement is:

> Hermes must perform first-pass intent inference itself before deciding whether to route to `dbs`, `STORM`, `anysearch`, `delegate_task`, external AI, `Science Superpowers`, or `grill-with-docs`.

---

## Current Activation Audit

### A. Already workflowized

| Tool / package | Natural-language trigger | Current role | Why it counts as workflowized |
|---|---|---|---|
| `dbs` / `dbskill` | “我有个研究想法”, “这个能不能做”, “我说不清但想研究这个” | question clarification / triage | stable trigger, clear output, clear next-hop |
| `STORM` | “多角度看看”, “先看全景”, “找矛盾” | perspective scan | stable trigger, contradiction output, persisted synthesis |
| `anysearch` / `agent-reach` | “查现成方案”, “搜各个平台相关资料”, “全网调研” | source baseline | stable fetch layer with source persistence |
| external AI consultation | “让 GPT/Claude 批评一下”, “找外部模型讨论” | heterogenous challenge | stable review loop with recovery + filtering |
| Obsidian persistence | “写进知识库”, “先入库再推进”, “保存这个认知” | durable knowledge sink | stable persistence target with read-back |

### B. Integrated, but not fully workflowized

| Tool / package | Current role | What is still missing |
|---|---|---|
| `delegate_task` | structured debate layer | more frequent natural-language triggering from real samples |
| `Science Superpowers` | claim-grade validation layer | more real-run examples where a vague research intent climbs into verification |
| `grill-with-docs` | protocol / plan interrogation layer | stronger automatic recognition of “this needs grilling” from user language |

### C. Installed, but not truly active in the research NL chain

| Tool / project | Current state | Why it is not counted as active |
|---|---|---|
| `twitter-cli` | installed, auth incomplete | not a stable default input path |
| `mem0` | installed, optional memory candidate | not part of the main research routing chain |
| `Decapod` (research-side) | important for repo governance | not a primary research-intake tool |
| `FastNodeSync-CLI` / FNS sync path | verified transport layer | useful for sync, not for research routing |

---

## Required Entry Behavior

When the user provides only:

- a vague idea,
- a broad concept,
- a half-sentence,
- a “this feels off” signal,
- a not-yet-formed research direction,

Hermes must do the following before asking the user to clarify:

1. generate candidate interpretations;
2. generate candidate boundaries;
3. generate candidate next hops;
4. only ask the user to choose when the candidate routes would lead to materially different workflows.

This is the correct control-plane behavior for fuzzy-input research routing.

---

## Default Next-Hop Logic

```text
vague idea / concept fragment
→ Hermes Stage 0 inference
→ candidate question packet
→ choose first hop
   - dbs          if the problem is not yet a problem statement
   - STORM        if the problem needs a quick landscape view
   - anysearch    if the problem already needs external source material
   - delegate_task if baseline understanding exists and blind-spot testing is needed
   - external AI  if same-model blind spots matter
   - Science Superpowers if the result is climbing toward a claim
   - grill-with-docs if the target is a draft protocol or plan text
```

---

## Repo-Level Meaning

This document changes the standard for adoption.

A research tool should not be considered “in use” merely because:

- it is installed;
- it appears in notes;
- it has a place in the abstract protocol.

It should count as “in use” only when:

- user natural language can trigger it through Hermes routing;
- the output is verifiable;
- the result lands in a durable sink;
- the route has survived a real sample.

---

## Relationship to Other Repo Documents

- `docs/RESEARCH_TOOL_ROUTING_PROTOCOL.md` defines the escalation order of research tools.
- `docs/ROUTING_MATRIX.md` maps natural language to repo frameworks and patterns.
- this document audits whether those routes are actually alive under fuzzy user input.

Together they answer three different questions:

1. **What is the intended route?**
2. **When should each research tool be used?**
3. **Which ones are actually alive in real natural-language use?**
