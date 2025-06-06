from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Vertical, Horizontal
import yaml
import os

TASK_FILE = "tasks/task_list.yaml"

def escape_markup(text: str) -> str:
    """Metin içindeki özel karakterleri kaçış karakteriyle değiştirir."""
    return text.replace("[", "\

\[").replace("]", "\\]

")

class TaskButton(Button):
    """Görevleri temsil eden düğme bileşeni."""
    def __init__(self, task_id: int, task_name: str, status: str):
        raw_label = f"[{task_id}] {task_name} ({status})"
        label = escape_markup(raw_label)
        super().__init__(label, id=f"task-{task_id}")

class RebelTUI(App):
    """REBEL LLM Görev Paneli uygulaması."""
    CSS_PATH = "ui/rebel_panel.css"

    def compose(self) -> ComposeResult:
        """UI bileşenlerini oluşturur."""
        yield Header()
        yield Static("REBEL LLM Görev Paneli", classes="panel-header")

        self.task_container = Vertical()
        self.ensure_task_file()
        self.refresh_tasks()
        yield self.task_container

        yield Horizontal(
            Button("Görevleri Sıfırla", id="reset-tasks"),
            Button("Logları Temizle", id="clear-logs"),
        )
        yield Footer()

    def ensure_task_file(self):
        """Görev dosyasının varlığını kontrol eder, yoksa oluşturur."""
        if not os.path.exists(TASK_FILE):
            with open(TASK_FILE, "w", encoding="utf-8") as f:
                yaml.dump({"tasks": []}, f, allow_unicode=True)

    def load_tasks(self) -> list:
        """YAML dosyasından görevleri yükler."""
        if os.path.exists(TASK_FILE):
            with open(TASK_FILE, "r", encoding="utf-8") as f:
                return yaml.safe_load(f).get("tasks", [])
        return []

    def refresh_tasks(self):
        """Görevleri UI içinde yeniler."""
        self.task_container.remove_children()
        tasks = self.load_tasks()
        for task in tasks:
            if all(key in task for key in ["id", "name", "status"]):
                btn = TaskButton(task["id"], task["name"], task["status"])
                self.task_container.mount(btn)
            else:
                print(f"Hatalı görev formatı: {task}")

if __name__ == "__main__":
    RebelTUI().run()