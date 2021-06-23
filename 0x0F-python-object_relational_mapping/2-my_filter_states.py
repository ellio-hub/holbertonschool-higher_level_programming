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
    search = sys.argv[4]
    query = """SELECT * FROM states where name = '{:s}'
            ORDER by id ASC""".format(search)
    c.execute(query)
    rows = c.fetchall()
    for r in rows:
        if r[1] == search:
            print(r)
    c.close()
    d.close()


if __name__ == "__main__":
    main()
