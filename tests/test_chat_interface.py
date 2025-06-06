import rebel_llm.chat_interface as chat_interface

def test_start_chat(monkeypatch, capsys):
    def fake_run_model():
        return "🔥 Rebel yanıtı"
    monkeypatch.setattr(chat_interface, "run_model_response", fake_run_model)
    monkeypatch.setattr("builtins.input", lambda _: "q")
    chat_interface.start_chat()
    captured = capsys.readouterr()
    assert "REBEL AI: Hazırım" in captured.out
    assert "🔥 Rebel yanıtı" in captured.out or "REBEL cevabı" in captured.out
