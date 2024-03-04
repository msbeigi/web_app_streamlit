

install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt 
run:
	python *.py

test:
	# python -m pytest -vv test_*.py

lint:
	pylint --disable=R,C,E1120,W3101 *.py
format:
	black *.py

all: install test lint format
