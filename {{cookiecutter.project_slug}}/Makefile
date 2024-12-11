.ONESHELL:

.DEFAULT_GOAL := run 

PYTHON = ./venv/bin/python3
PIP = ./venv/bin/pip

venv/bin/activate: requirements.txt
	python -m venv venv
	chmod +x venv/bin/activate
	. ./venv/bin/activate
	$(PIP) install -r requirements.txt

venv: venv/bin/activate
	. ./venv/bin/activate

run: venv
	streamlit run Main_Page.py 

clean:
	rm -rf __pycache__

.PHONY: run clean 
