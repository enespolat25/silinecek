liste=["enes","polat","türkiye"]
tersCevir= lambda a:a[::-1]
liste3=[tersCevir(a) for a in tersCevir(liste)]
print(liste3)