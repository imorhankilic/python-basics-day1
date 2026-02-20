ogrenciler = {
    "Ahmet":60,
    "Ayse":75,
    "Mehmet":42
}

print("Merhaba Hoşgeldiniz")
print("Öğrenci Listesi")

for isim in ogrenciler:
    print(f"- {isim}")

selectedStudent = input("Öğrenci adı giriniz: \n")

if selectedStudent in ogrenciler:
    print(f"Öğrenci adı: {selectedStudent} - Öğrenci not: {ogrenciler[selectedStudent]}")
else:
    print("Öğrenci bulunamadı")
