# Implement Plan: 激活旧项目到新工作流框架

## Current Status

已完成：

- `docs/LEGACY_PROJECT_ACTIVATION.md`
- `docs/ROUTING_MATRIX.md`
- `docs/frameworks/*.md` 8 张核心 Framework Cards
- `examples/instances/legacy-project-activation.json`
- `scripts/verify.py` required files 更新
- GitHub push 到 `https://github.com/sunshihao001/loop-`

## Remaining Steps

### Step 1: Validate current repository

```bash
cd /root/loop循环项目
python3 scripts/verify.py
git status --short --branch
```

Expected:

- `VERIFY OK`
- branch clean or only Trellis task bookkeeping changes

### Step 2: Record this Trellis task

Ensure this directory exists:

```text
.trellis/tasks/06-26-legacy-project-activation/
```

Required artifacts:

- `task.json`
- `prd.md`
- `design.md`
- `implement.md`

### Step 3: Update Obsidian hot/log

Record:

- local repo path;
- GitHub URL;
- Trellis task path;
- current activation status P1-P3 done, P4 next;
- verification output.

### Step 4: Commit Trellis task artifacts

Commit message suggestion:

```text
docs: track legacy project activation trellis task
```

### Step 5: Next real run

Create/execute the first verified run:

```text
Trellis + Obsidian + GitHub loop repo
```

Acceptance for first real run:

- A user request is routed through `ROUTING_MATRIX.md`;
- At least one Framework Card is loaded;
- An Instance records the chosen Framework/Pattern;
- Verification output exists;
- Obsidian hot/log records result.

## Rollback

If Trellis initialization added unwanted platform files, inspect `git status --short` and only keep files relevant to this repo's control-plane workflow. Do not delete user knowledge or unrelated project directories.
