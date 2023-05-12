from tkinter import *
a=input("isim gir:")
b=int(input("sayı gir:"))
sayfa= Tk()
sayfa.title("Benim Sayfam")#pencere baslıgı
sayfa.geometry("400x200")
etiket_1=Label(sayfa,text="İsim:")
etiket_2=Label(sayfa,text=a+" Polat")
etiket_3=Label(sayfa,text="Sayınız:")
etiket_4=Label(sayfa,text="Sayı çifttir", bg="red")
etiket_5=Label(sayfa,text="Sayı tektir", bg="green")

etiket_1.grid(row=0)
etiket_3.grid(row=1)
etiket_2.grid(row=0,column=1)

if(b%2==0):
	etiket_4.grid(row=1,column=1)
else:
	etiket_5.grid(row=1,column=1)




sayfa.mainloop()