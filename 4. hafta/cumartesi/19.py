a=list(range(1,7))
b=[eleman for eleman in a if eleman%2==0 and eleman%3==0]
print(b)

liste=["ali","enes","kerim","aslı","ender","yusuf","selahaddin"]
liste2=[isim for isim in liste if len(isim)>4]
print(liste2)