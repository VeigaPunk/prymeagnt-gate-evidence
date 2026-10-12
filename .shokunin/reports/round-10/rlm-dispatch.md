# RLM-dispatch craft round 10 — duplicate-key calibration

## Change
The receipt verifier now rejects duplicate keys in registry/settlement JSON and every session JSONL object, recursively, using Python stdlib `object_pairs_hook`. It reports a generic parse failure and does not include private JSON or paths. Existing `verify()` API is unchanged.

## Evidence
Native kernel interpreter command: `python3` (project-independent stdlib script). The independent tenth synthetic fixture uses wrong-then-right duplicate registry `status` and nested message `role`.

- Baseline `595797d8e5a349b9395e602601a5529b0c776ef5`: tenth fixture exit 0 (PASS).
- Current: tenth fixture exit 1 (generic duplicate-key failure).
- Original nine fixture exits remain `0/1/0/1/1/0/1/1/1`.
- Tenth fixture current exit: 1; baseline: 0.

Reproduce from repo root:
```sh
V=.shokunin/rlm-dispatch/corpus/verification
python3 "$V/verify_receipt.py" "$V/fixtures/duplicate-keys/registry.json" "$V/fixtures/duplicate-keys/sub-fixture-a/session.jsonl" "$V/fixtures/duplicate-keys/settlement.json"
```

## Axis verdict
Calibration improved narrowly: last-wins contradictory duplicate values no longer yield PASS. Operability unchanged: all nine controls retain their prior outcomes. Synthetic fixtures only; no live authentication, provider behavior, or usage/depletion claim.


## Evidence correction — isolated parser pathways
An independent review noted that the first tenth fixture combined registry and session duplicates. To isolate evidence, four separate synthetic fixture directories were added and retained:

| Fixture | Exact invocation inputs (under `.shokunin/rlm-dispatch/corpus/verification/fixtures/`) | Baseline exit | Current exit |
|---|---|---:|---:|
| Registry duplicate only | `duplicate-registry-only/registry.json`, `duplicate-registry-only/sub-fixture-a/session.jsonl`, `duplicate-registry-only/settlement.json` | 0 | 1 |
| Nested session `role` duplicate only | `duplicate-session-only/registry.json`, `duplicate-session-only/sub-fixture-a/session.jsonl`, `duplicate-session-only/settlement.json` | 0 | 1 |
| Settlement `status` duplicate only | `duplicate-settlement-only/registry.json`, `duplicate-settlement-only/sub-fixture-a/session.jsonl`, `duplicate-settlement-only/settlement.json` | 0 | 1 |
| Unique positive control | `duplicate-unique-positive/registry.json`, `duplicate-unique-positive/sub-fixture-a/session.jsonl`, `duplicate-unique-positive/settlement.json` | 0 | 0 |

All were run with native `python3`; README contains exact runnable commands. Each negative changes only the named input pathway. Original nine exits remain `0/1/0/1/1/0/1/1/1`. These are private synthetic copies, not live auth/provider evidence.
