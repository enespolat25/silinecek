tumListe=[]
tekler=[]
çiftler=[]
for i in range(7) :
    sayi=int(input("sayi gir"))
    tumListe.append(sayi)
    if sayi%2==0:
        çiftler.append(sayi)
    else:
        tekler.append(sayi)
print(tumListe)
print(tekler)
print(çiftler)