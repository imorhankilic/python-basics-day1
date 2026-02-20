yas=int(input("Yaşınızı girin: "))
if yas>=18:
    print("ehliyet alabilirsin")
else:
    print("ehliyet alamazsın")


# çoklu şartlar

puan = 40

if puan >= 90:
    print("A")
elif puan >= 80:
    print("B")
elif puan >= 70:
    print("C")


#Mantıksal operatörler
kullanici = "orhan"
sifre = "1234"

if kullanici =="orhan" and sifre == "1234":
    print("giris basarili")
else:
    print("Tekrar dene")

# == eşitse demek stringler için


#TEK SATIRDA İF

durum = "Geçti" if puan >= 50 else "Kaldı"

print(durum)