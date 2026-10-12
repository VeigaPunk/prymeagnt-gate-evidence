#!/usr/bin/env python3
"""Read-only check of the R5 session-boundary receipt and documented rows."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
receipt = json.loads((root / "live/observed-child-goal-r5.json").read_text())
assert receipt["query"] == "await goal.get()"
assert receipt["scope"] == "this child session"
assert receipt["result"] == {"goal": None, "remaining_tokens": None, "completion_budget_report": None}
assert receipt["parent_goal"] == "not-queried"
assert receipt["autonomous_receipt"] == "not-observed"
text = (root / "knowledge/goal-read-boundary-r5.md").read_text()
rows = re.findall(r"^\| (R[0-4]) \|", text, re.M)
assert rows == ["R0", "R1", "R2", "R3", "R4"], rows
print("child null goal read recorded; parent not queried; five distinct decision rows")
