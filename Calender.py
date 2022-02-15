from pydoc import text
import tkinter as tk
from tkinter.ttk import *
import calendar

root = tk.Tk()
root.config(background="grey")
root.geometry("350x150")
root.title('Calendar')
year = tk.IntVar()


def show():
    new = tk.Tk()
    year_var = year.get()
    op = calendar.calendar(year_var)
    view = Label(new, text=op, font="consolas 10 bold")
    view.grid(row=5, column=1, padx=20)
    new.mainloop()


cal = Label(root, text="Calendar", font=('times', '28', 'bold')).pack()
text = Label(root, text="Enter Year").pack()

space = tk.Entry(root, textvariable=year, width=30)
space.pack()
search = tk.Button(root, text="Search Year", command=show)
search.pack()

root.mainloop()
