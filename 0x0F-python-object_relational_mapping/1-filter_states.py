#!/usr/bin/python3
"""lists all states starting with N from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    """connect to mysql server"""
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE states.name LIKE 'N%'")
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    conn.close()
