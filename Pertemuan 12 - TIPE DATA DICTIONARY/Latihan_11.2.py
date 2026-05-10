warna = ['red', 'green', 'blue']
kode_warna = ['#FF0000', '#008000', '#0000FF']

data = dict(zip(warna, kode_warna))

hasil = {
    'green': data['green'],
    'blue': data['blue'],
    'red': data['red']
}

print(hasil)