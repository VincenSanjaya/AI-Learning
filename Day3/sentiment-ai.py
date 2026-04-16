from textblob import TextBlob

def analisa_perasaan(teks):
    # 1. Masukkan teks ke "Otak" NLP
    blob = TextBlob(teks)
    
    # 2. Ambil skor polaritas (-1 sangat negatif, 1 sangat positif)
    # Skor 0 artinya netral
    skor = blob.sentiment.polarity
    
    print(f"Kalimat: '{teks}'")
    if skor > 0.3:
        print(f"Hasil: SANGAT POSITIF 😍 (Skor: {skor:.2f})")
    elif skor > 0:
        print(f"Hasil: POSITIF 😊 (Skor: {skor:.2f})")
    elif skor < 0:
        print(f"Hasil: NEGATIF 😡 (Skor: {skor:.2f})")
    else:
        print(f"Hasil: NETRAL 😐")
    print("-" * 30)

# --- UJI COBA ---
analisa_perasaan("My code finally works after 100 errors!")
analisa_perasaan("I am so tired of this slow internet connection.")
analisa_perasaan("Today is a regular Thursday in Jakarta.")
