#!/usr/bin/env python3
"""Read-only verifier for a sanitized RLM child admission/settlement receipt."""
import argparse
import json
from pathlib import Path
import sys


class DuplicateKeyError(ValueError):
    pass


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def parse_json(text):
    return json.loads(text, object_pairs_hook=reject_duplicate_keys)
EXPECTED_PROVIDER = "openai-codex"
EXPECTED_MODEL = "gpt-6-luna"


def load(path):
    with Path(path).open(encoding="utf-8") as stream:
        return parse_json(stream.read())


def verify(registry_path, session_path, settlement_path):
    errors = []
    try:
        registry = load(registry_path)
        settlement = load(settlement_path)
    except DuplicateKeyError:
        return ["input contains duplicate JSON object keys"]
    except json.JSONDecodeError:
        return ["input contains malformed JSON syntax"]
    except UnicodeDecodeError:
        return ["input contains invalid UTF-8 encoding"]
    if not isinstance(registry, dict) or not isinstance(settlement, dict):
        return ["input JSON shape is invalid"]
    model = registry.get("model")
    if not isinstance(model, dict):
        return ["input JSON shape is invalid"]
    if registry.get("type") != "rlm_subagent":
        errors.append("registry type mismatch (expected rlm_subagent)")
    if model.get("provider") != EXPECTED_PROVIDER:
        errors.append("registry provider mismatch")
    if model.get("modelId") != EXPECTED_MODEL:
        errors.append("registry model mismatch")
    if registry.get("status") != "completed":
        errors.append("registry is not completed")
    if settlement.get("status") != "done" or settlement.get("settled") is not True:
        errors.append("collect receipt is not done and settled")
    if settlement.get("error") is not None:
        errors.append("collect receipt has an error")

    child_id = registry.get("childId")
    if not isinstance(child_id, str) or not child_id:
        errors.append("registry childId is missing")
    session_file = Path(session_path)
    registered_session = registry.get("sessionFile")
    if not isinstance(registered_session, str) or not registered_session:
        errors.append("registry sessionFile is missing")
    elif Path(registered_session).resolve() != session_file.resolve():
        errors.append("session path does not match registry sessionFile")
    if child_id and session_file.parent.name != child_id:
        errors.append("session path child ID does not match registry childId")
    if settlement.get("rlm_child_id") != child_id:
        errors.append("collect child ID does not match registry childId")

    try:
        events = [parse_json(line) for line in session_file.read_text(encoding="utf-8").splitlines() if line.strip()]
    except DuplicateKeyError:
        return ["input contains duplicate JSON object keys"]
    except json.JSONDecodeError:
        return ["input contains malformed JSON syntax"]
    except UnicodeDecodeError:
        return ["input contains invalid UTF-8 encoding"]
    if any(not isinstance(event, dict) for event in events):
        return ["input JSON shape is invalid"]
    for event in events:
        if event.get("type") == "message":
            message = event.get("message")
            if not isinstance(message, dict):
                return ["input JSON shape is invalid"]
            content = message.get("content", [])
            if not isinstance(content, list) or any(not isinstance(part, dict) for part in content):
                return ["input JSON shape is invalid"]
    model_changes = [e for e in events if e.get("type") == "model_change"]
    if not model_changes:
        errors.append("session has no model_change provenance")
    elif any(
        (event.get("provider"), event.get("modelId")) != (EXPECTED_PROVIDER, EXPECTED_MODEL)
        for event in model_changes
    ):
        errors.append("session provider/model mismatch")
    replies = [
        part.get("text", "")
        for event in events
        if event.get("type") == "message" and event.get("message", {}).get("role") == "assistant"
        for part in event.get("message", {}).get("content", [])
        if part.get("type") == "text"
    ]
    if not replies:
        errors.append("session has no assistant response")
    elif len(replies) != 1:
        errors.append("session has multiple assistant text replies")
    elif settlement.get("answer_preview") != replies[0]:
        errors.append("collect answer does not match session assistant reply")
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
    print("PASS: expected selector, correlated child, exact reply, and terminal settlement")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
