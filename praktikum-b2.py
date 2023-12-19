print("praktikum-b2\n")

print("Nama Lengkap : Muhammad Arham Arsyad")
print("Nim          : 231031042")
print("Prodi        : Sistem Informasi\n")

print("="*20+"\n")

a = 15
print("Nilai a adalah =",a)
a += 2 #ini operasi a = a + 2
print("Nilai a += 2 adalah =",a)

print()
a = 15
print("Nilai a adalah =",a)
a -= 2 #ini operasi a = a - 2
print("Nilai a -= 2 adalah =",a)

print()
a = 15
print("Nilai a adalah =",a)
a *= 2 #ini operasi a = a * 2
print("Nilai a *= 2 adalah =",a)

print()
a = 15
print("Nilai a adalah =",a)
a /= 2 #ini operasi a = a / 2
print("Nilai a /= 2 adalah =",a)

print()
a = 5
print("Nilai a adalah =",a)
a **= 2 #ini operasi a = a ** 2
print("Nilai a **= 2 adalah =",a)

print()
a = 35
print("Nilai a adalah =",a)
a %= 31 #ini operasi a = a % 31
print("Nilai a %= 31 adalah =",a)

print()
a = 35
print("Nilai a adalah =",a)
a //= 31 #ini operasi a = a // 31
print("Nilai a //= 31 adalah =",a)

###################################
print("\n"+"="*20+"\n")

bi = False
print("Nilia bi adalah =",bi)
bi |= True # Tanda | adalah or
print("Nilia bi |= True adalah =",bi) #akan menjadi False ketika keduanya False

print()
bi = False
print("Nilia bi adalah =",bi)
bi &= True # Tanda &= adalah and
print("Nilia bi &= True adalah =",bi) #akan menjadi True ketika keduanya True

print()
bi = False
print("Nilia bi adalah =",bi)
bi ^= True # Tanda ^= adalah xor
print("Nilia bi ^= True adalah =",bi) #Jika keduanya bernilai sama maka hasilnya akan False

##################################
print("\n"+"="*20+"\n")

a = 8
print("Nilai a =",a)
hasil = a == 7
print("Apakah a == 7 ?",hasil) # sama dengan
hasil = a > 7
print("apakah a > 7 ?",hasil) # lebih besar
hasil = a < 7
print("apakah a < 7 ?",hasil) # lebih kecil
hasil = a != 7
print("Apakah a != 7 ?",hasil) # tidak sama dengan
hasil = a >= 7
print("Apakah a >= 7 ?",hasil) # lebih besar sama dengan
hasil = a <= 7
print("Apakah a <= 7 ?",hasil) # lebih kecil sama dengan

#################################
print("\n"+"="*20+"\n")

a = True
b = False
hasil = a and a
print(a,"and",a,"adalah = ",hasil)
hasil = a and b
print(a,"and",b,"adalah = ",hasil)
hasil = b and a
print(b,"and",a,"adalah = ",hasil)
hasil = b and b
print(b,"and",b,"adalah = ",hasil)

print()
a = True
b = False
hasil = a or a
print(a,"or",a,"adalah = ",hasil)
hasil = a or b
print(a,"or",b,"adalah = ",hasil)
hasil = b or a
print(b,"or",a,"adalah = ",hasil)
hasil = b or b
print(b,"or",b,"adalah = ",hasil)

print()
a = True
b = False
hasil = a ^ a
print(a,"xor",a,"adalah = ",hasil)
hasil = a ^ b
print(a,"xor",b,"adalah = ",hasil)
hasil = b ^ a
print(b,"xor",a,"adalah = ",hasil)
hasil = b ^ b
print(b,"xor",b,"adalah = ",hasil)

print()
a = True
b = False
hasil = not a
print("not",a,"adalah = ",hasil)
hasil = not b
print("not",b,"adalah = ",hasil)









