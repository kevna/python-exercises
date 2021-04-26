POETRY := poetry run

.PHONY: lint FORCE

src/%.py src/%: FORCE
	$(POETRY) python -m $(subst /,.,$*)

ifdef threshold
THRESHOLD := --fail-under=$(threshold)
endif
lint:
	$(POETRY) mypy src tests
	$(POETRY) pylint $(THRESHOLD) src
	cd tests && $(POETRY) pylint $(THRESHOLD) tests

REPORT := term-missing:skip-covered
tests: FORCE
	$(POETRY) pytest --cov=src --cov-report=$(REPORT)

tests/%: FORCE
	$(POETRY) pytest $@ --cov=src/$* --cov-report=$(REPORT)

FORCE: ;
