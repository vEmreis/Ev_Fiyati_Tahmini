import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "train.csv")

data = pd.read_csv(csv_path)

print("Veri yüklendi. Boyut:", data.shape)
print("Sütunlar:", list(data.columns))

target = "MEDV"  

features = data.columns.drop(target)

X = data[features]
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train, y_train)

print("Model eğitildi.")

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\n--- MODEL SONUÇLARI ---")
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")


i = 0  

gercek_fiyat = y_test.iloc[i]
tahmin_fiyat = y_pred[i]

print("\n--- ÖRNEK TAHMİN ---")
print(f"Gerçek fiyat : {gercek_fiyat:.2f}")
print(f"Tahmin edilen: {tahmin_fiyat:.2f}")
print(f"Fark         : {abs(gercek_fiyat - tahmin_fiyat):.2f}")
