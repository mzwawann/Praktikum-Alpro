try:
    s1 = int(input("Masukkan sisi 1: "))
    s2 = int(input("Masukkan sisi 2: "))
    s3 = int(input("Masukkan sisi 3: "))

    if s1 == s2 == s3:
        print("3 sisi sama")
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print("2 sisi sama")
    else:
        print("Tidak ada yang sama")

except:
    print("Input tidak valid! Harus berupa angka.")