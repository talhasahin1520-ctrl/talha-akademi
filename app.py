from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Gemini Ayarı (API Anahtarını Render'dan alacak)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def hello():
    return {
        "durum": "aktif",
        "mesaj": "Nova Eğitim Backend ve Gemini Sistemi Çalışıyor Kanka!",
        "kurucu": "Talha"
    }

# Nova AI Soru Cevap Bölümü
@app.route('/soru', methods=['POST'])
def soru_sor():
    veri = request.json
    kullanici_sorusu = veri.get('soru')
    
    try:
        response = model.generate_content(kullanici_sorusu)
        return jsonify({"cevap": response.text})
    except Exception as e:
        return jsonify({"hata": str(e)}), 500

@app.route('/basvuru', methods=['POST'])
def basvuru_yap():
    gelen_veri = request.json
    isim = gelen_veri.get('isim', 'Bilinmiyor')
    alan = gelen_veri.get('alan', 'Belirtilmedi')
    print(f"🚨 YENİ BAŞVURU: {isim} - Uzmanlık Alanı: {alan}")
    return jsonify({
        "status": "success",
        "mesaj": f"Selam {isim}, başvurunu aldık kanka!"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
