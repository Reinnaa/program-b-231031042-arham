print("praktikum-3")
print("Nama : Muhammad Arham Arsyad")
print("Nim  : 231031042")
print("Prodi Sistem Informasi")

#################################
print("\n"+"="*20+"\n")

a = True
b = False
print("======NAND=======")
hasil = not(a and a)
print(a,"nand",a,"adalah = ",hasil)
hasil = not(a and b)
print(a,"nand",b,"adalah = ",hasil)
hasil = not(b and a)
print(b,"nand",a,"adalah = ",hasil)
hasil = not(b and b)
print(b,"nand",b,"adalah = ",hasil)

print("\n======NOR=======")
a = True
b = False
hasil = not(a or a)
print(a,"nor",a,"adalah = ",hasil)
hasil = not(a or b)
print(a,"nor",b,"adalah = ",hasil)
hasil = not(b or a)
print(b,"nor",a,"adalah = ",hasil)
hasil = not(b or b)
print(b,"nor",b,"adalah = ",hasil)

print("\n======NXOR=======")
a = True
b = False
hasil = not(a ^ a)
print(a,"xor",a,"adalah = ",hasil)
hasil = not(a ^ b)
print(a,"xor",b,"adalah = ",hasil)
hasil = not(b ^ a)
print(b,"xor",a,"adalah = ",hasil)
hasil = not(b ^ b)
print(b,"xor",b,"adalah = ",hasil)



print("\n"+"="*20+"\n")
#ini adalah operator membership
nama = "Muhammad Arham"
tes = "ha"
cek = tes in nama
print(tes,"Ada di",nama,"adalah : ",cek)

tes = "ah"
cek = tes in nama
print(tes,"Ada di",nama,"adalah : ",cek)
print()

tes1 = "a"
tes2 = "i"
tes3 = "u"
tes4 = "i"
tes5 = "o"
print("\n======IN=======")
cek = tes1 in nama
print(tes1,"Ada di",nama,"adalah : ",cek)
cek = tes2 in nama
print(tes2,"Ada di",nama,"adalah : ",cek)
cek = tes3 in nama
print(tes3,"Ada di",nama,"adalah : ",cek)
cek = tes4 in nama
print(tes4,"Ada di",nama,"adalah : ",cek)
cek = tes5 in nama
print(tes5,"Ada di",nama,"adalah : ",cek)

#Tugas kode ================
print("\n======NOT IN=======")
cek = not(tes1 in nama)
print(tes1,"Ada di",nama,"adalah : ",cek)
cek = not(tes2 in nama)
print(tes2,"Ada di",nama,"adalah : ",cek)
cek = not(tes3 in nama)
print(tes3,"Ada di",nama,"adalah : ",cek)
cek = not(tes4 in nama)
print(tes4,"Ada di",nama,"adalah : ",cek)
cek = not(tes5 in nama)
print(tes5,"Ada di",nama,"adalah : ",cek)

#Bitwise

a = 17
b = 7
a += 20
b += 80
print("\n======AND=======")
print("nilai ",a,"Biner Adalah     :",format(a,"09b"))
print("nilai ",b,"Biner Adalah     :",format(b,"09b"))
print("-------------------------------AND")
c = a & b
print("Nilai",a,"&",b,"Biner adalah :",format(c,"09b"))

print("\n======OR=======")
#tugas untuk or
print("nilai ",a,"Biner Adalah     :",format(a,"09b"))
print("nilai ",b,"Biner Adalah     :",format(b,"09b"))
print("-------------------------------OR")
c = a | b
print("Nilai",a,"|",b,"Biner adalah :",format(c,"09b"))

print("\n======XOR=======")
#tugas untuk xor
print("nilai ",a,"Biner Adalah     :",format(a,"09b"))
print("nilai ",b,"Biner Adalah     :",format(b,"09b"))
print("-------------------------------AND")
c = a ^ b
print("Nilai",a,"^",b,"Biner adalah :",format(c,"09b"))

print("\n======NOT=======")
c = ~a
print("nilai ",a,"Biner Adalah    :",format(a,"09b"))
print("Nilai not",a,"Biner adalah :",format(c,"09b"))
print()
c = ~b
print("nilai ",b,"Biner Adalah    :",format(a,"09b"))
print("Nilai not",b,"Biner adalah :",format(c,"09b"))

print("\n======Left Shift=======")
c = a << 2
print("nilai ",a,"Biner Adalah      :",format(a,"09b"))
print("Nilai ",a,"<< 2 Biner adalah :",format(c,"09b"))
c = b << 2
print("nilai ",b,"Biner Adalah      :",format(a,"09b"))
print("Nilai ",b,">> 2 Biner adalah :",format(c,"09b"))

print("\n======Right Shift=======")
c = a >> 2
print("nilai ",a,"Biner Adalah      :",format(a,"09b"))
print("Nilai ",a,"<< 2 Biner adalah :",format(c,"09b"))
c = b >> 2
print("nilai ",b,"Biner Adalah      :",format(a,"09b"))
print("Nilai ",b,"<< 2 Biner adalah :",format(c,"09b"))

print("\n======NOT AND=======")
#TUGAS UNTUK NAND
print("nilai ",a,"Biner Adalah        :",format(a,"09b"))
print("nilai ",b,"Biner Adalah        :",format(b,"09b"))
print("-------------------------------AND")
c = ~(a & b)
print("Nilai",a,"~(&)",b,"Biner adalah :",format(c,"09b"))

print("\n======NOT OR=======")
#TUGAS UNTUK NOR
print("nilai ",a,"Biner Adalah        :",format(a,"09b"))
print("nilai ",b,"Biner Adalah        :",format(b,"09b"))
print("-------------------------------OR")
c = ~(a | b)
print("Nilai",a,"~(|)",b,"Biner adalah :",format(c,"09b"))

print("\n======NOT XOR=======")
#TUGAS UNTUK NXOR
print("nilai ",a,"Biner Adalah     :",format(a,"09b"))
print("nilai ",b,"Biner Adalah     :",format(b,"09b"))
print("-------------------------------AND")
c = ~(a ^ b)
print("Nilai",a,"~(^)",b,"Biner adalah :",format(c,"09b"))

print("\n======NOT >> 2=======")
#TUGAS c = ~(a>>2)
c = ~(a >> 2)
print("nilai ",a,"Biner Adalah           :",format(a,"09b"))
print("--------------------------------not(>>)")
print("Nilai ",a,"not(>>) 2 Biner adalah :",format(c,"09b"))

print("\n======NOT << 2=======")
#TUGAS c = ~(a<<2)
c = ~(a << 2)
print("nilai ",a,"Biner Adalah      :",format(a,"09b"))
print("--------------------------------not(<<)")
print("Nilai ",a,"<< 2 Biner adalah :",format(c,"09b"))

