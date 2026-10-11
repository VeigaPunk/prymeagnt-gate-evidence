# Local receipt verifier

Run from repo root:

```sh
python3 .shokunin/rlm-dispatch/corpus/verification/verify_receipt.py REGISTRY.json SESSION.jsonl COLLECT.json
```

Inputs are local JSON/JSONL only; the command performs no network or runtime calls and does not modify them. The expected selector is intentionally fixed to the round's permitted `openai-codex/gpt-6-luna`. A pass requires matching registry and first session `model_change` provenance, completed registry status, registry `childId` matching both the session directory basename and collect `rlm_child_id`, exactly one assistant text reply matching collect `answer_preview`, and a `done`, settled, no-error collect receipt. These fields are present in the recorded round-2 receipt (`corpus/knowledge/2026-10-11-round2-admission.md`); fixture JSON uses synthetic sanitized IDs. Fixtures are synthetic examples, not authenticated live provenance or new runtime receipts.

Reproduce all checks from the repository root (first command must pass; second must fail for prior wrong-route/unsettled reasons; linked-good passes; mixed-child and wrong-reply fail):

```sh
V=.shokunin/rlm-dispatch/corpus/verification
python3 "$V/verify_receipt.py" "$V/fixtures/registry-good.json" "$V/fixtures/session-good.jsonl" "$V/fixtures/settlement-good.json"
python3 "$V/verify_receipt.py" "$V/fixtures/registry-wrong.json" "$V/fixtures/session-wrong.jsonl" "$V/fixtures/settlement-running.json"
python3 "$V/verify_receipt.py" "$V/fixtures/linked-good/registry.json" "$V/fixtures/linked-good/sub-fixture-a/session.jsonl" "$V/fixtures/linked-good/settlement.json"
python3 "$V/verify_receipt.py" "$V/fixtures/mixed-child/registry.json" "$V/fixtures/mixed-child/sub-fixture-a/session.jsonl" "$V/fixtures/mixed-child/settlement.json"
python3 "$V/verify_receipt.py" "$V/fixtures/wrong-reply/registry.json" "$V/fixtures/wrong-reply/sub-fixture-a/session.jsonl" "$V/fixtures/wrong-reply/settlement.json"
```
