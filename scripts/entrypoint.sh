#!/bin/bash

set -e
envsubst < ${APP_HOME}/app/scripts/uwsgi.ini.template > ${APP_HOME}/app/scripts/uwsgi.ini

function mariadb_ready(){
python << END
import sys
import MySQLdb
import os

try:
    database = os.getenv('DB_NAME', 'yourdbname')
    user = os.getenv('DB_USER', 'yourdbuser')
    password = os.getenv('DB_PASSWORD', 'yourdbpassword')
    host = os.getenv('DB_HOST', 'db')
    port = int(os.getenv('DB_PORT', '3306'))
    
    MySQLdb.connect(
        database=database,
        user=user,
        password=password,
        host=host,
        port=port,
        connect_timeout=5
    )
except MySQLdb.Error as err:
    print(f"Error: {err}")
    sys.exit(-1)
sys.exit(0)
END
}

function init_django() {
    until mariadb_ready; do
      >&2 echo "MariaDB is unavailable - sleeping"
      sleep 1
    done

    >&2 echo "MariaDB is up - continuing..."

    echo "Collecting static files..."
    python manage.py collectstatic --noinput

    echo "Applying database migrations..."
    python manage.py migrate

    echo "Applying compilemessages..."
    python manage.py compilemessages

    echo "Creating cache table..."
    python manage.py createcachetable

    echo "Checking for superuser..."
    python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser(
        username=os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin'),
        email=os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com'),
        password=os.getenv('DJANGO_SUPERUSER_PASSWORD', 'admin')
    )
    print('Superuser created.')
else:
    print('Superuser already exists.')
END
}

if [ "$1" = "python" ] && [ "$2" = "manage.py" ]; then
    if [ "$3" != "runserver" ]; then
        exec "$@"
    else
        init_django
        exec "$@"
    fi
elif [ "$1" = "bash" ] || [ "$1" = "sh" ]; then
    exec "$@"

elif [ "$1" = "celery" ] ; then
    exec "$@"
else
    init_django
    exec uwsgi "$@"
fi