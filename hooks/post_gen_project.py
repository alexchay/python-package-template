#!/usr/bin/env python

import shutil
import sys
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd().resolve()

REMOVE_PATHS = [
    "{% if not cookiecutter.add_vscode_settings %} .vscode/ {% endif %}",
    "{% if not cookiecutter.use_gotask %} Taskfile.yml {% endif %}",
    "{% if not cookiecutter.use_gotask %} taskfiles {% endif %}",
    "{% if not cookiecutter.use_poetry %} poetry.toml {% endif %}",
]


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

    # if task utility is not installed, report it and exit with error
    if shutil.which("task") is None:
        print("Task utility is not installed. Please install it manually. See https://taskfile.dev/installation/")
        sys.exit(1)
