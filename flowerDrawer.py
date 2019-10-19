from tkinter import *
import tkinter.messagebox
import turtle
tk = Tk()
tk.title("Flower Drawer")
E = Entry(tk)
E.grid(row=0, column=0)
L = Label(tk, text="Flower Color")
L.grid(row=0, column=1)
E1 = Entry(tk)
E1.grid(row=1, column=0)
L1 = Label(tk, text="Stem Color")
L1.grid(row=1, column=1)
E2 = Entry(tk)
E2.grid(row=2, column=0)
L2 = Label(tk, text="Pen Size")
L2.grid(row=2, column=1)
E3 = Entry(tk)
E3.grid(row=3, column=0)
L3 = Label(tk, text="Flower Size")
L3.grid(row=3, column=1)
E4 = Entry(tk)
E4.grid(row=4, column=0)
L4 = Label(tk, text="Turtle Speed")
L4.grid(row=4, column=1)


def value_error():
    tkinter.messagebox.showerror("Flower Drawer", "Error: Your input not pure number,\nPlease re-input!")


def main():
    flowerColor = E.get()
    stemColor = E1.get()
    try:
        penSize = int(E2.get())
    except ValueError:
        value_error()
        return
    try:
        flowerSize = int(E3.get())
    except ValueError:
        value_error()
        return
    try:
        speed = int(E4.get())
    except ValueError:
        value_error()
        return
    t = turtle.Pen()
    t.right(90)
    t.pensize(penSize)
    t.pencolor(stemColor)
    t.speed(speed)
    t.forward(300)
    t.left(180)
    t.forward(300)
    t.pencolor(flowerColor)
    for x in range(flowerSize):
        t.left(90)
        t.circle(x)


B = Button(tk, text="Start", command=main)
B.grid(row=5, column=0)
tk.mainloop()
