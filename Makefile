.PHONY: help install run_scan_web

PYTHON = python
PIP = pip

BLUE = \033[0;34m
NC = \033[0m

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(BLUE)%-30s$(NC) %s\n", $$1, $$2}'

install: ## Install project dependencies
	$(PIP) install -r requirements.txt

run_scan_web: ## Run the web scanning script
	$(PYTHON) src/scan_the_web.py