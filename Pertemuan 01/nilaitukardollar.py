# nilai kurs 1 US$ ke IDR
kursusd = 13950

# informasi program
print("Program konversi US$ ke IDR")
print("Kurs saat ini 1 US$ = ", kursusd, "Rupiah")

# input jumlah US$ yang mau ditukar
jumlahusd = float(input("Masukkan jumlah uang yang mau ditukar ke Rupiah: "))

# hitung nilainya dalam Rupiah
dalamrupiah = jumlahusd * kursusd

# tampilkan hasilnya
print("Hasil konversi = Rp. ", dalamrupiah)


