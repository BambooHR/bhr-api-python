#!/usr/bin/env python3
"""
Bump the project version in pyproject.toml per a semver classification.

Per the SPN-2931 spec, only `minor` and `patch` levels actually mutate
pyproject.toml. `major` is skipped (a human takes that decision), and
`none` is a no-op.

Usage:
    bump_version.py LEVEL [--pyproject PATH] [--dry-run]

LEVEL must be one of: major, minor, patch, none.

Outputs (written to $GITHUB_OUTPUT if set, also printed to stdout):
    bumped=true|false       — whether the version line was rewritten
    old_version=X.Y.Z       — version before this script ran
    new_version=X.Y.Z       — version after this script ran (== old when bumped=false)

Exit codes:
    0  Success.
    1  Bad arguments or pyproject.toml malformed.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

VALID_LEVELS = {"major", "minor", "patch", "none"}
VERSION_LINE_RE = re.compile(r'^(version\s*=\s*")(\d+)\.(\d+)\.(\d+)(".*)$', re.MULTILINE)


def emit_output(key: str, value: str) -> None:
    line = f"{key}={value}"
    print(line)
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        with open(output_path, "a", encoding="utf-8") as handle:
            handle.write(line + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("level", choices=sorted(VALID_LEVELS))
    parser.add_argument("--pyproject", default="pyproject.toml")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    pyproject = Path(args.pyproject)
    if not pyproject.exists():
        print(f"bump_version: pyproject not found: {pyproject}", file=sys.stderr)
        return 1

    content = pyproject.read_text(encoding="utf-8")
    match = VERSION_LINE_RE.search(content)
    if not match:
        print(
            f"bump_version: no `version = \"X.Y.Z\"` line found in {pyproject}",
            file=sys.stderr,
        )
        return 1

    prefix, major_s, minor_s, patch_s, suffix = match.groups()
    major, minor, patch = int(major_s), int(minor_s), int(patch_s)
    old_version = f"{major}.{minor}.{patch}"

    if args.level == "minor":
        new_version = f"{major}.{minor + 1}.0"
    elif args.level == "patch":
        new_version = f"{major}.{minor}.{patch + 1}"
    else:
        # major or none — caller asked us to skip writing.
        emit_output("bumped", "false")
        emit_output("old_version", old_version)
        emit_output("new_version", old_version)
        return 0

    new_content = (
        content[: match.start()]
        + f"{prefix}{new_version}{suffix}"
        + content[match.end():]
    )

    if not args.dry_run:
        pyproject.write_text(new_content, encoding="utf-8")

    emit_output("bumped", "true")
    emit_output("old_version", old_version)
    emit_output("new_version", new_version)
    return 0


if __name__ == "__main__":
    sys.exit(main())
