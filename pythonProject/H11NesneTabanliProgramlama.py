## 13. Nesne Tabanlı Programlama
"""OOP yani Object Oriented Programming ifadesi Türkçe'de Nesne Tabanlı Programlama, Nesneye Yönelik Programlama gibi vb. karşılıklarda bulunur. OOP, uygulamaları nesneler kullanarak oluşturmak demektir. Geliştirdiğimiz uygulamalardaki yordamları direk uygulama koduna yazmayıp, sınıflar içinde yazıyor ve sınıflardan nesneler türetiyor, bunları nesneler üzerinden çağırıyorsanız OOP yapıyorsunuz demektir. OOP gerçekleşmesi için aşağıdaki 4 özelliğin gerçekleştirilmesi zorunludur, gerçekleştirilmemesi durumunda OOP sayılmaz.

    1. Soyutlama (Abstraction)
    2. Sarmalama / Paketleme (Encapsulation)
    3. Miras Alma (Inheritance)
    4. Çok Biçimlilik (Polymorphism)
"""

### 13.1. Class (Sınıf)

"""Kendi veritiplerimi oluşturmak ve bu veri tiplerinden nesneler türetmemiz için
öncelikle nesneleri üreteceğimiz yapıyı tanımlamamız gerekir.
Bunu tasarladığımız yapıya da sınıf veya ingilizce adıyla class diyoruz.
"""

class Araba():
    marka =""
    model =""
    renk=""
    yas=0

    #alttaki metod bir yapici metoddut.__init__ seklinde tanimlaniyor.
    def __init__(self):#burada self anahtar kelimesi sınıfın kendisini işaret etmektedir.(c# daki this)
        print("init cagrildi")


araba1 = Araba()#yapici metod direk calisicak.



araba1.marka="Tofas"
araba1.model="Sahin"

print(araba1.marka)
print(araba1.model)

print(type(araba1)) #main in Araba classi oldugunu gosteriyor.
print(araba1)#Araba classindan tanimli bir nesne oldugunu bildiriyor.

print("--------------------------------")
### 13.2. init Fonksiyonu (yapıcı metod)
"""__init__

fonksiyonu python'da yapıcı(constructor) fonksiyondur ve sınıftan' \
' bir nesne türetildiginde otomatik olarak ilk çağırılan fonksiyondur.
"""

class Araba():
    marka = ""
    model = ""
    renk = ""
    yil = 0

    def __init__(self, marka="boş", model="boş", renk="boş",
                 yil=0):  # burada self anahtar kelimesi sınıfın kendisini işaret etmektedir.
        print("init2 cagirildi")
        self.marka = marka
        self.model = model
        self.renk = renk
        self.yil = yil

araba2 = Araba()
print(araba2.marka)

help(Araba)
print("--------------------------------")

araba3=Araba(marka="Bmw", model="ferrari", yil=4)

print(araba3.marka)
