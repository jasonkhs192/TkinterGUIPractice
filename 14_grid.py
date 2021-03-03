from tkinter import *

root = Tk()
root.title("Test")
string = "mystring"
lst = ""
lst2 = [1,2]

txt = Text(root, width=30, height=5)
txt.grid(row=5, column=0, columnspan=4, sticky=N+E+W+S, padx=3, pady=3)


def percent():
    global lst
    lst = lst + "%"
    txt.insert(END, lst)
    lst = ""

def c():
    txt.delete("1.0", END)


def del1():
    global lst
    lst = txt.get("1.0", END)
    x = len(lst) - 2
    lst2 = lst[:x]
    txt.delete("1.0", END)
    txt.insert(END, lst2)
    lst = ""

def plus():
    global lst
    lst = lst + "+"
    txt.insert(END, lst)
    lst = ""


def minus():
    global lst
    lst = lst + "-"
    txt.insert(END, lst)
    lst = ""

def zero():
    global lst
    lst = lst + "0"
    txt.insert(END, lst)
    lst = ""


def one():
    global lst
    lst = lst + "1"
    txt.insert(END, lst)
    lst = ""


def two():
    global lst
    lst = lst + "2"
    txt.insert(END, lst)
    lst = ""

def three():
    global lst
    lst = lst + "3"
    txt.insert(END, lst)
    lst = ""

def four():
    global lst
    lst = lst + "4"
    txt.insert(END, lst)
    lst = ""

def five():
    global lst
    lst = lst + "5"
    txt.insert(END, lst)
    lst = ""

def six():
    global lst
    lst = lst + "6"
    txt.insert(END, lst)
    lst = ""

def seven():
    global lst
    lst = lst + "7"
    txt.insert(END, lst)
    lst = ""

def eight():
    global lst
    lst = lst + "8"
    txt.insert(END, lst)
    lst = ""

def nine():
    global lst
    lst = lst + "9"
    txt.insert(END, lst)
    lst = ""

def enter():
    global lst
    lst = txt.get("1.0", END)

    lst = ""


btn_percent = Button(root, text="%", width=5, height=2, command=percent)
btn_ce = Button(root, text="CE", width=5, height=2, command=enter)
btn_c = Button(root, text="C", width=5, height=2, command=c)
btn_del = Button(root, text="Del", width=5, height=2, command=del1)

btn_percent.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_ce.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_c.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_del.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_zero = Button(root, text="0", width=5, height=2, command=zero)
btn_power = Button(root, text="x^2", width=5, height=2)
btn_root = Button(root, text="root", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)

btn_zero.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_power.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_root.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_seven = Button(root, text="7", width=5, height=2, command=seven)
btn_eight = Button(root, text="8", width=5, height=2, command=eight)
btn_nine = Button(root, text="9", width=5, height=2, command=nine)
btn_multi = Button(root, text="X", width=5, height=2)

btn_seven.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_eight.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_nine.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_multi.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_four = Button(root, text="4", width=5, height=2, command=four)
btn_five = Button(root, text="5", width=5, height=2, command=five)
btn_six = Button(root, text="6", width=5, height=2, command=six)
btn_minus = Button(root, text="-", width=5, height=2, command=minus)

btn_four.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_five.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_six.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_minus.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_one = Button(root, text="1", width=5, height=2, command=one)
btn_two = Button(root, text="2", width=5, height=2, command=two)
btn_three = Button(root, text="3", width=5, height=2, command=three)
btn_plus = Button(root, text="+", width=5, height=2, command=plus)

btn_one.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_two.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_three.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_plus.grid(row=4, column=3, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop()