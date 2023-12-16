import click

from taskweaver.cli.util import require_workspace


@click.command()
@require_workspace()
@click.option("--plugin-name", "-p", default="", help="The plugin to test", type=str, show_default=True)
def plugin_test(host: str, port: int, debug: bool, open: bool):
    """Start Plugin test"""

    print('test plugin ok')