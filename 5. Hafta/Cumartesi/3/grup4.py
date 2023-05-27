from tkinter import *

sayfa=Tk()
sayfa.title("Benim Sayfam")
sayfa.geometry("400x300")
l1=Label(sayfa, text="1",background="red",fg="white")
l1.pack()
l2=Label(sayfa, text="2",background="green",fg="black")
l2.pack(fill=X)
l3=Label(sayfa, text="3",background="blue",fg="red")
l3.pack(side=LEFT,fill=Y)

l4=Label(sayfa, text="4",background="green",fg="black")
l4.pack(fill=X)
l5=Label(sayfa, text="5",background="blue",fg="red")
l5.pack(side=LEFT,fill=Y)

l6=Label(sayfa, text="6",background="green",fg="black")
l6.pack(fill=X)
l7=Label(sayfa, text="7",background="blue",fg="red")
l7.pack(side=LEFT,fill=Y)

sayfa.mainloop()
