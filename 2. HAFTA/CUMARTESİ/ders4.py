def ikiCikar(sayi):
	print("Yöntem 1 çalıştı")
	return sayi-2
def UcEkle(sayi):
	print("Yöntem 2 çalıştı")
	return sayi+3
def DortleCarp(sayi):
	print("Yöntem 3 çalıştı")
	return sayi*4
print(DortleCarp(UcEkle(ikiCikar(10))))