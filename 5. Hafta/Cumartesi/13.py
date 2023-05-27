dosya=open("demo.txt", "a")
dosya.write("enes\n")
dosya.write("polat\n")

sehir="muş"
dosya.write(sehir+"\n")
dosya.write(input("nerelisiniz"))
dosya.write("\n")
dosya.close()

dosya2=open("demo.txt", "r")
print(dosya2.read())
