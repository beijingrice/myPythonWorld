from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import os
import threading
tk = Tk()
tk.title("Java IDE")
T = Text(tk, width=30, height=30)
T.grid(row=0, column=0)


def file_save():
    filename = tkinter.filedialog.asksaveasfilename(title="Save Java File", filetypes=[("Java File", "*.java")])
    try:
        with open(filename, "w+") as obj:
            obj.write(T.get("0.0", "end"))
    except PermissionError:
        tkinter.messagebox.showerror("Error", "Permission Error.")


def runner():

    def inner_runner():
        filename = tkinter.filedialog.askopenfilename(title="Open a java file and run.", filetypes=[("Java Files", "*.java")])
        os.system("java %s" % filename)

    main_thread = threading.Thread(target=inner_runner)
    main_thread.start()


B = Button(tk, text="Save", command=file_save)
B.grid(row=1, column=0)
B1 = Button(tk, text="Run", command=runner)
B1.grid(row=1, column=1)
tk.mainloop()
