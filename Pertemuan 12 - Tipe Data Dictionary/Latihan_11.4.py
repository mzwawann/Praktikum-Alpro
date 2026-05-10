domain_count = dict()

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

        domain = email.split("@")[1]

        if domain not in domain_count:
            domain_count[domain] = 1
        else:
            domain_count[domain] += 1

print(domain_count)
