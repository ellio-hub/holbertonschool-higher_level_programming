#!/usr/bin/python3
"""
function module
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost/{}'
                            .format(
                                        sys.argv[1],
                                        sys.argv[2],
                                        sys.argv[3]
                                            ),
                            pool_pre_ping=True
                                )
    session = Session(engine)
    w = '%a%'
    x = session.query(State).filter(State.name.like(w)).order_by(State.id)
    for v in x:
        print("{}: {}".format(v.id, v.name))
    session.close()
