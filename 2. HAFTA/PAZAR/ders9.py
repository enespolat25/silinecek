normal=open("normal.txt","a")
unlu=open("unlu.txt","a")

for a in range(4):
	isim=input("isim gir:")
	if isim[0]=="a" or isim[0]=="e" or isim[0]=="u"or isim[0]=="ü"or isim[0]=="ö"or isim[0]=="o"or isim[0]=="ı"or isim[0]=="i":
		unlu.write(isim+"\n")
	else:
		normal.write(isim+"\n")
normal.close()
unlu.close()

normal=open("normal.txt","r")
print(normal.read())
unlu=open("unlu.txt","r")
print(unlu.read())