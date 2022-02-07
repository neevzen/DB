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

select_talon_query = "SELECT Talon FROM Staff ORDER BY Talon DESC LIMIT 1"
connection.reconnect()
with connection.cursor() as cursor:
    cursor.execute(select_talon_query)
    result = cursor.fetchall()
    #print(result)
    for row in result:
        dada = result[0][0]
        print(dada)



#insert_talon_query = """
#INSERT INTO Staff (Talon)
#VALUES ('132')
#"""
number_old = dada
number = number_old + 1
connection.reconnect()
with connection.cursor() as cursor:
    cursor.execute("""
    INSERT INTO Staff (Talon, Status)
    VALUES ('""" + str(number) + """', 'NEW')""")
    connection.commit()

select_talon_query = "SELECT Talon, Status FROM Staff ORDER BY Talon DESC LIMIT 1"
connection.reconnect()
with connection.cursor() as cursor:
    cursor.execute(select_talon_query)
    result = cursor.fetchall()
    #print(dada)
    for row in result:
        dada = result[0][0]
        print(row[0], row[1])
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

print("<h1>UPDATE</h1>")
print("<h2>")
print(row[0])
print("</h2>")
print("""</body>
        </html>""")


