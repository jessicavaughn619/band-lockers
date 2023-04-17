import click
from db.models import Locker, Student, Instrument


@click.command()
@click.option('--name', prompt='Your name',
              help='The person to greet.')
@click.option('--repeat', default=1,
              help='How many times to be greeted.')

def say(name, repeat):
    """This script greets you."""
    for x in range(repeat):
        click.echo(f"Hello {name}!")


if __name__ == "__main__":
    say()