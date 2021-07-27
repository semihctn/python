class ogrenci():
    okul="ITU"
    rektor="İsmail Koyuncu"
    
    def __init__(self):
        self.isim=""
        self.soyisim=""
        self.hazirlik=""
        self.bolum=""
        self.sinif=""
        self.numara=""
        self.fakulte=""
    def yeni_sinif(self,x): #sınıf değişikliği fonksiyonu
        self.sinif=x
        
    
semih=ogrenci()
ali=ogrenci()
ayse=ogrenci()
fatma=ogrenci()

semih.isim="Semih"
semih.soyisim="Çetin"
semih.hazirlik="Irregular"
semih.bolum="Matematik Muhendisligi"
semih.sinif="3"
semih.numara="090200741"
semih.fakulte="FEB"
# semih.yeni_sinif("1") sinif değişikliği için fonksiyon

ali.isim="Ali"
ali.soyisim="Duran"
ali.hazirlik="Tam"
ali.bolum="Insaat Muhendisligi"
ali.sinif="2"
ali.numara="010100185"
ali.fakulte="Insaat"

ayse.isim="Ayse"
ayse.soyisim="Giden"
ayse.hazirlik="Irregular"
ayse.bolum="Bilgisayar Muhendisligi"
ayse.sinif="4"
ayse.numara="060401014"
ayse.fakulte="Bilgisayar"

fatma.isim="Fatma"
fatma.soyisim="Taklacı"
fatma.hazirlik="3 donem"
fatma.bolum="Fizik Muhendisligi"
fatma.sinif="1"
fatma.numara="090300532"
fatma.fakulte="FEB"

print(semih.isim)
print(semih.soyisim)
print(semih.okul)
print(semih.rektor)
print(semih.hazirlik)
print(semih.bolum)
print(semih.sinif)
print(semih.numara)
print(semih.fakulte + "\n")

print(ali.isim)
print(ali.soyisim)
print(ali.okul)
print(ali.rektor)
print(ali.hazirlik)
print(ali.bolum)
print(ali.sinif)
print(ali.numara)
print(ali.fakulte + "\n")

print(ayse.isim)
print(ayse.soyisim)
print(ayse.okul)
print(ayse.rektor)
print(ayse.hazirlik)
print(ayse.bolum)
print(ayse.sinif)
print(ayse.numara)
print(ayse.fakulte + "\n")

print(fatma.isim)
print(fatma.soyisim)
print(fatma.okul)
print(fatma.rektor)
print(fatma.hazirlik)
print(fatma.bolum)
print(fatma.sinif)
print(fatma.numara)
print(fatma.fakulte + "\n")


