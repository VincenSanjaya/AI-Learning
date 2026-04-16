import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Data Baru dengan 2 Fitur (Luas Tanah, Jumlah Kamar)
# Format data: [[Luas, Kamar], [Luas, Kamar], ...]
X = np.array([
    [50, 1],  # Rumah 1
    [70, 2],  # Rumah 2
    [80, 2],  # Rumah 3
    [100, 3], # Rumah 4
    [120, 3]  # Rumah 5
])

# Target tetap Harga (Juta Rp)
y = np.array([500, 700, 750, 950, 1100])

# 2. Inisialisasi dan Training Model Baru
model_multi = LinearRegression()
model_multi.fit(X, y)

# 3. Prediksi Baru
# Kita tanya: "Kalau luasnya 90m2 DAN ada 3 kamar, harganya berapa?"
# Bandingkan jika: "Kalau luasnya 90m2 TAPI cuma 1 kamar?"
rumah_a = np.array([[90, 3]])
rumah_b = np.array([[90, 1]])

prediksi_a = model_multi.predict(rumah_a)
prediksi_b = model_multi.predict(rumah_b)

print(f"Prediksi rumah A (90m2, 3 kamar): Rp {prediksi_a[0]:.2f} Juta")
print(f"Prediksi rumah B (90m2, 1 kamar): Rp {prediksi_b[0]:.2f} Juta")