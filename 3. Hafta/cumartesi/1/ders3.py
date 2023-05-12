tumliste=[]
tekler=[]
çiftler=[]
sayi1=int(input("sayı gir"))
tumliste.append(sayi1)
if sayi1%2==0:
	çiftler.append(sayi1)
else:
	tekler.append(sayi1)

sayi2=int(input("sayı gir"))
tumliste.append(sayi2)
if sayi2%2==0:
	çiftler.append(sayi2)
else:
	tekler.append(sayi2)

sayi3=int(input("sayı gir"))
tumliste.append(sayi3)
if sayi3%2==0:
	çiftler.append(sayi3)
else:
	tekler.append(sayi3)

sayi4=int(input("sayı gir"))
tumliste.append(sayi4)
if sayi4%2==0:
	çiftler.append(sayi4)
else:
	tekler.append(sayi4)

sayi5=int(input("sayı gir"))
tumliste.append(sayi5)
if sayi5%2==0:
	çiftler.append(sayi5)
else:
	tekler.append(sayi5)

print("Tüm liste:",tumliste)
print("Çiftler listesi: ",çiftler)
print("Tekler listesi",tekler)
