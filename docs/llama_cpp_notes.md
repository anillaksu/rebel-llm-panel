✅ Tam İçerik — docs/llama_cpp_notes.md
markdown
Kopyala
Düzenle
# 🧠 REBEL LLM - llama.cpp Notları

## 📦 Derleme Sonrası Binary Konumu
Derlemeden sonra binary dosyaları şu klasöre yerleşir:
rebel_llm/external/llama.cpp/build/bin/Release/

perl
Kopyala
Düzenle

## 🚀 Önemli Binary'ler
- `llama-simple.exe`: Temel sohbet başlatıcı (chat_interface.py tarafından kullanılır).
- `main.exe`: CLI üzerinden giriş yapılabilen temel model çalışma aracı.
- `quantize.exe`: GGUF modeli quantize etmek için kullanılır.
- `benchmark.exe`: Model hız testlerini yapar.

## 🗂️ Model Kullanımı
`.env` içinde model yolunu belirt:
MODEL_PATH=models/gemma-1.1-2b-it.Q4_K_M.gguf

bash
Kopyala
Düzenle

## 💡 Komut Örnekleri
**Test Amaçlı Çalıştırma:**
```bash
./llama-simple.exe -m models/gemma-1.1-2b-it.Q4_K_M.gguf
Quantize Etmek İçin:

bash
Kopyala
Düzenle
./quantize.exe models/original.gguf models/quantized.Q4_K_M.gguf Q4_K_M
⚙️ CMake Notları
Eğer curl problemi varsa:

pgsql
Kopyala
Düzenle
cmake .. -DLLAMA_CURL=OFF -G "Visual Studio 17 2022" -A x64 -DCMAKE_BUILD_TYPE=Release
📌 Bağlantılı Dosyalar
chat_interface.py → llama-simple.exe üzerinden modelle sohbet başlatır.

benchmark_runner.py → benchmark.exe ile test yapar.

.env → MODEL_PATH buradan alınır.

Not: Bu doküman, geliştiricinin sistemi daha hızlı kavraması için hazırlanmıştır. Otomatik kurulumdan sonra binary yolu değişirse .env güncellenmelidir.