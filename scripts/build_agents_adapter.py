"""Rebuild .agents/skills/*.md from SKILL.md + PLAYBOOK.md."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = next(ROOT.joinpath("skills").iterdir())
SKILL = SKILL_DIR / "SKILL.md"
PLAYBOOK = SKILL_DIR / "PLAYBOOK.md"
ADAPTER = ROOT / ".agents" / "skills" / f"{SKILL_DIR.name}.md"

HEADER = f"""# {SKILL_DIR.name.replace('-', ' ').title()} Skills Antigravity Skill

Use this file when the user asks for the {SKILL_DIR.name.replace('-', ' ')} lens.

Do not impersonate the source person. Use this as a decision framework.

---

"""


def main() -> None:
    body = SKILL.read_text(encoding="utf-8").strip()
    playbook = PLAYBOOK.read_text(encoding="utf-8").strip()
    ADAPTER.parent.mkdir(parents=True, exist_ok=True)
    ADAPTER.write_text(
        HEADER + body + "\n\n---\n\n" + playbook + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {ADAPTER}")


if __name__ == "__main__":
    main()
