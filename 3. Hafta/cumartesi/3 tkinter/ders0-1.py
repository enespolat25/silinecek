import tkinter as tk
a=int(input("sayı gir"))
window=tk.Tk()
cift=tk.Label(text="Sayı çifttir")
tek=tk.Label(text="sayı tektir")
if(a%2==0):
	cift.pack()
else:
	tek.pack()
window.mainloop()