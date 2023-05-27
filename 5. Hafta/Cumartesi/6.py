a=list(range(1,101))
b=[eleman for eleman in range(1,1004) if eleman%3==0 and eleman%5==0]
c=[i for i in a  if i%5==0 and b.count(i)>0]
print(c)