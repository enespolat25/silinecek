import os
if os.path.exists("olmayan.txt"):
	os.remove("olmayan.txt")
else:
	print("Böyle bir dosya zaten yok ki..")