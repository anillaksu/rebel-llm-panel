@echo off
setlocal

REM === Argument Check ===
set "ARG=%1"

REM === LOG START ===
echo ----------------------------- >> auto_publish_log.txt
echo [REBEL] Running: %ARG% >> auto_publish_log.txt
echo ----------------------------- >> auto_publish_log.txt
echo.

REM === AUTO PUBLISH FLOW ===
if "%ARG%"=="auto_publish" (
    echo [REBEL] git add .
    echo [REBEL] git add . >> auto_publish_log.txt
    git add . >> auto_publish_log.txt 2>&1

    echo [REBEL] git commit -m "REBEL AUTO PUBLISH COMMIT"
    echo [REBEL] git commit -m "REBEL AUTO PUBLISH COMMIT" >> auto_publish_log.txt
    git commit -m "REBEL AUTO PUBLISH COMMIT" >> auto_publish_log.txt 2>&1

    echo [REBEL] git push origin main
    echo [REBEL] git push origin main >> auto_publish_log.txt
    git push origin main >> auto_publish_log.txt 2>&1

    echo [REBEL] AUTO PUBLISH DONE!
    echo [REBEL] AUTO PUBLISH DONE! >> auto_publish_log.txt
) else (
    echo [REBEL] Unknown argument: %ARG%
    echo [REBEL] Unknown argument: %ARG% >> auto_publish_log.txt
)

endlocal
