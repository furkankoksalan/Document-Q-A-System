# Doküman Soru-Cevap Sistemi

Streamlit ve LangChain kullanılarak geliştirilmiş, PDF ve TXT dosyalarını analiz edebilen kapsamlı doküman soru-cevap sistemi.

## Genel Bakış

Bu proje, kullanıcıların dokümanlarını yükleyerek içerikleri hakkında sorular sorabilmelerini sağlar. En son teknoloji GPT modelleri kullanılarak geliştirilmiştir. Doküman işleme, vektör veritabanları ve konuşmalı yapay zeka teknolojilerini bir araya getirerek akıllı doküman analizi özellikleri sunar.

Sistem otomatik olarak dokümanları işler, aranabilir gömülü vektörler oluşturur ve doğru cevaplar vermek için konuşma bağlamını korur. Her cevap için kaynak referansları gösterir.

## Özellikler

- **Çoklu format desteği**: PDF ve TXT dokümanlarını işleme
- **Gelişmiş AI modelleri**: GPT-4o Mini, GPT-3.5 Turbo ve GPT-4 seçenekleri
- **Esnek gömme seçenekleri**: OpenAI ve HuggingFace embedding'leri arasında seçim
- **Vektör veritabanları**: Verimli arama için FAISS ve Chroma entegrasyonu
- **Konuşma hafızası**: Birden fazla soru arasında bağlamı koruma
- **Sohbet yönetimi**: Konuşma geçmişlerini oluşturma, kaydetme ve yükleme
- **Kaynak gösterimi**: Cevaplar için hangi doküman bölümlerinin kullanıldığını gösterme
- **Gerçek zamanlı streaming**: Cevapları oluşturulurken görme
- **Duyarlı arayüz**: Temiz, modern web arayüzü

## Kurulum

1. Repoyu klonlayın:
```bash
git clone <repository-url>
cd document-qa-system
```

2. Sanal ortam oluşturun:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

4. Çevre değişkenlerini yapılandırın:
```bash
echo "OPENAI_API_KEY=your-openai-api-key-here" > .env
```

## Kullanım

1. Uygulamayı başlatın:
```bash
streamlit run app.py
```

2. Tarayıcınızda `http://localhost:8501` adresini açın

3. Tercihlerinizi yapılandırın:
   - AI modeli seçin (GPT-4o Mini önerilir)
   - Embedding türü seçin (kalite için OpenAI, ücretsiz için HuggingFace)
   - Vektör veritabanı seçin (hız için FAISS, özellikler için Chroma)

4. PDF veya TXT dokümanlarını yükleyin

5. "Dokümanları İşle" butonuna tıklayın ve tamamlanmasını bekleyin

6. Dokümanlarınız hakkında soru sormaya başlayın!

## Yapılandırma Seçenekleri

### AI Modelleri
- **GPT-4o Mini**: Mükemmel performansla en uygun maliyetli seçenek
- **GPT-3.5 Turbo**: Genel kullanım için hızlı ve ekonomik
- **GPT-4**: Karmaşık sorgular için en yüksek kalite

### Embedding'ler
- **OpenAI**: Daha yüksek kalite embedding'ler (API kredisi gerektirir)
- **HuggingFace**: Sentence-transformers kullanan ücretsiz alternatif

### Vektör Veritabanları
- **FAISS**: Facebook'un hızlı benzerlik arama kütüphanesi
- **Chroma**: Gelişmiş özelliklerle modern vektör veritabanı

## Proje Yapısı

```
document-qa-system/
├── app.py                 # Ana Streamlit uygulaması
├── requirements.txt       # Python bağımlılıkları
├── .env.example          # Çevre değişkenleri şablonu
├── README.md             # Proje dokümantasyonu
└── chat_history_*.pkl    # Otomatik oluşturulan konuşma dosyaları
```

## Gereksinimler

- Python >= 3.8
- OpenAI API Anahtarı
- İnternet bağlantısı

## Bağımlılıklar

```
streamlit>=1.28.0
langchain>=0.1.0
langchain-community>=0.0.10
langchain-openai>=0.0.5
openai>=1.0.0
faiss-cpu>=1.7.4
chromadb>=0.4.0
pypdf>=3.17.0
sentence-transformers>=2.2.2
tiktoken>=0.5.0
python-dotenv>=1.0.0
```

## Sohbet Yönetimi

- **Yeni Sohbet**: Yeni sohbet başlatırken mevcut konuşmayı otomatik kaydeder
- **Otomatik Kayıt**: Konuşmalar zaman damgalı dosya adlarıyla kaydedilir
- **Sohbet Yükle**: Önceki konuşmaları anında yüklemek için dropdown'dan seçin
- **Temizle**: Mevcut konuşmayı hafızadan kaldır

## Performans İpuçları

### Maliyet Optimizasyonu
- Model: GPT-4o Mini
- Embedding: HuggingFace (ücretsiz)
- Veritabanı: FAISS

### Kalite Optimizasyonu
- Model: GPT-4
- Embedding: OpenAI
- Veritabanı: Chroma

### Hız Optimizasyonu
- Model: GPT-3.5 Turbo
- Embedding: HuggingFace
- Veritabanı: FAISS

## Sorun Giderme

### Yaygın Sorunlar

**Import Hataları:**
```bash
pip install --upgrade langchain langchain-community langchain-openai
```

**API Anahtarı Sorunları:**
- OpenAI API anahtarının geçerli olduğunu ve kredisi olduğunu kontrol edin
- .env dosyası formatını kontrol edin

**Hafıza Sorunları:**
- Daha küçük dokümanlar kullanın veya chunk boyutlarını azaltın
- Hafızayı boşaltmak için diğer uygulamaları kapatın

**Performans Sorunları:**
- FAISS genellikle büyük dokümanlar için Chroma'dan daha hızlıdır
- HuggingFace embedding'leri yerel olarak işlenir (daha yavaş ama ücretsiz)

## Güvenlik

Hassas verileri korumak için bir `.gitignore` dosyası oluşturun:
```
.env
*.pkl
__pycache__/
.streamlit/
```

