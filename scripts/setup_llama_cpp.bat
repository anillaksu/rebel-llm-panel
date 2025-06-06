@echo off
title REBEL LLM - llama.cpp Kurulumu
echo [REBEL] llama.cpp kurulumu başlatılıyor...

:: Git yüklü mü?
where git >nul 2>nul
if errorlevel 1 (
    echo [HATA] Git yüklü değil. https://git-scm.com/downloads adresinden yükleyin.
    pause
    exit /b
)

:: Visual Studio yüklü mü? (cl.exe kontrolü)
where cl >nul 2>nul
if errorlevel 1 (
    echo [HATA] Visual Studio C++ Build Tools eksik. Kurulum için: https://visualstudio.microsoft.com/visual-cpp-build-tools/
    pause
    exit /b
)

:: llama.cpp dizini
set LLAMA_DIR=rebel_llm\external\llama.cpp

:: Klasör varsa silinmesin, yeniden klonlama yok
if not exist %LLAMA_DIR% (
    git clone https://github.com/ggerganov/llama.cpp %LLAMA_DIR%
) else (
    echo [REBEL] llama.cpp zaten mevcut. Klonlama atlandı.
)

:: Build klasörünü oluştur ve geç
cd /d %LLAMA_DIR%
if not exist build mkdir build
cd build

:: Derleme işlemi (CURL kapalı, CMake ile)
cmake .. -G "Visual Studio 17 2022" -A x64 -DCMAKE_BUILD_TYPE=Release -DLLAMA_CURL=OFF
cmake --build . --config Release

echo [REBEL] llama.cpp kurulumu tamamlandı.
pause
