from cProfile import label
from cgitb import text
import random
from tkinter import *

root = Tk()
root.geometry("700x750")

root.title('Dice-simulator')

l1 = Label(root, text="", font=('times', 200))


def roll():
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')
    l1.pack(anchor='center')


b1 = Button(root, text="Let's roll...", command=roll)
b1.place(x=330, y=0)

root.mainloop()
