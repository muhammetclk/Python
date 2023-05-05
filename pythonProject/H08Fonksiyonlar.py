## 11. Fonksiyonlar

### 11.1. Metotlar

# Metot, program içerisinde belirli görevleri yerine getirmek için özelleştirilmiş kodbloklarına verilenisimdir.Bir
# objenin metotlarına ulaşabilmek için;
# objeIsmi.metotIsmi()

# Örnek: liste isimli bir listenin append metoduna erişmek için;

# liste.append(deger)
# help metodu ile pythondaki metotlar hakkında ayrıntılı bilgiye erişebiliriz.

# help(liste.append)

# metotlar çağırılıp çalıştırılır ve işleri biter.Fonksiyonları anlatırken bu cümle daha çok anlam kazanacak.


### 11.2. Metot tanımlama ve Çağırma

#Metot tanımlamak için;

"""   def metotAdi(parametre1, parametre2, .....(opsiyonel)):
       yapilacak islemler
       ....
        (deger dondurme) Fonksiyonlar icin  """


def merhaba():
       print("Hello")
       print("World")

print(type(merhaba))

merhaba()

for i in range(3):
    merhaba()

def topla(a,b):
    print("a+b:",a+b)

topla(4,5)


### 11.3. Fonksiyonlar ve return deyimi

#Fonksiyonlar, metotlardan farklı olarak geriye bir değer döndürürler ve bu değeri başka bir değişkene atamanıza ya da onunla işlem yapmanıza olanak tanırlar.

#Python programının içerisinde daha önce tanımlanmış hazır fonksiyonlara gömülü fonksiyonlar(built-in functions) denir.

#kedi metotlarınızı oluşturabileceğiniz gibi kendi fonksiyonlarınızı da oluşturup defalarca kullanabilirsiniz.


def topla(a,b):
    return a+b

result=topla(5,6)
print("a+b:",result)

result=topla(1,topla(4,topla(7,8)))
print("a+b:",result)

#faktoriyel hesaplayan fonksiyon
def faktoriyel(sayi):
    sonuc=1
    for i in range(1,sayi+1):
        sonuc*=i

    return sonuc

sonuc=faktoriyel(5)
print("faktoriyel:",sonuc)

#kombinasyon hesabı
#c=n!/(r!*(n-r)!)

n=int(input("n degerini giriniz:"))
r=int(input("r degerini giriniz:"))
c=faktoriyel(n)/(faktoriyel(r)*faktoriyel(n-r))
print("c:",c)


def topla(a, b):
    print("topla fonksiyonu adım 1")
    return a + b
    print("topla fonksiyonu adım 2")


def carp(a, b):
    print("carp fonksiyonu adım 1")
    return a * b
    print("carp fonksiyonu adım 2")


print(carp(topla(2, 3), topla(3, 4)))


### 11.4. Fonksiyonlarda Parametreler

#opsiyonel parametre tanımlama
def topla(a=0,b=0):
    return a+b

print(topla(2,3))
print(topla(4))
print(topla())


#sirasiz parametre girisi, isimli parametre
def bilgiler(ad="yok",soyad="yok",numara="yok"):
    return("ad: {}, soyad: {}, numara: {}".format(ad,soyad,numara))


print(bilgiler())
print(bilgiler("ali","can","123"))
print(bilgiler("ali","can"))
print(bilgiler("ali","123"))
print(bilgiler("ali","","123"))
print(bilgiler(ad="ali",numara="123"))
help(bilgiler)

### 11.5. Fonksiyonlarda Esnek Parametreler

def topla(*a):
    print(type(a))
    return a

print(topla(1,2,3,4,5,6,7))


def topla(*a):
    sonuc=0
    for i in a:
        sonuc+=i
    return sonuc
print(topla())
print(topla(3))
print(topla(2,3,4,5,4,3,2,4,5,6,8,9))


### 11.6. Fonksiyonlarda isimli esnek parametreler

def islem(**a):
    print(type(a))
    return a

print(islem(ad="ali",soyad="can",numara="123"))


def karsilikBul(*args,**kwargs):
    for kelime in args:
        if kelime in kwargs:
            print("{} ={}".format(kelime,kwargs[kelime]))
        else:
            print("{} kelime bulunamamistir.".format(kelime))



sozluk={"masa":"Desk","kalem":"Pencil","Bilgisayar":"Computer"}
karsilikBul("masa","kalem","silgi",**sozluk)
karsilikBul("kitap","programlama","fonksiyon",kitap="book",bilgisayar="computer",programlama="programming")

