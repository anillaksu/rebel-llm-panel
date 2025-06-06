@echo off
setlocal ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION

REM Get timestamp (universal way)
for /f "usebackq tokens=*" %%i in (`powershell -command "Get-Date -Format 'yyyy-MM-dd HH:mm:ss'"`) do set timestamp=%%i

REM Log header
echo ============================ >> publish_log.txt
echo REBEL AUTO PUBLISH → %timestamp% >> publish_log.txt
echo ============================ >> publish_log.txt

REM Git add
echo [REBEL] Running: git add . >> publish_log.txt
git add . >> publish_log.txt 2>&1

REM Git commit
echo [REBEL] Running: git commit -m "Auto publish → %timestamp%" >> publish_log.txt
git commit -m "Auto publish → %timestamp%" >> publish_log.txt 2>&1

REM Git push
echo [REBEL] Running: git push origin main >> publish_log.txt
git push origin main >> publish_log.txt 2>&1

REM Check errorlevel for success/failure
IF %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] Publish completed → %timestamp% >> publish_log.txt
) ELSE (
    echo [ERROR] Publish failed → %timestamp% >> publish_log.txt
)

REM Done
echo Done. Press any key to exit.
pause > nul
