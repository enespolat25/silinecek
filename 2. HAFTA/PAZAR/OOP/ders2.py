class Ogrenci:
	def __init__(self,isim,yas,dersler):
		self.isim=isim
		self.yas=yas
		self.dersler=dersler
	def __str__(self):
		return f"{self.isim} hanım {self.yas} yaşında aramıza katıldı\naldığı dersler:{self.dersler}"
	def isimGuncelle(self,yeniisim):
		self.isim=yeniisim
"""
abbas=Ogrenci("Abbas Polat",29,["kimya","ingilizce"])
abbas.isimGuncelle("ABBAS")
print(abbas.isim)
"""
enes=Ogrenci("Enes",36,{"matematik":44,"coğrafya":"kaldi","kimya":True})

ayla=Ogrenci("Ayla",11,{"Kimya":44,"coğrafya":"geçti","kimya":True})
#print(enes.yas)
#print(enes.dersler["kimya"])
#print(enes) 
print(ayla) 