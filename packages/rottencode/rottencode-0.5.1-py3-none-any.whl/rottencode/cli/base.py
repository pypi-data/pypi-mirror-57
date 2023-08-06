import importlib.util
import pathlib
import re

import click
import pkg_resources
import structlog

from .. import code, logging, utils

sl = structlog.get_logger()


class Regex(click.ParamType):
    name = "regex"

    def convert(self, value, param, ctx):
        try:
            regex = re.compile(value)
            return regex
        except re.error:
            self.fail(f"`{value}` is not a valid regular expression value", param, ctx)

    def __repr__(self):
        return "REGEX"


class FileOrModule(click.ParamType):
    name = "file or module"

    def convert(self, value, param, ctx):
        # test if a path exists
        path = pathlib.Path(value)
        if path.is_file():
            # try to load
            spec = importlib.util.spec_from_file_location(value, path)
        else:
            spec = importlib.util.find_spec(value)

        if spec is None:
            self.fail(f"`{value}` is not a file or a python module")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

    def __repr__(self):
        return "FileOrModule"


@click.group()
@click.option(
    "paths",
    "-p",
    "--path",
    default=None,
    multiple=True,
    help="Root path to locate modules.",
)
@click.option(
    "excludes",
    "-x",
    "--exclude",
    multiple=True,
    type=Regex(),
    help="A Regex to exclude full modue names.",
)
@click.option("log_level", "--log-level", default="warning")
@click.option(
    "modules",
    "-m",
    "--module",
    multiple=True,
    type=FileOrModule(),
    default=lambda: [],
    help="Python module or file to plugin.",
)
@click.pass_obj
def cli(obj, log_level, modules, **flags):
    logging.setup_logging(level=log_level)
    obj.selection = code.Selection(**flags)


def main():
    # load plugins first
    for entry_point in pkg_resources.iter_entry_points("rottencode.plugins.1"):
        entry_point.load()

    cli(obj=utils.adict())
