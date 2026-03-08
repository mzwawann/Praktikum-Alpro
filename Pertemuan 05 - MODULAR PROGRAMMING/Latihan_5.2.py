def cek_digit_belakang(a, b, c):
    digit1 = a % 10
    digit2 = b % 10
    digit3 = c % 10
    
    if digit1 == digit2 or digit1 == digit3 or digit2 == digit3:
        return True
    else:
        return False

a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

print(cek_digit_belakang(a, b, c))

