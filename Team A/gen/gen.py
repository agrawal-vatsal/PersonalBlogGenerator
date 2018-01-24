import click

@click.command()
def cli():
    click.echo('Generates the website to a configured deploy folder')