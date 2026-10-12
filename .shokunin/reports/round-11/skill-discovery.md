# Skill discovery R11 — direct source directory symlink

Date: 2026-10-12. Base `9804b13`; implementation/probe/log/scorecard commit `d41a8979ff5fc270d9f16d4d114cf0bd4afc10ec`. Author and committer: `skill-discovery-shokunin <skill-discovery@shokunin.local>`.

## One move

In `scripts/install-skills.sh`, skip a **direct source skill directory symlink** before `[ -d "$src" ]`. The glob `"$SOURCE"/*/` produces a trailing slash; a private native check found `[ -L "$src" ]` false and `[ -L "${src%/}" ]` true for this fixture. The added line checks `${src%/}`. This does not change non-directory links or general `SKILL.md` link policy.

## Actual baseline/current measurements

The executable `corpus/probes/r11-source-directory-link.sh <installer-path>` builds a private source, an absolute `outside-skill -> <private-temp>/external` directory symlink containing `SKILL.md`, and a regular `ordinary` directory containing `SKILL.md`. It runs each installer into a private project-local `.prime/agent/skills` target and separately calls `prime-agent prompt --cwd <private-project> --json` for mixed and symlink-only cases. Temporary files are removed by a trap. The baseline installer was extracted from `git show 9804b13:scripts/install-skills.sh`; current is `scripts/install-skills.sh`.

| Measurement | Baseline `9804b13` | Current `d41a897` |
|---|---|---|
| Mixed install exit / installed count | 0 / 2 | 0 / 1 |
| Mixed outside target / ordinary target | yes / yes | no / yes |
| Mixed fresh prompt exit | 0 | 0 |
| Mixed fresh inventory outside / ordinary | present / present | absent / present |
| Symlink-only install exit / installed count | 0 / 1 | 1 / 0 |
| Symlink-only outside / ordinary target | yes / no | no / no |
| Symlink-only fresh prompt exit | 0 | 0 |
| Symlink-only fresh inventory outside / ordinary | present / absent | absent / absent |

The current R9 native probe still reports mixed exit 0/count 1/fake absent; fake-only exit 1/count 0/fake absent. The current R10 native probe reports mixed exit 0/count 2, ghost and absolute absent, internal and peer installed and inventoried; external-only exit 1/count 0. `bash -n` on installer and R11 probe and `git diff --check` passed.

## Proposed one-axis verdict and limits

**Operability improved narrowly:** direct source directory symlinks no longer copy external directories and count them as installed; regular skill discovery and R9/R10 controls remain. **Freshness unchanged:** fresh CLI inventory is not evidence of daemon reload or an existing session refreshing. No daemon/session reload, provider inference, shared skill install, manifest/global harness change, merge, or push. This is private synthetic source/install evidence, not a blanket symlink policy.
