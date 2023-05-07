#import datetime
from datetime import datetime
x=datetime(1985,6,18,14,56,00)
"""
print(x)
print(x.strftime("%A")) # HANGİ GÜN
print(x.strftime("%a")) # hangi gün kısaltma
print(x.strftime("%w")) # haftanın kaçıncı günü/ 0 pazar
print(x.strftime("%d")) # ayın kaçıncı günü
print(x.strftime("%b")) # ay kısaltma
print(x.strftime("%B")) # ay 
print(x.strftime("%m")) #  kaçıncı ay
print(x.strftime("%y")) # yıl iki hane
print(x.strftime("%Y")) # yıl iki hane
"""
print(x.strftime("%c")) 