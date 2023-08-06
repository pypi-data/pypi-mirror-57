"""Events for analyzing rotten code structures."""
import ast
from dataclasses import dataclass

from . import code, python


@dataclass
class Event:
    module: python.Module


@dataclass
class Dependency(Event):
    on: python.Name


@code.Scanner.register(ast.Import)
def handle_import(node: ast.Import, module, state):
    for alias in node.names:
        yield Dependency(module=module, on=python.Name(alias.name))


@code.Scanner.register(ast.ImportFrom)
def handle_from_import(node: ast.ImportFrom, module, state):
    base_name = module.relate(node.level, node.module)
    for alias in node.names:
        name = base_name / alias.name
        yield Dependency(module=module, on=python.Name(name))
