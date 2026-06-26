#!/usr/bin/env python3
"""Verify loop循环项目 repository structure.

No third-party dependencies. Intended for local runs and GitHub Actions.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "docs/PROJECT_CHARTER.md",
    "docs/ARCHITECTURE.md",
    "docs/WORKFLOW_PROTOCOL.md",
    "docs/GOVERNANCE.md",
    "docs/PERSISTENCE.md",
    "docs/PATTERNS.md",
    "docs/LOOP_WORTHINESS_CHECKLIST.md",
    "docs/SOURCE_INDEX.md",
    "docs/LEGACY_PROJECT_ACTIVATION.md",
    "docs/ROUTING_MATRIX.md",
    "templates/INSTANCE_TEMPLATE.json",
    "examples/instances/basic-loop.json",
    "examples/instances/legacy-project-activation.json",
]

REQUIRED_README_TERMS = [
    "Intent",
    "Verify",
    "Learn",
    "Framework",
    "Pattern",
    "Instance",
]


def fail(message: str) -> None:
    raise SystemExit(f"VERIFY FAILED: {message}")


def main() -> None:
    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.exists():
            fail(f"missing required file: {rel}")
        if path.is_file() and path.stat().st_size == 0:
            fail(f"empty file: {rel}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for term in REQUIRED_README_TERMS:
        if term not in readme:
            fail(f"README.md missing term: {term}")

    arch = (ROOT / "docs/ARCHITECTURE.md").read_text(encoding="utf-8")
    for term in ["Framework", "Pattern", "Instance"]:
        if term not in arch:
            fail(f"ARCHITECTURE.md missing term: {term}")

    for rel in ["templates/INSTANCE_TEMPLATE.json", "examples/instances/basic-loop.json"]:
        with (ROOT / rel).open(encoding="utf-8") as f:
            data = json.load(f)
        for key in ["name", "frameworks", "patterns", "design_axes", "verification"]:
            if key not in data:
                fail(f"{rel} missing key: {key}")

    markdown_files = sorted(ROOT.rglob("*.md"))
    if len(markdown_files) < 8:
        fail(f"expected at least 8 markdown files, found {len(markdown_files)}")

    print("VERIFY OK")
    print(f"root: {ROOT}")
    print(f"required_files: {len(REQUIRED_FILES)}")
    print(f"markdown_files: {len(markdown_files)}")


if __name__ == "__main__":
    main()
