# RLM dispatch — round 14 report

## Move
Operability improved narrowly: `verify_receipt.py` now catches `UnicodeDecodeError` only at registry/settlement JSON decoding and session JSONL decoding. Each returns a generic `FAIL: input contains invalid UTF-8 encoding`, exit 1, with no traceback. Calibration is unchanged: no accepted-input criteria or authentication checks changed.

## Evidence
Native Python 3.14.2 on synthetic local fixtures. At each isolated boundary, only the target file contains invalid UTF-8 (`b"{\xff"`); other receipt files are copied valid positive data with registry `sessionFile` corrected to the local copied session. Baseline source is extracted from base `9804b13`.

| input boundary | baseline | current |
|---|---|---|
| registry | exit 1, uncaught `UnicodeDecodeError` traceback | exit 1, generic FAIL, no traceback |
| session JSONL | exit 1, uncaught `UnicodeDecodeError` traceback | exit 1, generic FAIL, no traceback |
| settlement | exit 1, uncaught `UnicodeDecodeError` traceback | exit 1, generic FAIL, no traceback |
| copied valid positive | PASS / 0 | PASS / 0 |

Regression controls (baseline/current exits): original nine `0/1/0/1/1/0/1/1/1`; R10 duplicate registry/session/settlement + unique positive `1/1/1/0`; R11 malformed-shape negatives + positive `1/1/1/1/0`; R12 malformed-syntax registry/session/settlement + valid positive `1/1/1/0`.

## Limits
Synthetic local inputs only. No provider, daemon, authentication, or live runtime operation was invoked. No claim about filesystem I/O errors, which remain uncaught, or behavior for encodings other than invalid UTF-8.
