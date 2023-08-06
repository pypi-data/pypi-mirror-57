__all__ = ["activate", "deactivate", "get_config"]

import atexit
import builtins
import copy
import functools
import sys
from pathlib import Path
from typing import Mapping, Optional, Tuple

import tomlkit
from dunamai import Style, Vcs, Version

_VERSION_PATTERN = r"^v(?P<base>\d+\.\d+\.\d+)(-?((?P<stage>[a-zA-Z]+)\.?(?P<revision>\d+)?))?$"


class _State:
    def __init__(
        self,
        patched_poetry_console_main: bool = False,
        patched_poetry_create: bool = False,
        patched_poetry_command_run: bool = False,
        original_version: str = None,
        version: Tuple[Version, str] = None,
    ) -> None:
        self.patched_poetry_console_main = patched_poetry_console_main
        self.patched_poetry_create = patched_poetry_create
        self.patched_poetry_command_run = patched_poetry_command_run
        self.original_version = original_version
        self.version = version
        self.original_import_func = builtins.__import__


_state = _State()


def _default_config() -> Mapping:
    return {
        "tool": {
            "poetry-dynamic-versioning": {
                "enable": False,
                "vcs": "any",
                "dirty": False,
                "pattern": _VERSION_PATTERN,
                "latest-tag": False,
                "subversion": {"tag-dir": "tags"},
            }
        }
    }


def _deep_merge_dicts(base: Mapping, addition: Mapping) -> Mapping:
    result = dict(copy.deepcopy(base))
    for key, value in addition.items():
        if isinstance(value, dict) and key in base and isinstance(base[key], dict):
            result[key] = _deep_merge_dicts(base[key], value)
        else:
            result[key] = value
    return result


def _find_higher_file(*names: str, start: Path = None) -> Optional[Path]:
    if start is None:
        start = Path().resolve()
    for level in [start, *start.parents]:
        for name in names:
            if (level / name).is_file():
                return level / name
    return None


def _get_pyproject_path(start: Path = None) -> Optional[Path]:
    return _find_higher_file("pyproject.toml", start=start)


def get_config(start: Path = None) -> Mapping:
    pyproject_path = _get_pyproject_path(start)
    if pyproject_path is None:
        return _default_config()["tool"]["poetry-dynamic-versioning"]
    pyproject = tomlkit.parse(pyproject_path.read_text())
    result = _deep_merge_dicts(_default_config(), pyproject)["tool"]["poetry-dynamic-versioning"]

    for key in ["pattern", "style", "metadata", "format"]:
        if key not in result:
            result[key] = None

    return result


def _get_version() -> Tuple[Version, str]:
    if _state.version:
        return _state.version

    config = get_config()
    pyproject_path = _get_pyproject_path()
    if pyproject_path is None:
        raise RuntimeError("Unable to find pyproject.toml")
    pyproject = tomlkit.parse(pyproject_path.read_text())
    if not _state.original_version:
        _state.original_version = pyproject["tool"]["poetry"]["version"]

    vcs = Vcs(config["vcs"])
    style = config["style"]
    if style is not None:
        style = Style(style)

    version = Version.from_vcs(
        vcs, config["pattern"], config["latest-tag"], config["subversion"]["tag-dir"]
    )
    serialized = version.serialize(config["metadata"], config["dirty"], config["format"], style)

    pyproject["tool"]["poetry"]["version"] = serialized
    pyproject_path.write_text(tomlkit.dumps(pyproject))
    _state.version = (version, serialized)
    return (version, serialized)


def _patch_poetry_create() -> None:
    try:
        has_factory_module = True
        poetry_factory_module = _state.original_import_func("poetry.factory", fromlist=["Factory"])
        original_poetry_create = poetry_factory_module.Factory.create_poetry
    except ModuleNotFoundError:
        has_factory_module = False
        poetry_factory_module = _state.original_import_func("poetry.poetry", fromlist=["Poetry"])
        original_poetry_create = poetry_factory_module.Poetry.create

    poetry_version_module = _state.original_import_func(
        "poetry.semver.version", fromlist=["Version"]
    )

    @functools.wraps(original_poetry_create)
    def alt_poetry_create(cls, *args, **kwargs):
        instance = original_poetry_create(cls, *args, **kwargs)
        dynamic_version = _get_version()[1]
        instance._package._version = poetry_version_module.Version.parse(dynamic_version)
        instance._package._pretty_version = dynamic_version
        return instance

    if has_factory_module:
        poetry_factory_module.Factory.create_poetry = alt_poetry_create
    else:
        poetry_factory_module.Poetry.create = alt_poetry_create
    sys.modules["poetry.poetry"] = poetry_factory_module


def _patch_poetry_command_run() -> None:
    poetry_command_run_module = _state.original_import_func(
        "poetry.console.commands.run", fromlist=["RunCommand"]
    )
    original_poetry_command_run = poetry_command_run_module.RunCommand.handle

    @functools.wraps(original_poetry_command_run)
    def alt_poetry_command_run(self, *args, **kwargs):
        # As of version 1.0.0b2, on Linux, the `poetry run` command
        # uses `os.execvp` function instead of spawning a new process.
        # This prevents the atexit `deactivte` hook to be invoked.
        # For this reason, we immediately call `deactivate` before
        # actually executing the run command.
        deactivate()
        return original_poetry_command_run(self, *args, **kwargs)

    poetry_command_run_module.RunCommand.handle = alt_poetry_command_run
    sys.modules["poetry.console.commands.run"] = poetry_command_run_module


def _patch_poetry_console_main(module, name, fromlist):
    if name == "poetry.console" and fromlist:
        console = module
    elif name == "poetry" and "console" in fromlist:
        console = module.console
    else:
        return False

    # We want to patch Poetry's main console function and make it do the
    # rest of the patching for us, to avoid an error when we try to do
    # the rest of it directly here and ProjectPackage can't be found yet.

    original_console_main = console.main

    @functools.wraps(original_console_main)
    def alt_poetry_console_main(*args, **kwargs):
        if not _state.patched_poetry_create:
            _patch_poetry_create()
            _state.patched_poetry_create = True

        if not _state.patched_poetry_command_run:
            _patch_poetry_command_run()
            _state.patched_poetry_command_run = True

        original_console_main(*args, **kwargs)

    console.main = alt_poetry_console_main
    return True


def _patch_builtins_import() -> None:
    @functools.wraps(builtins.__import__)
    def alt_import(name, globals=None, locals=None, fromlist=(), level=0):
        module = _state.original_import_func(name, globals, locals, fromlist, level)

        if not _state.patched_poetry_console_main:
            patched = _patch_poetry_console_main(module, name, fromlist)
            _state.patched_poetry_console_main = patched

        return module

    builtins.__import__ = alt_import


def activate() -> None:
    config = get_config()
    if not config["enable"]:
        return
    _patch_builtins_import()
    atexit.register(deactivate)


def deactivate() -> None:
    if _state.original_version:
        pyproject_path = _get_pyproject_path()
        if pyproject_path is None:
            return
        pyproject = tomlkit.parse(pyproject_path.read_text())
        pyproject["tool"]["poetry"]["version"] = _state.original_version
        pyproject_path.write_text(tomlkit.dumps(pyproject))
        _state.original_version = None
