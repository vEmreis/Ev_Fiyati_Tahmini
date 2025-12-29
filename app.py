import gradio as gr
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

print("APP BASLADI")

# Veri yükleme
data = pd.read_csv("train.csv")

X = data.drop("MEDV", axis=1)
y = data["MEDV"]

# Eğitim / test ayırma
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Ölçekleme
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Tahmin fonksiyonu
def predict_price(
    CRIM, ZN, INDUS, CHAS, NOX, RM,
    AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT
):
    values = np.array([[CRIM, ZN, INDUS, CHAS, NOX, RM,
                        AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]])
    values_scaled = scaler.transform(values)
    prediction = model.predict(values_scaled)[0]
    scaled_price = prediction * 18_000
    return f"{scaled_price:,.0f} $"

# Gradio arayüzü
interface = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Number(label="CRIM (Suç oranı)", minimum=0, maximum=100),
        gr.Number(label="ZN (Yerleşim alanı oranı %)", minimum=0, maximum=100),
        gr.Number(label="INDUS (Endüstriyel alan oranı)", minimum=0, maximum=30),
        gr.Radio(
            choices=[0, 1],
            label="CHAS (Nehir yakınlığı: 1=Evet, 0=Hayır)"
        ),
        gr.Number(label="NOX (Hava kirliliği)", minimum=0.3, maximum=1.0),
        gr.Slider(label="RM (Ortalama oda sayısı)", minimum=3, maximum=9, step=0.1),
        gr.Number(label="AGE (Eski bina oranı %)", minimum=0, maximum=100),
        gr.Number(label="DIS (İş merkezlerine uzaklık)", minimum=1, maximum=12),
        gr.Slider(label="RAD (Otoyol erişimi)", minimum=1, maximum=24, step=1),
        gr.Number(label="TAX (Vergi oranı)", minimum=150, maximum=800),
        gr.Number(label="PTRATIO (Öğrenci / Öğretmen oranı)", minimum=12, maximum=22),
        gr.Number(label="B (Sosyal yapı endeksi)", minimum=0, maximum=400),
        gr.Slider(label="LSTAT (Düşük gelirli nüfus %)", minimum=1, maximum=40, step=0.1)
    ],
    outputs=gr.Textbox(label="Tahmini Ev Fiyatı"),
    title="Ev Fiyatı Tahmin Sistemi",
    description="""
Bu arayüz, Boston konut verisi kullanılarak
makine öğrenmesi ile ev fiyatı tahmini yapar.
"""
)

# ÇALIŞTIR
interface.launch(share=True)
