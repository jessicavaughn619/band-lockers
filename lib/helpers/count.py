import click
from db.models import Instrument

@click.command()
@click.option('--instrument', prompt='Instrument type',
              help='Instrument to count.')
def count(instrument):
    """This script counts instruments."""
    Instrument.count_instruments(instrument=instrument)
    click.echo(f"What a cool {instrument}!")