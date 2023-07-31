#!/usr/bin/python3
"""a script that lists all states where name matches the argument
 from the database hbtn_0e_0_usa, protect from SQL injection by using
parameterised queries"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    state_name_searched = sys.argv[4]
    query = """SELECT * FROM states WHERE BINARY name = %s ORDER BY id;"""
    tuple1 = (state_name_searched,)
    cur.execute(query, tuple1)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
