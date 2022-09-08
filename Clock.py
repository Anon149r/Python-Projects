from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("Helevetica",80), background = "black", foreground = "limegreen")
label.pack(anchor='center')
label.pack()

time()

mainloop()