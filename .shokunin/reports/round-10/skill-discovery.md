# Skill discovery R10 — SKILL.md symlink boundary

Date: 2026-10-12

Base: `770c9b1`; code + fixture commit: `1b11d94`
Identity (author and committer): `skill-discovery-shokunin <skill-discovery@shokunin.local>`.

## Change

`scripts/install-skills.sh` now skips a `SKILL.md` symlink if its raw link is absolute or its resolved file is outside the source skill directory. A relative link resolved within that directory remains eligible; its `SKILL.md` content is copied as a regular file into the private target after the ordinary `cp -a`. Non-`SKILL.md` links were not changed. This is a narrow install rule, not a complete validator of source content or every symlink in a skill.

## Measured baseline/current

Run `corpus/probes/r10-skillmd-symlink.sh <installer-path>` from `.shokunin/skill-discovery/` (the script also works from any directory). Actual baseline installer was extracted by `git show 770c9b1:scripts/install-skills.sh` into a private executable. Each invocation uses new temporary source, target under a private project, and fresh `prime-agent prompt --cwd <private-project> --json`; all temporary data is removed. Fixtures: `r10-ghost/SKILL.md -> ../outside.md` (source-readable, broken after copying); `r10-absolute/SKILL.md` absolute link to a private external file; `r10-internal/SKILL.md -> docs/real.md`; and ordinary `r10-peer/SKILL.md`.

| Observation | Baseline `770c9b1` | Current `1b11d94` |
|---|---|---|
| Mixed install exit / printed installed count | 0 / 4 | 0 / 2 |
| Ghost target file / symlink | no / yes | no / no |
| Absolute target file / symlink | yes / yes | no / no |
| Internal target file / symlink | yes / yes | yes / no |
| Peer target file / symlink | yes / no | yes / no |
| Fresh-process prompt exit | 0 | 0 |
| Fresh inventory ghost / absolute / internal / peer | absent / present / present / present | absent / absent / present / present |
| External-only install exit / count | 0 / 2 | 1 / 0 |

`bash -n` (installer and probe), `git diff --check`, and path-scoped status verification passed. No shared install, daemon, reload, provider, manifest, global harness, push, or merge was run.

## Proposed axis result

- **Operability improved, narrowly:** invalid external `SKILL.md` links no longer count as installed; internal relative and ordinary fixtures remain installed and discoverable in the private fresh-process inventory.
- **Freshness unchanged:** a fresh CLI process was checked, not live daemon reload or inventory refresh. The synthetic fixtures do not establish behavior for arbitrary real-world skills.
