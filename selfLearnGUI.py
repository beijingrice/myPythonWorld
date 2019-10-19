from tkinter import *
from subprocess import call
import tkinter.filedialog
import tkinter.messagebox
import pygame
from pygame.locals import *
import pickle


def say(text):
    call(["say", text])


def write():
    # init dirt for use.
    # fill the dirt, then save it to a path.
    dirt = {}
    # init GUI.

    write_tk = Tk()
    write_tk.title = "Write Mode"


    def add_to_dirt():
        dirt[E.get()] = E1.get()


    def save():
        filename = tkinter.filedialog.asksaveasfilename(title="Save your English file", filetypes=[("English Word File", "*.dat")])
        writefile = open(filename,"wb+")
        pickle.dump(dirt,writefile)
        writefile.close()

    E = Entry(tk)
    E.grid(row=0, column=0)
    L = Label(tk, text="English word")
    L.grid(row=0, column=1)
    E1 = Entry(tk)
    E1.grid(row=1, column=0)
    L1 = Label(tk, text="Chinese word")
    L1.grid(row=1, column=1)

    # end.


def test():
    test_tk = Tk()


tk = Tk()
tk.title("English Self-Learn")
B = Button(tk, text="Write Mode", command=write)
B.grid(row=0, column=0)
B1 = Button(tk, text="Test Mode", command=test)
B1.grid(row=0, column=1)
