#!/usr/bin/env python3
import cgi
import html
import mysql.connector
from mysql.connector import connect, Error
from getpass import getpass
from mysql.connector import cursor

#mySQLServer = '188.120.232.22\MySQL'
#myDataBase = 'db_talon'

try:
    with connect(
            host=('188.120.232.22'),
            user=('queue'),
            password=('Font2320'),
            database=('db_talon'),
    ) as connection:
        print(connection)
except Error as e:
    print(e)

select_talon_query = "SELECT * FROM Staff"
connection.reconnect()
with connection.cursor() as cursor:
    cursor.execute(select_talon_query)
    result = cursor.fetchall()
    for row in result:
        a = str(row)
        print(a)
    #print(result)
connection.close()
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
<title>UPDATE</title>
        </head>
        <body>""")

print("<h1>Номер талона</h1>")
print("<h2>")
print(row)
print("</h2>")
print("""</body>
        </html>""")
