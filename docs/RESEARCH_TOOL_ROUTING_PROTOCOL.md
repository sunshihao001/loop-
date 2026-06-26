# Research Tool Routing Protocol

## Purpose

This document promotes the Obsidian-side `研究工具路由协议` into the repo control-plane as an engineering-facing routing rule.

It defines when research work should use:

- `dbs`
- `STORM`
- `anysearch`
- `delegate_task`
- external AI consultation
- `Science Superpowers`
- `grill-with-docs`
- real-run verification

The goal is to stop two failure modes:

1. doing shallow search + summary and mistaking it for research;
2. escalating every research request into a heavyweight validation flow.

---

## Core Sequence

```text
Research Request
→ Clarify the question
→ Build a source baseline
→ Produce a single-model baseline understanding
→ Run structured debate when needed
→ Add heterogenous-model challenge when needed
→ Run deep verification when needed
→ Test on a real task before defaulting
→ Promote to repo rule / pattern only after evidence
```

This is an escalation protocol, not a mandatory full pipeline.

---

## Layer A — Clarify the Question

### `dbs`

Use `dbs` first when the request is still vague.

#### Trigger

- User gives only a topic, direction, link, or “continue researching this”.
- We do not yet know whether the target is a concept, method, tool, protocol, or default rule candidate.
- We need to distinguish a lightweight understanding task from a validation task.

#### Output

- A clearer research question.
- A sharper statement of scope.
- An initial guess about whether the task stops at understanding or must climb to validation.

#### Stop condition

Leave `dbs` when we can state the question clearly enough to decide the next tool.

### `STORM`

Use `STORM` after or instead of `dbs` when the question is clear enough, but the landscape is not.

#### Trigger

- We need a quick full-map view before judgment.
- The topic has multiple plausible interpretations.
- The goal is to surface tensions, not yet to prove a claim.

#### Output

- multi-perspective scan
- contradiction map
- candidate hypotheses
- better search targets for the next layer

#### Not for

- final judgment
- claim verification
- replacing intake when no question exists yet

---

## Layer B — Build a Source Baseline

### `anysearch`

Use `anysearch` once the question is defined enough to search deliberately.

#### Trigger

- The answer depends on external posts, articles, docs, papers, or examples.
- We need a sample set or comparison set.
- We would otherwise infer too much from titles or fragments.

#### Output

- source candidates
- extracted materials
- a minimal but sufficient evidence pool for this round

#### Stop condition

Stop expanding sources when:

1. current materials are enough for the current question;
2. newly found materials are no longer changing the structure of the question;
3. we have at least one supportive angle and one skeptical angle.

### Single-model baseline understanding

Before debate or validation, we must create one baseline understanding.

#### Required artifacts

- source note
- understanding note
- uncertainty / access-limit statement

#### Why

- It gives every later layer a common baseline.
- It prevents debate from replacing first-pass comprehension.
- It distinguishes “collected a source” from “understood a source”.

---

## Layer C — Structured Debate

### `delegate_task`

Use `delegate_task` after baseline understanding exists and before rule promotion.

#### Trigger

- A single-model note may be missing important blind spots.
- The source may influence patterns, protocols, or default repo rules.
- The source mixes valuable mechanisms with inflated claims.
- We want a low-cost stress test of the baseline understanding.

#### Default roles

- Practical engineer: can this work in our environment?
- Skeptic: what evidence is missing, and where is the logic weak?
- Academic researcher: what prior art, theory, and validation status exist?

#### Output

- contradiction map
- consensus points
- single-model omissions
- shared blind spots of same-model debate

#### Limitation

`delegate_task` in this workflow is still same-family debate by default. It is a candidate-validation layer, not a final truth layer.

#### Promotion restriction

Debate output alone is not sufficient to promote a default repo rule.

---

## Layer D — Heterogenous Challenge

### External AI consultation

Use external AI consultation after structured debate when same-model bias matters.

#### Trigger

- Debate results may affect default rules.
- Same-model agreement looks coherent but may still share blind spots.
- We want another model family to attack the synthesis, not just summarize the source again.

#### Questions to ask

- What did these three views all miss?
- Which conclusion is most likely overstated?
- What would you reject before promotion to a default workflow rule?

#### Output

- heterogenous challenge notes
- downgraded / strengthened claims
- sharper list of what still needs proof

#### Restriction

External AI suggestions are not truth. They must be recovered, filtered, and compared against the source baseline.

---

## Layer E — Deep Validation

### `Science Superpowers`

Use `Science Superpowers` when a research result is about to become a claim.

#### Trigger

- We are about to say a conclusion is actually valid, not merely plausible.
- The work now depends on evidence strength, red-team review, or explicit verification design.
- The result may become a pattern, protocol, or default workflow rule.

#### Best use

Use it to validate the claim itself.

#### Typical outputs

- framed claim
- prior-work check
- validation design
- verify-before-claiming gate
- red-team feedback

### `grill-with-docs`

Use `grill-with-docs` when the target is a plan or protocol draft rather than an empirical claim.

#### Trigger

- We already have a draft protocol, plan, or argument.
- We need document-driven pressure against hidden ambiguity, definition slippage, or missing boundaries.
- The key risk is “sounds right in chat, weak on contact with the actual docs”.

#### Best use

Use it to interrogate the text of a proposal or protocol.

### Division of labor

- Validate the claim → prefer `Science Superpowers`.
- Interrogate the protocol text → prefer `grill-with-docs`.
- Use both when a protocol draft contains claim-level assumptions that also need proof.

---

## Layer F — Real-Run Verification

Research is not eligible for repo-default promotion until it survives a real task.

### Required when

- the result will be written into repo defaults;
- the result will become a reusable pattern;
- the result will steer future routing behavior.

### Questions

- Did this routing chain reduce misrouting on a real request?
- Did it produce a blind spot that shallow search + summary would have missed?
- Was the extra cost justified?
- Which layer is easiest to skip, and what breaks when it is skipped?

### Rule

A theory that has not survived a real task is still a candidate.

---

## Layer G — Promotion Rules

### Allowed to persist in Obsidian

A rule may be persisted in Obsidian as a live protocol as soon as it is useful for ongoing work.

### Allowed to promote into this repo

A rule may be promoted into the repo control-plane only if all of the following are true:

1. It has passed at least one candidate-validation layer above baseline understanding.
2. It has passed either heterogenous challenge or deep validation.
3. It has real-run evidence.
4. Its scope, budget boundary, and stop condition are explicit.

### Not promotable yet

Do not promote if the rule is:

- based on a single appealing article claim;
- based only on same-model debate;
- missing a real-run test;
- missing a “when not to use this” boundary.

---

## One-Page Routing Table

| Current state | Use first | Upgrade to | Stop when |
|---|---|---|---|
| vague research request | `dbs` | `STORM` / `anysearch` | the question is clear |
| clear question, unclear landscape | `STORM` | `anysearch` / `delegate_task` | contradiction map exists |
| need real sources | `anysearch` | source + note baseline | current-round evidence is sufficient |
| have sources, only first understanding exists | single-model baseline | `delegate_task` | baseline note is stable |
| need to test blind spots | `delegate_task` | external AI / `Science Superpowers` / `grill-with-docs` | contradictions and omissions are explicit |
| need model-family challenge | external AI | `Science Superpowers` / `grill-with-docs` | key new blind spots are recovered |
| need claim-grade validation | `Science Superpowers` | real-run verification | claim passes verification gate |
| need to stress-test a protocol draft | `grill-with-docs` | `Science Superpowers` / real-run | protocol boundaries are explicit |
| preparing repo-default promotion | real-run verification | repo promotion | evidence is sufficient |

---

## Default Escalation Paths

### Lightweight path

```text
request → dbs → STORM → anysearch → source/note baseline → stop
```

Use when the goal is understanding, not promotion.

### Medium path

```text
request → dbs → STORM → anysearch → baseline → delegate_task → external AI → stop
```

Use when the goal is a stronger working judgment, but not yet a default rule.

### Heavyweight path

```text
request → dbs → STORM → anysearch → baseline → delegate_task → external AI → Science Superpowers / grill-with-docs → real-run → promote
```

Use when the result may become a repo pattern, protocol, or routing default.

---

## Relationship to Existing Repo Documents

- `docs/WORKFLOW_PROTOCOL.md` defines the repo-wide control loop.
- `docs/ROUTING_MATRIX.md` maps natural-language task types to frameworks and patterns.
- `docs/MULTI_AGENT_DEBATE_PROTOCOL.md` defines one specific sub-protocol inside this research routing chain.
- This document defines **when research climbs from understanding to challenge to validation to promotion**.
