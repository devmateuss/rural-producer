VENV_DIR = venv
PYTHON = python3
PIP = $(VENV_DIR)/bin/pip
DJANGO_MANAGE = $(VENV_DIR)/bin/python manage.py

create-env:
	$(PYTHON) -m venv $(VENV_DIR)

install: create-env
	$(PIP) install -r requirements.txt

migrate:
	$(DJANGO_MANAGE) migrate

makemigrations:
	$(DJANGO_MANAGE) makemigrations

run:
	$(DJANGO_MANAGE) runserver 0.0.0.0:8000

clean:
	rm -rf $(VENV_DIR)

create-app:
	@read -p "Enter the app name: " app_name; \
	django-admin startapp $$app_name; \
	echo "App $$app_name created successfully."
