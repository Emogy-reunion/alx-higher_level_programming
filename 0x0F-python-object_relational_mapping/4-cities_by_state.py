#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa together with state"""
import MySQLdb
import sys


if __name__ == "__main__":
    """connect to database and perform operations"""
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name "
                   "FROM cities JOIN states ON cities.state_id=states.id")
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    conn.close()
