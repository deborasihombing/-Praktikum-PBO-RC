tinggi = int(input("Masukan tinggi segitiga : "))

for i in range(1, tinggi + 1):
    for j in range(1, tinggi - i + 1):
        print(" ", end = "")
    for j in range(1, 2*i):
        print("*", end = "")
  
print()
