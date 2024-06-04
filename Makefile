all: build

dev:
	-rm -rf .venv
	./scripts/dev_venv.sh

build:
	-rm -rf dist
	python3 -m pip install --upgrade build
	python3 -m build

upload:
	python3 -m twine upload --repository pypi dist/*

install:
	python3 -m pip install --force-reinstall dist/*.whl

test:
	python3 -m unittest

.PHONY: init build install test
