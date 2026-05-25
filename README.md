# Paul Graham Skills

Paul Graham / PG distilled into portable AI-agent skills for Cursor, Claude Code, Antigravity, and AGENTS.md-compatible tools.

This repository is intentionally standalone. Install only this repo if you only want the Paul Graham / PG lens.

## What Is Inside

```text
paul-graham-skills/
├── README.md
├── PRINCIPLES.md
├── AGENTS.md
├── EVALUATION.md
├── SOURCE_POLICY.md
├── skills/paul-graham/
│   ├── SKILL.md
│   └── PLAYBOOK.md
├── .agents/skills/paul-graham.md
├── adapters/
│   ├── AGENTS.md
│   └── GEMINI.md
└── scripts/
    ├── install.ps1
    └── validate.py
```

## Platforms

### Cursor

```powershell
.\scripts\install.ps1 -Platform cursor
```

For project-local installation:

```powershell
.\scripts\install.ps1 -Platform cursor -Scope project -ProjectPath "C:\path\to\project"
```

### Claude Code

Claude Code supports personal skills at `~/.claude/skills/<skill-name>/SKILL.md` and project skills at `.claude/skills/<skill-name>/SKILL.md`.

```powershell
.\scripts\install.ps1 -Platform claude
```

For project-local installation:

```powershell
.\scripts\install.ps1 -Platform claude -Scope project -ProjectPath "C:\path\to\project"
```

### Antigravity / AGENTS.md

Antigravity works best with project rules. This installer copies `.agents/skills/paul-graham.md` into the target project and adds a managed block to the target project's `AGENTS.md`.

```powershell
.\scripts\install.ps1 -Platform antigravity -Scope project -ProjectPath "C:\path\to\project"
```

If you prefer manual setup, copy `adapters/AGENTS.md` into your project `AGENTS.md`, and copy `.agents/skills/paul-graham.md` into your project `.agents/skills/`.

### Install Everywhere

```powershell
.\scripts\install.ps1 -Platform all -Scope project -ProjectPath "C:\path\to\project"
```

## Validate

```powershell
python .\scripts\validate.py
```

## Source Policy

This is a distilled behavioral package, not a mirrored corpus. It avoids long quotations, private paths, contact details, and source reconstruction.
