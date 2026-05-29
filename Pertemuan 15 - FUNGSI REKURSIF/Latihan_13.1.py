def cek_prima(n, pembagi=2):
    if n < 2:
        return False

    if pembagi == n:
        return True

    if n % pembagi == 0:
        return False

    return cek_prima(n, pembagi + 1)


try:
    bilangan = int(input("Masukkan bilangan: "))

    if cek_prima(bilangan):
        print(bilangan, "adalah bilangan prima")
    else:
        print(bilangan, "bukan bilangan prima")

except ValueError:
    print("Input harus berupa angka!")
    
    