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
    x = session.query(State).filter_by(id=2).first()
    x.name = "New Mexico"
    x = session.add(x)
    session.commit()
    session.close()
