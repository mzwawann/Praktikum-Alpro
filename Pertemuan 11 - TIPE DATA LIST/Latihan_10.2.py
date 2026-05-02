total = 0
count = 0

while True:
    user_input = input("Masukkan angka atau 'done' untuk selesai): ")
    
    if user_input.lower() == "done":
        break
    
    try:
        angka = float(user_input)
        total += angka
        count += 1
    except:
        print("Input tidak valid, masukkan angka!")

if count > 0:
    rata_rata = total / count
    print("Rata-rata:", rata_rata)
else:
    print("Tidak ada data yang dimasukkan.")