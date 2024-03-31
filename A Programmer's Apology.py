import math
from tkinter.messagebox import showinfo
from turtle import *
from tkinter import Tk, Button
def reply():
    showinfo(title="Accept my apology :'( !!", message="I'm so sorry, I hope this next thing will cheer you up, click ok then peek at the terminal! :)")
    for i in range(10):
        print("I'm so sorry! :(") #Prints in terminal after clicking OK
    print("Now click the 'x' on the button ;)")
    
root = Tk()
widget =Button(root, text="Click here to accept my apology :'( !!", command=reply, height = 10, width=30)
widget.pack()
def clicked():
    pass

root.mainloop()

def heart(k): 
    if Button(command=clicked):
        return 15*math.sin(k)**3

def heartb(k):
    if Button(command=clicked):
        return 12*math.cos(k)-5*\
        math.cos(2*k)-2*\
        math.cos(3*k)-\
        math.cos(4*k)
    
speed(9999)
bgcolor("green") #enter any color, this is background
if Button(command=clicked):
    for i in range(2000):
        goto(heart(i)*5, heartb(i)*5) #Adjust heart size, set to 5 stock for optimal speed
        for j in range(5):
            color("gold") #Any color, main heart
            goto(0,0) #x out of heart once shape is attained, will take a while for a full fill 

