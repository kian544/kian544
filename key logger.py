from tkinter import Tk, Text, BOTH

def record(event):
    "Event handling function for key press events"
    print(f'char= {event.keysym}')

root=Tk()
text = Text(root, width=40, height = 10)

text.bind('<KeyPress>', record)

text.pack(expand=True, fill=BOTH)

root.mainloop()
