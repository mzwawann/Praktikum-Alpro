def cari_kata(kalimat):
    kalimat = kalimat.lower()
    kata_list = kalimat.split()

    terpendek = kata_list[0]
    terpanjang = kata_list[0]
   
    for kata in kata_list:
        if len(kata) < len(terpendek):
            terpendek = kata
        if len(kata) > len(terpanjang):
            terpanjang = kata
    
    return terpendek, terpanjang

kalimat = input("Masukkan kalimat: ")
pendek, panjang = cari_kata(kalimat)

print("terpendek:", pendek)
print("terpanjang:", panjang)