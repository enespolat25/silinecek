unlu=open("unlu.txt","a")
normal=open("normal.txt","a")
unlul=["a","e","i","ı","u","ü","o","ö"]
for i in range(10):
    kelime=input("kelime giriniz")
    for i,y in enumerate(kelime):
        sayac=1
        for j in unlul:
            if y==j:
                unlu.write(kelime+"\n")
                sayac=2
                break
        if sayac==1:
            normal.write(kelime+"\n")
            break
unlu.close()
normal.close()
unlu=open("unlu.txt","r")
normal=open("normal.txt","r")
print(unlu.read())
print(normal.read())