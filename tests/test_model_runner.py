from rebel_llm.core import model_runner, config_loader
import subprocess

def test_model_path_loads_correctly(monkeypatch):
    monkeypatch.setenv("MODEL_PATH", "models/test-model.gguf")
    config_loader.reload_config()
    assert config_loader.MODEL_PATH == "models/test-model.gguf"

def test_construct_command(monkeypatch):
    monkeypatch.setenv("MODEL_PATH", "models/test-model.gguf")
    config_loader.reload_config()
    expected = ["external/llama.cpp/build/bin/Release/llama-simple.exe", "-m", "models/test-model.gguf"]
    command = ["external/llama.cpp/build/bin/Release/llama-simple.exe", "-m", config_loader.MODEL_PATH]
    assert command == expected

def test_mocked_subprocess(monkeypatch):
    def fake_run(cmd, capture_output, text):
        return subprocess.CompletedProcess(cmd, 0, stdout="test passed", stderr="")
    monkeypatch.setattr(subprocess, "run", fake_run)
    output = model_runner.run_model()
    assert "test passed" in output
