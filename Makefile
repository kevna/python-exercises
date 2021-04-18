POETRY := poetry run

.PHONY: test

ifdef threshold
THRESHOLD := --fail-under=$(threshold)
endif
lint:
	$(POETRY) mypy src tests
	$(POETRY) pylint $(THRESHOLD) src
	cd tests && $(POETRY) pylint $(THRESHOLD) tests

REPORT := term-missing:skip-covered
test:
	$(POETRY) pytest --cov=src --cov-report=$(REPORT)
