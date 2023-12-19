import os
os.system("cls")

pwd_benar = "si23b"
i = 0
limit = 3

while True:
    i += 1
    pwd = input("Masukkan Password: ")
    if pwd == pwd_benar:
        print("Selamat anda Login!")
        break
    else:
        if i == limit:
            print("Anda kehabisan kesempatan")
            break
        else:
            print("Password Salah")
            print(f"Kesempatan anda tersisa {limit-i} kali")      