from tkinter import *

root = Tk()
root.title("Test")

menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_edit = Menu(menu, tearoff=0)

def create_new_file():
    print("work")

menu.add_cascade(label="File", menu=menu_file)

menu_file.add_command(label="New  File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Save", state="disable")
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="Edit", menu=menu_edit)

menu_edit.add_command(label="Copy")
menu_edit.add_radiobutton(label="Test")
menu_edit.add_radiobutton(label="Test123")
menu_edit.add_checkbutton(label="Show")

root.config(menu=menu)
root.mainloop()