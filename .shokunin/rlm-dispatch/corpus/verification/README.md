# Local receipt verifier

Run from repo root:

```sh
python3 .shokunin/rlm-dispatch/corpus/verification/verify_receipt.py REGISTRY.json SESSION.jsonl COLLECT.json
```

Inputs are local JSON/JSONL only; the command performs no network or runtime calls and does not modify them. The expected selector is intentionally fixed to the round's permitted `openai-codex/gpt-6-luna`. A pass requires matching registry and first session `model_change` provenance, completed registry status, an assistant response, and `rlm.collect` status `done`, `settled: true`, `error: null`. Fixtures are sanitized synthetic examples, not new runtime receipts.
