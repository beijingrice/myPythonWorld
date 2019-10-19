from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
tk = Tk()
tk.title("Document test")
T = Text(tk, width=30, height=30)
T.grid(row=0, column=0)


def write():
    text = T.get("0.0","end")
    filename = tkinter.filedialog.asksaveasfilename(title="Save this document", filetypes=[("Text File", "*.txt")])
    with open(filename, "w+") as obj:
        obj.write(text)
    tkinter.messagebox.showwarning(title="Document test", body="Saved!")


def check():
    text = T.get("0.0","end")
    filename = tkinter.filedialog.askopenfile(title="Open a document", filetypes=[("Text File", "*.txt")])
    with open(filename, "r") as obj:
        text_by_file = obj.read()
    if text == text_by_file:
        tkinter.messagebox.showwarning(title="Document test", body="You are right!")
    if text != text_by_file:
        tkinter.messagebox.showwarning(title="Document Test", body="You are wrong!")


B = Button(tk, text="Save", command=write)
B.grid(row=1,column=0)
B1 = Button(tk, text="Check", command=check)
B1.grid(row=1, column=1)
tk.mainloop()