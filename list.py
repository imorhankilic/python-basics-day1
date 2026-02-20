liste = ["orhan", 19, "kocaeli"]
liste2 = ["elma","armut","karpuz"]

print(liste2[2])

#Listenin sonuna eleman ekleme
liste2.append(["muz"])
#istenen indexe eleman ekleme
liste2.insert(1,["kavun"])
#listeden belirli değeri silme
liste2.remove(["armut"])
#listeden belirli indexi siler
liste2.pop(0)
#listede kaç eleman olduğunu söyler
len(liste2)


# Parçalama
sayilar=[0,1,2,3,4,5]
print(sayilar[1:4]) #1den 4 e kadar 4 dahil değil
print(sayilar[:3]) #baştan 3 e kadar 3 dahil değil
print(sayilar[2:])#2den sona kadar 

# .sort() listeyi küçükten - büyüğe a'dan - z'ye sıralar
# .reverse() listeyi ters çevirir
# in operator listede var mı diye kontrol eder