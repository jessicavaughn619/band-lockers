#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import (Locker, Instrument, Student)

if __name__ == '__main__':
    engine = create_engine("sqlite:///band_lockers.db")
    session = Session(engine, future=True)


    import ipdb; ipdb.set_trace()