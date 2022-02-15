import tkinter as tk
from tkinter.ttk import *

root = tk.Tk()

root.geometry("450x300")
root.title("Trial Form")

name_var = tk.StringVar()
pass_var = tk.StringVar()


def submit():
    name = name_var.get()
    pas = pass_var.get()

    print("Name :" + name)
    print("Password :" + pas)

    name_var.set("")
    pass_var.set("")


username = Label(root, text="Username").place(
    x=40, y=60
)  # Label	It is used to display text or image on the screen

password = Label(root, text="Passowrd").place(x=40, y=90)

submit = tk.Button(root, text="Submit", command=submit).place(
    x=50, y=120
)  # Button	It is used to add buttons to your application

ext = Button(root, text="Exit").place(x=150, y=120)

ur_space = tk.Entry(root, textvariable=name_var, width=30).place(
    x=110, y=60
)  # Entry	It is used to input single line text entry from user

pass_space = tk.Entry(root, textvariable=pass_var, width=30, show="*").place(
    x=110, y=90
)


root.mainloop()
