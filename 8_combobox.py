from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Test")

values = [str(x) + " 일" for x in range(1,32)]

combobox = ttk.Combobox(root, height=5, values=values, state="readonly")
combobox.pack()
combobox.set("Pay Date")

def cmd():
    if combobox.get() != "Pay Date":
        print(combobox.get())
    else:
        print("Error")

button = Button(root, text="Select", command=cmd)
button.pack()
root.mainloop()