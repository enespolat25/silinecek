import datetime
class BTK:
	yil=datetime.datetime.now().strftime("%Y")
	katilimcisayisi=23
	def selamla(parametre):
		print("eğitim başladı.")
	
	

python=BTK()
print(python.yil)
python.katilimcisayisi=19
print(python.katilimcisayisi)

java=BTK()
print(java.yil)
java.yil=2020
java.katilimcisayisi=15
print(java.katilimcisayisi)

python.selamla()
java.selamla()


