from tkinter import *
# import pandas as pd
import tkinter as tk

def printIt():
    SelectList = lb.curselection()
    arrrr = [lb.get(i) for i in SelectList]
    print(arrrr[0]) # this will print the value you select


test_years = ["2016", "2017", "2018", "2019"]
root = tk.Tk()
root.title("Test Year Selection")
lb = Listbox(root, selectmode=MULTIPLE, height = len(test_years), width = 50) # create Listbox
for x in test_years: lb.insert(END, x)
lb.pack() # put listbox on window

tk.Button(root,text="Start",command=printIt).pack()
root.mainloop()