#!/usr/bin/env python3
"""Compare a parent-supplied redacted goal snapshot with a real read-only Git check.

Never reads a goal itself. Never classifies autonomous state, acceptance, or stop.
"""
import argparse
from datetime import datetime, timezone
import json
import re
import subprocess
import sys


def utc():
    return datetime.now(timezone.utc).isoformat()


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON object key")
        result[key] = value
    return result


def parse_status(raw):
    data = json.loads(raw, object_pairs_hook=_unique_object)
    if not isinstance(data, dict) or set(data) != {"goal", "observed_utc"}:
        raise ValueError("expected exactly redacted goal and UTC clock keys")
    timestamp = data["observed_utc"]
    if not isinstance(timestamp, str) or len(timestamp) > 40:
        raise ValueError("invalid UTC timestamp")
    # RFC 3339 §4.3 assigns -00:00 an unknown-local-offset meaning, unlike
    # Z/+00:00; it is not evidence that this clock value is UTC-referenced.
    if re.search(r"-00:00$", timestamp):
        raise ValueError("unknown local offset is not accepted as UTC")
    # RFC3339 permits arbitrary fractional-second precision. datetime stores
    # only microseconds, so use a validation copy and retain the original value.
    # datetime.fromisoformat accepts non-RFC3339 variants (space separator,
    # basic +0000 offset); require the RFC3339 timestamp shape first.
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:[Zz]|[+-]\d{2}:\d{2})", timestamp):
        raise ValueError("invalid UTC timestamp syntax")
    try:
        zone_match = re.search(r"(?:[Zz]|[+-]\d{2}:\d{2})$", timestamp)
        if zone_match is None:
            raise ValueError("invalid UTC timestamp")
        body, zone = timestamp[:zone_match.start()], zone_match.group(0)
        if "." in body:
            head, fraction = body.rsplit(".", 1)
            body = head + "." + fraction[:6]
        validation_timestamp = body + zone
        clock = datetime.fromisoformat(validation_timestamp[:-1] + "+00:00"
                                       if validation_timestamp[-1:] in "Zz" else validation_timestamp)
    except ValueError as exc:
        raise ValueError("invalid UTC timestamp") from exc
    if clock.utcoffset() is None or clock.utcoffset().total_seconds() != 0:
        raise ValueError("clock must be UTC")
    goal = data["goal"]
    if goal is None:
        return {"observed_utc": timestamp, "goal_present": False, "status": None,
                "tokens_used": None, "time_used_seconds": None, "token_budget": None}
    if not isinstance(goal, dict) or set(goal) != {"status", "tokens_used", "time_used_seconds", "token_budget"}:
        raise ValueError("goal must contain exactly status and three clock fields")
    status = goal["status"]
    if not isinstance(status, str) or not re.fullmatch(r"[a-z][a-z_-]{0,31}", status):
        raise ValueError("invalid status (no free text allowed)")
    for key in ("tokens_used", "time_used_seconds", "token_budget"):
        value = goal[key]
        if value is not None and (type(value) not in (int, float) or value < 0 or value == float("inf") or value != value):
            raise ValueError("invalid clock field")
    return {"observed_utc": timestamp, "goal_present": True, **goal}


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, help="full immutable Git commit hash")
    parser.add_argument("--candidate", required=True, help="full immutable Git commit hash")
    args = parser.parse_args()
    # A whitelist avoids interpreting user-supplied revisions as flags/ref expressions.
    if not all(re.fullmatch(r"[0-9a-f]{40}", v) for v in (args.base, args.candidate)):
        parser.error("base/candidate must each be a full 40-character lowercase commit hash")
    try:
        status = parse_status(sys.stdin.read())
    except (ValueError, TypeError) as exc:
        # Do not echo input, which might contain an objective or secrets.
        print("invalid redacted status; no gate run", file=sys.stderr)
        return 2
    for revision in (args.base, args.candidate):
        resolved = git("rev-parse", "--verify", f"{revision}^{{commit}}")
        if resolved.returncode != 0 or resolved.stdout.strip() != revision:
            print("invalid commit; no gate run", file=sys.stderr)
            return 2
    started = utc()
    observed = git("diff", "--check", args.base, args.candidate)
    ended = utc()
    # Deliberately omit stdout/stderr: Git failures may reveal private file paths or patch text.
    receipt = {
        "schema": "parent-redacted-goal-v1",
        "status_provenance": "parent-supplied projection; not verified by this program",
        "goal_snapshot": status,
        "gate": {"kind": "read-only Git diff --check", "base": args.base,
                 "candidate": args.candidate, "started_utc": started, "ended_utc": ended,
                 "exit_code": observed.returncode,
                 "result": "pass" if observed.returncode == 0 else "nonzero-unclassified"},
        "comparison": "same recording, independent inputs; no causal inference",
        "autonomous_gate": "not-assessed", "acceptance": "not-assessed",
        "loop_stop": "not-assessed", "mission_goal": "not-assessed",
        "goal_complete_called": False,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if observed.returncode == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
