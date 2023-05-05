# 3.2 Veri Tipi Donusumleri

a = 5
print(type(a))
a = 5.7
print(type(a))

a = 4
print(type(a))
a = float(a)
print(type(a))
print(a)

# float sayiyi int yapinca  noktadan sonrasini almaz.
a = 3.44
print(a)
print(type(a))
a = int(a)
print(type(a))
print(a)

# noktadan sonrasini almaz
a = 3.94
print(a)
print(type(a))
a = int(a)
print(type(a))
print(a)

# eger noktadan sonrasini dikkate alsin istersek round() fonksiyonu kullanilir.

a = 3.5  # 3.5 ve 5 den sonrasini yukari yuvarlar 3.4 asagi yuvarlar
print(a)
print(type(a))
a = round(a)
print(a)
print(type(a))


a = 2.1
b = 3.1
c = a*b
print(c)
print(round(c)) # yukari yuvarlar
print(round(c, 3)) # virgulden sonra iki sayi kalacak sekilde birakir.Sondaki hane sifirsa dahil etmez.

# stringe donusum
a = 8
print(a)
print(type(a))
a = str(a)
print(a)
print(type(a))

# string degerler ile int degerlerin toplami arasindaki fark
a = 5
b = 6
c = a+b
print(c)
d = str(a)+str(b) # 56 seklinde yazar.
print(d)


# complex sayiya donusum ve toplama
a = 5
b = 6
b=complex(b)
print(b)
c = a+b
print(c)
d = str(a)+str(b)
print(d)

#len fonksiyonu karakter sayisini(uzunlugunu) verir.

a = "34"
b = "5678asff"
print(len(a))
print(len(b))

# 3.3 Aritmetik Operatorler
"""
Toplama (+)
çıkartma (-)
çarpma (*)
bölme (/)
tam bölme (//)
mod alma (%)
üs alma (**) (kök almak isterseniz ikinci değere 0.5 yazılabilir)
"""
a = 10
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print(16**(1/2))

# 3.3.1. Matematiksel işlemlerde işlem önceliği ve parantezin önemi vardir.

# 3.4 String Veri Tipleri

# 'selam'

# "selam"

# """selam""" #3 tirnak ile degisken tanimlayabiliriz.(Yazilani ayni sekilde alir alt satirlarada gecebiliriz.)
result=""" merhaba 
  benim adim
  
                            Muhammet
  
  """
print(result)

# 3.4.1 String Dizileri
a = "Muhammet"
print(a)
print(a[0])
print(a[1])
print(a[3])
print(a[6])

a = "ahmet" #len() fonksiyonu stringin eleman sayısını verir
print(len(a)) #dizinin eleman sayısını verir
print(a[len(a)-1]) #dizinin son elemanını
print(a[-1])  #dizinin son elemanını
print(a[-2])  #dizinin sondan bir onceki elemanını

# string parcalama
a="Hello World"
print(a[2:7]) # 2 den 7 ye kadar olan karakterleri basar(llo w) 7 dahil olmuyor.

b=a[:5]
print(b)
b=a[5:]
print(b)


b = a[2:9:2] #2 ser atlayarak gider
print(b)

b = a[::2] # bastan sona ikiser atlayarak git
print(b)

b =a[::-1] # bastan sona tersten git
print(b)

# a[0]="M" #hata, stringleri dizi gibi okuyabilir ancak elemanlarını değiştiremeyiz

#string ifadeleri bu sekilde carpabiliriz.
a = "merhaba "
b = "Dünya!"
c = a+b
print(c)
c = a*3+b
print(c)
print("w"*3 +".google.com")


# 3.4.2. Kaçış Dizileri
# https://python-istihza.yazbel.com/kacis_dizileri.html

print("Ali \"boon canlı ders var mı?\" dedi.") # cift tirnak icinde cift tirnak kullandik.
print("c:\dersler\python")
print("c:\notlar\python") #hata \n zannetti
print("c:\\notlar\\python")

# 4.Print Fonksiyonu
print("merhaba")
print(7)
print(3.14)

# print fonksiyonunda birden fazla değeri arka arkaya yazdırmak istersek print(deger1,deger2,deger3,...)

print(7,3.14,"merhaba")

print(7,"\n",3.14,"\nmerhaba")

# 4.1. sep parametresi
print("merhaba","Dünya!")

print("merhaba","Dünya!",sep="-")

a = 31
b = 3
c = 2023
print(a,b,c,sep=".")

print("merhaba","Dünya!",sep="-")
print("merhaba","Dünya!",sep="/")
print("merhaba","Dünya!",sep="\n")

# 4.2. string.format

a = "merhaba {}, nasilsin".format("Muhammet")
print(a)

isim = "ali"
print("merhaba {},nasilsin".format(isim))

a=3
b=4
print("{} sayısı ile {} sayısının toplamları {}'dır.".format(a,b,a+b))

a=3
b=4
print("{1} sayısı ile {2} sayısının toplamları {0}'dır.".format(a,b,a+b))

# .f ile virgulden sonra gelicek basamak sayisini belirtiyoruz
yaz="{:.2f} ve {:.3f} sayıları ondalık sayılardır".format(3.1234567,4.987654321)
print(yaz)


print("{:s}".format("65")) #string
print("{:c}".format(65)) #char
print("{:d}".format(65)) #decimal
print("{:o}".format(65)) #octal 8lik sistem
print("{:x}".format(65)) #hex 16'lık sistem
print("{:b}".format(65)) #binary 2lik sistem

# noktadan oncesini 3 haneli olarak ayirir.
print("{:,}".format(12345567.8904))


# 5. Input

a = input("sayi girin:")
print(a)

a=input("adinizi giriniz:")
print("merhaba {}, nasilsin?".format(a))
print("merhaba"+a+"nasilsin")
print("merhaba",a,"nasilsin")

#kullanicinin girdigi str formatindadir.
a=input("sayı giriniz:")
print(type(a))
print(a*3)

# convert ediyoruz
a=int(input("1. sayıyı giriniz:"))
b=int(input("2. sayıyı giriniz:"))
print("girilen sayıların toplamı={}".format(a+b))

# hata yakalamasi ile sayi yerine karakter girersek yakaliypruz.
a=input("sayı giriniz")
try:
    a=int(a)
    print(a*3)
except:
    print("sayı istedik!",a," sence sayıya benziyor mu?")