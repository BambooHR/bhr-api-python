#!/usr/bin/env python3
"""
Error Documentation Generator for BambooHR Python SDK.

Generates exception documentation in docs/Exceptions/:
  - Exceptions.md — index of all exception classes with error handling examples
  - Classes/<Name>Exception.md — per-exception documentation with causes and tips
  - Classes/ApiException.md — base exception documentation
  - Classes/ClientException.md — client exception base class documentation
  - Classes/ServerException.md — server exception base class documentation

Templates are read from templates-python/ and rendered with a built-in Mustache renderer.

Usage:
    python scripts/generate_error_docs.py

Reference: PHP SDK scripts/generate_error_docs.php + scripts/generate_exceptions.php
"""

from __future__ import annotations

import importlib.util
import re
import sys
import types
from pathlib import Path

# ---------------------------------------------------------------------------
# Ensure the SDK package is importable
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Load exceptions.py and api_error_helper.py directly by file path to avoid
# triggering bamboohr_sdk/__init__.py (which requires dateutil, pydantic, etc.)
def _load_module(name: str, file_path: Path) -> types.ModuleType:
    spec = importlib.util.spec_from_file_location(name, file_path)
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    sys.modules[name] = mod
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod

_load_module("bamboohr_sdk.exceptions", PROJECT_ROOT / "bamboohr_sdk" / "exceptions.py")
_api_error_helper = _load_module(
    "bamboohr_sdk.api_error_helper",
    PROJECT_ROOT / "bamboohr_sdk" / "api_error_helper.py",
)
ERROR_MESSAGES = _api_error_helper.ERROR_MESSAGES


class _Mustache:
    """Minimal Mustache renderer — supports {{var}}, {{#list}}...{{/list}}, {{.}}."""

    _SECTION = re.compile(r"\{\{#(\w+)\}\}(.*?)\{\{/\1\}\}", re.DOTALL)
    _VAR = re.compile(r"\{\{(\w+|\.)\}\}")

    @classmethod
    def render(cls, template: str, data: dict) -> str:
        def replace_section(m: re.Match) -> str:
            key, body = m.group(1), m.group(2)
            items = data.get(key, [])
            if not items:
                return ""
            inner = body.strip("\n")
            parts = []
            for item in items:
                ctx = item if isinstance(item, dict) else {".": item}
                parts.append(cls._render_vars(inner, ctx))
            return "\n".join(parts)

        result = cls._SECTION.sub(replace_section, template)
        return cls._render_vars(result, data)

    @classmethod
    def _render_vars(cls, text: str, data: dict) -> str:
        return cls._VAR.sub(lambda m: str(data.get(m.group(1), m.group(0))), text)

TEMPLATE_DIR = PROJECT_ROOT / "templates-python"
DOCS_DIR = PROJECT_ROOT / "docs" / "Exceptions"
CLASSES_DIR = DOCS_DIR / "Classes"


def render_template(template_name: str, data: dict) -> str:
	"""Load a mustache template from templates-python/ and render it."""
	template_path = TEMPLATE_DIR / template_name
	if not template_path.exists():
		print(f"Error: Template file not found at {template_path}", file=sys.stderr)
		sys.exit(1)
	template = template_path.read_text()
	return _Mustache.render(template, data)


def main() -> None:
	# Create output directories
	DOCS_DIR.mkdir(parents=True, exist_ok=True)
	CLASSES_DIR.mkdir(parents=True, exist_ok=True)

	# Collect exceptions by category
	client_exceptions: list[dict] = []
	server_exceptions: list[dict] = []

	for status_code in sorted(ERROR_MESSAGES.keys()):
		info = ERROR_MESSAGES[status_code]
		if "type" not in info:
			print(f"Warning: Error code {status_code} does not have a type defined, skipping.")
			continue

		type_name = info["type"]
		title = info["title"]
		parent_class = "ClientException" if status_code < 500 else "ServerException"

		entry = {"name": type_name, "code": status_code, "title": title}
		if status_code < 500:
			client_exceptions.append(entry)
		else:
			server_exceptions.append(entry)

		# Generate per-exception doc
		doc_data = {
			"className": type_name,
			"statusCode": status_code,
			"description": title,
			"parentClass": parent_class,
			"causes": info.get("causes", []),
			"tips": info.get("tips", []),
		}
		doc_content = render_template("exception_doc.mustache", doc_data)
		(CLASSES_DIR / f"{type_name}Exception.md").write_text(doc_content)

	# Generate base class docs
	api_doc = render_template("api_exception_doc.mustache", {})
	(CLASSES_DIR / "ApiException.md").write_text(api_doc)

	client_names = [e["name"] for e in client_exceptions]
	client_doc = render_template("client_exception_doc.mustache", {"clientExceptions": client_names})
	(CLASSES_DIR / "ClientException.md").write_text(client_doc)

	server_names = [e["name"] for e in server_exceptions]
	server_doc = render_template("server_exception_doc.mustache", {"serverExceptions": server_names})
	(CLASSES_DIR / "ServerException.md").write_text(server_doc)

	# Generate the index
	index_data = {
		"clientExceptions": client_exceptions,
		"serverExceptions": server_exceptions,
	}
	index_content = render_template("error_codes_doc.mustache", index_data)
	(DOCS_DIR / "Exceptions.md").write_text(index_content)

	# Summary
	exception_count = len(client_exceptions) + len(server_exceptions)
	total_docs = exception_count + 3  # +3 for base classes
	print("Exception documentation generated successfully:")
	print(f"  {DOCS_DIR / 'Exceptions.md'}")
	print(f"  {exception_count} exception docs in {CLASSES_DIR}/")
	print(f"  3 base class docs (ApiException, ClientException, ServerException)")
	print(f"  {total_docs} total documentation files")


if __name__ == "__main__":
	main()
