def cek_angka(a, b, c):
    if a != b and a != c and b != c:
        if (a + b == c) or (a + c == b) or (b + c == a):
            return True
    return False

print(cek_angka(2, 3, 5))   
print(cek_angka(4, 6, 10))  
print(cek_angka(2, 2, 4))   
print(cek_angka(3, 4, 8))   

