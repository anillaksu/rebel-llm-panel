from core.config_loader import MODEL_PATH, LOG_FILE, DEFAULT_TASK_FILE
import os

def check_path(path, desc):
    if os.path.exists(path):
        print(f"[✓] {desc} bulundu: {path}")
    else:
        print(f"[✗] {desc} EKSİK veya YANLIŞ: {path}")

if __name__ == "__main__":
    print("🔍 REBEL LLM ENV CHECKER\n")
    check_path(MODEL_PATH, "Model dosyası")
    check_path(LOG_FILE, "Log dosyası")
    check_path(DEFAULT_TASK_FILE, "Görev listesi")
