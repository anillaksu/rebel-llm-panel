import subprocess
import threading
import queue
import re
import os

MODEL_PATH = os.getenv("MODEL_PATH", r"D:\projeler\REBELLIONLLM\rebel_llm\models\gemma-1.1-2b-it.Q4_K_M.gguf")
CMD = [
    r"D:\projeler\REBELLIONLLM\rebel_llm\external\llama.cpp\build\bin\Release\llama-simple-chat.exe",
    "-m", MODEL_PATH,
    "-c", "512",
    "-ngl", "35"
]

def clean_response(text):
    text = re.sub(r'\x1b\[[0-9;]*m', '', text)  # ANSI kodları sil
    text = re.sub(r'<\|im_(start|end|sep)\|>', '', text)
    text = re.sub(r'<start_of_turn.*?>', '', text)
    text = re.sub(r'<end_of_turn>', '', text)
    text = re.sub(r'(user|model)', '', text)
    return text.strip()

def enqueue_output(out, queue_):
    for line in iter(out.readline, ''):
        queue_.put(line)
    out.close()

def start_chat():
    print("[REBEL] Script başladı")
    print("[REBEL] Model path:", MODEL_PATH)

    process = subprocess.Popen(CMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)

    q = queue.Queue()
    t = threading.Thread(target=enqueue_output, args=(process.stdout, q))
    t.daemon = True
    t.start()

    print("REBEL AI: Hazırım, sorunuzu yazın (çıkmak için q):")
    while True:
        user_input = input("> ")
        if user_input.lower() == "q":
            try:
                process.stdin.close()
                process.terminate()
            except:
                pass
            break
        try:
            process.stdin.write(user_input + "\n")
            process.stdin.flush()
        except Exception as e:
            print(f"Hata yazarken: {e}")
            break

        output_lines = []
        while True:
            try:
                line = q.get(timeout=10)
            except queue.Empty:
                break
            output_lines.append(line)
            if line.strip().endswith("<end_of_turn>"):
                break

        raw_output = "".join(output_lines)
        clean_out = clean_response(raw_output)
        print("🔥 REBEL:", clean_out)

if __name__ == "__main__":
    print("[REBEL] __main__ bloğuna girildi")
    start_chat()
