from tkinter import *

root = Tk()
root.title("Test")

lst = []

def percent():
    global lst
    lst.append(" %")
    str1 = ""
    for i in lst:
        str1 = str1 + i

    print(str1)

def ce():
    global lst
    lst.append(" ce")
    str1 = ""
    for i in lst:
        str1 = str1 + i

    print(str1)

def c():
    global lst
    lst.append(" c")
    str1 = ""
    for i in lst:
        str1 = str1 + i

    print(str1)

def del1():
    global lst
    lst.pop()
    str1 = ""
    for i in lst:
        str1 = str1 + i

    print(str1)


btn_percent = Button(root, text="%", width=5, height=2, command=percent)
btn_ce = Button(root, text="CE", width=5, height=2, command=ce)
btn_c = Button(root, text="C", width=5, height=2, command=c)
btn_del = Button(root, text="Del", width=5, height=2, command=del1)

btn_percent.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_ce.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_c.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_del.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_random = Button(root, text="?", width=5, height=2)
btn_power = Button(root, text="x^2", width=5, height=2)
btn_root = Button(root, text="root", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)

btn_random.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_power.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_root.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_seven = Button(root, text="7", width=5, height=2)
btn_eight = Button(root, text="8", width=5, height=2)
btn_nine = Button(root, text="9", width=5, height=2)
btn_multi = Button(root, text="X", width=5, height=2)

btn_seven.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_eight.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_nine.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_multi.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_four = Button(root, text="4", width=5, height=2)
btn_five = Button(root, text="5", width=5, height=2)
btn_six = Button(root, text="6", width=5, height=2)
btn_minus = Button(root, text="-", width=5, height=2)

btn_four.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_five.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_six.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_minus.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_one = Button(root, text="1", width=5, height=2)
btn_two = Button(root, text="2", width=5, height=2)
btn_three = Button(root, text="3", width=5, height=2)
btn_plus = Button(root, text="+", width=5, height=2)

btn_one.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_two.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_three.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_plus.grid(row=4, column=3, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop()