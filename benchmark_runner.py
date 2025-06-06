import os
import subprocess
from rebel_llm.core.config_loader import MODEL_PATH
from rebel_llm.utils.logger import log_event

def run_benchmark():
    binary_path = "external/llama.cpp/build/bin/Release/benchmark.exe"
    if not os.path.exists(binary_path):
        log_event("benchmark_runner", f"Benchmark binary bulunamadı: {binary_path}", error=True)
        print(f"[HATA] Binary bulunamadı: {binary_path}")
        return

    if not os.path.exists(MODEL_PATH):
        log_event("benchmark_runner", f"Model dosyası bulunamadı: {MODEL_PATH}", error=True)
        print(f"[HATA] Model dosyası bulunamadı: {MODEL_PATH}")
        return

    try:
        log_event("benchmark_runner", f"Benchmark başlatılıyor: {binary_path} -m {MODEL_PATH}")
        subprocess.run([binary_path, "-m", MODEL_PATH])
    except Exception as e:
        log_event("benchmark_runner", f"Benchmark başarısız: {str(e)}", error=True)
        print(f"[HATA] Benchmark başarısız: {str(e)}")
