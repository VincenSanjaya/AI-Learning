def phishing_detector(email_text):
    # 1. Daftar kata kunci dan bobot risikonya (Risk Weight)
    keywords = {
        "urgent": 30, "important": 20, "suspended": 40,
        "password": 50, "verify": 40, "login": 30,
        "bank": 20, "account": 20, "click": 30,
        "money": 30, "winner": 50, "gift": 40
    }
    
    # 2. Preprocessing: Ubah semua jadi huruf kecil agar deteksi akurat
    email_text = email_text.lower()
    total_risk_score = 0
    found_keywords = []

    # 3. Analisis: Cek setiap kata di email
    for word, score in keywords.items():
        if word in email_text:
            total_risk_score += score
            found_keywords.append(word)

    # 4. Hasil Penilaian
    print(f"📩 Pesan: '{email_text[:50]}...'")
    print(f"🔍 Kata mencurigakan: {found_keywords}")
    print(f"📊 Skor Risiko: {total_risk_score}")

    if total_risk_score > 70:
        print("🚨 STATUS: HIGH RISK (PHISHING DETECTED!)")
    elif total_risk_score > 30:
        print("⚠️ STATUS: SUSPICIOUS (PROCEED WITH CAUTION)")
    else:
        print("✅ STATUS: SAFE")
    print("-" * 30)

# --- UJI COBA ---
phishing_detector("URGENT: Your bank account is suspended. Click here to login and verify your password.")
phishing_detector("Hi Vincen, do you want to play futsal this evening?")
phishing_detector("Congratulations! You are the winner of a $1000 gift. Click here now.")