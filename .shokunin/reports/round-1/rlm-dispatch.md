# rlm-dispatch — round 1 report

## Work performed
- Read the installed Godspeed directive and shokunin contract; confirmed the assigned source paths and read-only boundary. Evidence: `/home/vgpnk/.prime/agent/skills/godspeed/directive.md`; `/home/vgpnk/.agents/skills/shokunin/SKILL.md`; `.shokunin/rlm-dispatch/PROVINCE.md`.
- Read scorecard, append-only log, SHONEN, corpus seed, capability survey, smoke procedure, and both smoke logs. Evidence: `.shokunin/rlm-dispatch/SCORECARD.md`, `.shokunin/rlm-dispatch/LOG.md`, `.shokunin/rlm-dispatch/SHONEN.md`, `.shokunin/rlm-dispatch/corpus/knowledge/seed.md`, `docs/capability-survey.md`, `docs/smoke-testing.md`, `verification/smoke-test.log`, `verification/smoke-test-rerun-20261011.log`.
- Queried `rlm.find_models("OpenAI", limit=20)`; live output included `openai-codex/gpt-6-luna` and `openai-codex/gpt-6-sol`. Lookup proves current selector discovery, not child admission.
- Received parent-reported completed scout receipt for child `sub-9bfd0406`, explicit `model="openai-codex/gpt-6-luna"`, completed status, and child message. I did not independently inspect its ephemeral registry. Durable receipt details were checked in `verification/smoke-test-rerun-20261011.log`, Smoke test 2 rerun.
- No sub-lanes were spawned: the bounded read-only inspection and one live model lookup did not warrant eight lanes. No domain-source, MANIFEST, L0-question, or remote files were changed.

## Landed changes
- Added an explicit-selector decision table covering lookup vs admission, settlement, and provider verification, with source-backed cautions. `.shokunin/rlm-dispatch/corpus/knowledge/2026-10-11-selector-admission.md`; indexed in `.shokunin/rlm-dispatch/corpus/README.md`; logged in `.shokunin/rlm-dispatch/LOG.md`.
- Corpus/log commit: `d59015c1f95aed8244c1ec464dd590a3872339cc`.
- Round verdict entry in `.shokunin/rlm-dispatch/SCORECARD.md` was carried by commit `f12210537e8b2f0246c78547a82f28feb7cd2c62` (latest work commit before this report).

## Before → after measurements
- Claim: a durable published explicit-selector completed receipt is independently countable. Counting command: `grep -c 'Smoke test 2 rerun' verification/smoke-test-rerun-20261011.log`. Before: 1 at baseline `44a08fd0eeb22c7ed9766aae4675dd452eff232a`; after: 1 at work commit `f12210537e8b2f0246c78547a82f28feb7cd2c62`. The receipt pre-existed; count did not improve. The decision table did improve usability, but the assigned receipt-count claim is **unprovable-but-better**, not improved.
- Calibration: verdict **unchanged**. No current lane-owned spawn or independently inspected ephemeral child admission was produced. Parent-reported scout receipt and historical published evidence are not represented as independent inspection.

## Axis verdicts
- Operability — **unprovable-but-better**: live selector was found and an actionable admission/settlement decision table was added, but no new independently inspected lane receipt; published receipt count is unchanged.
- Calibration — **unchanged**: no new independent admission measurement to calibrate against.

## SHONEN
- [ ] Real decision tables/error patterns/checklists with cited sources; non-author verifier required. (Authored decision table; no named non-author verifier.)
- [ ] End-to-end domain task executed and logged; non-author verifier required. (No lane-owned end-to-end spawn; no named non-author verifier.)
- [ ] Instructions executable without oral context; non-author verifier required. (No independent non-author verification.)
- [ ] No cross-domain bleed; PROVINCE remains accurate; non-author verifier required. (Scope observed; no named non-author verifier.)
