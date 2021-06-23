#!/usr/bin/python3
"""
functio module
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
    x = sys.argv[4]
    r = session.query(State).filter_by(name=x).first()
    if r is not None:
        print(str(r.id))
    else:
        print("Not found")
    session.close()
