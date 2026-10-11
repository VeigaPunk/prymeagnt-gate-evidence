#!/usr/bin/env python3
"""Read-only verifier for a sanitized RLM child admission/settlement receipt."""
import argparse
import json
from pathlib import Path
import sys

EXPECTED_PROVIDER = "openai-codex"
EXPECTED_MODEL = "gpt-6-luna"


def load(path):
    with Path(path).open(encoding="utf-8") as stream:
        return json.load(stream)


def verify(registry_path, session_path, settlement_path):
    errors = []
    registry = load(registry_path)
    settlement = load(settlement_path)
    if registry.get("model", {}).get("provider") != EXPECTED_PROVIDER:
        errors.append("registry provider mismatch")
    if registry.get("model", {}).get("modelId") != EXPECTED_MODEL:
        errors.append("registry model mismatch")
    if registry.get("status") != "completed":
        errors.append("registry is not completed")
    if settlement.get("status") != "done" or settlement.get("settled") is not True:
        errors.append("collect receipt is not done and settled")
    if settlement.get("error") is not None:
        errors.append("collect receipt has an error")

    events = [json.loads(line) for line in Path(session_path).read_text(encoding="utf-8").splitlines() if line.strip()]
    model_changes = [e for e in events if e.get("type") == "model_change"]
    if not model_changes:
        errors.append("session has no model_change provenance")
    elif (model_changes[0].get("provider"), model_changes[0].get("modelId")) != (EXPECTED_PROVIDER, EXPECTED_MODEL):
        errors.append("session provider/model mismatch")
    if not any(e.get("type") == "message" and e.get("message", {}).get("role") == "assistant" for e in events):
        errors.append("session has no assistant response")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", help="rlm-subagent.json")
    parser.add_argument("session", help="session JSONL")
    parser.add_argument("settlement", help="sanitized rlm.collect result JSON")
    args = parser.parse_args()
    errors = verify(args.registry, args.session, args.settlement)
    if errors:
        print("FAIL: " + "; ".join(errors), file=sys.stderr)
        return 1
    print("PASS: expected selector provenance and terminal settled receipt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
