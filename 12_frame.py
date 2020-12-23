from tkinter import *

root = Tk()
root.title("Test")

Label(root, text="Select Menu").pack(side="top")
Button(root, text="Order").pack(side="bottom")
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", expand=True, fill="both")

Button(frame_burger, text="Burger").pack()
Button(frame_burger, text="Cheese Burger").pack()
Button(frame_burger, text="Chicken Burger").pack()

frame_drink = LabelFrame(root, text="Drink")
frame_drink.pack(side="right", expand=True, fill="both")
Button(frame_drink, text="Coke").pack()
Button(frame_drink, text="Sprite").pack()



root.mainloop()