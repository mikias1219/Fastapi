#!/bin/bash

# Create folders if they don't exist
mkdir -p app/api

# Create files if they don't exist
touch app/main.py
touch app/config.py
touch app/db.py
touch app/crud.py
touch app/schemas.py
touch app/services.py
touch app/auth.py
touch app/api/inventory.py
touch app/api/users.py
touch .env
touch requirements.txt
touch README.md

echo "Folder structure and files have been created if they didn't exist."
