# global ve locak değişkenler
c=2
print(c)
def fonksiyon():
	global c
	c=10
	print(c)
c=100
fonksiyon()
print(c)
c=8
print(c)