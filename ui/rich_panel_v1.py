from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import yaml
import os

TASK_FILE = "tasks/task_list.yaml"
console = Console()

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f).get("tasks", [])

def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        yaml.dump({"tasks": tasks}, f, allow_unicode=True)

def show_task_table(tasks):
    table = Table(title="🚀 REBEL LLM GÖREV PANELİ", show_lines=True)
    table.add_column("ID", style="cyan", justify="right")
    table.add_column("Görev Adı", style="magenta")
    table.add_column("Durum", style="green")

    for task in tasks:
        table.add_row(str(task["id"]), task["name"], task["status"])
    
    console.clear()
    console.print(table)

def reset_tasks(tasks):
    for task in tasks:
        task["status"] = "todo"
    save_tasks(tasks)
    console.print("[bold yellow]Tüm görev durumları sıfırlandı.[/bold yellow]")

def main():
    while True:
        tasks = load_tasks()
        show_task_table(tasks)
        
        action = Prompt.ask("\n[bold green]Ne yapmak istersin[/bold green] ([blue]sıfırla[/blue], [blue]çık[/blue], [blue]id gir[/blue])")
        
        if action.lower() == "çık":
            break
        elif action.lower() == "sıfırla":
            reset_tasks(tasks)
        elif action.isdigit():
            task_id = int(action)
            found = False
            for task in tasks:
                if task["id"] == task_id:
                    found = True
                    console.print(f"\n[bold]Seçilen görev:[/bold] {task['name']}")
                    status = Prompt.ask("Yeni durum?", choices=["todo", "in_progress", "done"], default=task["status"])
                    task["status"] = status
                    save_tasks(tasks)
                    console.print("[green]Görev güncellendi.[/green]")
                    break
            if not found:
                console.print("[red]Geçersiz ID.[/red]")
        else:
            console.print("[red]Bilinmeyen komut.[/red]")

if __name__ == "__main__":
    main()
