isim = input("Adın ne? ")
print(f"Merhaba {isim}")

#bu şekilde string alınır

yas = input("Yaşın kaç? ")
print(f"{yas} yaşındasın")

# BU ŞEKİLDE KULLANIM HATALIDIR 
#Bu şekilde kullanıldığında yazııyı string olarak alır

yas = int(input("Yaşın kaç? "))
print(f"Seneye {yas+1} yasında olacaksın.")

#Doğru kullanım budur.
# input açmadan önce int açılır int parantezi içine input girilir

ad, soyad = input("Adınızı ve soy adınızı boşluk bırakarak yazın:").split()
print(f"Hoşgeldin {ad + " " + soyad}")

#.split() aynı anda iki veri inputu almayı sağlar
