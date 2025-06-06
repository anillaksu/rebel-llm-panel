import os
import subprocess
from datetime import datetime

REPO_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
COMMIT_MESSAGE = f"🔄 Otomatik güncelleme - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def run_git_command(command):
    result = subprocess.run(command, shell=True, cwd=REPO_PATH, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"[HATA] Komut başarısız: {command}")
        print(result.stderr)
    else:
        print(result.stdout)

def main():
    print("[REBEL] GitHub push işlemi başlatılıyor...")

    run_git_command("git add .")
    run_git_command(f'git commit -m "{COMMIT_MESSAGE}"')
    run_git_command("git push")

    print("[REBEL] Tüm değişiklikler GitHub’a yollandı.")

if __name__ == "__main__":
    main()
