## 9. Koşullar
### 9.1. Mantıksal Veri Tipi (bool)
#bool veri tipi True ya da False değeri alan veri tipidir.


a = True
print(type(a))
print(a)
print("--------------")
b=5
c=bool(b)

print(c)
print("--------------")
b=-5
c=bool(b)

print(c)
print("--------------")
b=0
c=bool(b)
print(c)
print("--------------")
b=0.0
c=bool(b)
print(c)
print("--------------")

""" bir değişkenin değerini, değişkeni oluştururken belirlemek istemiyorsak ya da üzerinde
yazan değeri silmek istiyorsak  degisken=None """

a=5
print(type(a))
print(a)
a=None
print(type(a))
print(a)

print(1==1)
print(1==2)


a=[1,2,3]
b=[1,2,3]

print(a==b)

kullanici="ali"
sifre="123456"

print(kullanici=="ali" and sifre=="123456")

a=5
print(a==4)
print(not a==4)

print(not(5>4 and (2==3 or 5!=4)))

print("ali">"ahmet") #burada string saıralamasına göre "l", "h"'den sonra geldiği için ali ahmetten büyüktür


### 9.2. Koşullar (if)
#Koşullara geçmeden önce Python'da blok mantığından söz etmemiz gerek.

#Python'da bir kod bloğu "tab" kullanılarak girintili yazılmış ise o blok bir dışardaki bloğa ait demektir.

  #  if(kosul):
   #     islem1 #if'in icindedir
    # islem2 #if'in dışındadır


kosul=True

if(kosul):
    print("dogru")
    print("dogru devam")
print("disardayiz")

kosul=False

if(kosul):
    print("dogru")
    print("dogru devam")
print("disardayiz")


film=input("film adini giriniz:")
imdb=float(input("imdb puanini giriniz"))

if(imdb>7):
    print("Film 7 imdb uzeridir",film," isimli filmi izle")
else:
    print("film 7 imdb altindadir.",film," isimli filmi izleme")

Not=float(input("notunuzu giriniz")) #not isimli bir değişken tanımlayamayız. not operatörüne karşılık geliyor
if Not>=90:
    print("AA")
elif Not>=85:
    print("BA")
elif Not>=80:
    print("BB")
#... devam eder
else:
    print("hatali")

# if expression
a = 5

if a > 10:
    print("buyuk")
else:
    print("kucuk")

# bu kodun aynısını aşağıdaki şekilde de yazabiliriz

print("buyuk" if a > 10 else "kucuk")


print("""
----------------
Hesap Makinesi
İşlemler:
1. Toplama
2. Çıkartma
3. Çarpma
4. Bölme
----------------
""")

a=int(input("birinci sayı:"))
b=int(input("ikinci sayı:"))
islem=int(input("işlem:"))

if(islem==1):
    print("{} ile {}'nin toplamı {}'dur.".format(a,b,a+b))
elif islem==2:
    print("{} ile {}'nin farkı {}'dur.".format(a,b,a-b))
elif islem==3:
    print("{} ile {}'nin çarpımı {}'dur.".format(a,b,a*b))
elif islem==4:
    print("{} ile {}'nin bölmü {}'dur.".format(a,b,a/b))
else:
    print("başka yok ki!")



