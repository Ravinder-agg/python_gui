import tkinter as tk
from tkinter import font
from tkinter import ttk
import datetime
import time

def quit(*args):
    root.destroy()

def clock_time():
    time = datetime.datetime.now()
    time = (time.strftime("%d-%b-%y \n%I:%M:%S %p"))

    txt.set(time)
    root.after(1000,clock_time)


root = tk.Tk()
root.geometry('1000x400')
root.title("CLOCK with DATE")
root.attributes("-fullscreen",False)
root.configure(background='black')
root.bind('x',quit)   # when you press x program will quit
root.after(1000,clock_time)

fnt = font.Font(family="Halvetica", weight="bold", size=120)
txt = tk.StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground='white', background="black")
lbl.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

root.mainloop()