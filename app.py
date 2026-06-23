import tkinter as tk
from datetime import datetime

key_count = 0

def key_pressed(event):
    global key_count

    key = event.keysym
    key_count += 1

    key_label.config(text=f"You pressed: {key}")
    count_label.config(text=f"Total Keys Pressed: {key_count}")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("keystrokes.txt", "a") as file:
        file.write(f"{timestamp} - {key}\n")


def clear_log():
    global key_count

    open("keystrokes.txt", "w").close()

    key_count = 0
    count_label.config(text="Total Keys Pressed: 0")
    key_label.config(text="Log Cleared")


root = tk.Tk()

root.title("Keylogger Security Research")
root.geometry("600x400")

title = tk.Label(root, text="Keystroke Monitoring Simulator", font=("Arial", 14))
title.pack(pady=10)

text_box = tk.Text(root, height=10, width=60)
text_box.pack()

key_label = tk.Label(root, text="Press any key")
key_label.pack(pady=10)

count_label = tk.Label(root, text="Total Keys Pressed: 0")
count_label.pack()

clear_button = tk.Button(root, text="Clear Log", command=clear_log)
clear_button.pack(pady=10)

text_box.bind("<Key>", key_pressed)

root.mainloop()