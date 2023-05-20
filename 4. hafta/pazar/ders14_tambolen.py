def tam_bolenler(sayi):
	tam_bolen=[]
	for i in range(2,sayi+1):
		if(sayi%i==0):
			tam_bolen.append(i)
	return tam_bolen
while True:
	sayi=input("Sayı giriniz:")
	if(sayi=="q" or sayi=="Q"):
		break
	else:
		sayi=int(sayi)
		print("Tam bölenler:",tam_bolenler(sayi))