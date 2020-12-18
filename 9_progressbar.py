from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("Test")

pb = ttk.Progressbar(root, maximum=100, mode="determinate")
pb.start(10) #10 ms
pb.pack()

p_var2 = DoubleVar()
pb2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
pb2.pack()

def cmd():
    pb.stop()

def cmd2():
    for i in range(1, 101):
        time.sleep(0.1)
        p_var2.set(i)
        pb2.update()

#Manual process
def cmd3():
    p_var2.set(25)
    time.sleep(1)
    pb2.update()
    p_var2.set(80)
    time.sleep(2)

button = Button(root, text="Stop", command=cmd)
button.pack()

button2 = Button(root, text="Start", command=cmd2)
button2.pack()
root.mainloop()