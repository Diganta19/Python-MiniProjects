import time
from tkinter import *
import tkinter

root = Tk()  # THIS CREATES THE WINDOW FOR THE CLOCK

# NEXT WE MODIFY THE WINDOW WE CREATED THE ABOVE STEP

root.title("CLOCK")
root.geometry("359x150+0+0")
root.configure(background="black")


def start():
    text = time.strftime("%H:%M:%S %p")
    label.config(text=text)
    label.after(1000, start)


label = Label(root, font=("ds-digital", 50, "bold"), bg="black", fg="green", bd=50)
label.pack(anchor="center")
start()
print("done")
root.mainloop()
