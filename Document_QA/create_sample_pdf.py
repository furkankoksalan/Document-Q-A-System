# Örnek PDF Oluşturucu - Test için kullanabilirsiniz
# pip install reportlab

from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from datetime import datetime


def create_sample_pdf():
    """Test için örnek PDF dosyası oluşturur"""

    # PDF dosyası oluştur
    filename = f"ornek_dokuman_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)

    # Stil ayarları
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=30,
        alignment=1  # Center
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=12,
        textColor='#2E86AB'
    )

    # İçerik listesi
    story = []

    # Başlık
    story.append(Paragraph("📚 Yapay Zeka ve Makine Öğrenmesi Kılavuzu", title_style))
    story.append(Spacer(1, 20))

    # Giriş
    story.append(Paragraph("1. Giriş", heading_style))
    story.append(Paragraph("""
    Yapay zeka (AI), makinelerin insan benzeri düşünme ve öğrenme yeteneklerini taklit etmesini 
    sağlayan teknoloji dalıdır. Bu doküman, yapay zeka temellerinden başlayarak makine öğrenmesi 
    algoritmalarına kadar geniş bir yelpazede bilgi sunmaktadır.

    Yapay zeka günümüzde çok sayıda alanda kullanılmaktadır: sağlık, finans, otomotiv, eğitim 
    ve daha birçok sektörde devrim niteliğinde değişiklikler yaratmaktadır.
    """, styles['Normal']))
    story.append(Spacer(1, 20))

    # Makine Öğrenmesi
    story.append(Paragraph("2. Makine Öğrenmesi Nedir?", heading_style))
    story.append(Paragraph("""
    Makine öğrenmesi, bilgisayarların açık programlama olmadan öğrenmesini sağlayan bir yapay zeka 
    dalıdır. Algoritamalar, verilerden örüntüleri tanır ve tahminlerde bulunur.

    Makine öğrenmesi üç ana kategoriye ayrılır:
    • Gözetimli öğrenme (Supervised Learning)
    • Gözetimsiz öğrenme (Unsupervised Learning)  
    • Pekiştirmeli öğrenme (Reinforcement Learning)
    """, styles['Normal']))
    story.append(Spacer(1, 20))

    # Algoritma Türleri
    story.append(Paragraph("3. Popüler Algoritma Türleri", heading_style))
    story.append(Paragraph("""
    <b>Doğrusal Regresyon:</b> Sürekli değerleri tahmin etmek için kullanılan basit ama etkili bir algoritma.

    <b>Karar Ağaçları:</b> Veriye dayalı kararlar almak için kullanılan, yorumlanması kolay algoritmalar.

    <b>Rastgele Orman:</b> Birden fazla karar ağacını birleştirerek daha doğru tahminler yapar.

    <b>Sinir Ağları:</b> İnsan beyninin çalışma prensibinden esinlenen, karmaşık örüntüleri öğrenebilen yapılar.

    <b>Destek Vektör Makineleri (SVM):</b> Sınıflandırma ve regresyon problemleri için kullanılan güçlü algoritmalar.
    """, styles['Normal']))
    story.append(Spacer(1, 20))

    # Derin Öğrenme
    story.append(Paragraph("4. Derin Öğrenme", heading_style))
    story.append(Paragraph("""
    Derin öğrenme, çok katmanlı sinir ağlarını kullanan makine öğrenmesi yöntemidir. 
    Görüntü tanıma, doğal dil işleme ve konuşma tanıma gibi alanlarda çığır açan sonuçlar elde etmiştir.

    Derin öğrenmenin temel bileşenleri:
    • Nöronlar ve katmanlar
    • Aktivasyon fonksiyonları
    • Geri yayılım algoritması
    • Düzenlileştirme teknikleri

    Popüler derin öğrenme mimarileri arasında CNN (Konvolüsyonel Sinir Ağları), 
    RNN (Rekürrent Sinir Ağları) ve Transformer modelleri bulunmaktadır.
    """, styles['Normal']))
    story.append(PageBreak())

    # Uygulama Alanları
    story.append(Paragraph("5. Uygulama Alanları", heading_style))
    story.append(Paragraph("""
    <b>Sağlık:</b> Hastalık teşhisi, ilaç keşfi, tıbbi görüntü analizi

    <b>Finans:</b> Fraud detection, algoritmik trading, kredi risk değerlendirmesi

    <b>Otomotiv:</b> Otonom araçlar, trafik optimizasyonu, güvenlik sistemleri

    <b>E-ticaret:</b> Öneri sistemleri, fiyat optimizasyonu, müşteri segmentasyonu

    <b>Eğitim:</b> Kişiselleştirilmiş öğrenme, otomatik değerlendirme, akıllı tutor sistemleri

    <b>Medya:</b> İçerik üretimi, çeviri, ses tanıma ve sentezi
    """, styles['Normal']))
    story.append(Spacer(1, 20))

    # Etik ve Gelecek
    story.append(Paragraph("6. Etik Considerations ve Gelecek", heading_style))
    story.append(Paragraph("""
    Yapay zeka teknolojilerinin hızla gelişmesiyle birlikte etik konular da önem kazanmıştır:

    • Veri gizliliği ve güvenliği
    • Algoritma önyargıları ve adalet
    • İş piyasasına etkileri
    • Şeffaflık ve açıklanabilirlik
    • İnsan-makine işbirliği

    Gelecekte yapay zeka daha da gelişecek ve günlük yaşamımızın her alanında daha fazla 
    yer alacaktır. Önemli olan bu teknolojileri sorumlu bir şekilde geliştirmek ve kullanmaktır.
    """, styles['Normal']))
    story.append(Spacer(1, 20))

    # Sonuç
    story.append(Paragraph("7. Sonuç", heading_style))
    story.append(Paragraph("""
    Yapay zeka ve makine öğrenmesi, 21. yüzyılın en önemli teknolojik gelişmelerinden biridir. 
    Bu teknolojiler sayesinde daha önce imkansız görünen problemleri çözebilir, 
    verimliliği artırabilir ve yeni fırsatlar yaratabiliyoruz.

    Sürekli öğrenmek ve bu teknolojileri etik çerçevede kullanmak, 
    gelecekte başarılı olmak için kritik önem taşımaktadır.
    """, styles['Normal']))
    story.append(Spacer(1, 20))

    # Alt bilgi
    story.append(Paragraph("---", styles['Normal']))
    story.append(Paragraph(f"Bu doküman {datetime.now().strftime('%d.%m.%Y')} tarihinde test amaçlı oluşturulmuştur.",
                           styles['Normal']))

    # PDF'i oluştur
    doc.build(story)
    return filename


if __name__ == "__main__":
    # PDF oluştur
    try:
        filename = create_sample_pdf()
        print(f"✅ Örnek PDF oluşturuldu: {filename}")
        print("Bu dosyayı Streamlit uygulamanızda test edebilirsiniz!")
    except ImportError:
        print("❌ reportlab paketi yüklü değil. Lütfen yükleyin:")
        print("pip install reportlab")
    except Exception as e:
        print(f"❌ Hata: {e}")