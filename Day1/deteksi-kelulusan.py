from sklearn.linear_model import LogisticRegression
import numpy as np

# 1. Data [Jam Belajar, Jam Tidur]
X = np.array([
    [1, 8], [2, 7], [3, 9],  # Kelompok Kurang Belajar (Mungkin Gagal)
    [8, 5], [9, 6], [10, 7]  # Kelompok Rajin Belajar (Mungkin Lulus)
])

# 2. Label (0 = Gagal, 1 = Lulus)
y = np.array([0, 0, 0, 1, 1, 1])

# 3. Training Model
model_klasifikasi = LogisticRegression()
model_klasifikasi.fit(X, y)

# 4. Prediksi untuk Mahasiswa Baru
# Dia belajar 7 jam tapi cuma tidur 4 jam
mahasiswa_baru = np.array([[7, 4]])
hasil = model_klasifikasi.predict(mahasiswa_baru)
probabilitas = model_klasifikasi.predict_proba(mahasiswa_baru)

status = "LULUS" if hasil[0] == 1 else "GAGAL"
print(f"Hasil Prediksi: {status}")
print(f"Keyakinan AI: {probabilitas[0][hasil[0]]*100:.2f}%")