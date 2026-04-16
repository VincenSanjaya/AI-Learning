import tensorflow as tf
from tensorflow.keras import layers, models

# 1. Load data angka tulisan tangan (MNIST)
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0 # Normalisasi ke 0-1

# 2. Arsitektur CNN Sederhana
model = models.Sequential([
    # Layer 1: Mencari pola dasar (garis/tepi)
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    
    # Layer 2: Mengubah gambar jadi satu baris angka
    layers.Flatten(),
    
    # Layer 3: Memutuskan angka berapa ini (0-9)
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax') # 10 Output untuk angka 0-9
])

# 3. Compile dan Training
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Di dunia nyata, kita akan jalankan: model.fit(x_train, y_train, epochs=5)
print("Model CNN siap digunakan untuk mendeteksi pola!")