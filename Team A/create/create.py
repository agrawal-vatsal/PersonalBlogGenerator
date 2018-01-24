import click


@click.command()
def cli():
    click.echo('Initializes a new site at given path')
