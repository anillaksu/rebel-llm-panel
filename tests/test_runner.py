from rebel_llm.core.task_runner import run_task_by_id

def test_run_valid_task():
    assert run_task_by_id(1) is None  # 1 numaral? gorev zaten mevcut

def test_run_invalid_task():
    assert run_task_by_id(9999) is None  # Olmayan gorev hatas?z gecmeli
