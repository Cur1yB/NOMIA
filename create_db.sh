#!/bin/bash

export $(egrep -v '^#' .env | xargs)

psql -U $SUPERUSER -d postgres -c "CREATE DATABASE $DB_NAME;"
psql -U $SUPERUSER -d postgres -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"
psql -U $SUPERUSER -d postgres -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"
psql -U $SUPERUSER -d $DB_NAME -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO $DB_USER;"

echo "Superuser: $SUPERUSER"
echo "Database: $DB_NAME"
echo "User: $DB_USER"
echo "Password: $DB_PASSWORD"
echo "Host: $DB_HOST"
echo "Port: $DB_PORT"

python manage.py migrate

python manage.py load_questions_text
python manage.py load_questions_choices

echo "Initialization completed successfully!"