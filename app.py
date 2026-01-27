from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) # Sitenin bu Python sistemine bağlanabilmesi için şart kanka!

# Ana Sayfa Kontrolü
@app.route('/')
def hello():
    return {
        "durum": "aktif",
        "mesaj": "Nova Eğitim Backend Sistemi Çalışıyor Kanka!",
        "kurucu": "Talha"
    }

# Eğitmen Başvuru Sistemi (Python burada devreye giriyor)
@app.route('/basvuru', methods=['POST'])
def basvuru_yap():
    gelen_veri = request.json
    isim = gelen_veri.get('isim', 'Bilinmiyor')
    alan = gelen_veri.get('alan', 'Belirtilmedi')
    
    # İleride buraya veritabanı ekleyeceğiz, şimdilik terminale yazdıralım
    print(f"🚨 YENİ BAŞVURU: {isim} - Uzmanlık Alanı: {alan}")
    
    return jsonify({
        "status": "success",
        "mesaj": f"Selam {isim}, başvurunu aldık! 1000 TL ders başı ücret için seni arayacağız kanka!"
    })

if __name__ == "__main__":
    # Render'ın portunu otomatik ayarlar
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
