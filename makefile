
install:
	poetry install

build:
	poetry build

format:
	poetry run pre-commit run --all-files

clean:
	rm -rf dist

test:test_update
	poetry run pytest --cov vehicle tests

test_update:
	pytest --snapshot-update
