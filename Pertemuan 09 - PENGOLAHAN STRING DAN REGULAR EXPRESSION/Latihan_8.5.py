import re
from datetime import datetime

def cari_tanggal(teks):
    tanggal_list = re.findall(r'\d{4}-\d{2}-\d{2}', teks)
    sekarang = datetime.now()

    if not tanggal_list:
        print("Tidak ditemukan tanggal dengan format YYYY-MM-DD")
        return
    
    for tgl in tanggal_list:
        tgl_obj = datetime.strptime(tgl, "%Y-%m-%d")
        selisih = (sekarang - tgl_obj).days
        format_baru = tgl_obj.strftime("%d-%m-%Y")
        
        print(format_baru, "selisih", selisih, "hari")

teks = input("Masukkan kalimat: ")
cari_tanggal(teks)

