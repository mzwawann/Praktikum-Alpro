try:
    file1 = input("Masukkan nama file pertama: ")
    file2 = input("Masukkan nama file kedua: ")

    f1 = open(file1, 'r')
    teks1 = f1.read().lower()

    f2 = open(file2, 'r')
    teks2 = f2.read().lower()

    kata_file1 = set(teks1.split())
    kata_file2 = set(teks2.split())

    kata_sama = kata_file1.intersection(kata_file2)

    print("\nKata-kata yang muncul pada kedua file:")
    
    for kata in kata_sama:
        print(kata)

    f1.close()
    f2.close()

except FileNotFoundError:
    print("Error: File tidak ditemukan atau tidak bisa dibaca")
    
    