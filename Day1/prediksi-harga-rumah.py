import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Data (Fitur: Luas Tanah dalam m2, Target: Harga dalam Juta Rupiah)
# Anggap saja kita punya data 5 rumah
luas_tanah = np.array([50, 70, 80, 100, 120]).reshape(-1, 1) 
harga_rumah = np.array([500, 700, 750, 950, 1100])

# 2. Inisialisasi Model
model = LinearRegression()

# 3. Training (Proses Belajar)
# Di sini model mencari hubungan matematis antara luas dan harga
model.fit(luas_tanah, harga_rumah)

# 4. Prediksi
# Sekarang kita tanya: "Kalau luasnya 90m2, harganya berapa?"
luas_baru = np.array([[90]])
prediksi = model.predict(luas_baru)

print(f"Prediksi harga untuk rumah 90m2 adalah: Rp {prediksi[0]:.2f} Juta")
print(f"Akurasi Model (R2 Score): {model.score(luas_tanah, harga_rumah):.4f}")

# --- Tambahkan ini di bawah kode sebelumnya ---

# 5. Visualisasi Data dan Model
plt.figure(figsize=(10, 6))

# Gambar titik-titik data asli (Warna Biru)
plt.scatter(luas_tanah, harga_rumah, color='blue', label='Data Asli')

# Gambar garis prediksi model (Warna Merah)
# Kita memprediksi harga untuk seluruh jangkauan luas tanah
harga_prediksi_garis = model.predict(luas_tanah)
plt.plot(luas_tanah, harga_prediksi_garis, color='red', linewidth=2, label='Garis Regresi AI')

# Tambahan label agar jelas
plt.title('Analisis AI: Luas Tanah vs Harga Rumah')
plt.xlabel('Luas Tanah (m2)')
plt.ylabel('Harga Rumah (Juta Rp)')
plt.legend()
plt.grid(True)
plt.show()