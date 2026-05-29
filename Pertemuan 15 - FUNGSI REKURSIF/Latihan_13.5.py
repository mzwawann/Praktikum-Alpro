def faktorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * faktorial(n - 1)


def kombinasi(n, r):
    return faktorial(n) // (faktorial(r) * faktorial(n - r))


try:
    n = int(input("Masukkan nilai n : "))
    r = int(input("Masukkan nilai r : "))

    hasil = kombinasi(n, r)

    print("C(", n, ",", r, ") =", hasil)

except ValueError:
    print("Input harus berupa angka!")
    
    