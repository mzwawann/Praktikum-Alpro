def ganjil(bawah, atas):
    
    if bawah < atas:
        for i in range(bawah, atas + 1):
            if i % 2 != 0:
                print(i, end=" ")
    else:
        for i in range(bawah, atas - 1, -1):
            if i % 2 != 0:
                print(i, end=" ")

bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))

print("Deret bilangan ganjil:")
ganjil(bawah, atas)

