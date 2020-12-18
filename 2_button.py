from tkinter import *

root = Tk()
root.title("Test GUI")

button1 = Button(root, text="Button 1")
button1.pack()

button2 = Button(root, text="Button 2", padx=5, pady=10)
button2.pack()

button3 = Button(root, text="Button 3", padx=10, pady=5)
button3.pack()

button4 = Button(root, text="Button 4", width=10, height=3)
button4.pack()

button5 = Button(root, text="Button 5", fg="red", bg="yellow")
button5.pack()

photo = PhotoImage(file="arrow.png")
button6 = Button(root, image=photo, width=45, height=30)
button6.pack()

def cmd():
    print("Clicked")

button7 = Button(root, text="command", command=cmd)
button7.pack()

root.mainloop()
