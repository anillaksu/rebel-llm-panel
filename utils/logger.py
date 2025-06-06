import datetime
import os

def log_event(event_type, message):
    os.makedirs("logs", exist_ok=True)
    log_file = os.path.join("logs", "rebel_log.txt")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] [{event_type}] {message}\n")
