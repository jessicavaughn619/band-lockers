import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Enter Your Name',
              help='The person to greet.')
def greet(name):
    """This script greets you."""
    click.echo(" ")
    click.echo(f"~~ Welcome to Bando, {name}! ~~")
    click.echo(" ")
    click.echo("Here are some options to get started:")
    click.echo(" ")
    click.echo("Press S to search for information in the inventory.")
    click.echo("Press A to add new data to the inventory.")
    click.echo(" ") 

@cli.command()
@click.option('--search', type=int, prompt='Enter Locker Number',
              help='Provides locker combination given a locker number.')
def combo(locker):
    """Provides a locker combination given a locker number."""
    Locker.print_combo_by_locker_number(locker_number=locker)
    click.echo(f"What a cool {locker}!")

if __name__ == "__main__":
    engine = create_engine("sqlite:///db/band_lockers.db")
    session = Session(engine, future=True)
    print(" ")
    print("~~ Welcome to Bando! ~~")
    print(" ")
    cli()