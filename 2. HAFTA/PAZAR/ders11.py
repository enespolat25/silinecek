def isimKontrol(isim):
    unlu=["a","e","ı","i","o","ö","u","ü"]
    durum=True
    for i in unlu:
        if isim[0].lower()==i:
            f=open("unluHarf.txt","a")
            f.write(isim+"\n")
            f.close()
            durum=False
            break
    if durum==True:
        f=open("normalHarf.txt","a")
        f.write(isim+"\n")
        f.close()
           
j=0
while j<4:
    j+=1
    isim=input("isim giriniz=")
    isimKontrol(isim)