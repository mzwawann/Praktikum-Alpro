def perkalian(a, b):
    hasil = 0
    
    print(a, "x", b, "=", end=" ")
    
    for i in range(a):
        hasil = hasil + b
        print(b, end="")
        
        if i < a-1:
            print(" + ", end="")
    
    print(" =", hasil)

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

perkalian(a, b)