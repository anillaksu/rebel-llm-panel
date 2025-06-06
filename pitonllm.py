from llama_cpp import Llama

MODEL_PATH = "D:/projeler/REBELLIONLLM/rebel_llm/models/gemma-1.1-2b-it.Q4_K_M.gguf"

llm = Llama(model_path=MODEL_PATH)

def build_prompt(messages):
    prompt = ""
    for i, msg in enumerate(messages):
        role = msg["role"]
        if role == "assistant":
            role = "model"
        prompt += f"<start_of_turn>{role}\n{msg['content'].strip()}<end_of_turn>\n"
    return prompt

print("[REBEL] Başladı.")
print("REBEL AI: Hazırım, sorunu yaz (q ile çık).")

while True:
    user_input = input("> ").strip()
    if user_input.lower() == "q":
        print("Çıkılıyor.")
        break
    if not user_input:
        continue

    messages = [{"role": "user", "content": user_input}]
    prompt = build_prompt(messages)

    output = llm(prompt, max_tokens=128, stop=["<end_of_turn>"])
    text = output['choices'][0]['text'].strip()

    print("REBEL:", text)
