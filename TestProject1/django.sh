#!/bin/bash

# echo "Create Migrations"
# echo "-------------------"
python manage.py makemigrations
# echo "-------------------"

# echo "Migrate"
# echo "-------------------"
python manage.py migrate
# echo "-------------------"

# echo "Start Django Server"
# echo "-------------------"
# gunicorn app_project.wsgi:application --bind 0.0.0.0:8004 --worker-class=gthread --threads=9 --timeout 3600
# echo "-------------------"
# !/bin/bash

echo "Create Migrations"
echo "-------------------"
# python manage.py makemigrations
echo "-------------------"

echo "Migrate"
echo "-------------------"
# python manage.py migrate
echo "-------------------"
# DEFAULT_ENV=/app/.base_env

# CLIENT_ENV=/app/client.env
# MERGED_ENV=/app/.env
 
# if [ -f "$CLIENT_ENV" ]; then
#   echo "Merging client.env into .env..."
#   awk -F= '!seen[$1]++' "$DEFAULT_ENV" "$CLIENT_ENV" > "$MERGED_ENV"
# else
#   echo "No client.env found. Using default .env only."
#   cp "$DEFAULT_ENV" "$MERGED_ENV"
# fi
 
# # Normalize line endings (remove ^M from Windows-style files)
# sed -i 's/\r$//' "$MERGED_ENV"
 
# echo "Final .env created at $MERGED_ENV"

echo "Start Django Server"
echo "-------------------"
gunicorn TestProject1.wsgi:application --bind 0.0.0.0:8000 --worker-class=gthread --threads=9 --timeout 3600
# gunicorn app_project.wsgi:application --bind 0.0.0.0:80 --worker-class=gthread --threads=9 --timeout 3600
echo "-------------------"