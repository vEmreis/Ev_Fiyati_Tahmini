# Ev Fiyatı Tahmin Sistemi

Bu projede Boston Housing veri seti kullanılarak,
makine öğrenmesi tabanlı bir ev fiyatı tahmin modeli geliştirilmiştir.

## Kullanılan Yöntemler
- Linear Regression
- StandardScaler
- Train/Test Split

## Model Değerlendirme
Model, test verisi üzerinde R², MAE ve RMSE metrikleri ile değerlendirilmiştir.

## Arayüz
Proje, Gradio kütüphanesi kullanılarak web tabanlı bir arayüz ile sunulmuştur.

## Çalıştırma
```bash
pip install -r requirements.txt
python app.py
