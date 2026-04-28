#!/usr/bin/env python3
"""
Smoke test: validates all generated modules can be imported without errors.
Run after `make generate` to confirm the generated output is structurally sound.
"""

import sys
import traceback

errors: list[tuple[str, str]] = []
attrs_checked = 0


def fail(name: str) -> None:
    errors.append((name, traceback.format_exc()))


for pkg_name in ("bamboohr_sdk", "bamboohr_sdk.api", "bamboohr_sdk.models"):
    try:
        __import__(pkg_name)
    except Exception:
        fail(pkg_name)

# Verify each name exported by the api/models packages resolves to something
# (catches broken __init__.py re-exports).
for pkg_name in ("bamboohr_sdk.api", "bamboohr_sdk.models"):
    try:
        mod = sys.modules.get(pkg_name) or __import__(pkg_name, fromlist=["*"])
    except Exception:
        fail(pkg_name)
        continue
    names = getattr(mod, "__all__", None) or [
        n for n in dir(mod) if not n.startswith("_")
    ]
    for name in names:
        try:
            getattr(mod, name)
            attrs_checked += 1
        except Exception:
            fail(f"{pkg_name}.{name}")

if errors:
    print(f"Smoke test FAILED — {len(errors)} error(s):", file=sys.stderr)
    for name, tb in errors:
        print(f"  {name}:\n{tb}", file=sys.stderr)
    sys.exit(1)

print(f"Smoke test passed — {attrs_checked} exports resolved successfully.")
sys.exit(0)
