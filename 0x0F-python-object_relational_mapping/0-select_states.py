#!/usr/bin/python3
"""Lists all states from a database"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    rows = cursor.execute("SELECT * FROM states ORDER BY states.id")

    # print all items
    for i in range(rows):
        print(cursor.fetchone())
