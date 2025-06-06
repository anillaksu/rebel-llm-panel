# 📄 REBEL LLM System Specification (v1.0)

🕒 Last updated: 2025-06-05 16:42:49
🧠 Designed by: REBEL Systems

---

## 🔧 Genel Bakış

REBEL LLM, yerel çalışabilen, görev takipli, modüler bir yapay zekâ sistemidir. Kullanıcının veri güvenliğini önceleyen, offline çalışabilen, CLI ve TUI destekli bir LLM (Large Language Model) kontrol paneli sunar.

---

## 🧱 Sistem Mimarisi

```
[User] --> [run.bat]
             ↓
       [rebel_llm_launcher.py]
             ↓
     [rebel_panel_cli.py / main.py]
             ↓
    +--------+---------+------------+
    |        |         |            |
[task_runner]| [model_runner]| [log_manager]
             ↓
      [llama.cpp binaries]
```

---

## 📁 Klasör Yapısı

```
rebel_llm/
├── core/
│   ├── config_loader.py
│   ├── log_manager.py
│   └── task_runner.py
├── external/
│   └── llama.cpp/
├── models/
│   └── gemma-1.1-2b-it.Q4_K_M.gguf
├── sessions/
│   └── chat_session.yaml
├── tasks/
│   └── task_list.yaml
├── ui/
│   └── rebel_panel_cli.py
├── logs/
│   └── rebel.log
```

---

## 🔄 Dosya Akışı ve Fonksiyonlar

| Dosya | Açıklama |
|-------|----------|
| `run.bat` | Başlatıcı, Python ortamını çağırır |
| `rebel_llm_launcher.py` | `.env` dosyasını yükler, CLI'yi başlatır |
| `main.py` | Alternatif CLI başlatıcısı |
| `rebel_panel_cli.py` | Görev seçim arayüzünü yönetir |
| `task_runner.py` | Görev ID’sine göre işlem çalıştırır |
| `model_runner.py` | LLM modelini CLI veya exe ile başlatır |
| `chat_interface.py` | GGUF modeliyle terminalde sohbet sunar |
| `log_manager.py` | Sistem loglama & hata yakalama |
| `config_loader.py` | Ortam değişkenlerini çeker |
| `build_and_zip.py` | Sistemi paketler |
| `publish_to_github.py` | Projeyi GitHub'a yükler |

---

## 🔩 Harici Bileşenler

- `llama.cpp`: GGUF modelleri çalıştırmak için kullanılan C++ backend'i.
- `benchmark_runner.py`: Model hız/performans testi.
- `test_model.bat`: Manuel model testi.
- `setup_llama_cpp.bat`: Derleme ve entegrasyon setup dosyası.

---

## 🧪 Test Süreci

```bash
pytest tests/
test_model.bat
```

---

## ⚠️ Notlar

- `.env` dosyası zorunludur. `.env.example`'dan kopyalanmalı.
- Derleme sonrası binary dosyalarının yolu `.env` içinde tanımlanmalı.
- Kullandığın model GGUF formatında olmalı.

---

## 🧠 Tavsiyeler

- Her görev için `task_list.yaml` içeriğini sürekli güncel tut.
- `logs/rebel.log` dosyasını hatalar için periyodik kontrol et.
- Model değiştirirken `MODEL_PATH` değerini unutma.

