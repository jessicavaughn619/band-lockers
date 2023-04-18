import click

@click.command()
@click.option('--name', prompt='Enter Your Name',
                help='The person to greet.')
def greet(name):
    """This script greets you."""
    click.echo(" ")
    click.echo(f"~~ Welcome to Bando, {name}! ~~")
    click.echo(" ")
    click.echo("What would you like to do next?")
    click.echo(" ")
