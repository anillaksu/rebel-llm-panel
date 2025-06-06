@echo off
setlocal
set PYTHONPATH=%~dp0..
echo [REBEL] Ortam kontrol ediliyor...

echo [REBEL] GÖREV PANELİ başlatılıyor...
python main.py
pause
