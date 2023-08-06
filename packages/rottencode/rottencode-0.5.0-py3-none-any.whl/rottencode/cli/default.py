import click

from .. import stats
from .base import cli


@cli.command("graph")
@click.option("with_externals", "-e", "--ext/--no-ext", is_flag=True, default=False)
@click.option(
    "without_independent",
    "-i",
    "--no-independent/--independent",
    is_flag=True,
    default=False,
)
@click.option("cluster", "-c", "--cluster/--no-cluster", is_flag=True, default=False)
@click.pass_obj
def cli_graph(obj, with_externals, without_independent, cluster, **flags):
    """Generate a dot dependecy graph to show rotten packages."""
    analysis = stats.ModuleAnalysis(
        obj.selection,
        with_externals=with_externals,
        without_independent=without_independent,
        cluster=cluster,
    )
    analysis.report()


@cli.command("lost")
@click.pass_obj
def cli_lost(obj):
    """Compare imported packages against installed distributions to find unused ones."""
    analysis = stats.PackageCollector(obj.selection)
    analysis.report()
