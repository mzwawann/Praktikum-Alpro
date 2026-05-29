def palindrom(kalimat):
    kalimat = kalimat.replace(" ", "").lower()

    if len(kalimat) <= 1:
        return True
    
    if kalimat[0] != kalimat[-1]:
        return False
    
    return palindrom(kalimat[1:-1])


try:
    teks = input("Masukkan kalimat: ")

    if palindrom(teks):
        print(teks, "adalah palindrom")
    else:
        print(teks, "bukan palindrom")

except:
    print("Terjadi kesalahan pada input!")
    
    