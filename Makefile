dev:
	-rm -rf .venv
	./scripts/dev_venv.sh

test:
	python3 -m unittest
