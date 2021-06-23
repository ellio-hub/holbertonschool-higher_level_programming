#!/usr/bin/python3
'''
function module
'''
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    d = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         d=argv[3])

    c = d.cursor()
    c.execute("SELECT * FROM states WHERE\
    name LIKE BINARY 'N%' ORDER BY states.id")
    r = c.fetchall()
    for row in r:
        print(row)

    c.close()
    d.close()
