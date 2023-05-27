from tkinter import *  
def select():
    deger=" Seçim :"+ str(sp.get())
    label.config(text=deger)

root=Tk()
sp=Spinbox(root,from_=0,to=10, command=select, width=15, font=30)
sp.pack()
label=Label(root,text= " ")
label.pack()
root.mainloop()