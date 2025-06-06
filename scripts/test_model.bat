@echo off
title REBEL LLM - Model Testi
echo [REBEL] Model testi başlatılıyor...

:: Model ve binary yolları
set MODEL_PATH=models\gemma-1.1-2b-it.Q4_K_M.gguf
set BINARY_PATH=rebel_llm\external\llama.cpp\build\bin\Release\llama-simple.exe

:: Model dosyası kontrolü
if not exist %MODEL_PATH% (
    echo [HATA] Model dosyası bulunamadı: %MODEL_PATH%
    pause
    exit /b
)

:: Binary dosyası kontrolü
if not exist %BINARY_PATH% (
    echo [HATA] Binary dosyası bulunamadı: %BINARY_PATH%
    pause
    exit /b
)

:: Modeli çalıştır
%BINARY_PATH% -m %MODEL_PATH% -p "Merhaba, REBEL sistemini test ediyoruz." --n-predict 50

echo [REBEL] Test tamamlandı.
pause
