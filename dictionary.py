kullanici={
    "isim":"orhan",
    "yas":19,
    "sehir":"kocaeli",
    "ogrenci_mi":True
}

print(kullanici["isim"])
print(kullanici["sehir"])
print(kullanici["yas"])
print(kullanici["ogrenci_mi"])


# YA DA Bu şekilde kullanılaabilir

ogrenciler={
    "Ahmet":90,
    "Mehmet":64,
    "Zeynep":77
}

ogrenciAd = input("Bir ögrenci girin\n")

print(f"Ögrenci adı: {ogrenciAd} - Öğrenci notu: {ogrenciler[ogrenciAd]}")