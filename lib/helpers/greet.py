import click

@click.command()
@click.option('--name', prompt='Your name',
                help='The person to greet.')
def greet(name):
    """This script greets you."""
    click.echo(f"Hello {name}!")
