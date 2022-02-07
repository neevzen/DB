import mysql.connector
from mysql.connector import connect, Error

mySQLServer = '188.120.232.22\MySQL'
myDataBase = 'db_talon'

connection = connect("Driver={SQL Server};"
                              "Server='mySQLServer' + ';'"
                              "Database='myDataBase' + ';'"
                              "uid=queue;"
                              "pwd=Font2320;")
cursor = connection.cursor()

MySQLQuery = ("""
                SELECT Talon, Status, Who
                FROM dbo.Talons
                WHERE Who = 'Nedelkin' 
                """)

cursor.execute = (MySQLQuery)

results = cursor.fetchall()
print(results)

connection.close()