#!/usr/bin/env python3
# publish_to_github.py → REBEL AUTO PUBLISH SCRIPT 🌀

import subprocess
import datetime

def run_git_command(cmd):
    print(f"[REBEL] Running: {cmd}")
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

if __name__ == "__main__":
    print(f"\n🚀 REBEL AUTO PUBLISH STARTED → {datetime.datetime.now()}\n")

    # Git add all changes
    run_git_command("git add .")

    # Commit with timestamp
    commit_msg = f'Auto publish → {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    run_git_command(f'git commit -m "{commit_msg}"')

    # Push to origin main
    run_git_command("git push origin main")

    print(f"\n✅ REBEL AUTO PUBLISH COMPLETED → {datetime.datetime.now()}\n")
