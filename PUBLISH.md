# Publish Checklist

Suggested repository name: `paul-graham-skills`

Suggested description:

```text
Portable Paul Graham-inspired startup, writing, and maker-work skill package for Cursor, Claude Code, Antigravity, and AGENTS.md-compatible agents.
```

## Before Creating The Remote

Run:

```powershell
python .\scripts\validate.py
git status --short
```

Expected result:

- Validation passes.
- `git status --short` is empty.

## Create The GitHub Repository

Create an empty GitHub repository named `paul-graham-skills`.

Do not initialize it with a README, license, or `.gitignore`; this repository already contains those files where needed.

## Push

Use HTTPS:

```powershell
git remote add origin https://github.com/<your-github-user>/paul-graham-skills.git
git branch -M main
git push -u origin main
```

Or use SSH:

```powershell
git remote add origin git@github.com:<your-github-user>/paul-graham-skills.git
git branch -M main
git push -u origin main
```

## After Push

Open the GitHub repository page and confirm these paths are visible:

- `skills/paul-graham/SKILL.md`
- `skills/paul-graham/PLAYBOOK.md`
- `.agents/skills/paul-graham.md`
- `scripts/install.ps1`
- `scripts/validate.py`
