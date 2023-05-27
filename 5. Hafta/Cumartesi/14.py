unlu=open("unlu.txt","a")
normal=open("normal.txt","a")

for a in range(4):
    isim=input("isminizi yazar mısınız")
    if isim[0]=="a" or isim[0]=="e" or isim[0]=="u" or isim[0]=="ü" or isim[0]=="o" or isim[0]=="ö" or isim[0]=="ı" or isim[0]=="i":
        unlu.write(isim+"\n")
    else:
        normal.write(isim+"\n")

normal.close()
unlu.close()
n=open("normal.txt","r")
print("Normal isimler\n")
print(n.read())
print("*"*22)
u=open("unlu.txt","r")
print("\nUnlu isimler")
print(u.read())