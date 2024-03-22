#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    """connect to mysql server"""
    conn  = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    conn.close()
