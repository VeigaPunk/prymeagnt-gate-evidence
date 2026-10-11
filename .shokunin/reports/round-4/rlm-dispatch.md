# rlm-dispatch — round 4

## Work performed
- Extended `.shokunin/rlm-dispatch/corpus/verification/verify_receipt.py` to link registry `childId` to the session directory basename and collect `rlm_child_id`, and to require the sole assistant text reply to equal collect `answer_preview`. These are fields documented in the observed round-2 receipt (`.shokunin/rlm-dispatch/corpus/knowledge/2026-10-11-round2-admission.md`); no other mandatory receipt fields were added.
- Added sanitized positive linkage and negative mixed-child / wrong-reply fixtures; preserved the original positive and wrong-route/unsettled fixture cases. Reproduction commands and synthetic-only caveat are in `.shokunin/rlm-dispatch/corpus/verification/README.md`.
- Commit carrying work: `04559ca80ae1a5421092f869ed7248e827d36360`.

## Landed changes
- Round-4 log and scorecard evidence: `.shokunin/rlm-dispatch/LOG.md` and `.shokunin/rlm-dispatch/SCORECARD.md`, commit `04559ca80ae1a5421092f869ed7248e827d36360`.

## Before → after measurements
- Mixed-child counterfeit fixture: prior verifier accepted it (`PASS`, exit 0); verifier at `04559ca80ae1a5421092f869ed7248e827d36360` rejects it with `collect child ID does not match registry childId` (exit 1). Prior-version command: `python3 <prior verify_receipt.py> .shokunin/rlm-dispatch/corpus/verification/fixtures/mixed-child/registry.json .shokunin/rlm-dispatch/corpus/verification/fixtures/mixed-child/sub-fixture-a/session.jsonl .shokunin/rlm-dispatch/corpus/verification/fixtures/mixed-child/settlement.json`; current reproducible command is the fourth command in the verification README. The prior verifier was run against this same fixture using a temporary copy of its pre-round source.
- Current documented fixture command outcomes, re-run at the work commit: legacy positive exit 0; legacy negative exit 1; linked-good exit 0; mixed-child exit 1; wrong-reply exit 1. `python3 -m py_compile .shokunin/rlm-dispatch/corpus/verification/verify_receipt.py` and `git diff --check` also passed. All fixtures are synthetic and sanitized; this does not establish authenticated live provenance or a new live receipt.

## Owned-axis verdicts
- **Operability: improved.** The falsifiable mixed-child case went from accepted to rejected, with committed positive and negative fixtures and reproducible commands.
- **Calibration: unchanged.** No new live admission/settlement observation; synthetic checks test verifier behavior, not authentication of runtime provenance.

## SHONEN
- [~] Real decision tables / error patterns / checklists with cited sources — prior sourced corpus artifacts remain; this round uses the observed round-2 receipt field names.
- [~] End-to-end domain task executed and logged — local verifier linkage task executed; synthetic only.
- [~] Instructions executable without oral context — README has exact reproduction commands.
- [~] No cross-domain bleed and accurate province — changes confined to `.shokunin/rlm-dispatch/**` and this report.

No promotion: round 1 failed; round 4 is only the third admitted-round candidate if independently accepted. No global harness changes, push, or live provenance claim.
