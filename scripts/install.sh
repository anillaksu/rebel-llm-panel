#!/bin/bash
echo "[REBEL] Ortam kuruluyor..."

# Python bağımlılıkları yükleniyor
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

# .env dosyası kopyalanıyor
if [ ! -f rebel_llm/.env ]; then
  cp rebel_llm/.env.example rebel_llm/.env
  echo "[.env] Örnek dosya kopyalandı."
fi

# Klasörler oluşturuluyor
mkdir -p logs
mkdir -p tasks

echo "[REBEL] Kurulum tamamlandı. Başlatmak için: python rebel_llm_launcher.py"
