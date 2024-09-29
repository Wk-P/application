#!/bin/bash
source ~/application/DjangoProject/.venv/bin/activate && \
    uwsgi --stop ~/application/linux-scripts/run/uwsgi.pid && \

sudo rm -rf ~/application/DjangoProject/BackendService/db.sqlite3

python3 ~/application/DjangoProject/BackendService/manage.py makemigrations && \
python3 ~/application/DjangoProject/BackendService/manage.py migrate && \
python3 ~/application/DjangoProject/BackendService/manage.py collectstatic --noinput && \
python3 ~/application/DjangoProject/BackendService/manage.py create_users
python3 ~/application/DjangoProject/BackendService/manage.py create_item


while kill -0 $(cat ~/application/linux-scripts/run/uwsgi.pid) 2>/dev/null; do
    echo "Waiting for uWSGI to stop..."
    sleep 1
done

echo "uWSGI has stopped. Starting uWSGI again."

uwsgi --ini ~/application/linux-scripts/uwsgi.ini