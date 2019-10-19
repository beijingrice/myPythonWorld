from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import threading
import os
tk = Tk()
tk.title("Java runner")


def ui_runner():
    filename = tkinter.filedialog.askopenfilename(title="Open a java file and run", filetypes=[("Java file", "*.java")])

    def thread():
        os.system("java %s" % filename)

    main_thread = threading.Thread(target=thread)
    main_thread.start()


def entry_runner():
    filename = E.get()

    def thread():
        os.system("java %s" % filename)

    main_thread = threading.Thread(target=thread)
    main_thread.start()


def _quit():
    cmd = tkinter.messagebox.askyesno("Java Runner", "Are you sure you want to exit?")
    if cmd:
        tk.destroy()


E = Entry(tk)
E.grid(row=0, column=0)
L = Label(tk, text="Input java filename")
L.grid(row=0, column=1)
B = Button(tk, text="Run with entry", command=entry_runner)
B.grid(row=1, column=0)
B1 = Button(tk, text="Run with UI", command=ui_runner)
B1.grid(row=1, column=1)
tk.protocol("WM_DELETE_WINDOW", _quit)
tk.mainloop()
