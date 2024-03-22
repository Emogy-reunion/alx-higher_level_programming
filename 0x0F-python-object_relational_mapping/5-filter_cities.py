#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa together with state"""
import MySQLdb
import sys


if __name__ == "__main__":
    """connect to database and perform operations"""
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = conn.cursor()
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities JOIN states ON cities.state_id=states.id "
             "WHERE states.name=%s")
    cursor.execute(query, (sys.argv[4],))
    results = cursor.fetchall()
    tmp = list(row[1] for row in results)
    print(*tmp, sep=", ")
    cursor.close()
    conn.close()
