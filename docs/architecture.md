# 🧱 REBEL LLM Sistem Mimarisi

> "Karmaşıklık değil, modülerlik büyütür projeyi."

---

## 📦 Ana Modüller

### 1️⃣ `core/`
- **task_runner.py**: YAML görev dosyasını okuyup ilgili komutu çalıştırır.
- **log_manager.py**: Görev çıktılarının log dosyasına yazılmasını sağlar.
- **config_loader.py**: `.env` üzerinden ayarları çeker (model yolu, log yolu vs).
- **env_checker.py**: Kurulum sırasında sistem uyumluluğunu kontrol eder.

---

### 2️⃣ `ui/`
- **rebel_panel_cli.py**: Rich ile terminal arayüzü sağlar (TUI alternatifi).
- (❌ Textual denemesi iptal edildi, sade Rich ile devam.)

---

### 3️⃣ `tasks/`
- **task_list.yaml**: Tüm görevlerin listelendiği merkezi YAML dosyası.

---

### 4️⃣ `logs/`
- **rebel.log**: Tüm görevlerin çıktı ve hatalarının yazıldığı dosya.

---

### 5️⃣ `scripts/`
- **install.bat / install.sh**: Windows/Linux için setup scriptleri.
- **run.bat**: Ana paneli başlatmak için hızlı erişim dosyası.

---

### 6️⃣ `tests/`
- Birim testler (şimdilik `task_runner` için hazırlandı.)

---

## 🔁 Akış Diyagramı (Text Formatı)

[ run.bat / launcher.py ]
↓
[ rebel_panel_cli.py ]
↓
[ task_runner.py ] ←→ [ task_list.yaml ]
↓
[ log_manager.py ] → [ logs/rebel.log ]

yaml
Kopyala
Düzenle

---

## 🧪 Model ve LLM Modülü (Planlı)

- `model_controller.py`: GGUF model yükleme, VRAM test etme vs.
- Bu kısım ileride `benchmark_runner.py` ile entegre olacak.

---

## 📄 Dosya Yapısı Örneği

rebel_llm/
│
├── core/
├── ui/
├── tasks/
├── logs/
├── scripts/
├── tests/
│
├── rebel_llm_launcher.py
├── config.yaml
├── requirements.txt
└── .env

yaml
Kopyala
Düzenle

---

## 🧠 Not
Bu yapı sürekli genişletilebilir şekilde tasarlanmıştır. Yeni görev, model ya da UI modülü kolayca entegre edilebilir. Kodun içindeki her şey fonksiyonel ve modülerdir.

