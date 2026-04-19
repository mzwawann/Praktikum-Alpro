import re
import random
import string

def generate_password(panjang=8):
    karakter = string.ascii_letters + string.digits
    password = ''.join(random.choice(karakter) for i in range(panjang))
    return password

def proses_email(teks):
    email_list = re.findall(r'\S+@\S+', teks)

    if not email_list:
        print("Tidak ditemukan email")
        return
    
    for email in email_list:
        username = email.split("@")[0]
        password = generate_password()
        print(email, "username:", username, ", password:", password)

teks = input("Masukkan teks: ")
proses_email(teks)

