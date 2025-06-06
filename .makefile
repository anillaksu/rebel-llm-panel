# REBEL LLM Makefile

run:
	python rebel_llm_launcher.py

test:
	pytest tests/

reset:
	python rebel_llm/core/task_runner.py --reset

log:
	type logs/rebel.log

clean:
	del /Q logs\*.log
	del /Q tasks\*.yaml

install:
	pip install -r requirements.txt
