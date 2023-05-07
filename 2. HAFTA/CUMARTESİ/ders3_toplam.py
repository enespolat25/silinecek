def toplam_al(sayi):
    a=0
    for i in range(sayi+1):
        a=a+i
    print(f"{sayi} ile 0'a kadar sayıların toplamı:{a} eder")

sayi=int(input("sayı gir"))
toplam_al(int(sayi))