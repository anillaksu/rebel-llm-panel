import yaml
import subprocess
import os

TASK_FILE = "tasks/task_list.yaml"
LOG_FILE = "logs/rebel.log"

def log(message):
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")
    print(message)

def load_tasks():
    with open(TASK_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["tasks"]

def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        yaml.dump({"tasks": tasks}, f, allow_unicode=True)

def run_task(task):
    log(f"[RUNNING] {task['id']} - {task['name']}")
    try:
        # Gerçek komut çalıştırma
        result = subprocess.run(task["command"], shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            task["status"] = "done"
            log(f"[✓ DONE] {task['name']}")
        else:
            task["status"] = "failed"
            log(f"[✗ ERROR] {task['name']} - {result.stderr.strip()}")
    except Exception as e:
        task["status"] = "failed"
        log(f"[✗ EXCEPTION] {task['name']} - {str(e)}")

if __name__ == "__main__":
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == "pending":
            run_task(task)
    save_tasks(tasks)