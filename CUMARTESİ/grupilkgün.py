eleman=list(range(1,76,6)) #1den 75e 6şar artır liste oluştur
eleman.insert(2,90) #3. elemana 90 ekle
eleman.insert(8,100) #9. elemanı 100 ekle
eleman.pop() # son elemanı sill
eleman.insert(0,100) #0. indexe 100 ekle
eleman.sort() #listeyi sırala
a=max(eleman) # max eleman
b=min(eleman) #min eleman
c=a+b #max  min topla
eleman.append(c) #max+mini sona ekle
eleman[2]=40 #3. elemanı 40 olarak değiş
toplma=sum(eleman) #toplamını bul
sayi=len(eleman) #eleman sayısını bul
ort=toplma/sayi# ort
print(eleman) #ekrana yaz
print(ort) #ekrana yaz