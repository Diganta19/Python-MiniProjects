import tkinter as tk
import os
from tkinter import Text, filedialog

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', "r") as f:
        tempapp = f.read()
        tempapp = tempapp.split(',')
        apps = [x for x in tempapp if x.strip()]


def addFile():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select File",
        filetypes=(("executables", "*.exe"), ("all files", "*.*")),
    )
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def run():
    for app in apps:
        os.startfile(app)


def removeApp():
    if os.path.isfile('save.txt'):
        with open('save.txt', 'w') as f:
            f.close()


canvas = tk.Canvas(root, height=600, width=600, bg="#263D42")
canvas.pack()


frame = tk.Frame(root, bg="white")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(
    root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addFile
)
openFile.pack()

runApps = tk.Button(
    root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=run
)
runApps.pack()

rem = tk.Button(root, text='Remove All', padx=10, pady=5,
                fg="white", bg="#263D42", command=removeApp)
rem.pack()


for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open("save.txt", "w") as f:
    for app in apps:
        f.write(app + ",")
