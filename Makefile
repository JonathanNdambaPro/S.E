.PHONY: docs
docs:
	pdoc --html --skip-errors --force --output-dir docs package_1

.PHONY: test
test:
	pytest