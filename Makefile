.PHONY: tests
tests:
		pytest -v .

.PHONY: docs
docs:
		mkdocs serve