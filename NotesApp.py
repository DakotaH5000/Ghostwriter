import os
import _tkinter  #Used to create user GUI. 
from pynput.keyboard import Key, Listener 
import winsound  #Having an issue with sounds on key press, unsure if a windows feature or script feature, will be removed if unused. 


captured_keys = [] # This will be replaced by a linked list if not done, recreating the array every time a keystroke is made is inefficent as opposed to creating a pointer. 
f = open("note.txt", "a")

from tkinter import *
paused = False

def on_press(key):
    global paused
    global captured_keys
    if key == Key.esc:
        # Stop listener
        if paused:
            paused = False
        else: #Pausing / Saving
            paused = True
            with open("note.txt", "a") as f:
                f.write(''.join(captured_keys))
                captured_keys = []
    if not paused:
        try:
            key_str = key.char
            captured_keys.append(key_str) 
        except AttributeError:    #Handle special case keys that need either a special action or have issues with their natural implementation.
            key_str = str(key)
            if key_str == 'Key.space':
                key_str = ' '
                print(captured_keys)
                captured_keys.append(key_str)
            if key_str == 'Key.backspace':
                if len(captured_keys) != 0:
                    captured_keys.pop()
            if key_str == 'Key.enter':
                key_str = '\n'
                captured_keys.append(key_str)
            #The usage of a numpad key without the Numpad enabled will result in an error being thrown when joining the code together due to the lack of valid key being input bet a keystroke being logged. Keys mapped to a blank input instead. 
            #Num pad key 5 continues to have strange behavior that will require further testing. 
            if key_str == 'Key.end':
                key_str = ''
            if key_str == 'Key.down':
                key_str = ''
            if key_str == 'Key.up':
                key_str = ''
            if key_str == 'Key.left':
                key_str = ''
            if key_str == 'Key.right':
                key_str = ''
            if key_str == 'Key.page_up':
                key_str = ''
            if key_str == 'Key.page_adown':
                key_str = ''
            if key_str == 'Key.numpad5':
                key_str = ''

        

def on_release(key):
    if len(captured_keys) >= 150:
        print("Save soon!")
    

# Collect events until released
with Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()

