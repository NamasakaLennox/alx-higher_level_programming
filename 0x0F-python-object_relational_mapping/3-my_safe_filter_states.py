#!/usr/bin/python3
"""lists all states from the database that match a passed argument
Safe from SQL injection"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    # query execution
    cur.execute("SELECT * FROM states")

    [print(state) for state in cur.fetchall() if state[1] == argv[4]]

    cur.close()
    db.close()
