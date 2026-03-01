input_bulan = input("Masukkan bulan (1-12): ")

try:
    bulan = int(input_bulan)

    if bulan == 2:
        print("Jumlah hari: 29")
    elif bulan in [4, 6, 9, 11]:
        print("Jumlah hari: 30")
    elif bulan in [1, 3, 5, 7, 8, 10, 12]:
        print("Jumlah hari: 31")
    else:
        print("Bulan tidak valid!")

except:
    print("Input harus berupa angka!")
    
    