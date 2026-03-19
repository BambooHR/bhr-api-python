#!/usr/bin/env python3
"""
Update Error Documentation — runs both exception generation scripts.

1. generate_exceptions.py — updates exception classes in bamboohr_sdk/exceptions.py
2. generate_error_docs.py — generates docs/Exceptions/ from mustache templates

Usage:
    python scripts/update_error_docs.py

Reference: PHP SDK scripts/update_error_docs.sh
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"


def run_script(name: str) -> bool:
	"""Run a sibling script and stream its output. Returns True on success."""
	script = SCRIPTS_DIR / name
	if not script.exists():
		print(f"Error: {name} not found at {script}", file=sys.stderr)
		return False

	result = subprocess.run(
		[sys.executable, str(script)],
		cwd=PROJECT_ROOT,
	)
	return result.returncode == 0


def main() -> int:
	print("Updating error documentation...\n")

	exceptions_ok = run_script("generate_exceptions.py")
	if not exceptions_ok:
		print("  Warning: generate_exceptions.py failed — exception classes may not be updated")
	print()

	docs_ok = run_script("generate_error_docs.py")
	if not docs_ok:
		print("  Warning: generate_error_docs.py failed — exception docs may not be updated")

	print()
	if exceptions_ok and docs_ok:
		print("Error documentation update complete!")
	else:
		print("Error documentation update completed with warnings.")
	print("- Exception classes: bamboohr_sdk/exceptions.py")
	print("- Exception index: docs/Exceptions/Exceptions.md")
	print("- Exception docs: docs/Exceptions/Classes/")

	return 0 if docs_ok else 1


if __name__ == "__main__":
	sys.exit(main())
