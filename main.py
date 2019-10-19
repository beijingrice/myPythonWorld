from tkinter import *
import tkinter.messagebox
import time
import threading
tk = Tk()
tk.title("Timer")
E = Entry(tk)
E.grid(row=0, column=0)
L = Label(tk, text="Time remain")
L.grid(row=0, column=1)


def second_remain():
    cmd = tkinter.messagebox.askyesno("Timer", "Are you sure start a timer with second?")
    if not cmd:
        return

    def remain():
        try:
            time_remain = int(E.get())
        except ValueError:
            tkinter.messagebox.showerror("Timer: Error!", "Error with input!")
            time_remain = 0
        time.sleep(time_remain)
        tkinter.messagebox.showwarning("Timer", "Time is up!")

    remain_thread = threading.Thread(target=remain)
    remain_thread.start()


def minute_remain():
    cmd = tkinter.messagebox.askyesno("Timer", "Are you sure start a timer with minute?")
    if not cmd:
        return

    def remain():
        try:
            time_remain = int(E.get()) * 60
        except ValueError:
            tkinter.messagebox.showerror("Timer: Error!", "Error with input!")
            time_remain = 0
        time.sleep(time_remain)
        tkinter.messagebox.showwarning("Timer", "Time is up!")

    remain_thread = threading.Thread(target=remain)
    remain_thread.start()


def hour_remain():
    cmd = tkinter.messagebox.askyesno("Timer", "Are you sure start a timer with hour?")
    if not cmd:
        return

    def remain():
        try:
            time_remain = int(E.get()) * 3600
        except ValueError:
            tkinter.messagebox.showerror("Timer: Error!", "Error with input!")
            time_remain = 0
        time.sleep(time_remain)
        tkinter.messagebox.showwarning("Timer", "Time is up!")

    remain_thread = threading.Thread(target=remain)
    remain_thread.start()


B = Button(tk, text="Start timer with second", command=second_remain)
B.grid(row=1, column=0)
B1 = Button(tk, text="Start timer with minute", command=minute_remain)
B1.grid(row=1, column=1)
B2 = Button(tk, text="Start timer with hour", command=hour_remain)
B2.grid(row=1, column=2)
tk.mainloop()
