from tkinter import *

sayfa=Tk()
sayfa.title("Veri Girişi")
sayfa.geometry("800x400")

def Tikla():
    durum=True
    isim=veriGirisi.get()
    unlu=["a","e","ı","i","o","ö","u","ü"]
    for i in unlu:
        if isim[0]==i:
            label=Label(sayfa,text=isim+" ünlü ile başlıyor")
            label.grid(row=3,column=1)
            durum=False

    if durum==True:
        label=Label(sayfa,text=isim+" ünsüz ile başlıyor")
        label.grid(row=3,column=1)

    

isim=Label(sayfa,text="isim giriniz:",font=("Arial",25))
isim.grid(row=0,column=0)

veriGirisi=Entry(sayfa,width=50,font=("Arial",25))
veriGirisi.grid(row=0,column=1)
veriGirisi.insert(0,"isim giriniz")

buton=Button(sayfa,text="tıkla",command=Tikla)
buton.grid(row=1,column=1)

sayfa.mainloop()