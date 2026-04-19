def cek_anagram(kata1, kata2):
    kata1 = kata1.lower()
    kata2 = kata2.lower()
    
    urut1 = sorted(kata1)
    urut2 = sorted(kata2)
    
    if urut1 == urut2:
        return "Anagram"
    else:
        return "Bukan Anagram"

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

print(cek_anagram(kata1, kata2))