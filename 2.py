#!/usr/bin/env python3
import cgi
import html
import mysql.connector
from mysql.connector import connect, Error
from getpass import getpass
from mysql.connector import cursor
import datetime

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

select_talon_query = "SELECT Talon, Status FROM Staff ORDER BY Talon DESC LIMIT 20"
connection.reconnect()
with connection.cursor() as cursor:
    cursor.execute(select_talon_query)
    result = cursor.fetchall()
    #print(result)
    now = datetime.datetime.now()
    for row in result:
        #print (now.strftime("%d-%m-%Y %H:%M"))
        print(now.strftime("%d-%m-%Y %H:%M"), row[0], row[1])
