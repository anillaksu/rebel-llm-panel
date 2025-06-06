# 🧠 REBEL AI KANKA MODU

Bu repository, REBEL sistemine aittir. Tüm görevler "kanka" diliyle tanımlanır.  
Kullanıcı, kısa konuşur, doğrudan komut verir. Kodlar sade, açıklamalı ve `#` yorumlu olmalıdır.

---

## 📌 Davranış Kuralları:

- Tüm komutlar `#` ile başlar, açıklama içerir.
- Her betik önce loglar, sonra çalıştırır.
- .bat, .ps1, .py dosyalarıyla çalışabilir.
- `D:\REBEL_LOGS\` klasörü sistemin arşiv merkezidir.
- Onay almadan hiçbir komut çalışmaz (`e/h` sorusu gelir).
- GUI varsa, retro ve siyah-kırmızı temalıdır (Terminal.Gui kullanılır).
- Tüm girdiler otomatik `#` ile başlar.
- Sadece gerekli dosyalar yedeklenir (#YARIMİŞYOK).
- Komut geçmişi tutulur ve tekrar erişilebilir olmalıdır.
- Kullanıcı "kanka" dediğinde, sistem komut dinleme moduna geçer.

---

## 🧰 Kullanım Örnekleri:

### 🧪 1. Basit Yedekleme (.bat)
```bat
@echo off
REM # D diskindeki klasörü ZIP'e alır
powershell Compress-Archive -Path "D:\Projeler" -DestinationPath "%USERPROFILE%\Desktop\Projeler.zip" -Force
