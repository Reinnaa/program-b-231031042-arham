import os , sys
os.system("cls")

def judul():
    #judul
    print("program menghitung volume dan luas permukaan".center(45))
    print("menghitung luas balok".center(45))
    print()

def inputan():
    panjang = float(input("masukan lebar : "))
    lebar = float(input("masukan lebar : "))
    tinggi = float(input("masukan tinggi : "))
    return panjang,lebar,tinggi

def hitung(panjang,lebar,tinggi):
    volume = panjang*lebar*tinggi
    luas_surf = 2*(panjang*lebar + panjang*tinggi + lebar*tinggi)
    luas_non_surf = luas_surf - panjang*lebar
    return volume,luas_surf,luas_non_surf

def tampilan(pesan,nilai):
    print(f"nilai {pesan} = {nilai}")

def pilihan():
    back = input("lanjut?(y/n) : ").lower()
    if back == "y":
        os.system("cls")
        pass
    else:
        print("terima kasih")
        sys.exit()
    return

def main():
    while True:
        judul() #judul
        panjang,lebar,tinggi = inputan() #input
        volume,luas_surf,luas_non_surf = hitung(panjang,lebar,tinggi) #hitung
        tampilan("volume",volume) #tampilan
        tampilan("luas permukaan",luas_surf) #tampilan
        tampilan("luas permukaan tanpa tutup",luas_non_surf) #tampilan
        pilihan() #pilihan

main()