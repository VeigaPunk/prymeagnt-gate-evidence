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
