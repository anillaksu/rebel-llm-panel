@echo off
setlocal
set LOGDIR=D:\REBELLIONLLM\tools\logs
if not exist "%LOGDIR%" mkdir "%LOGDIR%"
set LOGFILE=%LOGDIR%\rebel_executor_log.txt

set /p CMD=🧠 Komut gir (örnek: dir, python script.py): 

echo %DATE% %TIME% >> "%LOGFILE%"
echo # %CMD% >> "%LOGFILE%"

set /p ONAY=🛡️ Komutu çalıştırmak istiyor musun? (e/h): 
if /I "%ONAY%"=="e" (
    echo [ÇALIŞTIRILIYOR] %CMD%
    echo ----------------------------- >> "%LOGFILE%"
    %CMD% >> "%LOGFILE%" 2>&1
    echo ✅ Tamamlandı >> "%LOGFILE%"
) else (
    echo 🚫 Komut iptal edildi >> "%LOGFILE%"
)

start "" "notepad++.exe" "%LOGFILE%"
pause
