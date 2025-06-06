import os
from core.config_loader import LOG_FILE

def log_event(message: str):
    """Log dosyasına olay ekler."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[REBEL] {message}\n")

def read_log() -> str:
    """Log dosyasını okur ve string olarak döner."""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return f.read()
    return "[REBEL] Henüz log bulunamadı."

def clear_log():
    """Log dosyasını temizler."""
    if os.path.exists(LOG_FILE):
        open(LOG_FILE, "w").close()
        log_event("Log temizlendi.")
