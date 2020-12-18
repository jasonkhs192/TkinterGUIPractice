from tkinter import *

root = Tk()
root.title("Test GUI")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "Write here")
entry = Entry(root, width=30)
entry.pack()
entry.insert(0, "One Line Entry")

def cmd():
    print(txt.get("1.0", END)) #1: First Line, 0: 0th column
    print(entry.get())
    txt.delete("1.0", END)
    entry.delete(0, END)

btn = Button(root, text="click", command=cmd)
btn.pack()

root.mainloop()
