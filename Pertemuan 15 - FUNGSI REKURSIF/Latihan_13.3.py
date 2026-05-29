def jumlah_ganjil(n):
    if n == 1:
        print("1", end='')
        return 1
    
    if n % 2 == 0:
        n = n - 1
    
    print(n, end=' + ')
    
    return n + jumlah_ganjil(n - 2)


try:
    bilangan = int(input("Masukkan bilangan ganjil terakhir: "))

    hasil = jumlah_ganjil(bilangan)

    print(" =", hasil)

except ValueError:
    print("Input harus berupa angka!")
    
    