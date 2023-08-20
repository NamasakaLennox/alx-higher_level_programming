#!/usr/bin/python3
"""lists all cities from the database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (argv[4],))

    rows = cur.fetchall()
    items = list(row[0] for row in rows)
    print(*items, sep=", ")

    cur.close()
    db.close()
