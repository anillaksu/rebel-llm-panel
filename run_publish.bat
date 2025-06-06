@echo off
set TIMESTAMP=%date% %time%
echo ============================ >> publish_log.txt
echo REBEL AUTO PUBLISH → %TIMESTAMP% >> publish_log.txt
echo ============================ >> publish_log.txt

git add .
git commit -m "Auto publish → %TIMESTAMP%" || echo No changes to commit.
git push origin main

IF %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] Publish completed → %TIMESTAMP% >> publish_log.txt
) ELSE (
    echo [ERROR] Publish failed → %TIMESTAMP% >> publish_log.txt
)

echo Done.
pause
