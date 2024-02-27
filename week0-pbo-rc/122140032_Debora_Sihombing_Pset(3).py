nama = input("Masukkan nama Anda: ")
nim = input("Masukkan NIM Anda: ")
resolusi = input("Masukkan Resolusi Anda di Tahun Ini: ")

with open("Me.txt", "w", encoding="utf-8") as file:
    file.write("Nama : {}\n".format(nama))   
    file.write("NIM : {}\n".format(nim))
    file.write("Resolusi Saya di Tahun Ini : {}\n".format(resolusi))
