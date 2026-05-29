def jumlah_digit(angka):
    if angka < 10:
        print(angka, end='')
        return angka
    
    depan = angka // (10 ** (len(str(angka)) - 1))
    
    sisa = angka % (10 ** (len(str(angka)) - 1))
    
    print(depan, end=' + ')
    
    return depan + jumlah_digit(sisa)


try:
    bilangan = int(input("Masukkan bilangan: "))

    hasil = jumlah_digit(bilangan)

    print(" =", hasil)

except ValueError:
    print("Input harus berupa angka!")
    
    