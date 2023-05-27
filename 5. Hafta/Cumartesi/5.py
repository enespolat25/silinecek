a=list(range(1,101)) # 1,2,3,4
b=list(range(5,104,10)) # 5,15,25,35,.... 95
c= [ eleman for eleman in a if eleman%15==0 and b.count(eleman)>0]
print(c)