__all__ = ["activate", "deactivate", "get_config"]

import atexit
import builtins
import functools
import sys
from pathlib import Path
from typing import Mapping

from poetry.exceptions import InvalidProjectFile
import tomlkit
import scmver

from . import version

__version__ = version.version

# raise InvalidProjectFile("hola")


class _State:
    def __init__(
        self,
        patched_poetry_console_main: bool = False,
        patched_poetry_create: bool = False,
        original_version: str = None,
        version: str = None,
    ) -> None:
        self.patched_poetry_console_main = patched_poetry_console_main
        self.patched_poetry_create = patched_poetry_create
        self.original_version = original_version
        self.version = version
        self.original_import_func = builtins.__import__


_state = _State()

def get_config() -> Mapping:
    pyproject_path = Path().resolve() / 'pyproject.toml'
    if not pyproject_path.exists():
        raise InvalidProjectFile("pyproject.toml not exists")
    return tomlkit.parse(pyproject_path.read_text())


def _get_version() -> str:
    if not _state.version:
        config = get_config()
        pyproject_path = Path().resolve() / 'pyproject.toml'
        if not pyproject_path.exists():
            raise InvalidProjectFile("pyproject.toml not exists")
        if not _state.original_version:
            _state.original_version = config["tool"]["poetry"]["version"]
        
        _config = config["tool"]["scmver"].copy()
        del _config['enable']
        try:
            del _config['no_deactivate']
        except KeyError:
            pass
        
        _state.version = scmver.get_version(**_config)
        
        if config["tool"]["poetry"]["version"] != _state.version:
            config["tool"]["poetry"]["version"] = _state.version
            pyproject_path.write_text(tomlkit.dumps(config))
    # print(_state.version)
    return _state.version


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
        dynamic_version = _get_version()
        # print(poetry_version_module.Version.parse(dynamic_version))
        instance._package._version = poetry_version_module.Version.parse(dynamic_version)
        instance._package._pretty_version = dynamic_version
        return instance

    if has_factory_module:
        poetry_factory_module.Factory.create_poetry = alt_poetry_create
    else:
        poetry_factory_module.Poetry.create = alt_poetry_create
    sys.modules["poetry.poetry"] = poetry_factory_module


def _patch_poetry_console_main(module, name, fromlist) -> None:
    if name == "poetry.console" and fromlist:
        console = module
    elif name == "poetry" and "console" in fromlist:
        console = module.console
    else:
        return
    
    # We want to patch Poetry's main console function and make it do the
    # rest of the patching for us, to avoid an error when we try to do
    # the rest of it directly here and ProjectPackage can't be found yet.

    original_console_main = console.main

    @functools.wraps(original_console_main)
    def alt_poetry_console_main(*args, **kwargs):
        if not _state.patched_poetry_create:
            _patch_poetry_create()
            _state.patched_poetry_create = True
        original_console_main(*args, **kwargs)

    console.main = alt_poetry_console_main
    _state.patched_poetry_console_main = True


def _patch_builtins_import() -> None:
    @functools.wraps(builtins.__import__)
    def alt_import(name, globals=None, locals=None, fromlist=(), level=0):
        module = _state.original_import_func(name, globals, locals, fromlist, level)
        
        if not _state.patched_poetry_console_main:
            patched = _patch_poetry_console_main(module, name, fromlist)
        
        return module

    builtins.__import__ = alt_import


def activate() -> None:
    try:
        config = get_config()
        enable = config['tool']["scmver"]["enable"]
    except InvalidProjectFile:
        enable = False
    except tomlkit.exceptions.NonExistentKey:
        enable = False

    if enable and _state.original_version == None:
        _patch_builtins_import()
        
        try:
            no_deactivate = config['tool']["scmver"]["no_deactivate"]
        except tomlkit.exceptions.NonExistentKey:
            no_deactivate = False
        
        if not no_deactivate:
            atexit.register(deactivate)


def deactivate() -> None:
    if _state.original_version:
        pyproject_path = Path().resolve() / 'pyproject.toml'
        if not pyproject_path.exists():
            raise InvalidProjectFile("pyproject.toml not exists")
        pyproject = tomlkit.parse(pyproject_path.read_text())
        pyproject["tool"]["poetry"]["version"] = _state.original_version
        pyproject_path.write_text(tomlkit.dumps(pyproject))
        _state.original_version = None
