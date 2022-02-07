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

select_talon_query = "SELECT Talon, Status, Who FROM Staff"
connection.reconnect()
with connection.cursor() as cursor:
    cursor.execute(select_talon_query)
    result = cursor.fetchall()
    #print(result)
    for row in result:
        dada = result[0][0]
        print(dada)



insert_talon_query = """
INSERT INTO Staff (Talon, Status, Who)
VALUES ('132', '', '')
"""
connection.reconnect()
with connection.cursor() as cursor:
    cursor.execute(insert_talon_query)
    connection.commit()

select_talon_query = "SELECT Talon, Status, Who FROM Staff"
connection.reconnect()
with connection.cursor() as cursor:
    cursor.execute(select_talon_query)
    result = cursor.fetchall()
    print(dada)
    for row in result:
        dada = result[0]
        #print(dada)

connection.close()
    #print(result)
#MySQLQuery = ("""
#               SELECT Talon, Status, Who
#                FROM dbo.Staff
#                WHERE Who = 'Nedelkin'
#                """)
#cursor = connection.cursor()
#cursor.execute = (MySQLQuery)


#results = cursor.fetchall()
#print(results)

