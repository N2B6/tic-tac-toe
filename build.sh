#!/usr/bin/env bash
# Exit on error
set -o errexit

# Create database file
mkdir -p database
touch database/db.sqlite3

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput --clear

# Apply migrations
python manage.py migrate 