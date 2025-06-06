@echo off
title REBEL LLM Kurulum
echo [*] Ortam hazırlanıyor...

:: Ana klasörler
mkdir logs
mkdir tasks
mkdir models
mkdir core
mkdir ui
mkdir setup

:: Sanal ortam
python -m venv venv
call venv\Scripts\activate.bat

:: Gerekli kütüphaneler
pip install --upgrade pip
pip install rich pyyaml

:: İlk görev dosyası kontrolü
if not exist tasks\task_list.yaml (
    echo tasks: > tasks\task_list.yaml
)

echo [✓] Kurulum tamam. REBEL LLM başlatılıyor...
python ui/rebel_panel_cli.py
pause
