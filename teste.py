from tkinter import *
from tkinter.ttk import *
import os

root = Tk()

# I set the length and maximum as shown to demonstrate the process in the
# proceeding function. Pay attention to the increment r
progress = Progressbar(root, orient=HORIZONTAL,
                       length=200 / 5, maximum=200 / 5, mode='determinate')


# Function


def my_func():
    t = 0
    r = 1 / 5
    for i in range(200):
        print(i)  # whatever function interests you
        t = t + r
        progress['value'] = t
        root.update_idletasks()


progress.pack()

# Button
Button(root, text='Start', command=bar).pack(pady=10)

mainloop()