# 1.Aciklama satiri asagidaki sekillerde verilebilir.


# aciklama satiri
print("Hello World")
"""
 coklu aciklama satiri
 coklu aciklama satiri
 
"""
print("How are you?")
print("Hello")

# 2.Degiskenler
# Pythonda degisken tanimlama

a = 5
b = 4
print(a)
print(a+b)

print(type(a))
a = 4.5
print(type(a))
a = "merhaba"
print(type(a))

# degiskenler sayiyla baslamaz ve anahtar kelimelerde kullanilmaz.


# degiskenlere ayni anda deger verebiliriz
a = b = 5
print(a, b)
a, b = 6, 7
print(a, b)

# temp kullanmadan degerlerin yeri degistirilebilir.
a, b = b, a
print(a)
print(b)


# 3. Veri Tipleri
# 3.1 Sayi Veri Tipleri(Number)
# Tam,Ondalik,Karmasik
# 3.1.1 Tam Sayilar(Integer)

a = -15
print(type(a))
a = 0
print(type(a))
a = 1000000
print(type(a))

# 3.1.2 Ondalik Sayilar(Float)

a = 3.15
print(type(a))
a = -4.168
print(type(a))

# 3.1.3 Karmasik Sayilar(Complex)

a = 10+2j
print(type(a))


