"""Tests for scripts/sync_accessors.py.

The important property under test is the safety one: the script rewrites only
the marked region and never touches hand-written code around it. Everything
else (naming, collision detection) exists to make the regen pipeline fail
loudly instead of producing a client that imports missing modules.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "sync_accessors.py"


def _load_module():
    """Import sync_accessors.py by path (scripts/ is not an importable package)."""
    spec = importlib.util.spec_from_file_location("sync_accessors", SCRIPT_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["sync_accessors"] = module
    spec.loader.exec_module(module)
    return module


sync_accessors = _load_module()


CLIENT_STUB = '''from __future__ import annotations

from typing import TYPE_CHECKING

# --- BEGIN GENERATED ACCESSOR IMPORTS ---
# --- END GENERATED ACCESSOR IMPORTS ---

HAND_WRITTEN_CONSTANT = "must survive"


class BambooHRClient:
    """Docstring that must survive."""

    def build(self):
        return self

    # --- BEGIN GENERATED ACCESSORS ---

    def stale_accessor(self):
        """Access the Stale API."""
        from bamboohr_sdk.api.stale_api import StaleApi
        return self.get_api(StaleApi)

    # --- END GENERATED ACCESSORS ---

    def manual(self):
        """Hand-written accessor that must never be regenerated."""
        from bamboohr_sdk.api.manual_api import ManualApi
        return self.get_api(ManualApi)
'''


class TestMethodNaming:
    def test_strips_api_suffix(self):
        assert sync_accessors.method_name_for("employee_tables_api") == "employee_tables"
        assert sync_accessors.method_name_for("change_tracking_api") == "change_tracking"

    def test_leaves_module_without_suffix_alone(self):
        assert sync_accessors.method_name_for("employees") == "employees"

    def test_human_name_splits_camel_case(self):
        assert sync_accessors.human_name_for("EmployeeTablesApi") == "Employee Tables"
        assert sync_accessors.human_name_for("ChangeTrackingApi") == "Change Tracking"
        assert sync_accessors.human_name_for("HoursApi") == "Hours"

    def test_human_name_keeps_acronyms_together(self):
        # A single leading capital is part of the word, not an acronym.
        assert sync_accessors.human_name_for("OAuthApi") == "OAuth"
        # Two or more capitals is an acronym and does split off the next word.
        assert sync_accessors.human_name_for("APIKeyApi") == "API Key"
        assert sync_accessors.human_name_for("PayGradesBandsApi") == "Pay Grades Bands"


class TestDiscoverApis:
    def test_reads_import_lines(self, tmp_path):
        api_init = tmp_path / "__init__.py"
        api_init.write_text(
            "# flake8: noqa\n\n"
            "from bamboohr_sdk.api.employees_api import EmployeesApi\n"
            "from bamboohr_sdk.api.change_tracking_api import ChangeTrackingApi\n"
        )
        assert sync_accessors.discover_apis(api_init) == [
            ("change_tracking_api", "ChangeTrackingApi"),
            ("employees_api", "EmployeesApi"),
        ]

    def test_missing_file_raises(self, tmp_path):
        with pytest.raises(sync_accessors.SyncError, match="not found"):
            sync_accessors.discover_apis(tmp_path / "nope.py")

    def test_empty_index_raises(self, tmp_path):
        api_init = tmp_path / "__init__.py"
        api_init.write_text("# flake8: noqa\n")
        with pytest.raises(sync_accessors.SyncError, match="Has the generator run"):
            sync_accessors.discover_apis(api_init)


class TestRenderBlock:
    def test_emits_one_accessor_per_api(self):
        block = sync_accessors.render_block([("employee_tables_api", "EmployeeTablesApi"), ("hours_api", "HoursApi")])
        assert "def employee_tables(self) -> EmployeeTablesApi:" in block
        assert "from bamboohr_sdk.api.employee_tables_api import EmployeeTablesApi" in block
        assert "return self.get_api(EmployeeTablesApi)" in block
        assert '"""Access the Employee Tables API."""' in block
        assert "def hours(self) -> HoursApi:" in block

    def test_block_is_marker_delimited(self):
        block = sync_accessors.render_block([("hours_api", "HoursApi")])
        assert block.startswith(sync_accessors.BEGIN_MARKER)
        assert sync_accessors.END_MARKER in block

    def test_reserved_name_collision_raises(self):
        # A spec tag named "Build" would generate build() and clobber the
        # builder's own build() method.
        with pytest.raises(sync_accessors.SyncError, match="collides"):
            sync_accessors.render_block([("build_api", "BuildApi")])

    def test_manual_is_reserved(self):
        # ManualApi is hand-written; a generated manual() would shadow it.
        with pytest.raises(sync_accessors.SyncError, match="collides"):
            sync_accessors.render_block([("manual_api", "ManualApi")])

    def test_duplicate_method_name_raises(self):
        with pytest.raises(sync_accessors.SyncError, match="produced by both"):
            sync_accessors.render_block([("hours_api", "HoursApi"), ("hours", "HoursAliasApi")])


class TestRenderImports:
    def test_emits_type_checking_guarded_imports(self):
        imports = sync_accessors.render_imports(
            [("employee_tables_api", "EmployeeTablesApi"), ("hours_api", "HoursApi")]
        )
        assert "if TYPE_CHECKING:" in imports
        assert "    from bamboohr_sdk.api.employee_tables_api import EmployeeTablesApi" in imports
        assert "    from bamboohr_sdk.api.hours_api import HoursApi" in imports

    def test_region_is_marker_delimited(self):
        imports = sync_accessors.render_imports([("hours_api", "HoursApi")])
        assert imports.startswith(sync_accessors.IMPORTS_BEGIN_MARKER)
        assert sync_accessors.IMPORTS_END_MARKER in imports


class TestApplyBlock:
    def test_replaces_only_the_marked_region(self):
        result = sync_accessors.sync_source(CLIENT_STUB, [("employee_tables_api", "EmployeeTablesApi")])

        # The stale generated accessor is gone, the new one is present.
        assert "stale_accessor" not in result
        assert "def employee_tables(self) -> EmployeeTablesApi:" in result

    def test_preserves_hand_written_code_outside_markers(self):
        result = sync_accessors.sync_source(CLIENT_STUB, [("employee_tables_api", "EmployeeTablesApi")])

        assert '"""Docstring that must survive."""' in result
        assert "def build(self):" in result
        assert 'HAND_WRITTEN_CONSTANT = "must survive"' in result
        # manual() sits below the END marker and must come through untouched.
        assert '"""Hand-written accessor that must never be regenerated."""' in result
        assert "from bamboohr_sdk.api.manual_api import ManualApi" in result

    def test_syncs_both_regions(self):
        result = sync_accessors.sync_source(CLIENT_STUB, [("employee_tables_api", "EmployeeTablesApi")])
        # Import region populated...
        assert "if TYPE_CHECKING:" in result
        assert "    from bamboohr_sdk.api.employee_tables_api import EmployeeTablesApi" in result
        # ...and the accessor annotated against it.
        assert "def employee_tables(self) -> EmployeeTablesApi:" in result

    def test_is_idempotent(self):
        once = sync_accessors.sync_source(CLIENT_STUB, [("employee_tables_api", "EmployeeTablesApi")])
        twice = sync_accessors.sync_source(once, [("employee_tables_api", "EmployeeTablesApi")])
        assert once == twice

    def test_missing_begin_marker_raises(self):
        source = CLIENT_STUB.replace(sync_accessors.BEGIN_MARKER, "    # nope")
        with pytest.raises(sync_accessors.SyncError, match=r"BEGIN marker .* not found"):
            sync_accessors.sync_source(source, [("hours_api", "HoursApi")])

    def test_missing_end_marker_raises(self):
        source = CLIENT_STUB.replace(sync_accessors.END_MARKER, "    # nope")
        with pytest.raises(sync_accessors.SyncError, match=r"END marker .* not found"):
            sync_accessors.sync_source(source, [("hours_api", "HoursApi")])

    def test_duplicate_markers_raise(self):
        source = CLIENT_STUB.replace(
            sync_accessors.BEGIN_MARKER,
            sync_accessors.BEGIN_MARKER + "\n" + sync_accessors.BEGIN_MARKER,
        )
        with pytest.raises(sync_accessors.SyncError, match="appears 2 times"):
            sync_accessors.sync_source(source, [("hours_api", "HoursApi")])


class TestRepositoryState:
    """Guards the real files, not fixtures."""

    def test_client_accessors_are_in_sync(self):
        # This is the regression test for the original breakage: if the spec
        # renames a tag and nobody reruns the sync, this fails here rather
        # than as a ModuleNotFoundError in the regen pipeline.
        apis = sync_accessors.discover_apis(sync_accessors.API_INIT)
        current = sync_accessors.CLIENT_FILE.read_text()
        assert current == sync_accessors.sync_source(current, apis), (
            "BambooHRClient accessors are out of sync with bamboohr_sdk/api/__init__.py. Run `make sync-accessors`."
        )

    def test_every_generated_api_is_importable(self):
        # Catches the exact failure mode from the broken run: an accessor
        # importing a module the generator no longer emits.
        import importlib

        for module, cls in sync_accessors.discover_apis(sync_accessors.API_INIT):
            imported = importlib.import_module(f"bamboohr_sdk.api.{module}")
            assert hasattr(imported, cls), f"{cls} missing from bamboohr_sdk.api.{module}"

    def test_rendered_block_survives_ruff_format(self):
        # The pipeline runs `make generate` (which syncs) then `make format`
        # then `make check-accessors`. If ruff reformats the block we just
        # rendered, that last step fails on every single run. Locking the
        # fixed point here means the renderer and the formatter can't drift
        # apart silently.
        import shutil
        import subprocess
        import tempfile

        ruff = shutil.which("ruff") or str(Path(sys.executable).parent / "ruff")
        if not Path(ruff).exists():
            pytest.skip("ruff not available")

        block = sync_accessors.render_block(sync_accessors.discover_apis(sync_accessors.API_INIT))
        # Wrap in a minimal class so the block is syntactically valid on its own.
        snippet = "class BambooHRClient:\n" + block

        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "snippet.py"
            target.write_text(snippet)
            subprocess.run(
                [ruff, "format", "--line-length", "120", str(target)],
                check=True,
                capture_output=True,
            )
            assert target.read_text() == snippet, (
                "ruff format rewrote the generated accessor block. Update render_block() "
                "in scripts/sync_accessors.py to emit formatter-stable output."
            )

    def test_manual_accessor_is_outside_the_generated_block(self):
        source = sync_accessors.CLIENT_FILE.read_text()
        end_marker_pos = source.index(sync_accessors.END_MARKER)
        assert source.index("def manual(self):") > end_marker_pos, (
            "manual() must live below the END marker or the sync will overwrite it."
        )
