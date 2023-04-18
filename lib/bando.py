#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import click

from db.models import Instrument, Locker, Student

# from helpers.greet import greet
# from helpers.count import count

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

@click.option('--instrument', prompt='Instrument type',
              help='Instrument to count.')
def count(instrument):
    """This script counts instruments."""
    Instrument.count_instruments(instrument=instrument)
    click.echo(f"What a cool {instrument}")

class Cli:
    def __init__(self):
        self.students = [student for student in session.query(Student)]
        self.lockers = [locker for locker in session.query(Locker)]
        self.instruments = [instrument for instrument in session.query(Instrument)]
        self.start()

    def start(self):
        greet()
        count()

if __name__ == "__main__":
    engine = create_engine("sqlite:///db/band_lockers.db")
    session = Session(engine, future=True)
    Cli()