import click

@click.command()
@click.option('--instrument', prompt='Instrument type',
              help='Instrument to count.')
def count(instrument):
    """This script counts instruments."""
    click.echo(f"What a cool {instrument}!")