#!/usr/bin/env python3
"""Read-only, non-mission Git whitespace-gate audit; prints JSON to stdout."""

import argparse
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path


def run(command, *, stdin=None):
    completed = subprocess.run(command, input=stdin, text=True, capture_output=True, check=False)
    return {"command": command, "stdin": stdin, "exit_code": completed.returncode,
            "stdout": completed.stdout, "stderr": completed.stderr}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--revision", default="HEAD", help="commit to inspect (default: HEAD)")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[4]
    os.chdir(root)
    commit = run(["git", "rev-parse", "--verify", f"{args.revision}^{{commit}}"])
    if commit["exit_code"]:
        print(json.dumps({"revision_lookup": commit}, indent=2))
        return 2
    revision = commit["stdout"].strip()
    context = {
        "cwd": str(root), "commit": revision, "git_executable": shutil.which("git"),
        "git_version": run(["git", "--version"]), "python": sys.version,
        "platform": platform.platform(),
        "environment": {name: os.environ.get(name) for name in
                        ("PATH", "LANG", "LC_ALL", "GIT_CONFIG_NOSYSTEM",
                         "GIT_CONFIG_GLOBAL", "GIT_CONFIG_SYSTEM", "GIT_INDEX_FILE")},
    }
    changed = run(["git", "diff", "--name-only", f"{revision}^", revision])
    positive = run(["git", "diff", "--check", f"{revision}^", revision])
    negative = run(["git", "diff", "--no-index", "--check", "/dev/null", "/dev/stdin"],
                   stdin="negative-control trailing-space \n")
    # The negative control is an in-memory input, not an edited project file.
    observations = {
        "context": context, "changed_files": changed,
        "project_gate": positive, "negative_control": negative,
        "interpretation": {
            "project_gate": "pass" if positive["exit_code"] == 0 else "fail",
            "negative_control": "fail" if negative["exit_code"] != 0 else "unexpected-pass",
            "mission_goal": "not-assessed", "loop_stop": "not-assessed",
            "goal_complete_called": False,
        },
    }
    print(json.dumps(observations, indent=2, sort_keys=True))
    return 0 if (changed["exit_code"] == 0 and changed["stdout"]
                 and positive["exit_code"] == 0 and negative["exit_code"] != 0
                 and "trailing whitespace" in negative["stdout"] + negative["stderr"]) else 1


if __name__ == "__main__":
    sys.exit(main())
