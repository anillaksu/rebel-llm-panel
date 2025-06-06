# main.py
from rich.console import Console
from rich.table import Table
from utils.logger import log_event
import yaml
from core.test_runner import run_basic_tests
import subprocess
import os
from datetime import datetime

# GLOBAL değişken (filter_status)
filter_status = "all"

# Görev listesi yükleniyor
with open("tasks.yaml", "r", encoding="utf-8") as f:
    raw_data = yaml.safe_load(f)

if isinstance(raw_data, dict) and "tasks" in raw_data:
    tasks_data = raw_data["tasks"]
else:
    tasks_data = raw_data

console = Console()

def get_active_model_name():
    models_dir = "models"
    if not os.path.exists(models_dir):
        return "[MODELS DİZİNİ YOK]"

    gguf_files = [f for f in os.listdir(models_dir) if f.endswith(".gguf")]
    if not gguf_files:
        return "[MODEL YOK]"

    gguf_files.sort(key=lambda x: os.path.getmtime(os.path.join(models_dir, x)), reverse=True)
    return gguf_files[0]

def display_task_table():
    active_model = get_active_model_name()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    title_text = f"🚀 REBEL LLM GÖREV PANELİ | Model: {active_model} | {current_time} | Filter: {filter_status.upper()}"

    table = Table(title=title_text)

    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Görev Adı", style="magenta")
    table.add_column("Durum", justify="center", style="green")

    for task in tasks_data:
        if isinstance(task, dict):
            id_ = str(task.get("id", "N/A"))
            name = task.get("title") or task.get("name") or "[BOŞ]"
            status = task.get("status", "N/A")

            if filter_status == "all" or status == filter_status:
                table.add_row(id_, name, status)
        else:
            log_event("TASK_ERROR", f"Geçersiz task girdisi: {task}")

    console.print(table)
def run_task_by_id(task_id):
    found = False
    for task in tasks_data:
        if isinstance(task, dict) and task.get("id") == task_id:
            found = True
            command = task.get("command")
            if command:
                print(f"[REBEL COMMAND] Task ID {task_id} → Komut çalıştırılıyor: {command}")
                log_event("TASK_COMMAND", f"Task ID {task_id} komut çalıştırıldı: {command}")
                try:
                    subprocess.run(command, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"[REBEL COMMAND ERROR] Komut çalıştırılırken hata oluştu: {e}")
            else:
                print(f"[REBEL] Task ID {task_id} için 'command' tanımlı değil.")
            break
    if not found:
        print(f"[REBEL] Task ID {task_id} bulunamadı.")

def display_task_details(task_id):
    found = False
    for task in tasks_data:
        if isinstance(task, dict) and task.get("id") == task_id:
            found = True
            print(f"\n[REBEL TASK DETAILS] → ID: {task_id}")
            print(f"Title : {task.get('title') or task.get('name') or '[BOŞ]'}")
            print(f"Status: {task.get('status', 'N/A')}")
            command = task.get("command", "YOK")
            print(f"Command: {command}")
            print("-" * 50)
            log_event("TASK_DETAILS", f"Task ID {task_id} detay görüntülendi.")
            break
    if not found:
        print(f"[REBEL] Task ID {task_id} bulunamadı.")

def run_tests():
    print("[REBEL TEST] Testler çalıştırılıyor...")
    run_basic_tests()
    log_event("TEST_RUN", "Testler çalıştırıldı.")

def reset_tasks():
    for task in tasks_data:
        if isinstance(task, dict):
            task["status"] = "pending"
    with open("tasks.yaml", "w", encoding="utf-8") as f:
        yaml.dump({"tasks": tasks_data}, f, allow_unicode=True)
    print("[REBEL RESET] Tüm görevler 'pending' yapıldı.")
    log_event("TASK_RESET", "Tüm görevler sıfırlandı.")

def display_logs():
    log_file = os.path.join("logs", "rebel_log.txt")
    if not os.path.exists(log_file):
        print("[REBEL] Log dosyası bulunamadı.")
        return
    print("\n[REBEL LOG] Son 20 satır gösteriliyor:")
    print("-" * 50)
    with open(log_file, "r", encoding="utf-8") as f:
        lines = f.readlines()[-20:]
        for line in lines:
            print(line.strip())
    print("-" * 50)
    log_event("LOG_VIEW", "Son 20 satır log görüntülendi.")
def filter_tasks(new_filter):
    global filter_status
    filter_status = new_filter.lower()
    print(f"[REBEL FILTER] Filtre ayarlandı: {filter_status.upper()}")
    log_event("FILTER_CHANGE", f"Filtre değiştirildi: {filter_status.upper()}")

def edit_tasks_file():
    tasks_file = "tasks.yaml"
    try:
        print(f"[REBEL EDIT] {tasks_file} dosyası açılıyor...")
        os.system(f'notepad "{tasks_file}"')
        log_event("TASKS_EDIT", "tasks.yaml düzenlendi.")
    except Exception as e:
        print(f"[REBEL ERROR] tasks.yaml düzenlenirken hata oluştu: {e}")

def save_panel_snapshot():
    snapshot_file = os.path.join("logs", "panel_snapshot.txt")
    try:
        with open(snapshot_file, "w", encoding="utf-8") as f:
            f.write(f"REBEL LLM PANEL SNAPSHOT | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("---------------------------------------------------\n")
            for task in tasks_data:
                if isinstance(task, dict):
                    id_ = str(task.get("id", "N/A"))
                    name = task.get("title") or task.get("name") or "[BOŞ]"
                    status = task.get("status", "N/A")
                    f.write(f"[{id_}] {name} → {status}\n")
            f.write("---------------------------------------------------\n")
        print(f"[REBEL SNAPSHOT] Panel snapshot kaydedildi: {snapshot_file}")
        log_event("PANEL_SNAPSHOT", "Panel snapshot alındı.")
    except Exception as e:
        print(f"[REBEL ERROR] Snapshot alınırken hata oluştu: {e}")

def view_file():
    file_options = {
        "1": "logs/rebel_log.txt",
        "2": "logs/last_action_log.txt",
        "3": "tasks.yaml"
    }

    print("\n[REBEL] Görüntülemek için dosya seç:")
    print("1 - logs/rebel_log.txt")
    print("2 - logs/last_action_log.txt")
    print("3 - tasks.yaml")
    print("q - Geri dön")

    choice = input("Seçiminiz: ").strip()

    if choice.lower() == "q":
        return

    selected_file = file_options.get(choice)
    if selected_file and os.path.exists(selected_file):
        print(f"\n[REBEL FILE VIEW] {selected_file} → içeriği:")
        print("-" * 50)
        with open(selected_file, "r", encoding="utf-8") as f:
            content = f.read()
            print(content)
        print("-" * 50)
        log_event("FILE_VIEW", f"{selected_file} görüntülendi.")
    else:
        print("[REBEL] Geçersiz seçim veya dosya bulunamadı.")
def update_task_status(task_id):
    found = False
    for task in tasks_data:
        if isinstance(task, dict) and task.get("id") == task_id:
            found = True
            task["status"] = "done"
            with open("tasks.yaml", "w", encoding="utf-8") as f:
                yaml.dump({"tasks": tasks_data}, f, allow_unicode=True)
            print(f"[REBEL UPDATE] Task ID {task_id} durumu DONE yapıldı.")
            log_event("TASK_UPDATE", f"Task ID {task_id} updated to done.")
            break
    if not found:
        print(f"[REBEL] Task ID {task_id} bulunamadı.")

def main_loop():
    print("[REBEL] Ortam kontrol ediliyor...")
    print("[REBEL] GÖREV PANELİ başlatılıyor...")
    while True:
        display_task_table()
        print("\nNe yapmak istersin (sıfırla, çık, id gir, t=test çalıştır, r=id ile komut çalıştır, d=id detay göster, l=log görüntüle, f=filtre, v=dosya görüntüle, e=görev düzenle, x=snapshot): ")
        choice = input().strip()

        # Log action
        with open("logs/last_action_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ACTION: {choice}\n")

        if choice.lower() == "çık":
            print("[REBEL] Çıkılıyor...")
            break
        elif choice.lower() == "sıfırla" or choice.lower() == "s":
            reset_tasks()
        elif choice.lower() == "t":
            run_tests()
        elif choice.lower() == "l":
            display_logs()
        elif choice.lower() == "f":
            new_filter = input("[REBEL] Filtre seç (done / pending / all): ").strip()
            if new_filter.lower() in ["done", "pending", "all"]:
                filter_tasks(new_filter)
            else:
                print("[REBEL] Geçersiz filtre seçimi.")
        elif choice.lower() == "r":
            try:
                task_id = int(input("[REBEL] Hangi ID'nin komutunu çalıştırmak istersin? ").strip())
                run_task_by_id(task_id)
            except ValueError:
                print("[REBEL] Geçersiz ID girdisi.")
        elif choice.lower() == "d":
            try:
                task_id = int(input("[REBEL] Hangi ID'nin detayını görmek istersin? ").strip())
                display_task_details(task_id)
            except ValueError:
                print("[REBEL] Geçersiz ID girdisi.")
        elif choice.lower() == "v":
            view_file()
        elif choice.lower() == "e":
            edit_tasks_file()
        elif choice.lower() == "x":
            save_panel_snapshot()
        else:
            try:
                # Eğer doğrudan ID girilmişse, onu done yap
                task_id = int(choice)
                update_task_status(task_id)
            except ValueError:
                print("[REBEL] Geçersiz seçim.")

if __name__ == "__main__":
    main_loop()
