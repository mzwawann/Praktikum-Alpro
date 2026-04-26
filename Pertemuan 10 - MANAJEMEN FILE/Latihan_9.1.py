file1 = input("Masukkan nama file pertama: ")
file2 = input("Masukkan nama file kedua: ")

try:
    f1 = open(file1)
    f2 = open(file2)

    baris1 = f1.readlines()
    baris2 = f2.readlines()

    max_len = max(len(baris1), len(baris2))

    for i in range(max_len):
        teks1 = baris1[i].strip() if i < len(baris1) else ""
        teks2 = baris2[i].strip() if i < len(baris2) else ""

        if teks1 != teks2:
            print(f"Perbedaan pada baris ke-{i+1}:")
            print(f"File 1: {teks1}")
            print(f"File 2: {teks2}")
            print("-" * 40)

    f1.close()
    f2.close()

except:
    print("Terjadi kesalahan! Pastikan file tersedia.")
    
    