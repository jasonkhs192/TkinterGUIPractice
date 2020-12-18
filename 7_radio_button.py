from tkinter import *

root = Tk()
root.title("Test GUI")

label1 = Label(root, text="Select Meal")
label1.pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="Big Mac", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="Cheese Burger", variable=burger_var, value=2)
btn_burger3 = Radiobutton(root, text="Chicken Burger", variable=burger_var, value=3)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label2 = Label(root, text="Select Drink")
label2.pack()

drink_var = IntVar()
btn_drink1 = Radiobutton(root, text="Coke", variable=drink_var, value=1)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="Sprite", variable=drink_var, value=2)
btn_drink3 = Radiobutton(root, text="Water", variable=drink_var, value=3)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def cmd():
    if burger_var.get() == 1:
        print("Big Mac")
    elif burger_var.get() == 2:
        print("Cheese Burger")
    elif burger_var.get() == 3:
        print("Chicken Burger")

    if drink_var.get() == 1:
        print("Coke")
    elif drink_var.get() == 2:
        print("Sprite")
    else:
        print("Water")



btn = Button(root, text="Click", command=cmd)
btn.pack()
root.mainloop()