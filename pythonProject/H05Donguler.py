## 10. Döngüler
# Bir işlemi birden çok defa yaptırmak istediğimizde döngü yapılarını tercih ederiz.

# Örneğin, 1'den 100'e kadar saydırmak istediğimizde küçük bir kod bloğu ile bunu hızlı bir şekilde gerçekleştirebiliriz.

# Bir başka deyişle 100 defa "merhaba" yazmak istediğimizde döngü kullanmazsak cidden 100 defa merhaba yazmamiz gerekecekti


### 10.1. For Döngüleri
# For döngüsüne geçmeden önce Python'da <b>in</b> deyimini öğrenmemiz gerekir.

#### 10.1.1. In Operatörü
# Python'da in operatörü, bir elemanın başka bir stringde, listede veya demette bulunup bulunmadığını kontrol eder.


liste=[1,2,3,4]
aranan=5
sonuc=aranan in liste
print(sonuc)

print(3 in [1,2,3,4,5])

print("s" in "merhaba")

#### 10.1.2. For Döngüsü
#    for degisken in veriYapisi:
 #       islemler

liste = [11, 12, 13, 14, 15, 16, 17]

for eleman in liste:
    print(eleman)


for i in range(0,7):
    print(liste[i])


toplam=0
for i in liste:
    toplam+=i
print(toplam)


# listedeki tek ve cift elemanlari bulan listeye atan toplamlarini bulan program

liste=[11,12,13,14,15,16,17]

tek=list()
cift=[]
teklerToplam=0
ciftlerToplam=0

for eleman in liste:
    if eleman %2==0:
        cift.append(eleman)
        ciftlerToplam+=eleman
    else:
        tek.append(eleman)
        teklerToplam+=eleman
print("Tekler Toplami: {} ve Ciftler Toplami: {} ".format(teklerToplam,ciftlerToplam))
print("tekler:",tek)
print("ciftler:",cift)


metin="merhaba"
for eleman in metin:
    print(eleman*3)



#türkçe karakter arama
trHarfler="üşğçöıİÜŞĞÇÖ"

""" sifre=input("sifre giriniz:")

for karakter in sifre:
    if karakter in trHarfler:
        print("turkce karakter kullanilmis")
"""

#iki boyutlu dizide gezinme
liste=[[1,2],[3,4],[5,6]]

for eleman in liste:
    print(eleman)

print("bosluk")

for eleman in liste:
    for icEleman in eleman:
        print(icEleman)


liste=[[1,2],[3,4],[5,6]]
for [i,j] in liste:
    print("i:{} j:{}".format(i,j))


liste=[[1,2,3],[4,5,6],[7,8,9]]
for [i,j,k] in liste:
    print("i:{}, j:{}, k:{}".format(i,j,k))

sozluk={1:"bir",2:"iki",3:"uc",4:"dort"}
print(sozluk.values())
print(sozluk.keys())
print(sozluk.items())

#keys'de gezinir
for eleman in sozluk:
    print(eleman)

# ustteki blogun aynısı
for eleman in sozluk.keys():
    print(eleman)

for eleman in sozluk.values():
    print(eleman)

for eleman in sozluk.items():
    print(eleman)

for [i,j] in sozluk.items():
    print("i:{} j:{}".format(i,j))

### 10.2. While Döngüleri

#Koşul sağlandığı sürece (True olduğu sürece) çalışan döngülerdir.

"""while (kosul):
    islemler

Döngü içerisinde koşula müdahale edilmelidir, aksi takdirde sonsuz döngüye girilir."""

kosul=True
a=1
while(kosul):
    a+=1
    print(a)
    if a==10: #bu if olmasa idi sonsuz döngü olur idi
        kosul=False

liste=[1,2,3,4,5,6,7,8,9]
indis=0
while(indis<len(liste)):
    print("listenin {} indisli elemanı: {}".format(indis,liste[indis]))
    indis+=1





while (True):
    print("""----------------
Hesap Makinesi
İşlemler:
1. Toplama
2. Çıkartma
3. Çarpma
4. Bölme
q. Çıkış
----------------
""")
    soru = input("işlem seçiniz")
    if (soru == "q"):
        print("oldu o zaman")
        break
    elif soru == "1":
        sayi1 = int(input("1.sayı"))
        sayi2 = int(input("2.sayı"))
        print(sayi1, "+", sayi2, "=", sayi1 + sayi2)
    elif soru == "2":
        sayi1 = int(input("1.sayı"))
        sayi2 = int(input("2.sayı"))
        print(sayi1, "-", sayi2, "=", sayi1 - sayi2)
    elif soru == "3":
        sayi1 = int(input("1.sayı"))
        sayi2 = int(input("2.sayı"))
        print(sayi1, "*", sayi2, "=", sayi1 * sayi2)
    elif soru == "4":
        sayi1 = int(input("1.sayı"))
        sayi2 = int(input("2.sayı"))
        print(sayi1, "/", sayi2, "=", sayi1 / sayi2)
    else:
        print("o yok bizde")


### 10.3. Döngülerle ilgili araçlar

# döngüleri kullanırken işimizi kolaylaştıracak bazı deyimler vardır

# range() fonksiyonu

# break deyimi

# continue deyimi

# pass deyimi

# else deyimi

#### 10.3.1. range() fonksiyonu
# Başlangıç, bitiş ve artırma değerlerine göre bir liste oluşturur.

a=range(0,10)
print(a)

a=range(0,10) #burada 10 aralığa dahil değildir.
print(*a) # birden fazla parametreli fonksiyon çağırılırken değişken dizisinin önüne * işareti konulur


a=range(10)
print(*a)

a=range(5,10)
print(*a)

a=range(5,20,2)
print(*a)

a=range(20,5,-2)
print(*a)


liste1=[1,2,3,4,5,6,7,8,9]
liste2=list(range(1,10))
print(type(liste1))
print(type(liste2))
print(liste1)
print(liste2)


liste1=[1,2,3,4,5,6,7,8,9]
for i in range(len(liste1)):
    print(liste[i])


for i in range(10):
    print("*"*i)


#### 10.3.2. break deyimi
# Döngü içerisinde herhangi bir anda break deyimi çalışırsa döngü sonlandırılır.

# break deyimi sadece içinde bulunduğu döngüyü sonlandırır.
# iç içe döngülerde en içteki break sadece kendinden bir üstteki döngüyü sonlandıracaktır.

i=0
while(i<10):
    print(i)
    i+=1

i=0
while(i<10):
    if(i==5):
        break
    print(i)
    i+=1
print("selam")


for i in range(3):
    for j in range(3):
        print("i:",i," j:",j)

while True:
    isim=input("adınızı giriniz, çıkmak için q:")
    if(isim=="q"):
        break
    else:
        print("hoşgeldin ",isim)


#### 10.3.3. continue deyimi

# Döngü içerisinde herhangi bir anda continue deyimi çalışırsa
# deyimden sonraki kodlar çalıştırılmaz ve döngünün başına gidilir.

liste=list(range(10))
for i in liste:
    if(i==3):
        continue
    print(i)

#### 10.3.4. pass deyimi
# Python'da görmezden gel, hiçbirşey yapma anlamına gelir.

while True:
    sayi=int(input("bir sayı giriniz"))
    if sayi==0:
        break
    elif sayi<0:
        pass
    else:
        print(sayi)

karakterDizisi="Bu yAzıdA küçük A yok."
calistiMi=False
for harf in karakterDizisi:
    if(harf=='a'):
        print("a harfi bulundu")
        calistiMi=True
        break
if calistiMi==False:
    print("a harfi bulunmadı")



karakterDizisi = "Bu yAzıdA küçük A yok."
for harf in karakterDizisi:
    if (harf == 'a'):
        print("a harfi bulundu")
        break
else:
    print("a harfi bulunmadı")




#### 10.3.6. List Comprehension


liste1=["a","b","c","d","e"]
liste2=[]
for i in liste1:
    liste2.append(i)
print(liste2)

# listedeki her bir i degeri icin i yi yazdir.
liste3=["a","b","c","d","e"]
liste4=[i for i in liste3]
print(liste4)

liste5=[3,4,5,6]
liste6=[i*2 for i in liste5]
print(liste6)


liste7=[[1,2],[3,4],[5,6],[7,8]]
liste8=[i*j for[i,j] in liste7]
print(liste8)


liste9=[[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste10=[]
for i in liste9:
    for j in i:
        print("j:",j, " i:", i)
        liste10.append(j)
print(liste10)


liste11=[[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste12=[j for i in liste11 for j in i]
print(liste12)