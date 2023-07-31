#!/usr/bin/python3
"""a script that takes the name of a state as an argument, and lists all cities
of that state, from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    state_name_searched = sys.argv[4]
    query = """SELECT cities.name\
 FROM states JOIN cities ON states.id = cities.state_id\
 WHERE states.name = %s ORDER BY cities.id ASC;"""
    tuple1 = (state_name_searched,)
    cur.execute(query, tuple1)
    cities = cur.fetchall()
    cities_list = ()
    for city in cities:
        cities_list = cities_list + city
    cities_string = ', '.join(cities_list)
    print(cities_string)
    cur.close()
    db.close()
