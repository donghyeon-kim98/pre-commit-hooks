#!/usr/bin/env python3

import ast
from pathlib import Path
from typing import Dict, Iterable

HOOKS_DIR = "hooks"
EXCLUDE_FILES = {"__init__.py", "consts.py", "helpers.py"}


def find_hook_files() -> Iterable[Path]:
    hooks_dir = Path(HOOKS_DIR)

    for filename in hooks_dir.glob("*.py"):
        if filename.name not in EXCLUDE_FILES:
            yield filename


def get_hook_docstrings() -> Dict[str, str]:
    docstrings = {}

    for hook_file in find_hook_files():
        with hook_file.open("r") as f:
            module = ast.parse(f.read())
            docstring = ast.get_docstring(module)
            docstrings[hook_file.stem.replace("_", "-")] = docstring or ""
    return docstrings


def write_hooks_md() -> None:
    with open("HOOKS.md", "w") as f:
        f.write("# Hooks\n")
        f.writelines(f"\n`{hook}`\n\n{docstring}\n" for hook, docstring in get_hook_docstrings().items())


if __name__ == "__main__":
    write_hooks_md()
