#!/usr/bin/env python3
"""Check basic structure for Ed-PdD-Copilot skills."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "plugins" / "ed-pdd-copilot" / "skills"

REQUIRED_REFERENCE_HINTS = {
    "governance-idea-evaluator": ["rubric.md", "fatal-flaws.md", "theory-anchors.md", "worked-examples.md"],
    "edtech-intro-drafter": ["four-part-logic.md", "paragraph-patterns.md", "alienation-patterns.md", "worked-examples.md"],
    "governance-paper-template": ["paper-types.md", "theory-to-design.md", "dual-topology.md", "section-skeleton.md", "worked-examples.md"],
    "mixed-methods-evidence-template": ["claim-evidence-matrix.md", "indicator-system.md", "quantitative-methods.md", "qualitative-methods.md", "triangulation.md"],
    "governance-figure-designer": ["figure-types.md", "layout-patterns.md", "label-language.md", "quality-audit.md"],
    "edtech-pre-submission-reviewer": ["review-rubric.md", "theory-policy-checklist.md", "method-evidence-checklist.md", "ethics-data-governance.md", "style-anti-patterns.md"],
    "ai-assisted-edtech-research-workflow": ["human-ai-boundary.md", "allowed-uses.md", "red-lines.md", "verification-checklist.md"],
}


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def main() -> int:
    if not SKILLS.exists():
        fail(f"Missing skills directory: {SKILLS}")

    failures = []
    for skill, refs in sorted(REQUIRED_REFERENCE_HINTS.items()):
        folder = SKILLS / skill
        skill_md = folder / "SKILL.md"
        agents = folder / "agents" / "openai.yaml"
        ref_dir = folder / "references"
        if not folder.exists():
            failures.append(f"{skill}: missing folder")
            continue
        if not skill_md.exists():
            failures.append(f"{skill}: missing SKILL.md")
        else:
            text = skill_md.read_text(encoding="utf-8")
            if not text.startswith("---\n") or f"name: {skill}" not in text or "description:" not in text:
                failures.append(f"{skill}: invalid frontmatter")
            if "TODO" in text or "placeholder" in text.lower():
                failures.append(f"{skill}: contains TODO/placeholder")
        if not agents.exists():
            failures.append(f"{skill}: missing agents/openai.yaml")
        if not ref_dir.exists():
            failures.append(f"{skill}: missing references directory")
        else:
            for ref in refs:
                path = ref_dir / ref
                if not path.exists():
                    failures.append(f"{skill}: missing references/{ref}")
                elif not path.read_text(encoding="utf-8").strip():
                    failures.append(f"{skill}: empty references/{ref}")

    if failures:
        for item in failures:
            print(item)
        return 1
    print("OK: all Ed-PdD-Copilot skill structure checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
