from tkinter import *

root = Tk()
root.title("Test GUI")

chkvar = IntVar()
checkbox = Checkbutton(root, text="Don't Show Again Today", variable=chkvar)
# checkbox.select()
# checkbox.deselect()
checkbox.pack()

def cmd():
    print(chkvar.get())

btn = Button(root, text="Click", command=cmd)
btn.pack()
root.mainloop()