from tkinter import Tk, Button, Entry, Label, END
from time import strptime, strftime
from tkinter.messagebox import showinfo

def compute():
    "Entry of date, returns weekday"
    global dateEnt
    date = dateEnt.get()
    weekday = strftime("%A", strptime(date, "%b %d, %Y"))
    showinfo(message = f'{date} was a {weekday}')
    dateEnt.insert(0, weekday+ " ")
def clear():
    global dateEnt
    dateEnt.delete(0,END)
root = Tk()
label = Label(root, text="Enter Date: ")
label.grid(row=0, column=0)
dateEnt=Entry(root)
dateEnt.grid(row=0, column =1)

button = Button(root, text="enter", command=compute)
button.grid(row=1, column=0)

button = Button(root, text="Clear", command=clear)
button.grid(row=1, column=1)
root.mainloop()
