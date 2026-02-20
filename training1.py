# hesap makinesi

print("sırasıyla 1. sayı ve 2. sayıyı girin")

sayi1 =int(input("1. sayıyı girin: "))
sayi2 =int(input("2. sayıyı girin: "))

print("işlem tipi seçin: \n1 = Toplama \n2 = Çıkartma \n3 = Çarpma \n4 = Bölme")

tip = int(input("İşlem tipini girip enter'a basın "))

if tip == 1:
    print(f"sonuç: {sayi1 + sayi2}")
elif tip == 2:
    print(f"sonuç: {sayi1-sayi2}")
elif tip == 3:
    print(f"sonuç: {sayi1*sayi2}")
elif tip == 4:
    print(f"sonuç: {sayi1/sayi2}")


