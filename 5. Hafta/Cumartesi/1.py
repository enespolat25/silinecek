from tkinter import *
sayfa=Tk()
ustframe=Frame(sayfa)
ustframe.pack()
altframe=Frame(sayfa)  
altframe.pack(side=LEFT)
buton1=Button(ustframe,text="Buton 1", fg="red")
buton2=Button(ustframe,text="Buton 2", fg="blue")
buton3=Button(ustframe,text="Buton 3", fg="green")
buton4=Button(altframe,text="Buton 4", fg="purple")
buton1.pack(side=LEFT)
buton2.pack(side=RIGHT)
buton3.pack(side=BOTTOM)
buton4.pack(side=LEFT)

sayfa.mainloop()