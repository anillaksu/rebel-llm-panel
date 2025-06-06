@echo off
title REBEL LLM Kurulumu
echo [REBEL] Ortam hazırlanıyor...

:: Python ortamını ve bağımlılıkları yükle
python -m pip install --upgrade pip
python -m pip install --user -r requirements.txt

:: PATH'e user script klasörü ekle (dotenv.exe erişimi için)
set "USER_SCRIPTS=%USERPROFILE%\AppData\Roaming\Python\Python313\Scripts"
echo [REBEL] PATH kontrol ediliyor...
setx PATH "%PATH%;%USER_SCRIPTS%" >nul
set PYTHONPATH=%CD%

:: .env dosyası yoksa örnek dosyadan kopyala
if not exist rebel_llm\.env (
    copy rebel_llm\.env.example rebel_llm\.env
    echo [.env] Dosyası kopyalandı.
)

:: Klasör yapısını oluştur
if not exist logs mkdir logs
if not exist tasks mkdir tasks

echo [REBEL] Kurulum tamamlandı. Başlatmak için: run.bat
pause
