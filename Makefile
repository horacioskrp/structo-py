.PHONY: install
install: ## Install dependencies
	poetry install

.PHONY: run
run: start

.PHONY: start
start: ## Starts the server
	$(eval include .env)
	$(eval export $(sh sed 's/=.*//' .env))

	poetry run python main.py