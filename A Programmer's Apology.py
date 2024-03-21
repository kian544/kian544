import math
from turtle import *
from tkinter import Tk, Button

from clickit import clicked
def reply():
    showinfo(title="Accept my apology :'( !!", message="I'm so sorry, I hope this next thing will cheer you up, click ok then peek at the terminal! :)")
    for i in range(10):
        print("I'm so sorry! :(") #Prints in terminal, right next to the heart while its creating
    print("Now click the 'x' on the button ;)")
    
root = Tk()
widget =Button(root, text="Click here to accept my apology :'( !!", command=reply, height = 10, width=30)
widget.pack()
root.mainloop()


def heart(k): 
    if Button(command=clicked):
        return 15*math.sin(k)**3

def heartb(k):#Credit to @heryyyy on tiktok for the heart code
    if Button(command=clicked):
        return 12*math.cos(k)-5*\
        math.cos(2*k)-2*\
        math.cos(3*k)-\
        math.cos(4*k)
    
speed(9999)
bgcolor("pink") #enter any color, this is background
if Button(command=clicked):
    for i in range(3000):
        goto(heart(i)*20, heartb(i)*20)
        for j in range(5):
            color("black") #Any color, main heart
            goto(0,0)

