@echo off
setlocal

REM === REBEL LLM AUTO PUBLISH START ===
echo ============================ > auto_publish_log.txt
echo REBEL LLM AUTO PUBLISH START >> auto_publish_log.txt
echo ============================ >> auto_publish_log.txt
echo. >> auto_publish_log.txt

echo 🚀 REBEL AUTO PUBLISH STARTED → %DATE% %TIME% >> auto_publish_log.txt
echo. >> auto_publish_log.txt

REM === RUN rebel_executor.cmd with auto_publish ===
call rebel_executor.cmd auto_publish

echo. >> auto_publish_log.txt
echo 🚀 REBEL AUTO PUBLISH COMPLETED → %DATE% %TIME% >> auto_publish_log.txt
echo. >> auto_publish_log.txt

endlocal
