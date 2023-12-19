nama = "Muhammad Arham Arsyad"
nim = "231031042"
meet = "praktikum 4 B"
prodi = "Sistem Informasi B"
email = "mrham1908@gmail.com"
tanggal = "11 oktober 2023"
sp = 40
print()
#print(len(nama))
print("-"*sp)

print(nama.center(sp))
print(nim.center(sp))
print("\n"*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(tanggal.rjust(sp)+f"\r{email}")
print("-"*sp+"\n")

paragraf = """halo,selamat datang perkenalkan nama saya {} dengan nim {} dari prodi {}. ini adalah file {}"""
p = paragraf.format(nama,nim,prodi,meet)
print(p)
print()

print("------8+++++++")
x = 9
hasil = x > 8
print(9,"hasilnya adalah : ",hasil)

print("++++++8-------")
x = 9
hasil = x < 8
print(x,"hasilnya adalah : ",hasil)
print()

print("------4++++++8-------")
x = 3
cek1 = x > 4
cek2 = x < 8
hasil = cek1 and cek2
print(x,"hasilnya adalah : ",hasil)
print()

print("++++++4-------8++++++")
x = 3
cek1 = x < 4
cek2 = x > 8
hasil = cek1 or cek2
print(x,"hasilnya adalah : ",hasil)


