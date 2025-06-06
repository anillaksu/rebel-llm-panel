from utils.logger import log_event

def run_task_by_id(task_id):
    print(f"[REBEL] Görev çalıştırılıyor: {task_id}")
    log_event("TASK", f"Görev çalıştırıldı: {task_id}")
