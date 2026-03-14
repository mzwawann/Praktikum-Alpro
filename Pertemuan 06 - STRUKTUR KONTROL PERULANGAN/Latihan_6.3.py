jumlah_mk = int(input("Masukkan jumlah mata kuliah: "))

total_nilai = 0

for i in range(1, jumlah_mk + 1):
    nilai = input("Masukkan nilai mata kuliah " + str(i) + ": ").upper()

    if nilai == "A":
        bobot = 4
    elif nilai == "B":
        bobot = 3
    elif nilai == "C":
        bobot = 2
    elif nilai == "D":
        bobot = 1
    else:
        print("Nilai tidak valid")
        bobot = 0

    total_nilai = total_nilai + (bobot * 3)

total_sks = jumlah_mk * 3
ips = total_nilai / total_sks
print("Nilai IPS anda semester ini", ips)

