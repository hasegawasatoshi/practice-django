#!/bin/ash
# wait-for-postgres.sh

set -e

cmd="$@"

export PGPASSWORD="$POSTGRES_PASSWORD"
until psql -h "$POSTGRES_HOST" -p 5432 -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd
