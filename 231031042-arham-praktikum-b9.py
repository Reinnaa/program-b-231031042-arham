import random as rd

angka = [1,2,3,4,5]

angka_benar = rd.choice(angka)

i = 0
limit = 3
while True:
    i+=1
    pilih = int(input("Tebak angka antara(1-5) : "))
    if pilih == angka_benar:
        benar = "anda benar angka yg benar adalah {}".format(angka_benar)
        print(benar)
        break
    elif pilih != angka_benar:
        if i == limit:
            print("Anda gagal :( ")
            break
        else:
            print(f"Tebakan Salah sisa {limit-i} kesempatan lagi!")

