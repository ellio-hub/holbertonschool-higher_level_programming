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
    state_name = sys.argv[4]
    c = d.cursor()
    c.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (state_name,))
    rows = c.fetchall()
    t = ""
    for r in rows:
        t += r[0] + ", "
    print(t[0:-2:])
    c.close()
    d.close()


if __name__ == "__main__":
    main()
