POETRY := poetry run

.PHONY: test

lint:
	$(POETRY) mypy src tests
	$(POETRY) pylint src
	cd tests && $(POETRY) pylint tests

REPORT := term-missing:skip-covered
test:
	$(POETRY) pytest --cov=src --cov-report=$(REPORT)
