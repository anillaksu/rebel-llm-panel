@echo off
setlocal ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION

REM Get timestamp (universal way)
for /f "usebackq tokens=*" %%i in (`powershell -command "Get-Date -Format 'yyyy-MM-dd HH:mm:ss'"`) do set timestamp=%%i

REM Log header
echo ============================ >> publish_log.txt
echo REBEL AUTO PUBLISH → %timestamp% >> publish_log.txt
echo ============================ >> publish_log.txt

REM Ekrana bilgi
echo [REBEL] Auto Publish Basladi → %timestamp%
echo -----------------------------

REM Git add
echo [REBEL] Running: git add .
git add . >> publish_log.txt 2>&1

REM Git commit
echo [REBEL] Running: git commit -m "Auto publish → %timestamp%"
git commit -m "Auto publish → %timestamp%" >> publish_log.txt 2>&1

REM Small delay to avoid file lock issues
timeout /T 1 > nul

REM Git push → doğrudan ekrana yazdır → yüzdelik % bar için
echo [REBEL] Running: git push origin main
git push origin main --progress

REM Check errorlevel for success/failure
IF %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] Publish completed → %timestamp%
    echo [SUCCESS] Publish completed → %timestamp% >> publish_log.txt
) ELSE (
    echo [ERROR] Publish failed → %timestamp%
    echo [ERROR] Publish failed → %timestamp% >> publish_log.txt
)

REM Done
echo -----------------------------
echo Done. Press any key to exit.
pause > nul
