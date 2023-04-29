a = [1,2,4,6,2,34,2,34,2,5,54,2,645,2,44,2,54,2,46,2,2,2,3]
def degerGuncelle(deger1,deger2):
    for i in range(len(a)):
        if a[i] == deger1:
            a[i] = deger2
    print(a)

degerGuncelle(2,100)