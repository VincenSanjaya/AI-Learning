import cv2
import os

def ai_face_gate_stable(image_path):
    # 1. Load detektor wajah (Haar Cascade) yang sudah ada di OpenCV
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)

    # 2. Baca Gambar
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: File '{image_path}' tidak ditemukan di folder ini!")
        return

    # 3. Ubah ke Hitam Putih (AI lebih cepat memproses dalam Grayscale)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 4. Proses Deteksi
    # scaleFactor: seberapa banyak gambar dikecilkan saat mencari wajah
    # minNeighbors: seberapa yakin AI bahwa itu adalah wajah
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 5. Logika Akses
    print("-" * 30)
    if len(faces) > 0:
        print(f"Sinyal: {len(faces)} Wajah Terdeteksi!")
        print("Status: ACCESS GRANTED ✅")
        
        # Gambar kotak di wajah yang ditemukan
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
            cv2.putText(img, "VERIFIED", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    else:
        print("Sinyal: Tidak ada wajah yang dikenali.")
        print("Status: ACCESS DENIED ❌")
    print("-" * 30)

    # 6. Simpan Hasil Log
    output_name = 'access_log_result.jpg'
    cv2.imwrite(output_name, img)
    print(f"Log visual disimpan sebagai: {output_name}")

# --- EKSEKUSI ---
# Pastikan ada file bernama 'test.jpg' di folder yang sama!
ai_face_gate_stable('test.JPG')