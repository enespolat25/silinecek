from tkinter import *
sayfa = Tk()
sayfa.title("Veri Girişi")
sayfa.geometry("800x1000")
def Tikla():
	yazi="Merhaba "+ veriGirisi.get()
	yaziLabel=Label(sayfa,text=yazi,font=("Arial", 36))
	yaziLabel.grid(row=2,column=1)
isim=Label(sayfa,text="İsim:",bg="yellow",fg="blue",font=("Arial", 25))
isim.grid(row=0,column=0)
veriGirisi=Entry(sayfa,width=25,font=("Arial", 36))
veriGirisi.grid(row=0,column=1)
veriGirisi.insert(0,"İsim giriniz")
buton= Button(sayfa,text="Beni Tıkla",command=Tikla,font=("Arial", 36))
buton.grid(row=1,column=1)
sayfa.mainloop()