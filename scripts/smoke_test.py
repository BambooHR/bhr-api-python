#!/usr/bin/env python3
"""
Smoke test: validates all generated modules can be imported without errors.
Run after `make generate` to confirm the generated output is structurally sound.
"""

import sys
import traceback

errors = []
loaded = 0


def try_import(module_path: str) -> None:
    global loaded
    try:
        __import__(module_path)
        loaded += 1
    except Exception:
        errors.append((module_path, traceback.format_exc()))


try_import("bamboohr_sdk.api")
try_import("bamboohr_sdk.models")

# Wildcard-style: import all names exported from each package
for pkg in ("bamboohr_sdk.api", "bamboohr_sdk.models"):
    try:
        mod = __import__(pkg, fromlist=["*"])
        names = getattr(mod, "__all__", [n for n in dir(mod) if not n.startswith("_")])
        for name in names:
            full = f"{pkg}.{name}" if "." not in name else name
            try_import(full)
    except Exception:
        errors.append((pkg, traceback.format_exc()))

if errors:
    print(f"Smoke test FAILED — {len(errors)} error(s):", file=sys.stderr)
    for module_path, tb in errors:
        print(f"  {module_path}:\n{tb}", file=sys.stderr)
    sys.exit(1)

print(f"Smoke test passed — {loaded} modules loaded successfully.")
sys.exit(0)
