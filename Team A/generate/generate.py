import click

@click.command()
def cli():
    click.echo('Start a local http server that regenerates based on the requested file')