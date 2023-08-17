#!/usr/bin/env python

import shutil
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd().resolve()

REMOVE_PATHS = ["{% if not cookiecutter.add_vscode_settings %} .vscode/ {% endif %}"]


def remove_path(path: str) -> None:
    if path.strip():
        full_path = Path(PROJECT_DIRECTORY) / path.strip()
        if full_path.is_file():
            full_path.unlink()
        elif full_path.is_dir():
            shutil.rmtree(full_path)
        else:
            print(f"Path '{full_path}' is neither a file nor a directory.")


if __name__ == "__main__":
    for rm_path in REMOVE_PATHS:
        remove_path(rm_path)
