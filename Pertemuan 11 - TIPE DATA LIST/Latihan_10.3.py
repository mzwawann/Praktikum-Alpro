try:
    filename = input("Masukkan nama file: ")
    handle = open(filename)

    kata_unik = set()

    for line in handle:
        line = line.strip()
        words = line.split()

        for word in words:
            kata_unik.add(word.lower())

    print("Kata unik dalam file:")
    print(kata_unik)

    handle.close()

except:
    print("File tidak ditemukan!")