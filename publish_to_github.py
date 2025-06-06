# publish_to_github.py
import subprocess
import datetime

def run_git_command(cmd):
    print(f"\n[REBEL] Running: {cmd}")
    result = subprocess.run(cmd, shell=True, text=True)
    if result.returncode != 0:
        print(f"[ERROR] Command failed: {cmd}")
        exit(1)

if __name__ == "__main__":
    print(f"\n🚀 REBEL AUTO PUBLISH STARTED → {datetime.datetime.now()}\n")

    run_git_command("git add .")
    commit_message = f"Auto publish → {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    run_git_command(f"git commit -m \"{commit_message}\" || echo 'No changes to commit.'")
    run_git_command("git push origin main")
