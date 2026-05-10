data = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Menampilkan judul
print("key\tvalue\titem")

# Melakukan perulangan pada dictionary
for key, value in data.items():
    print(key, "\t", value, "\t", key)