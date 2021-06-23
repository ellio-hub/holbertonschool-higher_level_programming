#!/usr/bin/python3
"""
function module
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    x = session.query(City).all()
    for r in x:
        print("{}: {} -> {}".format(r.id, r.name, r.state.name))
    session.close()
