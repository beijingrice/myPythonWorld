import threading
import datetime
from tkinter import *
tk = Tk()
tk.title("Time remain to school!")


def time_remain_calc(time_up=datetime.datetime(2019, 10, 7, 22, 0, 0, 0)):
    return (time_up - datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")


L = Label(tk, text=time_remain_calc())
L.grid(row=0, column=0)


def main():
    L.text = time_remain_calc()


MainThread = threading.Thread(target=main)
MainThread.start()
