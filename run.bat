@echo off
setlocal
set PYTHONPATH=%~dp0..
echo [REBEL] Ortam kontrol ediliyor...

echo [REBEL] Başlatılıyor...
python rebel_panel_cli.py
pause
