'''
isimler = ["Ada", "Yigit", "Zekeriya", "Mahmut",]
yaslar = [1998, 2000, 1998, 1987]

nu = isimler.index("Yigit")

isimler.sort()

print(isimler)
'''
'''
ogrenciler= {
    100 : {
        "ad" : "Cinar",
        "soyad" : "Mahmudo",
        "yas" : 22 ,
        "notlar": [70,80,20]},
    101 : {
        "ad" : "ali",
        "soyad" : "koc",
        "yas" : 33 }
} 

sonuc= ogrenciler[100]["notlar"]


print(sonuc)
'''

'''
urunler= {}
id = input('id: ')
ad = input('ad: ')
(fiyat) = input('fiyat: ')

urunler[id]= {
    "ad": ad,
    "fiyat": int(fiyat)
}
print(urunler)
'''
'''
urunler = {
    '100' : {
        'ad': 'Kola',
        'fiyat' : 10
    },
    '101' : {
        'ad': 'Gazoz',
        'fiyat' : 20
    },
   '102' : {
 
        'ad': 'Su',
        'fiyat' : 30
    }
}

id= input('Armak istediginiz urun id?')
urun= urunler[id]

print(f"id: {id} urunun adi: {urun['ad']} urunun fiyati: {urun['fiyat']} " )

'''
'''
arabalar= {
    "marka": "obel",
    "model": "aaa",
    "yil" : "1999"
}
sonuc= arabalar["marka"]
sonuc= arabalar.get("marka")

'''
#for x in arabalar.items():
 #   print(x)
'''

sonuc = "marka" in arabalar 
print(sonuc)


player1= {
    "id" = 1
    "isim" = "Zekeriya"
    "yil" = 1983
    "uyruk" = "turkiye"
    "is" = "yazilimci"
    "tarih" = "getir, pisano, metglobal"

}
player2= {
    "id" = 2
    "isim" = "Ceren"
    "yil" = 1999
    "uyruk" = "turkiye"
    "is" = "muhendis"
    "tarih" = "biges, turkuvaz, belbim"

}
'''
'''
kullanici= input("Kullanici Adi Giriniz: ") neden hata veriyor
sifre= int(input("Sifrenizi Giriniz: "))

if (kullanici == "aysegul") and (sifre == 1234):
    print("Giris Basarilidir")
else : 
    print("Giris Basarisizdir") 
    
'''


'''
urunler = [
    {'name' : 'iphone8', 'price' : '4000' },
    {'name' : 'iphone8 plus', 'price' : '5000' },
    {'name' : 'iphoneX', 'price' : '7000' },
    {'name' : 'iphoneXR', 'price' : '8000'},
    {'name' : 'iphone11', 'price' : '9000'},
    {'name' : 'samsung', 'price' : '600'},
]

kelime= input("Aramak istediginiz model nedir")
for urun in urunler: 
    if urun['name'].find(kelime) > -1:
        print("Aradiginiz model bulundu")
'''

'''
adet = int(input("Adet Sayisinizi Giriniz: "))
urunler = []
i = 0 
while (i < adet):
    ad= input("urunun adini giriniz")
    fiyat= input("urunun fiyat giriniz")
    urunler.append({
        'ad': 'urunun adi',
        'fiyat': 'urunun fiyati'
    })
    i +=1
'''


'''
for i in range(1, 11):
    print("----------------")
    for k in range(1, 11):
        print("{} x {} = {} ".format (i, k , i*k ))

  '''
'''
  sayi=input('Sayi giriniz')

  asalmi = True 

  if sayi ==1 :
      asalmi = False 
'''





# import the necessary packages
import cv2
# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("deneme2.png")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))
# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
cv2.imshow("Image", image)
cv2.waitKey(0)