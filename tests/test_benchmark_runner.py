import pytest
import rebel_llm.benchmark_runner as benchmark_runner

def test_run_benchmark(monkeypatch, capsys):
    executed = {}

    def fake_run(command, check):
        executed['cmd'] = command
        executed['check'] = check

    monkeypatch.setattr("subprocess.run", fake_run)

    benchmark_runner.run_benchmark()
    cmd = executed.get('cmd', [])
    
    assert benchmark_runner.MODEL_PATH in cmd
    assert "benchmark" in cmd[0] or "benchmark.exe" in cmd[0]
    assert executed['check'] is True
