# Ev Fiyatı Tahmin Sistemi

Bu projede, konut fiyatlarını etkileyen çevresel ve sosyoekonomik faktörler
kullanılarak makine öğrenmesi tabanlı bir ev fiyatı tahmin sistemi
geliştirilmiştir.

Proje kapsamında doğrusal regresyon modeli eğitilmiş ve model çıktıları,
kullanıcı etkileşimi sağlamak amacıyla web tabanlı bir arayüz üzerinden
sunulmuştur.

---

## Kullanılan Veri Seti

Projede Boston Housing veri seti kullanılmıştır.  
Veri seti, konut fiyatlarını etkileyen suç oranı, hava kirliliği,
ortalama oda sayısı, vergi oranı ve sosyoekonomik göstergeler gibi
13 farklı öznitelikten oluşmaktadır.

Hedef değişken:
- **MEDV**: Evlerin medyan değeri (bin dolar)

---

## Kullanılan Yöntemler

- Linear Regression
- StandardScaler ile veri ölçekleme
- Train / Test Split (%80 - %20)

Model, sade ve yorumlanabilir bir yapı sunması nedeniyle tercih edilmiştir.

---

## Model Değerlendirme

Model performansı test verisi üzerinde aşağıdaki metrikler ile değerlendirilmiştir:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Skoru

Elde edilen sonuçlar, modelin konut fiyatlarındaki genel eğilimleri
başarılı bir şekilde yakalayabildiğini göstermektedir.

---

## Kullanıcı Arayüzü

Model, **Gradio** kütüphanesi kullanılarak geliştirilen web tabanlı
bir arayüz üzerinden sunulmuştur.

Kullanıcı, konut özelliklerini girerek tahmini ev fiyatını
anlık olarak görüntüleyebilmektedir.

Tahmin sonuçları, sunum sırasında daha anlaşılır olması amacıyla
günümüz konut fiyatlarına ölçeklenmiştir.

---

## Çalıştırma Talimatları

Gerekli kütüphaneleri yüklemek için:

```bash
pip install -r requirements.txt
