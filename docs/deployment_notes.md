🚀 docs/deployment_notes.md — REBEL LLM Dağıtım ve Kullanım Notları
markdown
Kopyala
Düzenle
# 📦 REBEL LLM Dağıtım Notları

> "Bir sistem ancak sahada çalışıyorsa gerçek sistemdir."

---

## 🧭 Dağıtım Amacı

REBEL LLM, **tamamen offline çalışan**, **yerel görevleri yürüten**, **modüler bir AI yardımcı platformudur.**

Kurulumun amacı:
- Bilgisayar içindeki görevleri otomatik yönetmek.
- Panel üzerinden işleri kontrol etmek.
- Model tabanlı otomasyonları başlatmak.

---

## 💡 Gereksinimler

| Bileşen         | Gereken |
|----------------|---------|
| Python         | 3.10+   |
| pip            | 21+     |
| Sistem         | Windows 10/11 (Linux desteği planlı) |
| Ek Paketler    | `rich`, `pyyaml`, `python-dotenv` |

---

## ⚙️ Kurulum Adımları (Windows)

```bash
# 1. Depoyu klonla
git clone https://github.com/kullanici/rebel_llm.git
cd rebel_llm

# 2. Ortamı hazırla
scripts\install.bat

# 3. Yapılandırmayı yap
copy rebel_llm\.env.example rebel_llm\.env
notepad rebel_llm\.env  # Gerekirse düzenle

# 4. Başlat
run.bat
🧪 Testler
bash
Kopyala
Düzenle
pytest tests/
🧱 Portable Kullanım
Sistemi zip'le (rebel_llm/)

.env içinde tüm yolları göreceli yap.

Taşınabilir diskten çalıştırmak için:

run.bat veya rebel_llm_launcher.py kullan.

Loglar ve görevler, dizin içinde kalır.

🔐 Güvenlik Notu
Internet bağlantısına ihtiyaç yoktur.

Tüm görevler lokal shell komutlarıdır.

LLM modelleri offline GGUF tabanlıdır.

🧠 Geliştirici İpuçları
Yeni görev eklemek için task_list.yaml'a satır ekle.

Komutların çıktıları logs/rebel.log'a düşer.

core/ altındaki modüller genişletmeye açık.

📎 Notlar
Sistemin ileriki versiyonlarında model benchmark, ses tanıma, otomatik güncelleme gibi sistemler eklenecek.