install:
	pip install --upgrade pip &&\
		pip install -r requirement.txt

test:
	python -m pytest -vv test_main.py

format:
	black *.py

lint:
	pylint --disable=R, C main.py, hello.py

all: install lint test