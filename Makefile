POETRY := poetry run

.PHONY: test

lint:
	$(POETRY) mypy src tests
	$(POETRY) pylint --fail-under=9.5 src
	cd tests && $(POETRY) pylint tests

REPORT := term-missing:skip-covered
test:
	$(POETRY) pytest --cov=src --cov-report=$(REPORT)
