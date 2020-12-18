from tkinter import *

root = Tk()
root.title("Test GUI")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "One")
listbox.insert(1, "Two")
listbox.insert(2, "Three")
listbox.insert(3, "Four")
listbox.insert(4, "Five")
listbox.insert(END, "Six")
listbox.pack()

def cmd():
    #delete
    listbox.delete(END)

def cmd2():
    # count list size
    print(listbox.size())

def cmd3():
    # check item
    print(listbox.get(0, 2))

def cmd4():
    # Highlighted item position
    print(listbox.curselection())

btn = Button(root, text="Delete", command=cmd)
btn.pack()

btn2 = Button(root, text="Total Count", command=cmd2)
btn2.pack()

btn3 = Button(root, text="1~3 Item", command=cmd3)
btn3.pack()

btn4 = Button(root, text="Position", command=cmd4)
btn4.pack()

root.mainloop()
