
markdown
Kopyala
Duzenle
# ?? REBEL LLM Panel

Terminal tabanl?, offline cal??an LLM gorev kontrol paneli.  
Kendi sistemini kur, LLama.cpp modelini cal??t?r, gorevi yonet, loglar? incele.  

---

## ?? Ozellikler

- Gorev yonetim paneli (`Textual UI` tabanl?)
- GGUF formatl? LLM model deste?i (LLama.cpp submodule uzerinden)
- TTS deste?i
- Gorev loglama
- YAML gorev takibi
- Subprocess gorev cal??t?rma
- Basit benchmark runner

---

## ??? Kurulum

### 1?? Repo'yu Klonla:

```bash
git clone https://github.com/anillaksu/rebel-llm-panel.git
cd rebel-llm-panel
2?? Submodule Init:
bash
Kopyala
Duzenle
git submodule init
git submodule update
?? external/llama.cpp dizini LLama.cpp submodule olarak yuklenir.

3?? Gereksinimleri Kur:
bash
Kopyala
Duzenle
pip install -r requirements.txt
?? Cal??t?rma
bash
Kopyala
Duzenle
python main.py
Panel uzerinden tum gorev yonetimi yap?labilir.

?? Notlar
models/ klasoru .gitignore alt?nda ¡÷ LLM modellerini manuel ekleyin.

Buyuk dosyalar icin BFG + Git LFS kullan?m? onerilir.

????? Lisans
MIT License

yaml
Kopyala
Duzenle

---

### YAP:

1?? `README.md` dosyas?n? bununla guncelle  
2?? `git add README.md`  
3?? `git commit -m "Update README.md with submodule + usage instructions"`  
4?? `git push origin main`

---

**Bitince yaz ¡÷ s?radaki ad?mda `publish_to_github.py` guncellemesini de tam dosya protokolune uygun vericem.**  
#YARIM??YOK devam. ??