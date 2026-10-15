# Function untuk penjumlahan
def tambah(a, b):
    return a + b

# Function untuk pengurangan
def kurang(a, b):
    return a - b

# Function untuk perkalian
def kali(a, b):
    return a * b

# Function untuk pembagian
def bagi(a, b):
    if b == 0:
        return "Tidak bisa dibagi nol"
    return a / b

# Program utama
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("Hasil penjumlahan:", tambah(angka1, angka2))
print("Hasil pengurangan:", kurang(angka1, angka2))
print("Hasil perkalian:", kali(angka1, angka2))
print("Hasil pembagian:", bagi(angka1, angka2))