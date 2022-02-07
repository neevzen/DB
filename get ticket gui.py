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




def clicked():
    select_talon_query = "SELECT Talon FROM Staff ORDER BY Talon DESC LIMIT 1"
    connection.reconnect()
    with connection.cursor() as cursor:
        cursor.execute(select_talon_query)
        result = cursor.fetchall()
        #print(result)
        for row in result:
            dada = result[0][0]
            print(dada)

        number_old = dada
        number = number_old + 1
        connection.reconnect()
    with connection.cursor() as cursor:
        cursor.execute("""
        INSERT INTO Staff (Talon, Status, Services)
        VALUES ('""" + str(number) + """', 'NEW', 'Online Services')""")
        connection.commit()
        mb.showinfo('Ticket', 'Номер вашего талона: ' + str(number))
        connection.close()


def clicked1():
    select_talon_query = "SELECT Talon FROM Staff ORDER BY Talon DESC LIMIT 1"
    connection.reconnect()
    with connection.cursor() as cursor:
        cursor.execute(select_talon_query)
        result = cursor.fetchall()
        #print(result)
        for row in result:
            dada = result[0][0]
            print(dada)

        number_old = dada
        number = number_old + 1
        connection.reconnect()
    with connection.cursor() as cursor:
        cursor.execute("""
        INSERT INTO Staff (Talon, Status, Services)
        VALUES ('""" + str(number) + """', 'NEW', 'SC4148')""")
        connection.commit()
        mb.showinfo('Ticket', 'Номер вашего талона: ' + str(number))
        connection.close()



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
btn = Button(window, text="Online Services", command=clicked, width=20, height=5)
btn.grid(column=1,row=1)
btn1 = Button(window, text="SC4148", command=clicked1, width=20, height=5)
btn1.grid(column=3, row=1)
window.mainloop()
