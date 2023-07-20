import tkinter as tk
from tkinter import *
root =  tk.Tk ()
root.geometry("500x400")
root.title("Keylogger")

# def butaction():
#     print("GUI")

empty =Label(root , text="KeyLogger Project",font='Verdana').grid(row=2,column=2)
Button(root,text="Start Keylogger",command=Button).grid(row=5,column=2)
root.mainloop()