@echo off
REM === REBEL: Visual Studio Geliştirici Terminali (Yönetici olarak) ===

powershell -Command "Start-Process 'cmd.exe' -ArgumentList '/k \"\"D:\Microsoft Visual Studio\2022\Community\Common7\Tools\LaunchDevCmd.bat\"\"' -Verb RunAs"

pause
