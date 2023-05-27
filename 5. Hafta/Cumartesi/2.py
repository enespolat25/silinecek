from tkinter import *
sayfa=Tk()
sayfa.title("Benim Sayfam")
sayfa.geometry("400x200")
bir=Label(sayfa,text="Bir", bg="red", fg="white")
bir.pack()
iki=Label(sayfa,text="İki", bg="green", fg="black")
iki.pack(fill=X)
uc=Label(sayfa,text="Üç", bg="blue", fg="white")
uc.pack(fill=Y,side=LEFT)

sayfa.mainloop()