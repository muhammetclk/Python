#benimModulumDeneme1.py isimli dosyanın içeriği

sozluk={1:"bir",2:"iki",3:"üç",4:"dört",5:"beş",6:"altı",7:"yedi",8:"sekiz",9:"dokuz",10:"on",20:"yirmi",30:"otuz",40:"kırk",50:"elli",60:"atmış",70:"yetmiş",80:"seksen",90:"doksan"}

def oku(sayi):
    """
    bu fonksiyon girilen iki basamaklı sayının okunuşunu dönmektedir.
    :param sayi: 2 basamaklı sayı
    :return: string
    """
    birinci=sayi%10
    ikinci=(sayi//10)*10
    okunus=sozluk[ikinci] + " " + sozluk[birinci]
    return okunus

def selam(ad=""):
    return "merhaba {} hoşgeldin!".format(ad)


