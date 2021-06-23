#!/usr/bin/python3
'''
function module
'''
import MySQLdb


def main():
    d = MySQLdb.connect(host='localhost',
                        port=3306,
                        user=argv[1],
                        passwd=argv[2],
                        database=argv[3])

    c = d.cursor()

    c.execute('SELECT * FROM states ORDER BY id ASC')
    rows = c.fetchall()
    for i in rows:
        print(i)
    c.close()
    d.close()

if __name__ == "__main__":
    from sys import argv
    main()
