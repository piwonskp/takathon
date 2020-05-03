import os
from glob import iglob
from importlib import import_module
from pathlib import PurePath


def get_files(path):
    if os.path.isdir(path):
        path = os.path.join(path, "**", "*.py")
        return iglob(path, recursive=True)
    return [path]


def path_to_name(path):
    path, _ = os.path.splitext(path)
    if os.path.basename(path) == "__init__":
        path = os.path.dirname(path)

    return ".".join(PurePath(path).parts)


def import_module_by_path(path):
    return import_module(path_to_name(path))


def get_modules(path):
    return map(import_module_by_path, get_files(path))
