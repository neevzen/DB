from tkinter import *
from tkinter import messagebox as mb
import openpyxl
import mysql.connector
from mysql.connector import connect, Error
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

select_talon_query = """
SELECT Talon, Status
FROM Staff
WHERE Status = 'NEW'
ORDER BY Talon DESC
"""
connection.reconnect()
with connection.cursor() as cursor:
    cursor.execute(select_talon_query)
    result = cursor.fetchall()
    #print(result)
    now = datetime.datetime.now()
    for row in result:
        #print (now.strftime("%d-%m-%Y %H:%M"))
        print(now.strftime("%d-%m-%Y %H:%M"), row[0], row[1])




def clicked():
    select_talon_query = "SELECT Talon, Status FROM Staff WHERE Status = 'NEW' ORDER BY Talon DESC LIMIT 1"
    connection.reconnect()
    with connection.cursor() as cursor:
        cursor.execute(select_talon_query)
        result = cursor.fetchall()
        #print(result)
        for row in result:
            dada = result[0][0]
            print(dada, row[1])

        number_old = dada
        number = number_old + 1
        connection.reconnect()
    with connection.cursor() as cursor:
        cursor.execute("""
        UPDATE
            Staff
        SET
            Status = "OK"
        WHERE
            Talon = '""" + str(dada) + """'
        """)
        connection.commit()
        mb.showinfo('Ticket', 'Принят талон: ' + str(dada))
        connection.close()




def clicked1():
    print("B")



window = Tk()
window.title("Электронная очередь")
window.geometry('620x500')

window.update_idletasks()
s = window.geometry()
s = s.split('+')
s = s[0].split('x')
width_window = int(s[0])
height_window = int(s[1])

w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w = w // 2
h = h // 2
w = w - width_window // 2
h = h - height_window // 2
window.geometry('+{}+{}'.format(w, h))



lbl = Label(window, text="Выберите услугу", width=20, height=10)
lbl.grid(column=2,row=0)
btn = Button(window, text="Принять", command=clicked, width=20, height=5)
btn.grid(column=1,row=1)
btn1 = Button(window, text="Продать", command=clicked1, width=20, height=5)
btn1.grid(column=3, row=1)
window.mainloop()
