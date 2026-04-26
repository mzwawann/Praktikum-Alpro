filename = input("nama file: ")

try:
    handle = open(filename)

    for line in handle:
        line = line.strip()
        
        if "||" in line:
            soal, jawaban_benar = line.split("||")
            
            print(soal.strip())
            user_jawab = input("Jawab: ")

            if user_jawab.strip().lower() == jawaban_benar.strip().lower():
                print("Jawaban benar!")
            else:
                print("Jawaban salah!")

    handle.close()

except:
    print("File tidak ditemukan!")
    
    