#!/usr/bin/python3
'''
function module
'''
import sys
import MySQLdb


def main():
    conn = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8"
                            )
    c = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    c.execute(query)
    rows = c.fetchall()
    for x in rows:
        if x[1][0] == 'N':
            print(x)
    c.close()
    conn.close()


if __name__ == "__main__":
    main()
