input_user = input("Masukkan bilangan: ")

try:
    bilangan = int(input_user)
    hasil = "Positif" if bilangan > 0 else "Negatif" if bilangan < 0 else "Nol"
    print(hasil)
except:
    print("Input tidak valid! Harus berupa angka.")

