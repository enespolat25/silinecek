from tkinter import*
sayfa=Tk()
sayfa.title("Basamak")
sayfa.geometry("120x120")
bir =Label(sayfa,text="Bir",bg="white",fg="white")
bir.pack(fill=X,side=TOP)
iki=Label(sayfa,text="iki",bg="red",fg="red")
iki.pack(fill=Y,side=LEFT)
üç=Label(sayfa,text="üç",bg="white",fg="white")
üç.pack(fill=X,side=TOP)
dort=Label(sayfa,text="üç",bg="red",fg="red")
dort.pack(fill=Y,side=LEFT)
bes=Label(sayfa,text="bes",bg="white",fg="white")
bes.pack(fill=X,side=TOP)
alti=Label(sayfa,text="alti",bg="red",fg="red")
alti.pack(fill=Y,side=LEFT)
yedi=Label(sayfa,text="yedi",bg="white",fg="white")
yedi.pack(fill=X,side=TOP)
sekiz=Label(sayfa,text="sekiz",bg="red",fg="red")
sekiz.pack(fill=Y,side=LEFT)
dokuz=Label(sayfa,text="dokuz",bg="white",fg="white")
dokuz.pack(fill=X,side=TOP)
on=Label(sayfa,text="on",bg="red",fg="red")
on.pack(fill=Y,side=LEFT)

sayfa.mainloop()