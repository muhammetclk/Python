
# 6. Listeler
# Diğer programlama dillerindeki dizilere karşılık gelir.
# Listelerin içine istediğiniz türden değişlen yazabilirsiniz.

liste=[] # bos liste olusturur.diger bir yol liste=list()

print(type(liste))
print(liste)

liste = [5, 6, 7, "Hello World", 4.16]
print(liste)
print(len(liste))

liste=list("merhaba") #her harfi bir eleman olarak aliyor.
print(liste)
print(liste[0])
liste[1] = "a" #elemanin degerini degistirebiliriz.string dizisi ile islem yaparken degistiremiyorduk.
print(liste)

print(liste[-1]) #sondan basa gider
print(liste[len(liste)-1])

print(liste[3:]) # 3. indisten sona gider
print(liste[2:6]) # 6. dahil olmuyor!!!!
print(liste[:3])
print(liste[::2]) # bastan sona 2 ser atlayar gider. 0 2 4 6 insilerini yazdirir.
print(liste[::-1]) # terse dogru sona kadar gider


liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = liste1+liste2
print(liste3)
print(type(liste3))

print(liste1)
liste4 = liste1*3 # listedeki elemanlarin aynisindan 3 kere olusturur.
print(liste4)

print(liste3)
liste3[1:3]=[10,20] #listenin 1 ve 2. indexine 10 20 atar.
print(liste3)

print(liste3)
del(liste3[3]) # del ile listenin 3. indexindeki elemani sildik.
print(liste3)


liste4 = list(range(10)) # 10 indislik biz liste olusturur. 0 dan belirtilen yere kadar
print(liste4)

# 6.1 Liste METODLARI

#listeismi.  tusuna basilirsa olusturulan listenin metodlari goruntulenir.

liste=[1,2,3]
print(liste)
liste.append(7) # listenin sonuna belirtilen degeri ekler.
print(liste)

print(liste)
liste.pop() # index numarasini vermezsek bu sekilde listenin sonundan eleman siler.
print(liste)

liste.pop(2) #2 indekteki elamani siler.
print(liste)



print(liste)
a = liste.pop((1)) # listeden silmeden once return ozelligi var,silinen indexteki degeri alabiliyoruz.
print(a)
print(liste)


liste=[7,4,7,3,19,6,4,3,4,33,5]
print(liste)
liste.sort()  # listeyi siralar default kucukten buyuge
print(liste)

print(liste)
liste.sort(reverse=True) # bu sekilde buyukten kucuge siralar.
print(liste)


print(liste)
liste.insert(4,20) # 4. indexe 20 degerini atar digerlerini kaydirir.
print(liste)

# help(liste.count)

print(liste.count(4)) # girdigimiz deger listede kac kere gorunmus bunun sayisini verir.
print(liste.count(35))

help(liste.index) # deger girmezsek default deger var.Eger girdigimiz deger yoksada hata verir

print(liste)
print(liste.index(4)) # 4 un ilk goruldugu indexi verir.


print(liste.index(25)if 25 in liste else "yok ki!") # 25 listede varmi yokmu


# 6.2 Ic ice LISTELER

liste=[[1,2,3],[4,5],[7,8,9,10]]
print(liste)

print(liste[2][2]) # ikinici dizinin 2. indisteki elemani =9

liste2=[2,3.14,[4,5,6],"merhaba"]

print(liste2[3][4]) #3.satirdaki dizinin 4. indexteki degerini verir.

# print(liste2[1][1]) hata verir boyle bir liste yok.1. satirdaki float bir liste elamani



# 7 DEMETLER(TUPLE)

#Listelerde anlatılan işlemlerin çoğu demetler içinde geçerlidir. demetlerde sadece index ve count metodları bulunur.

# Listelerden temel farkı, herhangi bir elemana erişip değiştirilemiyor oluşudur.

# Değiştirilmesini istemediğimiz veriler varsa demetler tercih edilebilir.


demet=(1,2,3,4,5,6)
print(type(demet))
print(demet)

print(demet[4])
# demet[4]=6    # deger degisikligi yapamiyoruz.

print(demet.index(5))


# 8 SOZLUKLER (DICTIONARY)
#Listelerden farklı olarak anahtar(key):değer(value) ilişkisi ile kullanılır.

sozluk={"bir":1,"iki":2,"uc":3,"dort":4,"bes":5}

print(type(sozluk))
print(sozluk)

print(sozluk["iki"])

# print(sozluk["alti"]) boyle bir anahtar olmadigi icin hata verir.

sozluk["alti"]=6 #deger eklemesi yapabliriz.

print(sozluk)


sozluk2={"bir":[1,2,3],"iki":[[1,2],[3,4],[5,6]],"uc":9.15}
print(sozluk2)

print(sozluk2["iki"])
print(type(sozluk2["iki"]))

print(sozluk2["iki"][1][0]) # 3 sayisini verir

sozluk2["iki"][2][1]=20

print(sozluk2["iki"])


sozluk3={1:"bir",2:"iki",3:"üç"}
print(sozluk3[2])

sozluk4={"sayilar":{"bir":1,"iki":2,"uc":3},"meyveler":{"kirmizi":"kiraz","sari":"muz"}}

print(sozluk4["meyveler"]["kirmizi"])

icsozluk=sozluk4["sayilar"]
print(icsozluk)


sozluk={"bir":1,"iki":2,"üç":3,"dört":4,"beş":5}
anahtarlar=sozluk.keys()
print(anahtarlar)
print(type(anahtarlar))

anahtarlar2=list(sozluk.keys())
print(type(anahtarlar2))
print(anahtarlar2.count("altı")) #50.kod blogundaki hatayi bunu kullanarak engelleyebiliriz.

degerler1=sozluk.values()
print(degerler1)
print(type(degerler1))
degerler2=list(degerler1)
print(degerler2)
print(type(degerler2))

print(sozluk.items())

for i,j in sozluk.items():
    print(i,j)

