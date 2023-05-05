## 12. Modüller
# Modüller bazı işlevleri kolaylıkla  yerine getirmemizi sağlayan birtakım fonksiyonları nitelikleri içinde barındıran araçlardır.

#Diğer dillerde kullanılan kütüphane mantığına karşılık gelmektedir. Python'da daha önce tanımlanmış modülleri kullanabileceğimiz gibi kendi modüllerimizi yazarak onları da kullanabiliriz.

#random ve datetime modüllerini daha önce kullanmıştık.

### 12.1. Hazır Modüller
#Python içerisinde daha önce tanımlanmış hazır modüllerdir.

import random #import ederek random modulune erisiyoruz
liste=list(range(10))
liste=random.sample(liste,10) #random modulunden sample fonksiyonunu kullaniyoruz.
print(liste)
# help(random.sample) listedeki elemanlari karistiriyor

import datetime
tarih=datetime.datetime.now() #datetime modulunden datatime classina ait now fonksiyonunu kullandik
print(tarih)


import math #matematik modulunu import eder
print(dir(math)) # modül içerisindeki fonksiyonları listeler
# help(math) # modülün ve içerisindeki fonksiyonların ayrıntılı bilgisini verir

print(math.factorial(5))
import math as matematik #math modulunu cagir ancak ben ona matematik diyecegim
print(matematik.factorial(5))

from math import * #bu sekilde math modulu icerisindeki tum fonksiyonlar calismamiza dahil edilir
print(factorial(5))

from math import factorial,cos,floor # belli fonksiyonlari dahil eder
print(floor(5.7))



# from modulIsmi import * ile ilgili;
# Cağırdığınız modül içerisinde bizim kudumuzdda kullandığımız aynı isimli bir fonksiyon varsa
# son tanımlanan fonksiyon hangisi ise python onu kabul eder
print("-------------")
from math import floor
print(floor(5.7))

def floor(sayi):
    print("bu benim floor'um")
    return (sayi*10)//10

print(floor(5.7))

print("---------")
def floor(sayi):
    print("bu benim floor'um")
    return (sayi*10)//10

print(floor(5.7))

from math import floor
print(floor(5.7))

### 12.2. Üçüncü Şahıs Modülleri
"""Farklı
kullanıcıların
yazdığı
modüllerdir.GitHub
gibi
ortamlardan
bulabileceğiniz
gibi
tanımlı
modülleri
aşağıdaki
şekilde
de
indirebilir
ve
kullanabilirsiniz.

terminal
ekranında;
pip3
install
modul_adi

pip3
install
django
"""

print("=============================")

### 12.3. Kendi Modülümüzü Yazmak
"""Bu aşamada  modülü farklı bir dosyada tutacağımızdan farklı bir ortamda (pycharm) gibi ortamlar kullanılabilir.

bir tane python dosyası oluşturacağız (modulumuz bu dosya olacak).  Modül ile programımızı aynı klasöre koyacağız.

Modül dosyası içerisindeki kodlar  #benimModulumDeneme1.py isimli dosyanın içeriği"""


import benimModulumDeneme1
print(dir(benimModulumDeneme1))
help(benimModulumDeneme1)

print(benimModulumDeneme1.oku(27))
print(benimModulumDeneme1.selam("ali"))