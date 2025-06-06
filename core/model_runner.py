import subprocess
from rebel_llm.core.config_loader import MODEL_PATH

def run_model():
    command = ["external/llama.cpp/build/bin/Release/llama-simple.exe", "-m", MODEL_PATH]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout
