from rebel_llm.core.task_runner import run_task_by_id

def test_run_known_task():
    result = run_task_by_id(5)  # örnek: 5 numaralı görev çalışmalı
    assert result is None

def test_handle_missing_task():
    result = run_task_by_id(999)  # bilinmeyen görev ID'si
    assert result is None
