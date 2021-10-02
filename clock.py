from tkinter import Tk, mainloop
from tkinter.ttk import Label

from time import strftime

root = Tk()
root.title("My Python Clock")

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background = "black", foreground = "cyan")
label.pack(anchor='center')
time()

mainloop()
