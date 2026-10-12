# RLM-dispatch craft round 11 — JSON shape safety

## Change

Commit `8e5acd5eaf7b2296c13e33111c47d53683a38f06` adds small structural guards before the receipt verifier's nested dereferences. Registry and settlement roots must be objects; registry `model` must be an object; parsed session JSONL records must be objects, and message records must have an object `message` with list-of-object `content`. Invalid shapes receive the generic `input JSON shape is invalid` error. The `verify(registry_path, session_path, settlement_path)` API is unchanged. No provider or daemon was invoked.

## Isolated regressions and controls

All commands below use native `python3` from the repository root, via `V=.shokunin/rlm-dispatch/corpus/verification` and script `$V/verify_receipt.py`. Each regression directory contains otherwise-positive synthetic inputs; only its named shape is malformed.

| Case | Fixture | Baseline | Current |
|---|---|---:|---:|
| Registry model null | `fixtures/shape-r11/registry-model-null` | uncaught `AttributeError`, exit 1 / traceback | generic FAIL, exit 1 |
| Registry root array | `fixtures/shape-r11/registry-root-array` | uncaught `AttributeError`, exit 1 / traceback | generic FAIL, exit 1 |
| Settlement root null | `fixtures/shape-r11/settlement-root-null` | uncaught `AttributeError`, exit 1 / traceback | generic FAIL, exit 1 |
| Message event null | `fixtures/shape-r11/session-message-null` | uncaught `AttributeError`, exit 1 / traceback | generic FAIL, exit 1 |
| Valid shape positive | `fixtures/shape-r11/positive` | PASS, exit 0 | PASS, exit 0 |

The four malformed probes ran separately. Baseline means the verifier at `HEAD^` (`65b0abb`), checked from a temporary copy of the script; current means the committed R11 verifier.

Original nine fixture current exits remain `0/1/0/1/1/0/1/1/1`; this matches the baseline sequence documented in R10. R10 duplicate registry/session/settlement and unique positive controls remain current exits `1/1/1/0`. Native `python3 -m py_compile .shokunin/rlm-dispatch/corpus/verification/verify_receipt.py` and `git diff --check` succeeded (exit 0).

## One-axis verdict

- **Operability: improved narrowly.** Four independent malformed-shape cases that surfaced uncaught Python exceptions now fail as normal generic verifier results; valid positive is still accepted and prior controls retain their outcomes.
- **Calibration: unchanged.** No receipt acceptance criterion changed; only input structure is checked before dereferencing. This synthetic local test does not establish provider authentication, authentication success, provider behavior, or usage/depletion claims.

Scope: `.shokunin/rlm-dispatch/**` and this report only. No integration, manifest, or global harness changes. Canonical Git author and committer: `rlm-dispatch-shokunin <rlm-dispatch@shokunin.local>`.


## Evidence correction — fixture-local session paths

Independent review found that three negative fixtures pointed the registry `sessionFile` at the `linked-good` session rather than their own fixture. The `registry-model-null`, `session-message-null`, and `settlement-root-null` registries now point to their respective local `sub-fixture-a/session.jsonl`; `registry-root-array` is intentionally a root array without a session field. This removes the extra path-mismatch factor from the three object-shaped negatives.

Revalidated with native `python3`, separately for each input. Baseline verifier from `8e5acd5^` produced uncaught traceback / exit 1 on each of the four malformed fixtures; current verifier produced generic FAIL / exit 1. The positive fixture passed with exit 0 on baseline and current. Current original nine outcomes remain `0/1/0/1/1/0/1/1/1`; R10 duplicate-registry/session/settlement and unique-positive outcomes remain `1/1/1/0`. These corrections do not change the round verdict: operability improved narrowly; calibration unchanged.

Scope caveat: malformed JSON syntax, file/read errors, and NUL input are unrelated and were not tested or claimed as covered by this shape-validation change. No provider or daemon was invoked.
