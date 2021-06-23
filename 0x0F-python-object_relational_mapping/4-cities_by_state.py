#!/usr/bin/python3
"""
function module
"""
import sys
import MySQLdb


def main():
    d = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8"
                            )
    c = d.cursor()
    query = """SELECT  cities.id, cities.name, states.name
                FROM cities INNER JOIN states ON cities.state_id=states.id"""
    c.execute(query)
    rows = c.fetchall()
    for r in rows:
        print(r)
    c.close()
    d.close()


if __name__ == "__main__":
    main()
