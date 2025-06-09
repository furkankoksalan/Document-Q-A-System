# Document Q&A System

```
#=================================================================
# Streamlit ve LangChain kullanarak geliştirilmiş doküman soru-cevap sistemi
#=================================================================

# Hakkında
#---------
Bu proje, PDF ve TXT dosyalarını yükleyerek içerikleri hakkında
sorular sorabileceğiniz gelişmiş bir doküman analiz sistemidir.
OpenAI'nin GPT modelleri ve LangChain framework'ü kullanılarak
oluşturulmuştur.

Temel amacı, kullanıcıların büyük dokümanları hızlıca analiz edip
içeriklerinden bilgi çıkarabilmelerini ve vektör veritabanları
kullanarak akıllı arama yapabilmelerini sağlamaktır.

# Ana Özellikler
#---------------
• PDF/TXT dosya desteği
• Akıllı doküman arama
• Çoklu sohbet yönetimi
• Kaynak gösterimi
• Seçilebilir vektör veritabanı entegrasyonu
• Otomatik sohbet kaydetme

# Özellikler
#-----------
✓ Multi-format doküman desteği (PDF, TXT)
✓ Çoklu GPT model desteği (GPT-4o Mini, GPT-3.5, GPT-4)
✓ Seçilebilir embedding türleri (OpenAI/HuggingFace)
✓ Seçilebilir vektör veritabanları (FAISS/Chroma)
✓ Konuşma hafızası ve bağlam takibi
✓ Kaynak doküman referansları
✓ Responsive web arayüzü

# Kurulum
#---------
git clone <repository-url>
cd document-qa-system

# Sanal ortam oluştur
python -m venv venv

# Sanal ortamı aktifleştir
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Bağımlılıkları yükle
pip install -r requirements.txt

# Konfigürasyon
#--------------
# .env dosyası oluştur
echo "OPENAI_API_KEY=your-openai-api-key-here" > .env

# Çalıştırma
#-----------
streamlit run app.py

# Kullanım
#---------
1. Tarayıcıda http://localhost:8501 adresini ziyaret et
2. API anahtarını yapılandır (.env dosyasından otomatik yüklenir)
3. PDF/TXT dosyalarını yükle
4. AI model, embedding ve vektör veritabanı seç
5. "Process Documents" butonuna tıkla
6. Dokümanlar hakkında soru sormaya başla

# Proje Yapısı
#--------------
document-qa-system/
├── app.py                 # Ana Streamlit uygulaması
├── requirements.txt       # Python bağımlılıkları
├── .env.example          # Çevre değişkenleri şablonu
├── README.md             # Bu dokümantasyon
└── chat_history_*.pkl    # Otomatik oluşturulan sohbet dosyaları

# Gereksinimler
#--------------
Python >= 3.8
OpenAI API Key
İnternet bağlantısı
PDF/TXT dokümanları

# Bağımlılıklar
#--------------
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

# Model Seçenekleri
#------------------
AI Modeller:
├── gpt-4o-mini     → En ekonomik seçenek (önerilen)
├── gpt-3.5-turbo   → Hızlı ve uygun fiyatlı
└── gpt-4           → En yüksek kalite

Embedding Türleri:
├── OpenAI          → Yüksek kalite (ücretli)
└── HuggingFace     → Ücretsiz alternatif

Vektör Veritabanları:
├── FAISS           → Hızlı ve verimli
└── Chroma          → Modern özellikler

# API Anahtarı
#--------------
# OpenAI API anahtarını al:
# 1. https://platform.openai.com adresine git
# 2. API Keys bölümünden yeni anahtar oluştur
# 3. .env dosyasına OPENAI_API_KEY=your_key_here şeklinde ekle

# Sohbet Yönetimi
#----------------
• Yeni Sohbet      → Mevcut sohbet otomatik kaydedilir
• Otomatik Kayıt   → Tarih-saat ile dosya oluşturur
• Sohbet Yükle     → Dropdown'dan seçerek anında yükle
• Temizle          → Mevcut sohbeti sil

# Doküman İşleme
#---------------
Desteklenen Formatlar:
├── PDF            → Çok sayfalı PDF dokümanları
└── TXT            → Düz metin dosyaları

İşlem Adımları:
1. Dosya yükleme
2. Metin bölme (chunking)
3. Embedding oluşturma
4. Vektör veritabanına kaydetme
5. QA zinciri kurma

# Teknik Detaylar
#----------------
Framework        : Streamlit
LLM Library      : LangChain
Default Chunk    : 1000 karakters
Chunk Overlap    : 200 karakter
Memory Type      : ConversationBufferMemory
Temperature      : 0.7
Retriever K      : 4 doküman

# Sorun Giderme
#--------------
# LangChain import hatası
pip install --upgrade langchain langchain-community langchain-openai

# API key problemi
export OPENAI_API_KEY=your_key_here

# Büyük dosyalar için
# Daha küçük chunk_size kullanın

# Port değiştir
streamlit run app.py --server.port 8502

# Cache temizle
streamlit cache clear

# Performans İpuçları
#--------------------
Maliyet Optimizasyonu:
├── Model: gpt-4o-mini
├── Embedding: OpenAI veya HuggingFace (seçilebilir)
└── Veritabanı: FAISS veya Chroma (seçilebilir)

Kalite Optimizasyonu:
├── Model: gpt-4
├── Embedding: OpenAI veya HuggingFace (seçilebilir)
└── Veritabanı: FAISS veya Chroma (seçilebilir)

Hız Optimizasyonu:
├── Model: gpt-3.5-turbo
├── Embedding: OpenAI veya HuggingFace (seçilebilir)
└── Veritabanı: FAISS veya Chroma (seçilebilir)

# Güvenlik
#----------
# .gitignore dosyası oluştur
echo ".env" >> .gitignore
echo "*.pkl" >> .gitignore
echo "__pycache__/" >> .gitignore

# Katkıda Bulunma
#----------------
git fork
git checkout -b feature/yeni-ozellik
git commit -m "Yeni özellik eklendi"
git push origin feature/yeni-ozellik

```
