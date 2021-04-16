POETRY := poetry run

.PHONY: test

lint:
	$(POETRY) pylint src
	#cd test && $(POETRY) pylint tests
	$(POETRY) mypy src #tests

REPORT := term-missing:skip-covered
test:
	$(POETRY) pytest --cov=src --cov-report=$(REPORT)
