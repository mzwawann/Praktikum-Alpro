def hapus_spasi_berlebih(kalimat):
    kalimat = kalimat.strip()
    
    kata = kalimat.split()
    hasil = ' '.join(kata)
    
    return hasil

kalimat = input("Masukkan kalimat: ")
print(hapus_spasi_berlebih(kalimat))

