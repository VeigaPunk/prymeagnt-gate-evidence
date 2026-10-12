# Local receipt verifier

Run from repo root:

```sh
python3 .shokunin/rlm-dispatch/corpus/verification/verify_receipt.py REGISTRY.json SESSION.jsonl COLLECT.json
```

Inputs are local JSON/JSONL only; the command performs no network or runtime calls and does not modify them. The expected selector is intentionally fixed to the round's permitted `openai-codex/gpt-6-luna`. Registry fixtures carry the observed `sessionFile` field with sanitized repo-relative paths. A pass requires native registry `type: "rlm_subagent"` (missing and any other value fail; no legacy omission is accepted), matching registry and every session `model_change` provenance, completed registry status, registry `sessionFile` resolving to the supplied session path, registry `childId` matching both the session directory basename and collect `rlm_child_id`, exactly one assistant text reply matching collect `answer_preview`, and a `done`, settled, no-error collect receipt. These fields are present in the recorded round-2 receipt (`corpus/knowledge/2026-10-11-round2-admission.md`); fixture JSON uses synthetic sanitized IDs. Fixtures are synthetic examples, not authenticated live provenance or new runtime receipts.

Reproduce all checks from the repository root (commands 1 and 6 pass; commands 2–5 and 7–8 fail. Command 3 is the wrong-type regression (baseline accepted it, current verifier rejects it).):

```sh
V=.shokunin/rlm-dispatch/corpus/verification
python3 "$V/verify_receipt.py" "$V/fixtures/registry-good.json" "$V/fixtures/session-good.jsonl" "$V/fixtures/settlement-good.json"
python3 "$V/verify_receipt.py" "$V/fixtures/registry-wrong.json" "$V/fixtures/session-wrong.jsonl" "$V/fixtures/settlement-running.json"
python3 "$V/verify_receipt.py" "$V/fixtures/linked-good/registry.json" "$V/fixtures/linked-good/sub-fixture-a/session.jsonl" "$V/fixtures/linked-good/settlement.json"
python3 "$V/verify_receipt.py" "$V/fixtures/mixed-child/registry.json" "$V/fixtures/mixed-child/sub-fixture-a/session.jsonl" "$V/fixtures/mixed-child/settlement.json"
python3 "$V/verify_receipt.py" "$V/fixtures/wrong-reply/registry.json" "$V/fixtures/wrong-reply/sub-fixture-a/session.jsonl" "$V/fixtures/wrong-reply/settlement.json"
python3 "$V/verify_receipt.py" "$V/fixtures/two-matching-model-changes/registry.json" "$V/fixtures/two-matching-model-changes/sub-fixture-a/session.jsonl" "$V/fixtures/two-matching-model-changes/settlement.json"
python3 "$V/verify_receipt.py" "$V/fixtures/late-forbidden-switch/registry.json" "$V/fixtures/late-forbidden-switch/sub-fixture-a/session.jsonl" "$V/fixtures/late-forbidden-switch/settlement.json"
python3 "$V/verify_receipt.py" "$V/fixtures/swapped-session/registry.json" "$V/fixtures/swapped-session/alternate/sub-fixture-a/session.jsonl" "$V/fixtures/swapped-session/settlement.json"
```
