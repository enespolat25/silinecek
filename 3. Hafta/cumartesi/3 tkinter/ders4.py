from tkinter import *
a=input("yazı gir:")
sayfa= Tk()
sayfa.title("Benim Sayfam")#pencere baslıgı
sayfa.geometry("400x200")
etiket_1=Label(sayfa,text="İsim"+a)
etiket_2=Label(sayfa,text="Parola")
data1=Entry(sayfa)
data2=Entry(sayfa)

etiket_1.grid(row=0)
etiket_2.grid(row=1)
data1.grid(row=0,column=1)
data2.grid(row=1,column=1)



sayfa.mainloop()