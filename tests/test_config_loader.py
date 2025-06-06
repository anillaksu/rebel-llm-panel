from rebel_llm.core import config_loader

def test_model_path_from_env(monkeypatch):
    monkeypatch.setenv("MODEL_PATH", "models/test-model.gguf")
    config_loader.reload_config()
    assert config_loader.MODEL_PATH == "models/test-model.gguf"

def test_default_model_path(monkeypatch):
    monkeypatch.delenv("MODEL_PATH", raising=False)
    config_loader.reload_config()
    assert config_loader.MODEL_PATH == "models/gemma-1.1-2b-it.Q4_K_M.gguf"

def test_log_file_from_env(monkeypatch):
    monkeypatch.setenv("LOG_FILE", "logs/test.log")
    config_loader.reload_config()
    assert config_loader.LOG_FILE == "logs/test.log"

def test_task_file_from_env(monkeypatch):
    monkeypatch.setenv("DEFAULT_TASK_FILE", "tasks/test.yaml")
    config_loader.reload_config()
    assert config_loader.DEFAULT_TASK_FILE == "tasks/test.yaml"
