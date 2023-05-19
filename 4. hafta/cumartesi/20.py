liste1=["mat","kim","cog","bed","res","müz"]
liste2=["kimya", "resim","müzik"]

liste3=[a for b in liste2 for a in liste1  if b.find(a)!=-1]
print(liste3)