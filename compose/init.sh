#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z "${COMPOSE_POSTGRESQL_SERVICE_HOST:-db}" "${COMPOSE_POSTGRESQL_SERVICE_PORT:-5432}"; do
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py create_db

exec "$@"
