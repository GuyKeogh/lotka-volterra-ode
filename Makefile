.PHONY: fmt
fmt:
	poetry run isort .
	poetry run black .

.PHONY: lint
lint:
	poetry run flake8 .

.PHONY: test
test:
	poetry run pytest tests

.PHONY: check
check:
	make fmt lint test