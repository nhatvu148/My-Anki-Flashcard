VENV_BIN_DIR = venv/bin
PIP = "$(VENV_BIN_DIR)/pip"
PYTHON = "$(VENV_BIN_DIR)/python"

define create-venv
python3 -m venv venv
endef

.PHONY: venv
venv:
	@$(create-venv)
	@$(PIP) install -r requirements.txt

run:
	@$(PYTHON) ./main.py

check:
	$(PYTHON) -m autopep8 --in-place --aggressive main.py
	$(PYTHON) -m flake8 --ignore=E501,F403,F405,E131,E131,F401,F821 main.py > error.txt
