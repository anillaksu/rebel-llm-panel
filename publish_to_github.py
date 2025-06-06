import subprocess
import datetime

def run_git_command(cmd):
    print(f"\n[REBEL] Running: {cmd}")
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

print(f"\n🚀 REBEL AUTO PUBLISH STARTED → {datetime.datetime.now()}")

run_git_command("git add .")

run_git_command(f'git commit -m "Auto publish → {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"')

# YENİ → Önce status göster → ondan sonra push
run_git_command("git status")

run_git_command("git push origin main")
