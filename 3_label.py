from tkinter import *

root = Tk()
root.title("Test GUI")

label1 = Label(root, text="Hello world")
label1.pack()

photo = PhotoImage(file="arrow.png")
photo2 = PhotoImage(file="star.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="Changed")

def change2():
    label2.config(image=photo2)
button = Button(root, text="click", command=change)
button.pack()

button2 = Button(root, text="click", command=change2)
button2.pack()

root.mainloop()