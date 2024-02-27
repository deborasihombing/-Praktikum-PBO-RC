jumlah_siswa = int (input("Masukan banyak siswa : "))
nilai_siswa = {}

for i in range (jumlah_siswa) :
    nama = input("Masukan nama siswa {}: ".format(i+1))
    nilai = float(input("Masukan nilai siswa {}: ".format(i+1)))

    nilai_siswa[nama] = nilai

print("\nNilai siswa : ")
for nama, nilai_angka in nilai_siswa.items():
    print(f"{nama} : {nilai}")
