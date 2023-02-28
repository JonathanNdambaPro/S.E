.PHONY: docs
docs:
	pdoc --html --skip-errors --force --output-dir docs package_1

.PHONY: test
test:
	pytest --cov=package_2/sub_package --cov-report term-missing --cov-fail-under=80