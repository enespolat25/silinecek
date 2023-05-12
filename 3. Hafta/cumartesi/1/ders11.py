liste=[5,4,3,2,1,0,-1,-2,-3,-4,-5]
print("işe başladım")
def Bol():
	for i in liste:
		try:
			sonuc=100/i
			print(sonuc)
		except ZeroDivisionError as e:
			print("lütfen paydada 0 bulundurmayınız")
	print("iş bitti patron")	
Bol()
print("hayat devam ediyor")