# Runtime Immediate Activation Principle

## Purpose

This document promotes a new workflow rule from the Obsidian-side main protocol into the repo control-plane:

> when a same-day conversation produces a confirmed **workflow-level correction**, that correction should not be treated as passive archived knowledge; it should immediately become the current runtime rule for the same active workstream.

This principle exists to stop a specific failure mode:

- a new workflow rule is correctly discovered;
- the rule is written into notes and protocols;
- but the active session continues behaving according to the old pattern.

---

## The Failure Being Fixed

Wrong behavior:

```text
new workflow insight
→ save to knowledge base
→ maybe apply later
→ active session still behaves like before
```

Correct behavior:

```text
new workflow-level correction
→ save to knowledge base
→ immediately override the old runtime habit in the current workstream
→ continue execution under the new rule
```

---

## Scope

This applies only to **workflow-level corrections**, not every new fact.

A correction counts as workflow-level when it changes one or more of:

- how Hermes should route the next step;
- whether the system should continue automatically or stop;
- what counts as a valid handoff or checkpoint;
- what must be persisted before advancing;
- what the active default behavior should be for the same thread of work.

---

## Runtime Rule

Once a workflow-level correction is:

1. identified,
2. articulated clearly enough to execute,
3. accepted by the user or otherwise validated in-session,

then Hermes should:

- treat it as immediately active for the same workstream;
- apply it to the next routing / execution decision;
- avoid falling back to the previous habit unless there is a strong reason.

Fallback to the old behavior is allowed only when:

- the user explicitly withdraws the correction;
- later verification falsifies it;
- it conflicts with a higher-priority boundary or safety rule.

---

## Relationship to Existing Principles

This principle binds together three already-established repo ideas:

1. **Fuzzy-input routing** — Hermes must infer candidate routes before asking the user to finish the question.
2. **Auto-continue where appropriate** — if the next hop is already clear, do not stall in explanation mode.
3. **Learning loop** — once the correction is confirmed, it should update future behavior.

This document adds the missing bridge:

> the correction must affect the **current runtime**, not only future memory.

---

## Minimal Execution Test

A same-day workflow correction passes the runtime-immediate-activation test only if all of the following happen in one continuous line of work:

1. a workflow problem is noticed;
2. the workflow rule is updated in the source of truth;
3. the next action in the same thread follows the new rule;
4. the assistant does not stop at explanation if the new rule says to continue;
5. the result is persisted and verifiable.

---

## Current Example

Current validated example from this repo line of work:

- user observed that vague-input routing was still being treated too passively;
- user then observed that same-day loop insights were still being treated as archived knowledge instead of active runtime rules;
- the principle was written into the Obsidian main protocol;
- the next action in the same session was to immediately propagate that rule into repo control docs and execute a real sample test.

This is the intended behavior.

---

## Adoption Meaning

This repo should not treat workflow corrections as “done” when they are merely documented.

A correction is only operationally complete when it is:

- documented,
- applied in the current workstream,
- verified by follow-up action,
- preserved in durable state.
