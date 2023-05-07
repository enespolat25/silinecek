def fact(sayi):
  deger = 1  
  if sayi >= 0:
    for i in range (1, sayi+1): 
      deger = deger*i
    print("Girdiğiniz sayının faktöriyeli:",deger)
  else:
    print ("Negatif sayıların faktöriyeli olmaz!")

fact(3)