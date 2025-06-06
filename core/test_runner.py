from utils.logger import log_event
import os

def run_basic_tests():
    print("[TEST] Log sistemi test ediliyor...")
    log_event("TEST", "Test log girdisi.")

    print("[TEST] Dosya sistemi test ediliyor...")
    os.makedirs("test_dir", exist_ok=True)
    with open("test_dir/test_file.txt", "w") as f:
        f.write("Test içeriği.")

    print("[TEST] Tüm testler TAMAMLANDI.")
