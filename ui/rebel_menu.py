import yaml

def list_tasks():
    with open("tasks/task_list.yaml", "r", encoding="utf-8") as f:
        tasks = yaml.safe_load(f)["tasks"]
    print("\nREBEL Görev Listesi:\n")
    for t in tasks:
        print(f"[{t['id']}] {t['name']} - ({t['status']})")
    print("\n")

if __name__ == "__main__":
    list_tasks()
