# Real-Run Sample — Runtime Immediate Activation Principle

## Goal

Test whether a same-day workflow correction is treated as an immediately active runtime rule rather than passive archived knowledge.

## Triggering User Input

> 这样感觉hermes还是没有搞清今天做的循环工作流和现在之间的关系，已经应用

Then:

> 执行，并运行上面想法进行测试

## Prior Same-Day Corrections Already Established

1. Fuzzy-input research routing should be handled by Hermes proactively.
2. Where the next hop is already clear, the workflow should not stop in explanation mode.
3. The user explicitly confirmed that this logic should update the overall workflow, not remain a local note.

## Hypothesis

If runtime immediate activation is working, Hermes should:

1. update the main protocol;
2. propagate the correction into repo control docs;
3. execute a real sample test in the same session;
4. avoid stopping at a mere conceptual explanation.

## Actual Execution

### Step 1 — Main protocol updated

Updated Obsidian source-of-truth docs:

- `20_Notes/AI_Agent工作流_Framework_Pattern_Instance三层协议.md`
- `20_Notes/研究工具工作流化与模糊表达路由审计.md`
- `hot.md`
- `20_Notes/log.md`

### Step 2 — Repo control-plane propagation

Created / updated repo docs:

- `docs/RUNTIME_IMMEDIATE_ACTIVATION_PRINCIPLE.md`
- `docs/FUZZY_INPUT_RESEARCH_ROUTING_AUDIT.md`
- `docs/WORKFLOW_PROTOCOL.md`
- `docs/README.md` (via `README.md` at repo root if referenced)
- `docs/ROUTING_MATRIX.md`
- `docs/SOURCE_INDEX.md`

### Step 3 — Verification run

Command executed:

```bash
cd '/root/loop循环项目' && python3 scripts/verify.py
```

Expected success criterion: `VERIFY OK`

### Step 4 — Persistence

Result persisted back to Obsidian `hot.md` / `20_Notes/log.md` after the run.

## Pass Criteria

The sample passes if:

- the workflow correction was not left as note-only knowledge;
- the repo control-plane was updated in the same thread;
- a real verification command was run;
- the result was persisted.

## Status

`pending verification output`
