#!/usr/bin/env python

from pathlib import Path

PROJECT_DIRECTORY = Path.cwd().resolve()

REMOVE_PATHS = []


def remove_path(path: str) -> None:
    full_path = Path(PROJECT_DIRECTORY) / path
    if path.is_file():
        full_path.unlink()
    elif path.is_dir():
        full_path.rmdir()
    else:
        print(f"Path '{full_path}' is neither a file nor a directory.")


if __name__ == "__main__":
    for path in REMOVE_PATHS:
        remove_path(path)
