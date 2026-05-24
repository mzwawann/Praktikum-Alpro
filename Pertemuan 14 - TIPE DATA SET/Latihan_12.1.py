n = int(input("Masukkan jumlah kategori: "))

data_aplikasi = {}

for i in range(n):
    nama_kategori = input("Masukkan nama kategori: ")

    print("Masukkan 5 nama aplikasi di kategori", nama_kategori)

    aplikasi = []

    for j in range(5):
        nama_aplikasi = input("Nama aplikasi: ")
        aplikasi.append(nama_aplikasi)

    data_aplikasi[nama_kategori] = aplikasi

print("\nData aplikasi:")
print(data_aplikasi)

daftar_set = {}

for kategori, aplikasi in data_aplikasi.items():
    daftar_set[kategori] = set(aplikasi)

semua_kategori = list(daftar_set.values())

hasil_intersection = semua_kategori[0]

for i in range(1, len(semua_kategori)):
    hasil_intersection = hasil_intersection.intersection(
        semua_kategori[i]
    )

print("\nAplikasi yang muncul di semua kategori:")
print(hasil_intersection)

semua_aplikasi = []

for aplikasi in daftar_set.values():
    semua_aplikasi.extend(aplikasi)

unik_satu_kategori = set()

for app in semua_aplikasi:
    jumlah = 0

    for aplikasi in daftar_set.values():
        if app in aplikasi:
            jumlah += 1

    if jumlah == 1:
        unik_satu_kategori.add(app)

print("\nAplikasi yang hanya muncul di satu kategori:")
print(unik_satu_kategori)

if n > 2:

    tepat_dua = set()

    for app in semua_aplikasi:
        jumlah = 0

        for aplikasi in daftar_set.values():
            if app in aplikasi:
                jumlah += 1

        if jumlah == 2:
            tepat_dua.add(app)

    print("\nAplikasi yang muncul tepat di dua kategori:")
    print(tepat_dua)