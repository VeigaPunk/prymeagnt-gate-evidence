# RLM-dispatch — Round 12: malformed syntax

## Change

The receipt verifier now catches `json.JSONDecodeError` only at the two JSON parsing boundaries: registry/settlement JSON loading and session JSONL event parsing. It returns the generic `input contains malformed JSON syntax` failure. The distinct duplicate-key failure remains in place. No broad `Exception` or `ValueError` catch was added.

## Isolated native checks

Baseline is the verifier from base `1f888d5`; current is the working verifier. Each malformed fixture has valid companion inputs, and the positive fixture uses valid unique-key inputs.

| Input pathway | Baseline | Current |
|---|---|---|
| Registry JSON syntax | uncaught `JSONDecodeError` traceback, exit 1 | generic `FAIL`, exit 1; no traceback |
| Session JSONL syntax | uncaught `JSONDecodeError` traceback, exit 1 | generic `FAIL`, exit 1; no traceback |
| Settlement JSON syntax | uncaught `JSONDecodeError` traceback, exit 1 | generic `FAIL`, exit 1; no traceback |
| Unique valid positive | PASS, exit 0 | PASS, exit 0 |

The nine prior controls retain baseline/current exits `0/1/0/1/1/0/1/1/1`. The three isolated R10 duplicate pathways and unique-positive control retain `1/1/1/0`. R11 isolated malformed-shape controls and positive retain `1/1/1/1/0`. Checks used native `python3`; `py_compile` and `git diff --check` pass.

## One-axis verdict

- **Operability: improved narrowly.** Malformed syntax in each JSON/JSONL pathway now yields a normal verifier failure rather than an uncaught parser traceback; prior controls and the positive remain stable.
- **Calibration: unchanged.** Valid-input receipt acceptance rules did not change.

Synthetic local fixtures only. No provider, daemon, or live authentication was used. No claim is made about file/read errors, NUL paths, or general I/O handling. Scope is `.shokunin/rlm-dispatch/**` plus this report; no manifest/global harness/integration changes.

Canonical Git author and committer: `rlm-dispatch-shokunin <rlm-dispatch@shokunin.local>`.


## Report-last ordering correction

The initial R12 commit `011008216c10ef4dcf132e8ae90b9b5dbb67d424` included both verifier/fixture changes and this report, so it did not follow the requested report-last sequence. That commit is preserved without rewriting history. This report-only follow-up commit records the correction after the code commit; the final report closure is therefore committed separately after code. No code or fixture changes are included here.
