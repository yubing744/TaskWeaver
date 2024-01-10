import click

from taskweaver.cli.util import require_workspace


@click.command(name="plugin_test")
@require_workspace()
@click.option("--plugin-name", "-g", default="", help="The plugin to test", type=str, show_default=True)
def plugin_test(plugin_name: str):
    """Start Plugin test"""

    print('test plugin ok')