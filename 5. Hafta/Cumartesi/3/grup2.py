from tkinter import *

sayfa = Tk()
sayfa.title("Benim Sayfam")
sayfa.geometry("400x200")

bir = Label(sayfa,text="Bir",bg="red", fg="White")
bir.pack(fill=X)

iki = Label(sayfa,text="İki",bg="green", fg="black")
iki.pack(side=LEFT,fill=Y)

uc = Label(sayfa,text="Uc",bg="blue", fg="white")
uc.pack(fill=X)

dort = Label(sayfa,text="Dort",bg="yellow", fg="white")
dort.pack(side=LEFT,fill=Y)

bes = Label(sayfa,text="Bes",bg="pink", fg="white")
bes.pack(fill=X)

alti = Label(sayfa,text="Altı",bg="orange", fg="white")
alti.pack(side=LEFT,fill=Y)

sayfa.mainloop()
