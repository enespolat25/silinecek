"""
turkce=["ç","ş","ö","ü"]
degis=["c","s","o","u"]

isim="özgür"
for b in isim:
	for a,d in enumerate(turkce):
		if(b==d):
			isim=isim.replace(b,degis[a])	
print(isim)
"""
ad=input("İsminizi yazar mısınız")
def IsimKontrol(isim):
	if(len(isim)<=4):
		print("isminiz en çok 4 harflidir")
	else:
		print("isminiz en az 5 harflidir")
	turkce=["ç","Ş","ö","ü","ş"]
	degis=["c","S","o","u","s"]
	for b in isim:
		for a,d in enumerate(turkce):
			if(b==d):
				isim=isim.replace(b,degis[a])
	print(isim)
IsimKontrol(ad)