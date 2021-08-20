#!/bin/bash

# Create Logs Dir.
mkdir -p logs

# PY-Lint
python -m pipenv run python scripts/watcher.py > logs/pylint.log 2>&1 &

# Django Server
python -m pipenv run python manage.py runserver
