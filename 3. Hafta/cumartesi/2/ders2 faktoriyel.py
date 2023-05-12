def faktoriyel(sayi):
	deger=sayi
	faktoriyel=1
	if(sayi==0 or sayi==1):
		print("Faktoriyel {} :{} eder".format(sayi,faktoriyel))
	elif sayi<0:
		print("Negatif sayıların faktöriyeli olmaz!")
	else:
		while (sayi>=1):
			faktoriyel*=sayi
			sayi-=1
		print("Faktoriyel {} :{} eder".format(deger,faktoriyel))

sayi=int(input("Faktoriyeli alınacak sayıyı giriniz"))
faktoriyel(sayi)