import os
import shutil
import zipfile
from datetime import datetime

def zip_directory(src_dir, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(src_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, src_dir)
                zipf.write(full_path, rel_path)

def main():
    project_root = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(project_root)
    zip_name = f"REBEL_LLM_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    zip_path = os.path.join(base_dir, zip_name)

    print("[REBEL] Yapı paketleniyor...")
    zip_directory(base_dir, zip_path)
    print(f"[REBEL] Paket oluşturuldu: {zip_path}")

if __name__ == "__main__":
    main()
