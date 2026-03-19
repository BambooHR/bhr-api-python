#!/usr/bin/env python3
"""Post-generation pipeline for the BambooHR Python SDK.

Runs after openapi-generator has output to the project root.
Performs the following steps:
    1. Clean up unwanted generator artifacts
    2. Remove PublicAPIApi files (internal-only API)
    3. Strip PublicAPIApi references from FILES manifest and __init__.py files
    4. Format generated code with ruff
    5. Add custom headers to API documentation
    6. Clean up obsolete files (compare old vs new FILES manifest)

Usage:
    python scripts/post_generate.py
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PACKAGE_DIR = PROJECT_ROOT / "bamboohr_sdk"
DOCS_DIR = PROJECT_ROOT / "docs"
FILES_MANIFEST = PROJECT_ROOT / ".openapi-generator" / "FILES"


def cleanup_generator_artifacts() -> None:
    """Remove unwanted files the generator may leave at the project root."""
    print("Cleaning up generator artifacts...")

    for unwanted in [
        ".gitlab-ci.yml",
        ".github",
        "test-requirements.txt",
    ]:
        path = PROJECT_ROOT / unwanted
        if path.is_file():
            path.unlink()
            print(f"  Removed {unwanted}")
        elif path.is_dir():
            shutil.rmtree(path)
            print(f"  Removed {unwanted}/")


def remove_public_api() -> None:
    """Remove PublicAPIApi files and references (internal-only, not for SDK)."""
    print("Removing PublicAPIApi references...")

    # Files to delete
    targets = [
        PACKAGE_DIR / "api" / "public_api_api.py",
        PROJECT_ROOT / "test" / "test_public_api_api.py",
        DOCS_DIR / "PublicAPIApi.md",
    ]

    for target in targets:
        if target.exists():
            target.unlink()
            print(f"  Deleted: {target.relative_to(PROJECT_ROOT)}")

    # Strip from FILES manifest
    if FILES_MANIFEST.exists():
        lines = FILES_MANIFEST.read_text().splitlines()
        filtered = [line for line in lines if "PublicAPIApi" not in line and "public_api_api" not in line]
        FILES_MANIFEST.write_text("\n".join(filtered) + "\n")
        removed_count = len(lines) - len(filtered)
        if removed_count:
            print(f"  Removed {removed_count} entries from FILES manifest")

    # Strip from all Python files that may import/reference PublicAPIApi
    # This covers api/__init__.py, the main package __init__.py, etc.
    python_files_to_clean = [
        PACKAGE_DIR / "api" / "__init__.py",
        PACKAGE_DIR / "__init__.py",
    ]

    for pyfile in python_files_to_clean:
        if not pyfile.exists():
            continue
        lines = pyfile.read_text().splitlines()
        filtered = [line for line in lines if "PublicAPIApi" not in line and "public_api_api" not in line]
        if len(filtered) < len(lines):
            pyfile.write_text("\n".join(filtered) + "\n")
            removed = len(lines) - len(filtered)
            print(f"  Stripped {removed} PublicAPIApi reference(s) from {pyfile.relative_to(PROJECT_ROOT)}")

    # Strip from generated README if it exists
    readme = DOCS_DIR / "README.md"
    if readme.exists():
        content = readme.read_text()
        lines = content.splitlines()
        filtered = [line for line in lines if "PublicAPIApi" not in line and "public_api_api" not in line]
        readme.write_text("\n".join(filtered) + "\n")


def format_generated_code() -> None:
    """Format generated code with ruff."""
    print("Formatting generated code with ruff...")

    api_dir = PACKAGE_DIR / "api"
    model_dir = PACKAGE_DIR / "models"

    dirs_to_format = [str(d) for d in [api_dir, model_dir] if d.exists()]
    if not dirs_to_format:
        print("  No generated directories to format")
        return

    # Run ruff format
    result = subprocess.run(
        [sys.executable, "-m", "ruff", "format", *dirs_to_format],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    if result.returncode != 0:
        print(f"  Warning: ruff format returned {result.returncode}")
        if result.stderr:
            print(f"  {result.stderr.strip()}")
    else:
        print("  Formatting complete")

    # Run ruff check with auto-fix
    result = subprocess.run(
        [sys.executable, "-m", "ruff", "check", "--fix", *dirs_to_format],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    if result.returncode != 0 and result.stderr:
        print(f"  Warning: ruff check --fix: {result.stderr.strip()}")


def add_custom_headers_to_docs() -> None:
    """Add custom content to specific API documentation files."""
    print("Adding custom headers to API documentation...")

    # Define modifications as (file_path_relative_to_docs, content_to_add) pairs
    doc_modifications: list[tuple[str, str]] = [
        (
            "WebhooksApi.md",
            "Please also refer to this link for notes on security and an explanation "
            "of global & permissioned webhooks: "
            "https://documentation.bamboohr.com/docs/webhooks",
        ),
        # Add more entries here as needed:
        # ("AnotherApi.md", "Some other custom content"),
    ]

    for filename, content in doc_modifications:
        filepath = DOCS_DIR / filename
        if not filepath.exists():
            print(f"  Warning: {filepath.relative_to(PROJECT_ROOT)} not found, skipping")
            continue

        lines = filepath.read_text().splitlines()
        # Insert content after line 2 (after the title)
        if len(lines) >= 2:
            lines.insert(2, "")
            lines.insert(3, content)
            lines.insert(4, "")
            filepath.write_text("\n".join(lines) + "\n")
            print(f"  Added content to {filepath.relative_to(PROJECT_ROOT)}")


def fix_model_types() -> None:
    """Patch generated models where the API returns types that differ from the spec.

    The BambooHR API frequently returns string representations of numeric values
    (e.g. ``"64"`` instead of ``64``). The OpenAPI spec declares these as integers,
    which causes Pydantic ``StrictInt`` validation to reject the actual responses.

    This function applies targeted patches so the generated models accept what the
    API actually sends. Each patch is documented with the model, field, and the
    mismatch it corrects.
    """
    print("Fixing model type mismatches...")

    MODELS_DIR = PACKAGE_DIR / "models"

    # Each entry: (filename, old_text, new_text, description)
    patches: list[tuple[str, str, str, str]] = [
        # --- ID fields returned as strings instead of integers ---
        (
            "country_schema.py",
            "id: StrictInt | None = Field(default=None, description=\"Unique identifier for the country\")",
            "id: StrictInt | StrictStr | None = Field(default=None, description=\"Unique identifier for the country\")",
            "CountrySchema.id: API returns string IDs like '1'",
        ),
        (
            "time_off_types_and_default_hours_time_off_types_inner.py",
            "id: StrictInt = Field(description=\"Time off type ID\")",
            "id: StrictInt | StrictStr = Field(description=\"Time off type ID\")",
            "TimeOffTypesAndDefaultHoursTimeOffTypesInner.id: API returns string IDs like '64'",
        ),
        (
            "goals_aggregate_v1_comments_inner.py",
            "goal_id: StrictInt | None = Field(",
            "goal_id: StrictInt | StrictStr | None = Field(",
            "GoalsAggregateV1CommentsInner.goalId: API returns string IDs like '25'",
        ),
        (
            "goals_aggregate_v1_comments_inner.py",
            "comment_count: StrictInt | None = Field(",
            "comment_count: StrictInt | StrictStr | None = Field(",
            "GoalsAggregateV1CommentsInner.commentCount: API returns string counts",
        ),
        # --- Numeric amounts returned as strings ---
        (
            "time_off_types_and_default_hours_default_hours_inner.py",
            "amount: StrictFloat | StrictInt = Field(description=\"Default hours for the day\")",
            "amount: StrictFloat | StrictInt | StrictStr = Field(description=\"Default hours for the day\")",
            "TimeOffTypesAndDefaultHoursDefaultHoursInner.amount: API returns string '0'",
        ),
    ]

    # Ensure StrictStr is imported in files that need it.
    # Newline-anchored to avoid substring matching the already-patched line.
    import_patches: list[tuple[str, str, str, str]] = [
        (
            "goals_aggregate_v1_comments_inner.py",
            "from pydantic import BaseModel, ConfigDict, Field, StrictInt\n",
            "from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr\n",
            "GoalsAggregateV1CommentsInner: add StrictStr import",
        ),
    ]

    all_patches = import_patches + patches
    applied = 0
    total = len(all_patches) + 2  # +2 for the enum and structural patches below

    for filename, old_text, new_text, description in all_patches:
        filepath = MODELS_DIR / filename
        if not filepath.exists():
            print(f"  Skipped (file not found): {description}")
            continue

        content = filepath.read_text()
        if old_text not in content:
            if new_text in content:
                print(f"  Already applied: {description}")
                applied += 1
            else:
                print(f"  Warning - pattern not found: {description}")
            continue

        content = content.replace(old_text, new_text, 1)
        filepath.write_text(content)
        print(f"  Applied: {description}")
        applied += 1

    # --- Enum patch: GoalFiltersV1FiltersInner.id ---
    # Handled with simple replacements on the specific strings, not full lines,
    # so it works regardless of how ruff formats the surrounding code.
    desc = "GoalFiltersV1FiltersInner.id enum: API returns 'status-inProgress' (camelCase)"
    gfi_path = MODELS_DIR / "goal_filters_v1_filters_inner.py"
    if gfi_path.exists():
        gfi_content = gfi_path.read_text()
        if "status-inProgress" in gfi_content:
            print(f"  Already applied: {desc}")
            applied += 1
        else:
            gfi_content = gfi_content.replace(
                '"status-in_progress", "status-completed"',
                '"status-in_progress", "status-inProgress", "status-completed"',
            )
            gfi_content = gfi_content.replace(
                "'status-in_progress', 'status-completed'",
                "'status-in_progress', 'status-inProgress', 'status-completed'",
            )
            gfi_path.write_text(gfi_content)
            print(f"  Applied: {desc}")
            applied += 1
    else:
        print(f"  Skipped (file not found): {desc}")

    # --- Structural patch: GoalFiltersV1.from_dict ---
    # Handled separately because the old pattern is a subset of the new text,
    # which would cause duplication with simple str.replace.
    desc = "GoalFiltersV1.from_dict: handle list input (API returns array, not object)"
    gf_path = MODELS_DIR / "goal_filters_v1.py"
    if gf_path.exists():
        gf_content = gf_path.read_text()
        list_check = "if isinstance(obj, list):"
        if list_check in gf_content:
            print(f"  Already applied: {desc}")
            applied += 1
        else:
            anchor = "        if not isinstance(obj, dict):\n            return cls.model_validate(obj)"
            insertion = (
                "        if isinstance(obj, list):\n"
                '            return cls.model_validate({"filters": [GoalFiltersV1FiltersInner.from_dict(_item) for _item in obj]})\n'
                "\n"
            )
            if anchor in gf_content:
                gf_content = gf_content.replace(anchor, insertion + anchor, 1)
                gf_path.write_text(gf_content)
                print(f"  Applied: {desc}")
                applied += 1
            else:
                print(f"  Warning - pattern not found: {desc}")
    else:
        print(f"  Skipped (file not found): {desc}")

    print(f"  {applied}/{total} model patches applied")


def cleanup_obsolete_files() -> None:
    """Run the cleanup obsolete files script in force mode."""
    print("Cleaning up obsolete files...")

    cleanup_script = PROJECT_ROOT / "scripts" / "cleanup_obsolete_files.py"
    if not cleanup_script.exists():
        print("  Warning: cleanup_obsolete_files.py not found, skipping")
        return

    result = subprocess.run(
        [sys.executable, str(cleanup_script), "--force"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    print(result.stdout.strip())
    if result.returncode != 0 and result.stderr:
        print(f"  Warning: {result.stderr.strip()}")


def update_error_docs() -> None:
    """Update exception classes and generate exception documentation."""
    print("Updating exception classes and documentation...")

    update_script = PROJECT_ROOT / "scripts" / "update_error_docs.py"
    if not update_script.exists():
        print("  Warning: update_error_docs.py not found, skipping")
        return

    result = subprocess.run(
        [sys.executable, str(update_script)],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    print(result.stdout.strip())
    if result.returncode != 0:
        print(f"  Warning: update_error_docs.py returned {result.returncode}")
        if result.stderr:
            print(f"  {result.stderr.strip()}")


def main() -> int:
    print("Running post-generation pipeline...")

    cleanup_generator_artifacts()
    remove_public_api()
    format_generated_code()
    fix_model_types()
    add_custom_headers_to_docs()
    update_error_docs()
    cleanup_obsolete_files()

    print("Post-generation pipeline complete!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
