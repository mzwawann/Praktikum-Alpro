input_user = input("Masukkan bilangan: ")

try:
    bilangan = int(input_user)

    if bilangan > 0:
        print("Positif")
    elif bilangan < 0:
        print("Negatif")
    else:
        print("Nol")

except:
    print("Input tidak valid! Harus berupa angka.")
    
    