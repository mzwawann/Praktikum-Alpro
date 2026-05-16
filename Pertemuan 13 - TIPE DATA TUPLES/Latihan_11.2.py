data = ("Kurniawan Firdaus", "71251186", "Bantul, DI Yogyakarta")

print("Data:", data)

nama, nim, alamat = data

print("NIM :", nim)
print("NAMA :", nama)
print("ALAMAT :", alamat)

tpl_nim = tuple(nim)
print("NIM:", tpl_nim)

nama_depan = tuple(nama.split()[0][1:])
print("NAMA DEPAN:", nama_depan)

nama_terbalik = tuple(nama.split()[::-1])
print("NAMA TERBALIK:", nama_terbalik)

