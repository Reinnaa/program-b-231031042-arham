nama = input("masukan nama : ")
pendapatan = int(input("masukan pendapatan karyawan : "))

if pendapatan > 1000:
    status = "status : berhak"
else:
    status = "status : tidak berhak"

print(status)