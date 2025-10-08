import click
import re
import sys

@click.command()
@click.option("--translate", prompt = True)
def cli(translate):

    click.echo(f"{translate}\n")

    if click.confirm("Continue?"):
        cli()

    sys.exit(0)
