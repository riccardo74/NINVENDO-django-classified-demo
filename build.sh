#!/usr/bin/env bash
# build.sh

set -o errexit  # exit on error

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate