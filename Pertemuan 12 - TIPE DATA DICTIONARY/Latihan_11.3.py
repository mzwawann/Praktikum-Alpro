count = dict()

fname = input("Masukkan nama file : ")

try:
    fhand = open(fname)
except:
    print("File tidak dapat dibuka")
    exit()

for line in fhand:
    if line.startswith("From "):
        words = line.split()
        email = words[1]

        if email not in count:
            count[email] = 1
        else:
            count[email] += 1

print(count)