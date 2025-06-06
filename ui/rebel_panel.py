from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Vertical, Horizontal
import yaml
import os

TASK_FILE = "tasks/task_list.yaml"
LOG_FILE = "logs/rebel.log"
MODEL_FILE = "models/gemma-1.1-2b-it.Q4_K_M.gguf"

AUTO_TASKS = [
    {"id": 1, "name": "Sistem dosyalarını oluştur", "command": "echo init", "status": "done"},
    {"id": 2, "name": "Model kontrolü yap", "command": "echo model_check", "status": "pending"},
    {"id": 3, "name": "Görevleri yürüt", "command": "python runner/task_runner.py", "status": "pending"},
    {"id": 4, "name": "Sistem loglarını görüntüle", "command": "type logs/rebel.log", "status": "pending"}
]

class TaskButton(Button):
    def __init__(self, task_id: int, task_name: str, status: str):
        label = f"[{task_id}] {task_name} ({status})"
        super().__init__(label, id=str(task_id))

class RebelTUI(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("REBEL LLM Görev Paneli", classes="panel-header")
        self.task_container = Vertical()
        self.ensure_task_file()
        self.refresh_tasks()
        yield self.task_container

        yield Horizontal(
            Button("🧹 Görevleri Sıfırla", id="reset_tasks"),
            Button("🗑️ Logları Temizle", id="clear_logs"),
            Button("📦 Model Durumu", id="check_model"),
            Button("📄 Logları Göster", id="show_logs")
        )
        self.log_display = Static("Log görünümü burada")
        yield self.log_display
        yield Footer()

    def ensure_task_file(self):
        os.makedirs("tasks", exist_ok=True)
        if not os.path.exists(TASK_FILE):
            with open(TASK_FILE, "w", encoding="utf-8") as f:
                yaml.dump({"tasks": AUTO_TASKS}, f, allow_unicode=True)

    def load_tasks(self):
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)["tasks"]

    def save_tasks(self, tasks):
        with open(TASK_FILE, "w", encoding="utf-8") as f:
            yaml.dump({"tasks": tasks}, f, allow_unicode=True)

    def refresh_tasks(self):
        self.task_container.clear()
        tasks = self.load_tasks()
        for task in tasks:
            btn = TaskButton(task["id"], task["name"], task["status"])
            self.task_container.mount(btn)

    def update_task_status(self, task_id: str):
        tasks = self.load_tasks()
        for task in tasks:
            if str(task["id"]) == str(task_id):
                task["status"] = "done"
                os.system(task["command"])
        self.save_tasks(tasks)
        self.refresh_tasks()

    def reset_tasks(self):
        self.save_tasks(AUTO_TASKS)
        self.refresh_tasks()
        self.log_display.update("[✓] Tüm görevler sıfırlandı.")

    def clear_logs(self):
        os.makedirs("logs", exist_ok=True)
        open(LOG_FILE, "w", encoding="utf-8").close()
        self.log_display.update("[🗑️] Log dosyası temizlendi.")

    def check_model(self):
        if os.path.exists(MODEL_FILE):
            self.log_display.update(f"[✓] Model dosyası mevcut: {MODEL_FILE}")
        else:
            self.log_display.update(f"[✗] Model bulunamadı: {MODEL_FILE}")

    def show_logs(self):
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                content = f.read()
                self.log_display.update(content if content else "[ ] Log dosyası boş.")
        else:
            self.log_display.update("[✗] Log dosyası bulunamadı.")

    def on_button_pressed(self, event: Button.Pressed):
        match event.button.id:
            case "reset_tasks":
                self.reset_tasks()
            case "clear_logs":
                self.clear_logs()
            case "check_model":
                self.check_model()
            case "show_logs":
                self.show_logs()
            case _:
                self.update_task_status(event.button.id)

if __name__ == "__main__":
    RebelTUI().run()