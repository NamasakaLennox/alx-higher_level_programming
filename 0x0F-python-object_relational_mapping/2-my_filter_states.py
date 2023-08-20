#!/usr/bin/python3
"""lists all states from the database that match a passed argument"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    # query execution
    cur.execute("SELECT * FROM states WHERE BINARY name='{:s}' ORDER BY id ASC"
                .format(argv[4]))

    # fetch
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
