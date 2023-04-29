liste = [1,2,3,4,5,6,3,5,6,1,8,7,5,4,3,1,2,5]

def sayiCikar(sayi):
    sayac = 0
    for i in liste:
        if int(i) == sayi:
            sayac += 1
            liste.remove(i)
    
    print("adet=",sayac)
    print(liste)

sayiCikar(5)