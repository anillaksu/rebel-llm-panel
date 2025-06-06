import os
from dotenv import load_dotenv

def reload_config():
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    load_dotenv(env_path)

reload_config()

MODEL_PATH = os.getenv('MODEL_PATH', r"D:\projeler\REBELLIONLLM\rebel_llm\models\gemma-1.1-2b-it.Q4_K_M.gguf")
LLAMA_EXE_PATH = os.getenv('LLAMA_EXE_PATH', r"D:\projeler\REBELLIONLLM\rebel_llm\external\llama.cpp\build\bin\Release\llama-simple-chat.exe")
