@echo off
REM === REBEL: LLM Chat Başlatıcı ===

cd /d D:\projeler\REBELLIONLLM\rebel_llm
set PYTHONPATH=D:\projeler\REBELLIONLLM

REM Eğer run_chat.bat varsa onu çalıştır:
if exist run_chat.bat (
    call run_chat.bat
) else (
    REM run_chat.bat yoksa chat_interface.py çalıştır:
    python D:\projeler\REBELLIONLLM\rebel_llm\chat_interface.py
)

pause
