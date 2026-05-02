def tiga_terbaik(data):
    data_sorted = sorted(data, reverse=True)
    return data_sorted[:3]

angka = [10, 5, 8, 20, 15, 3, 25]
hasil = tiga_terbaik(angka)

print("3 bilangan terbaik:", hasil)