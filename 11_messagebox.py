import tkinter.messagebox as msg
from tkinter import *

root = Tk()
root.title("Test")

def info():
    msg.showinfo("Alert", "Processed")

def info2():
    msg.showwarning("Warning", "Are you sure?")

def info3():
    msg.showerror("Error", "Error has happened")

def info4():
    msg.askokcancel("Confirm", "Continue or Cancel")

def info5():
    msg.askretrycancel("Confirm", "Try again?")

def info6():
    msg.askyesno("Confirm", "Yes or No")

def info7():
    response = msg.askyesnocancel(title=None, message="Not done, Proceed?")
    if response == 1:
        print("Yes")
    elif response == 0:
        print("No")
    else:
        print("Cancel")

Button(root, command=info, text="Alert").pack()
Button(root, command=info2, text="Warning").pack()
Button(root, command=info3, text="Error").pack()
Button(root, command=info4, text="Ask").pack()
Button(root, command=info5, text="AskRetry").pack()
Button(root, command=info6, text="YesNo").pack()
Button(root, command=info7, text="YNCancel").pack()

root.mainloop()