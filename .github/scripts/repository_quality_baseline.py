#!/usr/bin/env python3
"""Dependency-free baseline checks for repository JSON contracts and manifests."""
from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path

EXCLUDED_DIRS = {".git", ".venv", "venv", "node_modules", "dist", "build", "vendor"}
CONTRACT_DIRS = {"schema", "schemas", "manifest", "manifests", "contracts", "capabilities", "skills"}
CONTRACT_FILENAMES = {"package.json", "tsconfig.json"}


def is_contract_json(path: Path) -> bool:
    parts = [part.lower() for part in path.parts]
    return path.name.lower() in CONTRACT_FILENAMES or any(part in CONTRACT_DIRS for part in parts[:-1])


def find_contract_json(root: Path) -> list[Path]:
    found = []
    for path in root.rglob("*.json"):
        relative = path.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in relative.parts):
            continue
        if path.is_file() and is_contract_json(relative):
            found.append(path)
    return sorted(found)


def validate_json_file(path: Path) -> str | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            json.load(handle)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return f"{path}: {exc}"
    return None


def run_self_test() -> None:
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        schema_dir = root / "schemas"
        schema_dir.mkdir()
        (schema_dir / "valid.schema.json").write_text('{"type":"object"}', encoding="utf-8")
        (schema_dir / "invalid.schema.json").write_text('{"type":', encoding="utf-8")
        (root / "ordinary.json").write_text('{"ignored":true}', encoding="utf-8")
        selected = find_contract_json(root)
        assert len(selected) == 2, f"expected 2 contract files, got {selected}"
        errors = [validate_json_file(path) for path in selected]
        assert sum(error is not None for error in errors) == 1, errors
    print("Repository quality baseline self-test: PASS")


def run_check(root: Path) -> int:
    files = find_contract_json(root)
    errors = [error for path in files if (error := validate_json_file(path))]
    if errors:
        print("JSON contract validation: FAIL")
        for error in errors:
            print(f" - {error}")
        return 1
    print(f"JSON contract validation: PASS ({len(files)} contract/config JSON file(s) checked)")
    if not files:
        print("No contract/config JSON files exist yet; the check will cover them when added.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true", help="run dependency-free validator tests")
    parser.add_argument("--check", action="store_true", help="validate repository contract/config JSON")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    if args.self_test:
        run_self_test()
    if args.check:
        return run_check(args.root.resolve())
    if not args.self_test:
        parser.error("choose --self-test and/or --check")
    return 0


if __name__ == "__main__":
    sys.exit(main())
