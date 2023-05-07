from tkinter import *

sayfa= Tk()
sayfa.title("Beni Tıkla")
sayfa.geometry("400x300")

def Tikla():
	yazi=Label(sayfa,text="Beni Tıkladın").pack()
buton= Button(sayfa, text="Beni Tıkla", command=Tikla, fg="blue").pack()


sayfa.mainloop()