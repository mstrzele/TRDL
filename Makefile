SHELL = /bin/sh

PYTHON  ?= python3
PIP      = .venv/bin/pip
OPENSSL ?= openssl
GREP    ?= grep
DIRENV  ?= direnv
DOCKER  ?= docker
COMPOSE ?= $(DOCKER) compose
AB      ?= ab

all: clean install

.venv:
	$(PYTHON) -m venv .venv

app/requirements.txt: .venv

~/.config/direnv/direnv.toml:
	@touch $@
	@grep -Fxq '[global]' $@ || echo '[global]' | tee -a $@
	@grep -Fxq 'load_dotenv = true' $@ || echo 'load_dotenv = true' | tee -a $@

export POSTGRES_PASSWORD=$(shell $(OPENSSL) rand -base64 16)
.env: ~/.config/direnv/direnv.toml
	@echo "POSTGRES_PASSWORD='$(POSTGRES_PASSWORD)'" > $@
	$(DIRENV) allow

.PHONY: install
install: app/requirements.txt
	$(PIP) install -r $<

tests/output.csv: REQUESTS=2000
tests/output.csv: CONCURRENCY=1
tests/output.csv: .env
	$(COMPOSE) up --build --wait || ($(COMPOSE) down -v && false)
	$(COMPOSE) run app flask init-db || ($(COMPOSE) down -v && false)
	$(AB) -n $(REQUESTS) -c $(CONCURRENCY) -e $@ http://127.0.0.1:8080/v1/value
	$(COMPOSE) down -v

.PHONY: clean
clean:
	rm -f tests/output.csv
	$(COMPOSE) rm -fsv
	rm -f .env
	rm -fr .venv
