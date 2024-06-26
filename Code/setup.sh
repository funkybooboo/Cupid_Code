#!/bin/bash

# make sure you are using your virtual environment
source "$VIRTUAL_ENV/bin/activate"

# Install Python dependencies using poetry
poetry install

# Create Django .env file
cp server/.env.example server/.env
echo "VAULT_PATH=$PWD/server/core/static/" >> server/.env

# Activate poetry shell
poetry shell

# Apply Django migrations
cd server || exit
# Check if python3 command is available
if command -v python3 &>/dev/null; then
    python3 manage.py makemigrations
    python3 manage.py migrate
# Check if python command is available
elif command -v python &>/dev/null; then
    python manage.py makemigrations
    python manage.py migrate
else
    echo "Python interpreter not found. Please install Python."
    exit 1
fi

# Navigate to Vue client directory
cd ../client || exit

# Install npm dependencies
npm install

# Go back to Code directory
cd .. || exit