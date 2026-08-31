#!/usr/bin/env python3
"""Keep ``BambooHRClient``'s convenience accessors in sync with the generated APIs.

Why this exists
---------------
``bamboohr_sdk/client/bamboohr_client.py`` is hand-written, but a block of it
is pure boilerplate: one three-line accessor per generated API class. That
block used to be maintained by hand, which meant the SDK silently broke
whenever the upstream spec renamed a tag.

That is not hypothetical. The spec renamed ``Tabular Data`` -> ``Employee
Tables`` and ``Last Change Information`` -> ``Change Tracking``. The generator
correctly produced ``employee_tables_api.py`` / ``change_tracking_api.py``, the
obsolete-file cleanup correctly deleted the old modules, and the hand-written
accessors were left importing modules that no longer existed. The regen
pipeline failed with ``ModuleNotFoundError`` on code nobody had touched. The
same spec also added ~15 brand-new tags that got no accessors at all, because
adding them was a manual step somebody had to remember.

So the accessor block is now generated from the one source of truth that the
generator itself maintains: ``bamboohr_sdk/api/__init__.py``.

Preserving hand-written code
----------------------------
This script only ever rewrites the text *between* two marker comments:

    # --- BEGIN GENERATED ACCESSORS ---
    # --- END GENERATED ACCESSORS ---

Everything outside those markers is byte-for-byte untouched. That is the whole
safety property, and it's what lets hand-written accessors coexist with
generated ones. ``manual()`` is the live example: ``ManualApi`` is hand-written
(it never appears in the generated ``api/__init__.py``), it has a real
docstring with usage examples, and it lives *below* the END marker where this
script cannot reach it.

If the markers are missing, the script refuses to do anything rather than
guessing where the block belongs.

Usage
-----
    python scripts/sync_accessors.py            # rewrite the block in place
    python scripts/sync_accessors.py --check    # exit 1 if out of sync (CI)
    python scripts/sync_accessors.py --diff     # show what would change
"""

from __future__ import annotations

import argparse
import difflib
import keyword
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
API_INIT = PROJECT_ROOT / "bamboohr_sdk" / "api" / "__init__.py"
CLIENT_FILE = PROJECT_ROOT / "bamboohr_sdk" / "client" / "bamboohr_client.py"

BEGIN_MARKER = "    # --- BEGIN GENERATED ACCESSORS ---"
END_MARKER = "    # --- END GENERATED ACCESSORS ---"

# A second generated region, at module level, holding the TYPE_CHECKING
# imports that give the accessors real return annotations. It has to be
# separate from the method block because the imports belong at the top of
# the file, and it has to be generated for the same reason the methods do:
# a hand-maintained import list goes stale on the next tag rename.
IMPORTS_BEGIN_MARKER = "# --- BEGIN GENERATED ACCESSOR IMPORTS ---"
IMPORTS_END_MARKER = "# --- END GENERATED ACCESSOR IMPORTS ---"

IMPORT_RE = re.compile(
    r"^from\s+bamboohr_sdk\.api\.(?P<module>\w+)\s+import\s+(?P<cls>\w+)\s*$",
    re.MULTILINE,
)

# Method names on BambooHRClient that a generated accessor must never shadow.
# If the spec ever grows a tag that collides with one of these, we want a loud
# failure here rather than an accessor quietly clobbering `build()` or
# `configuration`. Kept as a literal list (not introspected off the class) so
# that importing the SDK is not a prerequisite for running this script.
RESERVED_NAMES = frozenset(
    {
        "api_client",
        "auth_builder",
        "build",
        "configuration",
        "get_api",
        "last_request_id",
        "manual",
        "oauth2_middleware",
        "timeout",
        "token_manager",
        "with_api_key",
        "with_debug",
        "with_host",
        "with_http_client",
        "with_logging",
        "with_oauth",
        "with_oauth_refresh",
        "with_retries",
        "with_timeout",
        "for_company",
        "on_token_refresh",
    }
)


class SyncError(RuntimeError):
    """Raised when the accessor block cannot be generated safely."""


def discover_apis(api_init: Path) -> list[tuple[str, str]]:
    """Read the generated API package index and return its ``(module, class)`` pairs.

    ``bamboohr_sdk/api/__init__.py`` is written by openapi-generator on every
    run and then post-processed (``PublicAPIApi`` is stripped out), so it is
    the most accurate view of what actually exists. Hand-written APIs such as
    ``ManualApi`` are deliberately absent from it.

    :param api_init: Path to ``bamboohr_sdk/api/__init__.py``.
    :return: ``(module_name, class_name)`` pairs, sorted by module name.
    :raises SyncError: If the file is missing or contains no API imports.
    """
    if not api_init.is_file():
        raise SyncError(f"generated API index not found: {api_init}")

    matches = [(match["module"], match["cls"]) for match in IMPORT_RE.finditer(api_init.read_text())]
    if not matches:
        raise SyncError(
            f"no `from bamboohr_sdk.api.<module> import <Class>` lines found in {api_init}. "
            "Has the generator run?"
        )

    return sorted(set(matches))


def method_name_for(module: str) -> str:
    """Derive the accessor method name from a generated module name.

    ``employee_tables_api`` -> ``employee_tables``. The generator already
    emits snake_case module names, so this is just suffix removal.

    :param module: Generated module name, e.g. ``"change_tracking_api"``.
    :return: The snake_case accessor method name.
    """
    return module[: -len("_api")] if module.endswith("_api") else module


def human_name_for(cls: str) -> str:
    """Turn an API class name into the prose used in the accessor docstring.

    ``EmployeeTablesApi`` -> ``"Employee Tables"``.

    The second alternation splits a run of capitals off a following word, but
    only after at least two capitals, so ``APIKeyApi`` reads as ``"API Key"``
    while ``OAuthApi`` stays ``"OAuth"`` instead of becoming ``"O Auth"``.

    :param cls: Generated API class name, e.g. ``"EmployeeTablesApi"``.
    :return: A space-separated display name.
    """
    stem = cls[: -len("Api")] if cls.endswith("Api") else cls
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z]{2})(?=[A-Z][a-z])", " ", stem)


def render_imports(apis: list[tuple[str, str]]) -> str:
    """Render the module-level ``TYPE_CHECKING`` import region.

    These imports exist purely so the accessors can carry real return
    annotations. They are guarded by ``TYPE_CHECKING`` so importing the
    client stays cheap — the runtime import still happens lazily inside each
    accessor, preserving the existing import-on-first-use behaviour.

    :param apis: ``(module_name, class_name)`` pairs from :func:`discover_apis`.
    :return: The import region text, newline-terminated.
    """
    lines = [
        IMPORTS_BEGIN_MARKER,
        "# Generated by scripts/sync_accessors.py — do not edit by hand.",
        "if TYPE_CHECKING:",
    ]
    lines += [f"    from bamboohr_sdk.api.{module} import {cls}" for module, cls in apis]
    lines += [IMPORTS_END_MARKER, ""]
    return "\n".join(lines)


def render_block(apis: list[tuple[str, str]]) -> str:
    """Render the full generated accessor block, markers included.

    :param apis: ``(module_name, class_name)`` pairs from :func:`discover_apis`.
    :return: The block text, newline-terminated.
    :raises SyncError: If a derived method name is unusable (reserved,
        duplicated, or a Python keyword).
    """
    lines = [
        BEGIN_MARKER,
        "    # Generated by scripts/sync_accessors.py from bamboohr_sdk/api/__init__.py.",
        "    # Do not edit by hand — run `make sync-accessors` instead. Hand-written",
        "    # accessors (e.g. manual()) belong BELOW the END marker.",
    ]

    seen: dict[str, str] = {}
    for module, cls in apis:
        name = method_name_for(module)

        if name in RESERVED_NAMES:
            raise SyncError(
                f"generated accessor {name}() for {cls} collides with an existing "
                f"BambooHRClient member. Rename the spec tag, or add an explicit "
                f"mapping in scripts/sync_accessors.py."
            )
        if keyword.iskeyword(name):
            raise SyncError(f"generated accessor name {name!r} (for {cls}) is a Python keyword.")
        if name in seen:
            raise SyncError(f"generated accessor name {name!r} produced by both {seen[name]} and {cls}.")
        seen[name] = cls

        # The blank line between the local import and the return is not
        # cosmetic: `ruff format` inserts one there. Emitting it here keeps
        # the block a fixed point, so `make format` cannot leave the tree in
        # a state where `make check-accessors` reports a spurious drift.
        lines += [
            "",
            f"    def {name}(self) -> {cls}:",
            f'        """Access the {human_name_for(cls)} API."""',
            f"        from bamboohr_sdk.api.{module} import {cls}",
            "",
            f"        return self.get_api({cls})",
        ]

    lines += ["", END_MARKER, ""]
    return "\n".join(lines)


def apply_region(source: str, block: str, begin: str, end: str) -> str:
    """Splice a rendered region into *source*, replacing everything between markers.

    This is the whole safety mechanism: only the text between *begin* and
    *end* is touched, so hand-written code above, below, and between regions
    survives byte-for-byte.

    :param source: Current file contents.
    :param block: Rendered replacement text, markers included.
    :param begin: The opening marker line.
    :param end: The closing marker line.
    :return: The updated source text.
    :raises SyncError: If the markers are absent, duplicated, or out of order.
    """
    for marker, label in ((begin, "BEGIN"), (end, "END")):
        count = source.count(marker)
        if count == 0:
            raise SyncError(
                f"{label} marker {marker.strip()!r} not found in {CLIENT_FILE.name}. "
                f"Add the marker pair back around the generated region."
            )
        if count > 1:
            raise SyncError(f"{label} marker {marker.strip()!r} appears {count} times; expected exactly one.")

    start_idx = source.index(begin)
    end_idx = source.index(end)
    if end_idx < start_idx:
        raise SyncError(f"END marker precedes BEGIN marker for {begin.strip()!r} in {CLIENT_FILE.name}.")

    return source[:start_idx] + block + source[end_idx + len(end) + 1 :]


def sync_source(source: str, apis: list[tuple[str, str]]) -> str:
    """Apply both generated regions (TYPE_CHECKING imports and accessors).

    :param source: Current contents of ``bamboohr_client.py``.
    :param apis: ``(module_name, class_name)`` pairs from :func:`discover_apis`.
    :return: The fully synced source text.
    :raises SyncError: If either region cannot be applied safely.
    """
    source = apply_region(source, render_imports(apis), IMPORTS_BEGIN_MARKER, IMPORTS_END_MARKER)
    return apply_region(source, render_block(apis), BEGIN_MARKER, END_MARKER)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Do not write; exit 1 if the accessors are out of sync with the generated APIs.",
    )
    parser.add_argument(
        "--diff",
        action="store_true",
        help="Print a unified diff of the pending changes without writing. Implies --check semantics for output only.",
    )
    args = parser.parse_args()

    try:
        apis = discover_apis(API_INIT)
        current = CLIENT_FILE.read_text()
        updated = sync_source(current, apis)
    except SyncError as syncException:
        print(f"sync_accessors: {syncException}", file=sys.stderr)
        return 2

    if args.diff or (args.check and current != updated):
        diff = difflib.unified_diff(
            current.splitlines(keepends=True),
            updated.splitlines(keepends=True),
            fromfile=f"a/{CLIENT_FILE.relative_to(PROJECT_ROOT)}",
            tofile=f"b/{CLIENT_FILE.relative_to(PROJECT_ROOT)}",
        )
        sys.stdout.writelines(diff)

    if current == updated:
        print(f"sync_accessors: up to date ({len(apis)} generated accessors).")
        return 0

    if args.check:
        print(
            "sync_accessors: accessors are OUT OF SYNC with the generated APIs. "
            "Run `make sync-accessors` and commit the result.",
            file=sys.stderr,
        )
        return 1

    # --diff is a preview: report what would change, but never touch the file.
    if args.diff:
        print("sync_accessors: --diff is read-only; re-run without it to apply.")
        return 0

    CLIENT_FILE.write_text(updated)
    print(f"sync_accessors: rewrote {len(apis)} generated accessors in {CLIENT_FILE.relative_to(PROJECT_ROOT)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
