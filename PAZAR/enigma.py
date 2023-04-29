Alfabe = ["a","A","b","B","c","C","ç","Ç","d","D","e","E","f","F","g","G","ğ","Ğ","h","H","ı","I","i","İ","j","J","k","K",
"l","L","m","M","n","N","o","O","ö","Ö","p","P","r","R","s","S","ş","Ş","t","T","u","U","ü","Ü","v","V","y","Y","z","Z"]
SifreKarakter = ["z","Z","Y","y","V","v","Ü","ü","u","U","T","t","Ş","ş","s","S","R","r","P","p","Ö","ö","O","o","n","N",
"M","m","Q","q","K","k","J","j","i","İ","I","ı","H","h","Ğ","ğ","g","G","F","f","e","E","D","d","C","c","B","b","a","A","Ç","ç"]

varriable = input("Lütfen Şifrelenmesi İstediğiniz Metini Giriniz= ")

def encryption(text):
    if (len(text)) <= 10:
        print("Girdiğiniz Metin Kısaymış İşlem Hızlı Oldu Beybisi")
    else:
        print("Girdiğin Metin Uzunmuş Ama Olsun Beybisi Hallettim Muaah <3")
    for i in text:
        for j,k in enumerate(Alfabe):
            if (i==k):
                text=text.replace(i,SifreKarakter[j])
    return(text)

def encryption2(text2):
    for i in text2:
        for j,k in enumerate(Alfabe):
            if (i==j):
                text2=text2.replace(i,SifreKarakter[j])
    return(text2)

returnBack = encryption(varriable)
print("Şifrelenmiş Metininiz= ",returnBack)

varriable2 = int(input("Lütfen Şifrenin Geri Çözülmesi İçin 1 Yazınız= "))

if (varriable2 == 1):
   print("Geri Çözdüğünüz Metin= ",encryption2(varriable))
else:
    print("Peki Sen Bilirsin")