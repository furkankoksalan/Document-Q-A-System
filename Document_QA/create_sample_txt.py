# Örnek TXT dosyası oluşturucu
from datetime import datetime


def create_sample_txt():
    """Test için örnek TXT dosyası oluşturur"""

    filename = f"ornek_metin_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    content = """PYTHON PROGRAMLAMA DİLİ HAKKINDA

Python, 1991 yılında Guido van Rossum tarafından geliştirilen yüksek seviyeli bir programlama dilidir. 
Basit sözdizimi ve güçlü kütüphaneleri sayesinde hem yeni başlayanlar hem de profesyoneller 
tarafından tercih edilmektedir.

PYTHON'UN ÖZELLİKLERİ

1. Basit ve Okunabilir Sözdizimi
Python, İngilizce'ye benzer bir sözdizimi kullanır. Bu özellik, kodu yazmayı ve okumayı kolaylaştırır.
Örnek:
print("Merhaba Dünya!")

2. Platform Bağımsızlığı
Python kodu Windows, Mac, Linux gibi farklı işletim sistemlerinde çalışabilir.

3. Büyük Kütüphane Ekosistemi
- NumPy: Sayısal hesaplamalar
- Pandas: Veri analizi
- Matplotlib: Veri görselleştirme
- Django: Web geliştirme
- TensorFlow: Makine öğrenmesi

PYTHON'UN KULLANIM ALANLARI

Web Geliştirme:
Django ve Flask gibi framework'ler sayesinde güçlü web uygulamaları geliştirilebilir.

Veri Bilimi:
Pandas, NumPy ve Jupyter Notebook ile veri analizi ve görselleştirme yapılabilir.

Makine Öğrenmesi:
Scikit-learn, TensorFlow ve PyTorch kütüphaneleri ile AI modelleri geliştirilebilir.

Otomasyon:
Tekrarlayan görevleri otomatikleştirmek için scriptler yazılabilir.

TEMEL PYTHON KAVRAMLARI

Değişkenler:
Python'da değişken tanımlamak çok basittir:
isim = "Python"
sayi = 42
pi = 3.14

Veri Türleri:
- str (metin): "Merhaba"
- int (tam sayı): 42
- float (ondalık): 3.14
- bool (mantıksal): True/False
- list (liste): [1, 2, 3]
- dict (sözlük): {"isim": "Python"}

Kontrol Yapıları:
if sayi > 0:
    print("Pozitif sayı")
elif sayi < 0:
    print("Negatif sayı")
else:
    print("Sıfır")

Döngüler:
for i in range(5):
    print(i)

while sayi > 0:
    sayi -= 1

Fonksiyonlar:
def selamla(isim):
    return f"Merhaba {isim}!"

PYTHON ÖĞRENİM KAYNAKLARI

1. Resmi Dokümantasyon: python.org
2. Online Platformlar: Codecademy, Coursera, edX
3. Kitaplar: "Python Crash Course", "Automate the Boring Stuff"
4. Pratik Projeler: GitHub, Kaggle

PYTHON TOPLULUĞU

Python'un güçlü bir topluluğu vardır. PyCon konferansları, yerel meetup'lar ve 
online forumlar sayesinde sürekli öğrenme ve gelişim mümkündür.

İLERİ SEVİYE KONULAR

Object-Oriented Programming (OOP):
class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def bilgi_ver(self):
        return f"{self.marka} {self.model}"

Decorators:
@property
def isim(self):
    return self._isim

Generators:
def sayac():
    for i in range(10):
        yield i

SONUÇ

Python, öğrenmesi kolay ama aynı zamanda güçlü bir programlama dilidir. 
Web geliştirmeden veri bilimine, otomasyondan makine öğrenmesine kadar 
geniş bir yelpazede kullanım alanı bulur.

Bu döküman, Python programlama dili hakkında temel bilgileri içermektedir 
ve soru-cevap sisteminizi test etmek için hazırlanmıştır.

Oluşturulma Tarihi: """ + datetime.now().strftime('%d.%m.%Y %H:%M') + """
Test Amaçlı Doküman
"""

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    return filename


if __name__ == "__main__":
    filename = create_sample_txt()
    print(f"✅ Örnek TXT dosyası oluşturuldu: {filename}")
    print("Bu dosyayı Streamlit uygulamanızda test edebilirsiniz!")