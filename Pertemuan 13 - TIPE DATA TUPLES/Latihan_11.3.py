jam_email = dict()
lst = list()

fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("File tidak ditemukan")
    quit()

for baris in fhand:

    if baris.startswith("From "):

        kata = baris.split()
        waktu = kata[5]
        jam = waktu.split(":")[0]
        jam_email[jam] = jam_email.get(jam, 0) + 1

for key, val in jam_email.items():
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)
    
    