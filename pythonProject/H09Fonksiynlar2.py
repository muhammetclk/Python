### 11.7. Local ve Global değişkenler

a=5
print("1. a=",a)

def islem():
    #print("2. a=",a) #error, a degiskeni tanimlanmamis
    a=2
    a+=1
    return a

sayi1=islem()
sayi2=a
print("sayi1=",sayi1,", sayi2=",sayi2)

a=5 #global degisken
print("1. a=",a)

def islem():
    global a # burada globaldeki a degiskenini kullanmak istedigimizi soylemis oluyoruz
    print("2. a=",a)
    a=2
    a+=1
    return a

sayi1=islem()
sayi2=a
print("sayi1=",sayi1,", sayi2=",sayi2)

# diğer dillerden farklı olarak if ve while içinde oluşturulan değişkenler de global değişkenlermiş gibi değerlendirilir.
sayi=5
while sayi<10:
    a=20
    sayi+=1

print(a)

### 11.8. Lambda Fonksiyonları

#list comprehension'da olduğu gibi lambda fonksiyonları da fonksiyon oluşturmanın hızlı yoludur. Tekbir satırda fonksiyon oluşturmamızı sağlar. Kullanmak için;

 #   etiket=lambda parametre1,parametre2,... : islem

def topla(a,b):
    return a+b

topla2=lambda a,b:a+b

print(topla(2,3))
print(topla2(2,3))
def ciftMi(sayi):
    if sayi % 2==0:
        return True
    else:
        return False

ciftMi2=lambda sayi : sayi%2==0

print(ciftMi(2))
print(ciftMi(3))
print(ciftMi2(2))
print(ciftMi2(3))

### 11.9. Fonksiyon Örnekleri
#### 11.9.1. asal sayı bul (fonksiyon), ikisayi arasındaki asallar (önceki fonksiyonu çağırarak)
#### 11.9.2. arkadaş sayı bul (fonksiyon), ikisayi arasındaki arkadaş sayılar (önceki fonksiyonu çağırarak)
#### 11.9.3. mükemmel sayı bul (fonksiyon), ikisayi arasındaki mükemmel sayılar (önceki fonksiyonu çağırarak)
#### 11.9.4. gönderilen bir listenin sıralanması (fonksiyon)
#### 11.9.5. gönderilen bir sayının, gönderilen bir sırali listede aranması (fonksiyon)