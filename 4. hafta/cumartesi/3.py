from tkinter import *

def select():
    string = "Selection is "+str(sp.get())
    l.config(text=string)

root = Tk()
sp = Spinbox(root,from_=0,to=10,command=select,width = 15,font=30)
sp.pack()
l=Label(root,text=" ")
l.pack()
mainloop()