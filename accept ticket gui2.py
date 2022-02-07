from tkinter import *
from tkinter import messagebox as mb
import tkinter as tk
from mysql.connector import connect, Error
import datetime

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
SELECT Talon, Status, Services
FROM Staff
WHERE Status = 'NEW'
ORDER BY Talon DESC
LIMIT 30
"""
connection.reconnect()
with connection.cursor() as cursor:
    cursor.execute(select_talon_query)
    result = cursor.fetchall()
    #print(result)
    now = datetime.datetime.now()
    for row in result:
        #print (now.strftime("%d-%m-%Y %H:%M"))
        datatime = now.strftime("%d-%m-%Y %H:%M")
        nomerok = '[' + '"' + str(row[0]) + '"' + "," + ']'
        ticket = row[0]
        #print(datatime, nomerok, ticket)
        #print(ticket)
        print(nomerok)
qwe = nomerok




def clicked():
    SelectList = lb.curselection()
    arrrr = [lb.get(i) for i in SelectList]
    select_talon_query = "SELECT Talon, Status FROM Staff WHERE Status = 'NEW' ORDER BY Talon DESC LIMIT 1"
    connection.reconnect()
    with connection.cursor() as cursor:
        cursor.execute(select_talon_query)
        result = cursor.fetchall()
        #print(result)
        for row in result:
            dada = result[0][0]
            print(dada, row[1])
            print(select_talon_query)

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
            Talon = '""" + str(arrrr[0][0]) + """'
        """)
        connection.commit()
        mb.showinfo('Ticket', 'Принят талон: ' + str(arrrr[0][0]))

connection.close()
####################################


###################################
def clicked1():
    connection.reconnect()
    with connection.cursor() as cursor:
        cursor.execute(select_talon_query)
        result = cursor.fetchall()
        for row in result:
            nomerok = '[' + '"' + str(row[0]) + '"' + "," + ']'
            print(nomerok)

    lb.delete(0,END)
    for x in result: lb.insert(END, x)

    connection.close()


print(result)
test_years = result
root = tk.Tk()
root.title("Пульт оператора СУО")

root.update_idletasks()
s = root.geometry()
s = s.split('+')
s = s[0].split('x')
width_window = int(s[0])
height_window = int(s[1])

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2
h = h // 2
w = w - width_window // 2
h = h - height_window // 2
root.geometry('+{}+{}'.format(w, h))



Button(root,text="Следующий",command=clicked).pack()
Button(root,text="Обновить список",command=clicked1).pack()
lbl = Label(root, text="Выберите услугу", width=20, height=1).pack()
lb = Listbox(root, selectmode=SINGLE, height = 20, width = 60) # create Listbox
for x in test_years: lb.insert(END, x)
lb.pack(side=RIGHT) # put listbox on window



root.mainloop()


