#import SQL database
import sqlite3
import json
from unittest import result

sql_query = "select * from Superheros"

with sqlite3.connect("Superheros.db") as db:
    cursor = db.cursor()
    cursor.execute(sql_query)

results = cursor.fetchall()

print(results)